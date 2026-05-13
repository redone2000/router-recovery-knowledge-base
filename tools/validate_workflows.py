#!/usr/bin/env python3
"""Validate local recovery workflow JSON files."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from profile_utils import repo_path


SCHEMA_PATH = repo_path("schema/recovery_workflow.schema.json")
DEFAULT_WORKFLOW_DIR = repo_path("workflows")


def is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
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
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def collect_paths(paths: list[str]) -> list[Path]:
    if paths:
        candidates = [repo_path(path) for path in paths]
    else:
        candidates = [DEFAULT_WORKFLOW_DIR]

    files: list[Path] = []
    for candidate in candidates:
        if candidate.is_dir():
            files.extend(sorted(candidate.rglob("*.json")))
        elif candidate.suffix == ".json":
            files.append(candidate)
        else:
            raise ValueError(f"not a JSON file or directory: {candidate}")
    return sorted(dict.fromkeys(files))


def validate_object(data: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = set(schema.get("required", []))
    properties = schema.get("properties", {})

    for field in sorted(required):
        if field not in data:
            errors.append(f"missing required field: {field}")

    for field in sorted(set(data) - set(properties)):
        errors.append(f"unknown field not allowed by schema: {field}")

    for field, value in data.items():
        field_schema = properties.get(field)
        if not field_schema:
            continue
        expected_type = field_schema.get("type")
        if expected_type is not None and not type_matches(value, expected_type):
            errors.append(f"invalid type for {field}: expected {expected_type}, got {type(value).__name__}")
        if "enum" in field_schema and value not in field_schema["enum"]:
            errors.append(f"invalid value for {field}: {value}")
        if field_schema.get("format") == "date" and not validate_date(value):
            errors.append(f"invalid date for {field}: expected YYYY-MM-DD")

    phases = data.get("phases")
    if isinstance(phases, list):
        phase_ids = [phase.get("phase_id") for phase in phases if isinstance(phase, dict)]
        if len(phase_ids) != len(set(phase_ids)):
            errors.append("phase_id values must be unique")

    if data.get("workflow_type") == "passive_tftp_put":
        mapping = data.get("profile_mapping") if isinstance(data.get("profile_mapping"), dict) else {}
        methods = mapping.get("recovery_methods") if isinstance(mapping.get("recovery_methods"), list) else []
        if "tftp_passive" not in methods:
            errors.append("passive_tftp_put workflow must map to recovery method tftp_passive")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Local workflow .json files or directories. Defaults to workflows/**/*.json.")
    args = parser.parse_args()

    try:
        paths = collect_paths(args.paths)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not paths:
        print("No workflow JSON files found.")
        return 0

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    issues: list[tuple[str, str]] = []
    checked = 0
    for path in paths:
        checked += 1
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append((str(path), f"invalid JSON: {exc}"))
            continue
        if not isinstance(data, dict):
            issues.append((str(path), "workflow file must contain a JSON object"))
            continue
        for error in validate_object(data, schema):
            issues.append((str(path), error))

    print(f"Checked {checked} workflow file(s).")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for path, message in issues:
            print(f"{path}: {message}")
        return 1

    print("No workflow validation issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
