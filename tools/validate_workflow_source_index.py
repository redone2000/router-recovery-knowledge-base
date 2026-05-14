#!/usr/bin/env python3
"""Validate local workflow source-index JSONL files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from profile_utils import iter_jsonl, repo_path
from validate_profiles import validate_date


DEFAULT_GLOB = "data/workflow_source_index*.jsonl"

ALLOWED_STATUSES = {
    "indexed",
    "indexed_context_only",
    "skipped",
    "rejected",
}

ALLOWED_WORKFLOWS = {
    "web_recovery",
    "passive_tftp_put",
    "post_upload_phase",
    "recovery_preparation",
    "active_tftp_server",
    "nmrp",
    "rescue_mode",
}

ALLOWED_SOURCE_TYPES = {
    "official_documentation",
    "vendor_support_forum",
    "openwrt_wiki",
    "github_docs",
    "third_party_repository",
    "verified_community_guide",
    "community_forum_post",
    "social_media",
}

ALLOWED_SCOPES = {
    "workflow_level",
    "brand_level",
    "series_level",
    "model_level",
    "hardware_version_level",
    "firmware_version_level",
    "unknown",
}

REQUIRED_FIELDS = {
    "source_id",
    "status",
    "workflow_target",
    "source_type",
    "source_url",
    "source_document",
    "applicability_scope",
    "vendor",
    "series",
    "model",
    "profile_generation_allowed",
    "workflow_update_allowed",
    "independent_source_count",
    "evidence_topics",
    "evidence_snippets",
    "evidence_gaps",
    "conflicts",
    "collector_notes",
    "extracted_date",
}

LIST_FIELDS = {
    "workflow_targets",
    "evidence_topics",
    "evidence_snippets",
    "evidence_gaps",
    "conflicts",
}

SCOPE_GAP_REQUIREMENTS = {
    "workflow_level": "workflow_level_not_model_specific",
    "brand_level": "brand_level_not_model_specific",
    "series_level": "series_level_not_model_specific",
    "unknown": "applicability_scope_unknown",
}

WORKFLOW_TOPIC_HINTS = {
    "web_recovery": ("recovery", "firmware_upload", "web"),
    "passive_tftp_put": ("tftp", "put", "upload"),
    "post_upload_phase": ("post_upload", "upload", "wait", "reboot"),
    "recovery_preparation": ("preparation", "static_ip", "ethernet"),
    "active_tftp_server": ("tftp", "server", "filename"),
    "nmrp": ("nmrp",),
    "rescue_mode": ("rescue", "recovery_mode", "reset"),
}


Issue = tuple[str, int, str]


def collect_paths(paths: list[str]) -> list[Path]:
    if paths:
        candidates = [repo_path(path) for path in paths]
    else:
        candidates = sorted(repo_path("data").glob("workflow_source_index*.jsonl"))

    files: list[Path] = []
    for candidate in candidates:
        if candidate.is_dir():
            files.extend(sorted(candidate.glob("workflow_source_index*.jsonl")))
        elif candidate.suffix == ".jsonl":
            files.append(candidate)
        else:
            raise ValueError(f"not a JSONL file or directory: {candidate}")
    return sorted(dict.fromkeys(files))


def is_public_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_row(row: dict[str, Any], path: Path) -> list[str]:
    issues: list[str] = []

    for field in sorted(REQUIRED_FIELDS - set(row)):
        issues.append(f"missing required field: {field}")

    if row.get("status") not in ALLOWED_STATUSES:
        issues.append(f"invalid status: {row.get('status')}")

    workflow_target = row.get("workflow_target")
    if workflow_target not in ALLOWED_WORKFLOWS:
        issues.append(f"invalid workflow_target: {workflow_target}")

    workflow_targets = row.get("workflow_targets", [workflow_target])
    if not isinstance(workflow_targets, list) or not workflow_targets:
        issues.append("workflow_targets must be a non-empty array when present")
    else:
        for target in workflow_targets:
            if target not in ALLOWED_WORKFLOWS:
                issues.append(f"invalid workflow_targets value: {target}")
        if workflow_target not in workflow_targets:
            issues.append("workflow_target must be included in workflow_targets")

    if row.get("source_type") not in ALLOWED_SOURCE_TYPES:
        issues.append(f"invalid source_type: {row.get('source_type')}")

    if row.get("applicability_scope") not in ALLOWED_SCOPES:
        issues.append(f"invalid applicability_scope: {row.get('applicability_scope')}")

    evidence_gaps = row.get("evidence_gaps")
    scope_gap = SCOPE_GAP_REQUIREMENTS.get(row.get("applicability_scope"))
    if scope_gap and isinstance(evidence_gaps, list) and scope_gap not in evidence_gaps:
        issues.append(f"non-model scope must include evidence gap: {scope_gap}")

    if row.get("profile_generation_allowed") is not False:
        issues.append("workflow source index rows must not allow profile generation")

    if not isinstance(row.get("workflow_update_allowed"), bool):
        issues.append("workflow_update_allowed must be boolean")

    independent_source_count = row.get("independent_source_count")
    if not isinstance(independent_source_count, int) or isinstance(independent_source_count, bool) or independent_source_count < 1:
        issues.append("independent_source_count must be an integer greater than or equal to 1")

    if not is_public_url(row.get("source_url")):
        issues.append("source_url must be a public http(s) URL")

    source_document = row.get("source_document")
    if not isinstance(source_document, str) or not source_document.strip():
        issues.append("source_document must be a non-empty string")
    else:
        doc_path = repo_path(source_document)
        if not doc_path.exists():
            issues.append(f"source_document does not exist: {source_document}")
        elif path.resolve() == doc_path.resolve():
            issues.append("source_document cannot point to the index file itself")

    for field in LIST_FIELDS:
        if field in row and not isinstance(row[field], list):
            issues.append(f"{field} must be an array")

    for field in ("evidence_topics", "evidence_snippets"):
        if not isinstance(row.get(field), list) or not row[field]:
            issues.append(f"{field} must be a non-empty array")

    topics = " ".join(str(topic).lower() for topic in row.get("evidence_topics", []))
    if isinstance(workflow_targets, list):
        for target in workflow_targets:
            hints = WORKFLOW_TOPIC_HINTS.get(target, ())
            if hints and not any(hint in topics for hint in hints):
                issues.append(f"evidence_topics must include a topic matching workflow target: {target}")

    if row.get("status") == "indexed_context_only" and row.get("workflow_update_allowed") is True:
        issues.append("context-only rows must not set workflow_update_allowed=true")

    collector_notes = str(row.get("collector_notes", "")).lower()
    if "profile" not in collector_notes or not any(marker in collector_notes for marker in ("not", "no ", "without", "must not", "does not")):
        issues.append("collector_notes must explicitly state the profile-generation boundary")

    source_type = row.get("source_type")
    if (
        row.get("workflow_update_allowed") is True
        and source_type in {"third_party_repository", "social_media"}
        and "reviewer approval" not in collector_notes
    ):
        issues.append(f"{source_type} rows with workflow_update_allowed=true must require reviewer approval in collector_notes")

    if not validate_date(row.get("extracted_date")):
        issues.append("extracted_date must be YYYY-MM-DD")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help=f"Workflow source-index JSONL files. Defaults to {DEFAULT_GLOB}.")
    args = parser.parse_args()

    try:
        paths = collect_paths(args.paths)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not paths:
        print("No workflow source-index JSONL files found.")
        return 0

    issues: list[Issue] = []
    checked = 0
    for path in paths:
        for record in iter_jsonl(path):
            checked += 1
            line_no = record.line_number
            row = record.data
            if record.json_error:
                issues.append((str(path), line_no, record.json_error))
                continue
            if not isinstance(row, dict):
                issues.append((str(path), line_no, "line must contain a JSON object"))
                continue
            for message in validate_row(row, path):
                issues.append((str(path), line_no, message))

    print(f"Checked {checked} workflow source-index row(s).")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for path, line_no, message in issues:
            print(f"{path}:{line_no}: {message}")
        return 1

    print("No workflow source-index validation issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
