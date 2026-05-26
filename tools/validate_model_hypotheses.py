#!/usr/bin/env python3
"""Validate AI-assisted model hypothesis JSONL files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from typing import Any

from profile_utils import collect_jsonl_paths, iter_jsonl, repo_path


SCHEMA_PATH = repo_path("schema/model_hypothesis.schema.json")
DEFAULT_SCAN_DIRS = ("model_hypotheses",)
Issue = tuple[str, int, str]


def is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def type_matches(value: Any, expected: Any) -> bool:
    if isinstance(expected, list):
        return any(type_matches(value, item) for item in expected)
    if expected == "null":
        return value is None
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    return True


def validate_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_schema_value(value: Any, schema: dict[str, Any], path: str) -> list[str]:
    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type is not None and not type_matches(value, expected_type):
        errors.append(f"{path}: expected {expected_type}, got {type(value).__name__}")
        return errors
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: invalid value {value!r}")
    pattern = schema.get("pattern")
    if pattern and isinstance(value, str) and not re.match(pattern, value):
        errors.append(f"{path}: does not match pattern {pattern}")
    if schema.get("format") == "date" and not validate_date(value):
        errors.append(f"{path}: expected YYYY-MM-DD date")

    if isinstance(value, dict) and schema.get("type") == "object":
        properties = schema.get("properties", {})
        required = set(schema.get("required", []))
        for field in sorted(required):
            if field not in value:
                errors.append(f"{path}.{field}: missing required field")
            elif not is_non_empty(value.get(field)) and field != "evidence_items" and "null" not in properties.get(field, {}).get("type", []):
                errors.append(f"{path}.{field}: must be non-empty")
        if schema.get("additionalProperties") is False:
            for field in sorted(set(value) - set(properties)):
                errors.append(f"{path}.{field}: unknown field not allowed")
        for field, child_value in value.items():
            child_schema = properties.get(field)
            if child_schema:
                errors.extend(validate_schema_value(child_value, child_schema, f"{path}.{field}"))

    if isinstance(value, list) and schema.get("type") == "array":
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            errors.append(f"{path}: expected at least {min_items} item(s)")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(validate_schema_value(item, item_schema, f"{path}[{index}]"))

    return errors


def validate_hypothesis(hypothesis: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors = validate_schema_value(hypothesis, schema, "<root>")
    status = hypothesis.get("hypothesis_status")
    evidence_strength = hypothesis.get("evidence_strength")
    evidence_items = hypothesis.get("evidence_items")
    promotion_gate = hypothesis.get("promotion_gate")
    app_copy_allowed = hypothesis.get("app_copy_allowed")

    if status != "research_seed" and not evidence_items:
        errors.append("non-research_seed hypotheses require at least one evidence_item")
    if evidence_strength == "ai_research_seed" and status != "research_seed":
        errors.append("ai_research_seed evidence_strength is only allowed with research_seed status")
    if status == "research_seed":
        if promotion_gate != "do_not_promote":
            errors.append("research_seed hypotheses must use promotion_gate do_not_promote")
        if app_copy_allowed is not False:
            errors.append("research_seed hypotheses must set app_copy_allowed false")
        if evidence_strength == "ai_research_seed" and hypothesis.get("suspected_workflows") != ["unknown"]:
            errors.append("ai_research_seed records must use suspected_workflows ['unknown']")
    if status == "ready_for_incoming_review":
        if promotion_gate != "ready_for_owner_review":
            errors.append("ready_for_incoming_review requires promotion_gate ready_for_owner_review")
        if evidence_strength in {"none", "ai_research_seed", "single_unverified_source"}:
            errors.append("ready_for_incoming_review requires stronger evidence than a seed or single unverified source")
    if promotion_gate == "ready_for_owner_review" and not evidence_items:
        errors.append("ready_for_owner_review requires evidence_items")

    for index, item in enumerate(evidence_items if isinstance(evidence_items, list) else []):
        if not isinstance(item, dict):
            continue
        if item.get("source_type") != "ai_research_seed" and not is_non_empty(item.get("source_url")) and not is_non_empty(item.get("source_document")):
            errors.append(f"evidence_items[{index}] must include source_url or source_document unless it is ai_research_seed")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Model hypothesis .jsonl files or directories. Defaults to model_hypotheses/*.jsonl.")
    args = parser.parse_args()

    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        paths = collect_jsonl_paths(args.paths, default_dirs=DEFAULT_SCAN_DIRS)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not paths:
        print("No model hypothesis JSONL files found.")
        return 0

    issues: list[Issue] = []
    checked = 0
    for path in paths:
        for record in iter_jsonl(path):
            checked += 1
            if record.json_error:
                issues.append((str(path), record.line_number, f"invalid JSONL: {record.json_error}"))
                continue
            assert record.data is not None
            for error in validate_hypothesis(record.data, schema):
                issues.append((str(path), record.line_number, error))

    print(f"Checked {checked} model hypothesis record(s) across {len(paths)} file(s).")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for path, line_number, message in issues:
            print(f"{path}:{line_number}: {message}")
        return 1

    print("No validation issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
