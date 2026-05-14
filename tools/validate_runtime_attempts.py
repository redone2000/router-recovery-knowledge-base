#!/usr/bin/env python3
"""Validate App runtime recovery attempt JSON files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from profile_utils import repo_path


SCHEMA_PATH = "schema/app_runtime_attempt.schema.json"
DEFAULT_SCAN_DIRS = ("runtime_attempts",)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


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


def collect_paths(paths: list[str]) -> list[Path]:
    if paths:
        candidates = [repo_path(path) for path in paths]
    else:
        candidates = [repo_path(directory) for directory in DEFAULT_SCAN_DIRS]

    files: list[Path] = []
    for candidate in candidates:
        if candidate.is_dir():
            files.extend(sorted(candidate.rglob("*.json")))
        elif candidate.suffix == ".json":
            files.append(candidate)
        else:
            raise ValueError(f"not a JSON file or directory: {candidate}")

    return sorted(dict.fromkeys(files))


def privacy_errors(attempt: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    firmware = attempt.get("firmware_file") if isinstance(attempt.get("firmware_file"), dict) else {}
    privacy = attempt.get("privacy") if isinstance(attempt.get("privacy"), dict) else {}

    if firmware.get("local_path_recorded") is not False:
        errors.append("firmware_file.local_path_recorded must be false")
    if privacy.get("local_only_by_default") is not True:
        errors.append("privacy.local_only_by_default must be true")
    if privacy.get("private_paths_redacted") is not True:
        errors.append("privacy.private_paths_redacted must be true")
    if privacy.get("serials_redacted") is not True:
        errors.append("privacy.serials_redacted must be true")

    filename = firmware.get("filename_recorded")
    if isinstance(filename, str) and ("/" in filename or "\\" in filename):
        errors.append("firmware_file.filename_recorded must not contain a local path")

    device = attempt.get("device") if isinstance(attempt.get("device"), dict) else {}
    if device.get("serial_number_recorded") is True and privacy.get("serials_redacted") is not True:
        errors.append("serial numbers must be redacted before export")

    return errors


def validate_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parts = value.split("-")
    return len(parts) == 3 and all(part.isdigit() for part in parts)


def validate_schema_value(value: Any, schema: dict[str, Any], path: str) -> list[str]:
    errors: list[str] = []

    expected_type = schema.get("type")
    if expected_type is not None and not type_matches(value, expected_type):
        errors.append(f"{path}: expected {expected_type}, got {type(value).__name__}")
        return errors

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: invalid value {value!r}")

    if schema.get("format") == "date" and not validate_date(value):
        errors.append(f"{path}: expected YYYY-MM-DD date")

    if isinstance(value, dict) and schema.get("type") == "object":
        properties = schema.get("properties", {})
        required = set(schema.get("required", []))
        for field in sorted(required):
            if field not in value:
                errors.append(f"{path}.{field}: missing required field")
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


def validate_attempt(path: Path, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        attempt = load_json(path)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]

    if not isinstance(attempt, dict):
        return ["attempt JSON must be an object"]

    errors.extend(validate_schema_value(attempt, schema, "<root>"))
    errors.extend(privacy_errors(attempt))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Runtime attempt JSON files or directories")
    args = parser.parse_args()

    try:
        schema = load_json(repo_path(SCHEMA_PATH))
        paths = collect_paths(args.paths)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    total_errors = 0
    for path in paths:
        errors = validate_attempt(path, schema)
        if errors:
            total_errors += len(errors)
            for error in errors:
                print(f"{path}: {error}")

    print(f"Checked {len(paths)} runtime attempt file(s).")
    if total_errors:
        print(f"Found {total_errors} validation issue(s).", file=sys.stderr)
        return 1
    print("No validation issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
