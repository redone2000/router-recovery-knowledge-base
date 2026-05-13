#!/usr/bin/env python3
"""Export SEO keyword candidates from workflows and incidents."""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from profile_utils import repo_path, safe_write_text


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def load_json_files(directory: str) -> list[dict[str, Any]]:
    root = repo_path(directory)
    if not root.exists():
        return []
    records: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data["_source_file"] = str(path.relative_to(repo_path(".")))
            records.append(data)
    return records


def add_keyword(bucket: OrderedDict[str, dict[str, Any]], keyword: str, category: str, intent: str, source: str, notes: str | None = None) -> None:
    normalized = " ".join(keyword.split())
    if not normalized:
        return
    key = normalized.lower()
    if key not in bucket:
        bucket[key] = {
            "keyword": normalized,
            "category": category,
            "intent": intent,
            "sources": [],
            "notes": [],
        }
    if source not in bucket[key]["sources"]:
        bucket[key]["sources"].append(source)
    if notes and notes not in bucket[key]["notes"]:
        bucket[key]["notes"].append(notes)


def workflow_keywords(workflows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    bucket: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for workflow in workflows:
        source = str(workflow.get("_source_file"))
        title = str(workflow.get("title") or "")
        workflow_type = str(workflow.get("workflow_type") or "")
        if title:
            add_keyword(bucket, title, "workflow", "workflow_explainer", source)
            add_keyword(bucket, f"how {title.lower()} works", "workflow", "workflow_explainer", source)
        for query in workflow.get("panic_entry_queries", []) if isinstance(workflow.get("panic_entry_queries"), list) else []:
            add_keyword(bucket, str(query), "panic_symptom", "troubleshooting", source, "Defined as workflow panic entry query.")
        for signal in workflow.get("readiness_signals", []) if isinstance(workflow.get("readiness_signals"), list) else []:
            if not isinstance(signal, dict):
                continue
            signal_name = str(signal.get("signal") or "").replace("-", " ")
            if signal_name:
                add_keyword(bucket, f"router recovery {signal_name}", "readiness_signal", "troubleshooting", source, str(signal.get("warning") or ""))
        for failure in workflow.get("failure_modes", []) if isinstance(workflow.get("failure_modes"), list) else []:
            if not isinstance(failure, dict):
                continue
            symptom = str(failure.get("symptom") or "")
            if symptom:
                add_keyword(bucket, symptom, "failure_mode", "troubleshooting", source, "Workflow failure mode.")
        if workflow_type == "post_upload_phase":
            add_keyword(bucket, "firmware upload complete but router not working", "post_upload", "troubleshooting", source)
            add_keyword(bucket, "router recovery upload finished no web UI", "post_upload", "troubleshooting", source)
        if workflow_type == "passive_tftp_put":
            add_keyword(bucket, "router TFTP put no ACK", "tftp", "troubleshooting", source)
            add_keyword(bucket, "TFTP timeout router recovery", "tftp", "troubleshooting", source)
    return list(bucket.values())


def incident_keywords(incidents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    bucket: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for incident in incidents:
        source = str(incident.get("_source_file"))
        vendor = str(incident.get("vendor") or "").strip()
        model = str(incident.get("model") or "").strip()
        symptom = str(incident.get("symptom") or "")
        if symptom:
            add_keyword(bucket, symptom, "incident_symptom", "troubleshooting", source, "Observed-only incident symptom.")
        if vendor and model and symptom:
            add_keyword(bucket, f"{vendor} {model} {symptom}", "model_incident", "long_tail_troubleshooting", source, "Model-specific observed-only incident.")
        for signal in incident.get("observed_signals", []) if isinstance(incident.get("observed_signals"), list) else []:
            add_keyword(bucket, str(signal), "incident_signal", "troubleshooting", source, "Observed signal from incident.")
        for pattern in incident.get("failed_patterns", []) if isinstance(incident.get("failed_patterns"), list) else []:
            add_keyword(bucket, str(pattern), "failed_pattern", "troubleshooting", source, "Failed pattern from incident.")
        for pattern in incident.get("successful_patterns", []) if isinstance(incident.get("successful_patterns"), list) else []:
            add_keyword(bucket, str(pattern), "successful_pattern", "tool_or_workaround", source, "Successful pattern from incident.")
    return list(bucket.values())


def foundation_keywords() -> list[dict[str, Any]]:
    bucket: OrderedDict[str, dict[str, Any]] = OrderedDict()
    source = "docs/recovery_language.md"
    seeds = [
        ("router bricked what to do", "panic_symptom", "troubleshooting"),
        ("192.168.1.1 not working after firmware update", "panic_symptom", "troubleshooting"),
        ("router recovery mode", "foundation", "concept_explainer"),
        ("router recovery window", "foundation", "concept_explainer"),
        ("router recovery static IP setup", "foundation", "how_to"),
        ("ping works but router page not opening", "panic_symptom", "troubleshooting"),
        ("upload complete does not mean recovery complete", "post_upload", "troubleshooting"),
        ("router recovery observed-only behavior", "evidence_language", "concept_explainer"),
    ]
    for keyword, category, intent in seeds:
        add_keyword(bucket, keyword, category, intent, source)
    return list(bucket.values())


def build_export() -> dict[str, Any]:
    workflows = load_json_files("workflows")
    incidents = load_json_files("incidents")
    sections = {
        "foundation_keywords": foundation_keywords(),
        "workflow_keywords": workflow_keywords(workflows),
        "incident_keywords": incident_keywords(incidents),
    }
    all_keywords: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for items in sections.values():
        for item in items:
            add_keyword(
                all_keywords,
                str(item["keyword"]),
                str(item["category"]),
                str(item["intent"]),
                ", ".join(item.get("sources", [])),
                "; ".join(item.get("notes", [])) if item.get("notes") else None,
            )
    suggested_pages = []
    for keyword in all_keywords.values():
        if keyword["category"] in {"panic_symptom", "post_upload", "tftp", "failure_mode", "incident_symptom", "model_incident"}:
            suggested_pages.append(
                {
                    "slug": slugify(str(keyword["keyword"])),
                    "primary_keyword": keyword["keyword"],
                    "intent": keyword["intent"],
                    "source_categories": [keyword["category"]],
                    "stage": "candidate",
                }
            )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_inputs": {
            "workflows": [workflow.get("_source_file") for workflow in workflows],
            "incidents": [incident.get("_source_file") for incident in incidents],
            "foundations": ["docs/recovery_language.md"],
        },
        "sections": sections,
        "all_keywords": list(all_keywords.values()),
        "suggested_pages": suggested_pages,
        "safety_note": "SEO candidates are not recovery guidance. They must route into reviewed workflow/profile content before publication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="exports/seo_keyword_candidates.json", help="Output path. Must not already exist.")
    args = parser.parse_args()

    report = build_export()
    output_path = repo_path(args.output)
    safe_write_text(output_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote SEO keyword candidates: {output_path}")
    print(f"Keywords: {len(report['all_keywords'])}; suggested pages: {len(report['suggested_pages'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
