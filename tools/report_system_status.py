#!/usr/bin/env python3
"""Generate a status report for the recovery knowledge system."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from profile_utils import iter_jsonl, repo_path, safe_write_text


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object: {path}")
    return data


def load_profiles(directory: str) -> list[dict[str, Any]]:
    root = repo_path(directory)
    if not root.exists():
        return []
    profiles: list[dict[str, Any]] = []
    for path in sorted(root.glob("*.jsonl")):
        for record in iter_jsonl(path):
            if record.json_error or record.data is None:
                profiles.append(
                    {
                        "_file": str(record.path.relative_to(repo_path("."))),
                        "_line": record.line_number,
                        "_error": record.json_error,
                    }
                )
                continue
            profile = dict(record.data)
            profile["_file"] = str(record.path.relative_to(repo_path(".")))
            profile["_line"] = record.line_number
            profiles.append(profile)
    return profiles


def load_jsonl_records(directory: str) -> list[dict[str, Any]]:
    root = repo_path(directory)
    if not root.exists():
        return []
    records: list[dict[str, Any]] = []
    for path in sorted(root.glob("*.jsonl")):
        for record in iter_jsonl(path):
            if record.json_error or record.data is None:
                records.append(
                    {
                        "_file": str(record.path.relative_to(repo_path("."))),
                        "_line": record.line_number,
                        "_error": record.json_error,
                    }
                )
                continue
            item = dict(record.data)
            item["_file"] = str(record.path.relative_to(repo_path(".")))
            item["_line"] = record.line_number
            records.append(item)
    return records


def load_json_tree(directory: str) -> list[dict[str, Any]]:
    root = repo_path(directory)
    if not root.exists():
        return []
    records: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        record = load_json(path)
        record["_file"] = str(path.relative_to(repo_path(".")))
        records.append(record)
    return records


def load_lifecycle_decisions() -> list[dict[str, Any]]:
    path = repo_path("data/profile_lifecycle_decisions.jsonl")
    if not path.exists():
        return []
    decisions: list[dict[str, Any]] = []
    for record in iter_jsonl(path):
        if record.json_error or record.data is None:
            decisions.append({"_file": str(record.path), "_line": record.line_number, "_error": record.json_error})
            continue
        decisions.append(dict(record.data))
    return decisions


def profile_summary(profiles: list[dict[str, Any]]) -> dict[str, Any]:
    by_confidence = Counter(str(profile.get("confidence_level") or "unknown") for profile in profiles if "_error" not in profile)
    by_vendor = Counter(str(profile.get("vendor") or "UNKNOWN") for profile in profiles if "_error" not in profile)
    return {
        "count": len(profiles),
        "valid_count": sum(1 for profile in profiles if "_error" not in profile),
        "invalid_count": sum(1 for profile in profiles if "_error" in profile),
        "confidence_distribution": dict(sorted(by_confidence.items())),
        "vendor_distribution": dict(sorted(by_vendor.items())),
        "profiles": [
            {
                "id": profile.get("id"),
                "vendor": profile.get("vendor"),
                "model": profile.get("model"),
                "confidence_level": profile.get("confidence_level"),
                "file": profile.get("_file"),
            }
            for profile in profiles
            if "_error" not in profile
        ],
    }


def hypothesis_summary(hypotheses: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [hypothesis for hypothesis in hypotheses if "_error" not in hypothesis]
    by_status = Counter(str(hypothesis.get("hypothesis_status") or "unknown") for hypothesis in valid)
    by_vendor = Counter(str(hypothesis.get("vendor") or "UNKNOWN") for hypothesis in valid)
    return {
        "count": len(hypotheses),
        "valid_count": len(valid),
        "invalid_count": sum(1 for hypothesis in hypotheses if "_error" in hypothesis),
        "status_distribution": dict(sorted(by_status.items())),
        "vendor_distribution": dict(sorted(by_vendor.items())),
        "ready_for_incoming_review_count": sum(
            1
            for hypothesis in valid
            if hypothesis.get("hypothesis_status") == "ready_for_incoming_review"
            and hypothesis.get("promotion_gate") == "ready_for_owner_review"
        ),
        "hypotheses": [
            {
                "id": hypothesis.get("id"),
                "vendor": hypothesis.get("vendor"),
                "model": hypothesis.get("model"),
                "hypothesis_status": hypothesis.get("hypothesis_status"),
                "evidence_strength": hypothesis.get("evidence_strength"),
                "promotion_gate": hypothesis.get("promotion_gate"),
                "file": hypothesis.get("_file"),
            }
            for hypothesis in valid
        ],
    }


def build_report() -> dict[str, Any]:
    incoming = load_profiles("incoming")
    reviewed = load_profiles("reviewed")
    final = load_profiles("final")
    hypotheses = load_jsonl_records("model_hypotheses")
    incidents = load_json_tree("incidents")
    workflows = load_json_tree("workflows")
    decisions = load_lifecycle_decisions()

    paused_profiles = sorted(
        {
            str(decision.get("profile_id"))
            for decision in decisions
            if decision.get("decision") in {"paused", "blocked"} and decision.get("profile_id")
        }
    )
    blocked_incidents = [
        {
            "incident_id": incident.get("incident_id"),
            "vendor": incident.get("vendor"),
            "model": incident.get("model"),
            "symptom": incident.get("symptom"),
            "profile_gate": incident.get("profile_gate"),
            "resolution": incident.get("resolution"),
            "file": incident.get("_file"),
        }
        for incident in incidents
        if incident.get("profile_gate") == "blocked"
    ]

    seo_path = repo_path("exports/seo_keyword_candidates.json")
    seo_summary: dict[str, Any]
    if seo_path.exists():
        seo_data = load_json(seo_path)
        seo_summary = {
            "keyword_count": len(seo_data.get("all_keywords", [])),
            "suggested_page_count": len(seo_data.get("suggested_pages", [])),
            "file": "exports/seo_keyword_candidates.json",
        }
    else:
        seo_summary = {"keyword_count": 0, "suggested_page_count": 0, "file": None}

    recommended_next_actions = []
    if any(profile.get("id") == "asus-rt-ac86u-unknown-unknown" for profile in incoming):
        recommended_next_actions.append("Owner confirm ASUS RT-AC86U lab observation before reviewed-candidate migration.")
    if "netgear-r7000-unknown-unknown" in paused_profiles:
        recommended_next_actions.append("Keep NETGEAR R7000 out of reviewed/final until lab retest resolves timing incident.")
    if workflows:
        recommended_next_actions.append("Draft Web Recovery workflow before expanding TP-Link/AX model coverage.")
    if hypotheses:
        recommended_next_actions.append("Use model_hypotheses/ for AI-assisted model expansion; promote none without Owner approval.")

    prohibited_actions = [
        "Do not write final/ automatically.",
        "Do not create incoming profiles directly from AI model hypotheses.",
        "Do not promote incidents directly to profile guidance.",
        "Do not use R7000 as App-ready guidance while paused.",
        "Do not expand broad model coverage before workflow and incident gates are stable.",
    ]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "profiles": {
            "incoming": profile_summary(incoming),
            "reviewed": profile_summary(reviewed),
            "final": profile_summary(final),
        },
        "model_hypotheses": hypothesis_summary(hypotheses),
        "incidents": {
            "count": len(incidents),
            "blocked_profile_gate_count": len(blocked_incidents),
            "blocked_incidents": blocked_incidents,
        },
        "workflows": {
            "count": len(workflows),
            "workflow_ids": sorted(str(workflow.get("workflow_id")) for workflow in workflows),
            "draft_count": sum(1 for workflow in workflows if workflow.get("status") == "draft"),
        },
        "lifecycle_decisions": {
            "count": len(decisions),
            "paused_profiles": paused_profiles,
        },
        "seo": seo_summary,
        "recommended_next_actions": recommended_next_actions,
        "prohibited_actions": prohibited_actions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="reports/system_status_latest.json", help="Output path. Must not already exist.")
    args = parser.parse_args()

    report = build_report()
    output_path = repo_path(args.output)
    safe_write_text(output_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote system status report: {output_path}")
    print(
        "Incoming: {incoming}; reviewed: {reviewed}; final: {final}; hypotheses: {hypotheses}; incidents: {incidents}; workflows: {workflows}".format(
            incoming=report["profiles"]["incoming"]["count"],
            reviewed=report["profiles"]["reviewed"]["count"],
            final=report["profiles"]["final"]["count"],
            hypotheses=report["model_hypotheses"]["count"],
            incidents=report["incidents"]["count"],
            workflows=report["workflows"]["count"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
