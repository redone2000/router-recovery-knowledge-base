#!/usr/bin/env python3
"""Validate local collection queue and source-index JSONL templates."""

from __future__ import annotations

import argparse
import ipaddress
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from profile_utils import REPO_ROOT, iter_jsonl, load_enums, repo_path
from validate_profiles import validate_date


WORK_QUEUE_REQUIRED = {
    "queue_id",
    "status",
    "queue_status",
    "priority",
    "vendor",
    "model",
    "hardware_version_hint",
    "firmware_version_hint",
    "target_sources",
    "collection_goal",
    "allowed_source_types",
    "disallowed_actions",
    "evidence_requirements",
    "stop_conditions",
    "prohibited_profile_fields",
    "owner_notes",
}

SOURCE_INDEX_REQUIRED = {
    "source_id",
    "queue_id",
    "status",
    "source_type",
    "source_url",
    "source_document",
    "vendor",
    "model",
    "hardware_version",
    "firmware_version",
    "recovery_methods_claimed",
    "evidence_snippets",
    "evidence_gaps",
    "conflicts",
    "collector_notes",
    "extracted_date",
}

CANDIDATE_QUEUE_REQUIRED = {
    "queue_id",
    "queue_status",
    "status",
    "priority",
    "vendor",
    "model",
    "hardware_version_hint",
    "firmware_version_hint",
    "selection_reason",
    "expected_source_types",
    "risk_notes",
    "prohibited_profile_fields",
    "disallowed_actions",
}

SOURCE_PLAN_REQUIRED = {
    "queue_id",
    "vendor",
    "model",
    "source_plan_status",
    "expected_source_types",
    "future_search_queries",
    "must_verify",
    "stop_conditions",
    "disallowed_outputs",
    "risk_notes",
}

WORK_QUEUE_REQUIRED_SAFETY = {
    "guess_tftp_direction",
    "access_router_ip",
    "send_tftp_udp_packets",
}

WORK_QUEUE_REQUIRED_STOPS = {
    "tftp_direction_unclear",
    "source_conflict_found",
}

SOURCE_INDEX_REQUIRED_GAP_EXAMPLES = {
    "tftp_direction_unclear",
}

PROHIBITED_PROFILE_FIELDS = {
    "recovery_methods",
    "network_recovery",
    "source_evidence",
    "confidence_level",
}

CANDIDATE_REQUIRED_DISALLOWED = {
    "web_fetching",
    "source_collection",
    "page_opening",
    "search",
    "downloading",
    "guess_tftp_direction",
    "infer_default_ip",
    "infer_firmware_filename",
    "access_router_ip",
    "send_tftp_udp_packets",
    "network_scanning",
    "write_incoming",
    "write_reviewed",
    "write_final",
}

CANDIDATE_FORBIDDEN_PROFILE_KEYS = {
    "recovery_methods",
    "network_recovery",
    "source_evidence",
    "confidence_level",
    "source_url",
    "source_document",
}

SOURCE_PLAN_REQUIRED_DISALLOWED_OUTPUTS = {
    "recovery_methods",
    "network_recovery",
    "source_evidence",
    "confidence_level",
    "IP addresses",
    "firmware filenames",
    "TFTP direction",
}

IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
PRIVATE_PLACEHOLDER_HOSTS = {"example.invalid"}


Issue = tuple[str, int, str]


def has_private_ip(value: Any) -> bool:
    text = value if isinstance(value, str) else repr(value)
    for match in IPV4_RE.findall(text):
        try:
            ip = ipaddress.ip_address(match)
        except ValueError:
            continue
        if ip.is_private or ip.is_loopback or ip.is_link_local:
            return True
    return False


def is_placeholder_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and parsed.hostname in PRIVATE_PLACEHOLDER_HOSTS


def ensure_list(row: dict[str, Any], field: str, issues: list[str]) -> list[Any]:
    value = row.get(field)
    if not isinstance(value, list) or not value:
        issues.append(f"{field} must be a non-empty array")
        return []
    return value


def validate_work_queue_row(row: dict[str, Any], source_types: set[str], stage0: bool) -> list[str]:
    issues: list[str] = []
    missing = sorted(WORK_QUEUE_REQUIRED - set(row))
    for field in missing:
        issues.append(f"missing required field: {field}")

    if stage0 and row.get("status") != "template_only":
        issues.append("Stage 0 work queue status must be template_only")
    if stage0 and row.get("queue_status") != "template_only":
        issues.append("Stage 0 work queue queue_status must be template_only")
    if not stage0 and row.get("queue_status") != "proposed_only":
        issues.append("Stage 1 queue-only queue_status must be proposed_only")

    if not isinstance(row.get("priority"), int):
        issues.append("priority must be an integer")

    target_sources = ensure_list(row, "target_sources", issues)
    for url in target_sources:
        if not isinstance(url, str) or not is_placeholder_url(url):
            issues.append(f"target_sources must use placeholder https://example.invalid URLs in Stage 0: {url}")

    allowed_source_types = ensure_list(row, "allowed_source_types", issues)
    invalid_source_types = sorted(set(str(item) for item in allowed_source_types) - source_types)
    for item in invalid_source_types:
        issues.append(f"invalid allowed_source_types value: {item}")

    disallowed_actions = set(str(item) for item in ensure_list(row, "disallowed_actions", issues))
    missing_safety = sorted(WORK_QUEUE_REQUIRED_SAFETY - disallowed_actions)
    for item in missing_safety:
        issues.append(f"missing required disallowed action: {item}")

    stop_conditions = set(str(item) for item in ensure_list(row, "stop_conditions", issues))
    missing_stops = sorted(WORK_QUEUE_REQUIRED_STOPS - stop_conditions)
    for item in missing_stops:
        issues.append(f"missing required stop condition: {item}")

    if has_private_ip(row):
        issues.append("template contains a private, loopback, or link-local IP literal")

    prohibited_fields = set(str(item) for item in ensure_list(row, "prohibited_profile_fields", issues))
    missing_profile_blocks = sorted(PROHIBITED_PROFILE_FIELDS - prohibited_fields)
    for item in missing_profile_blocks:
        issues.append(f"missing prohibited profile field marker: {item}")

    return issues


def validate_source_index_row(row: dict[str, Any], source_types: set[str], recovery_methods: set[str], stage0: bool) -> list[str]:
    issues: list[str] = []
    missing = sorted(SOURCE_INDEX_REQUIRED - set(row))
    for field in missing:
        issues.append(f"missing required field: {field}")

    if stage0 and row.get("status") != "template_only":
        issues.append("Stage 0 source index status must be template_only")

    source_type = row.get("source_type")
    if source_type not in source_types:
        issues.append(f"invalid source_type: {source_type}")

    source_url = row.get("source_url")
    if not isinstance(source_url, str) or not is_placeholder_url(source_url):
        issues.append(f"source_url must use placeholder https://example.invalid URL in Stage 0: {source_url}")

    methods = ensure_list(row, "recovery_methods_claimed", issues)
    invalid_methods = sorted(set(str(item) for item in methods) - recovery_methods)
    for item in invalid_methods:
        issues.append(f"invalid recovery_methods_claimed value: {item}")

    snippets = ensure_list(row, "evidence_snippets", issues)
    if stage0:
        for snippet in snippets:
            if not isinstance(snippet, str) or "[PLACEHOLDER_ONLY]" not in snippet:
                issues.append("Stage 0 evidence_snippets must be explicit [PLACEHOLDER_ONLY] text")

    gaps = set(str(item) for item in ensure_list(row, "evidence_gaps", issues))
    if row.get("source_id") == "src-template-002":
        missing_gaps = sorted(SOURCE_INDEX_REQUIRED_GAP_EXAMPLES - gaps)
        for item in missing_gaps:
            issues.append(f"missing required evidence gap example: {item}")

    if not validate_date(row.get("extracted_date")):
        issues.append("extracted_date must be YYYY-MM-DD")

    if has_private_ip(row):
        issues.append("template contains a private, loopback, or link-local IP literal")

    return issues


def validate_candidate_queue_row(row: dict[str, Any], source_types: set[str]) -> list[str]:
    issues: list[str] = []
    missing = sorted(CANDIDATE_QUEUE_REQUIRED - set(row))
    for field in missing:
        issues.append(f"missing required field: {field}")

    forbidden_keys = sorted(CANDIDATE_FORBIDDEN_PROFILE_KEYS & set(row))
    for field in forbidden_keys:
        issues.append(f"candidate queue must not populate profile field: {field}")

    if row.get("queue_status") != "proposed_only":
        issues.append("candidate queue queue_status must be proposed_only")
    if row.get("status") != "proposed_candidate":
        issues.append("candidate queue status must be proposed_candidate")

    priority = row.get("priority")
    if not isinstance(priority, int) or not 1 <= priority <= 5:
        issues.append("priority must be an integer from 1 to 5")

    expected_source_types = ensure_list(row, "expected_source_types", issues)
    invalid_source_types = sorted(set(str(item) for item in expected_source_types) - source_types)
    for item in invalid_source_types:
        issues.append(f"invalid expected_source_types value: {item}")

    disallowed_actions = set(str(item) for item in ensure_list(row, "disallowed_actions", issues))
    missing_disallowed = sorted(CANDIDATE_REQUIRED_DISALLOWED - disallowed_actions)
    for item in missing_disallowed:
        issues.append(f"missing required disallowed action: {item}")

    prohibited_fields = set(str(item) for item in ensure_list(row, "prohibited_profile_fields", issues))
    missing_profile_blocks = sorted(PROHIBITED_PROFILE_FIELDS - prohibited_fields)
    for item in missing_profile_blocks:
        issues.append(f"missing prohibited profile field marker: {item}")

    ensure_list(row, "risk_notes", issues)

    if has_private_ip(row):
        issues.append("candidate queue contains a private, loopback, or link-local IP literal")

    return issues


def validate_source_plan_row(row: dict[str, Any], source_types: set[str]) -> list[str]:
    issues: list[str] = []
    missing = sorted(SOURCE_PLAN_REQUIRED - set(row))
    for field in missing:
        issues.append(f"missing required field: {field}")

    forbidden_keys = sorted(CANDIDATE_FORBIDDEN_PROFILE_KEYS & set(row))
    for field in forbidden_keys:
        issues.append(f"source plan must not populate profile field: {field}")

    if row.get("source_plan_status") != "proposed_only":
        issues.append("source plan status must be proposed_only")

    expected_source_types = ensure_list(row, "expected_source_types", issues)
    invalid_source_types = sorted(set(str(item) for item in expected_source_types) - source_types)
    for item in invalid_source_types:
        issues.append(f"invalid expected_source_types value: {item}")

    ensure_list(row, "future_search_queries", issues)
    ensure_list(row, "must_verify", issues)
    ensure_list(row, "stop_conditions", issues)
    ensure_list(row, "risk_notes", issues)

    disallowed_outputs = set(str(item) for item in ensure_list(row, "disallowed_outputs", issues))
    missing_disallowed = sorted(SOURCE_PLAN_REQUIRED_DISALLOWED_OUTPUTS - disallowed_outputs)
    for item in missing_disallowed:
        issues.append(f"missing required disallowed output: {item}")

    if has_private_ip(row):
        issues.append("source plan contains a private, loopback, or link-local IP literal")

    return issues


def validate_file(path: Path, kind: str, mode: str) -> list[Issue]:
    enums = load_enums()
    source_types = enums.get("source_type", set())
    recovery_methods = enums.get("recovery_method", set())
    issues: list[Issue] = []
    rows = 0
    stage0 = mode == "stage0-template"

    for record in iter_jsonl(path):
        rows += 1
        if record.json_error or record.data is None:
            issues.append((str(record.path), record.line_number, f"invalid JSONL: {record.json_error}"))
            continue
        if kind == "candidate_queue":
            row_issues = validate_candidate_queue_row(record.data, source_types)
        elif kind == "source_plan":
            row_issues = validate_source_plan_row(record.data, source_types)
        elif kind == "work_queue":
            row_issues = validate_work_queue_row(record.data, source_types, stage0)
        else:
            row_issues = validate_source_index_row(record.data, source_types, recovery_methods, stage0)
        for issue in row_issues:
            issues.append((str(record.path), record.line_number, issue))

    if rows == 0:
        issues.append((str(path), 0, "file has no JSONL records"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-queue", default="data/work_queue.template.jsonl", help="Work queue JSONL file.")
    parser.add_argument("--source-index", default="data/source_index.template.jsonl", help="Source index JSONL file.")
    parser.add_argument(
        "--mode",
        choices=("stage0-template", "stage1-proposed"),
        default="stage0-template",
        help="Validation mode.",
    )
    args = parser.parse_args()

    work_queue = repo_path(args.work_queue)
    source_index = repo_path(args.source_index)
    issues: list[Issue] = []

    if args.mode == "stage1-proposed" and "source_plan" in work_queue.name:
        work_queue_kind = "source_plan"
    else:
        work_queue_kind = "candidate_queue" if args.mode == "stage1-proposed" else "work_queue"
    targets = [(work_queue, work_queue_kind)]
    if args.mode == "stage0-template":
        targets.append((source_index, "source_index"))

    for path, kind in targets:
        if not path.exists():
            issues.append((str(path), 0, "file does not exist"))
            continue
        if REPO_ROOT not in path.parents:
            issues.append((str(path), 0, "file must be inside this repository"))
            continue
        issues.extend(validate_file(path, kind, mode=args.mode))

    if issues:
        print(f"Found {len(issues)} collection template issue(s):")
        for path, line_number, message in issues:
            print(f"{path}:{line_number}: {message}")
        return 1

    print(f"Collection {args.mode} files passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
