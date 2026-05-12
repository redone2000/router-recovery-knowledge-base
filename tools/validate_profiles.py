#!/usr/bin/env python3
"""Validate local router recovery profile JSONL files."""

from __future__ import annotations

import argparse
import ipaddress
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

from profile_utils import (
    DERIVED_FIELDS,
    QUALITY_FIELDS,
    add_common_path_args,
    collect_jsonl_paths,
    iter_jsonl,
    load_enums,
    load_schema,
)


Issue = tuple[str, int, str]


def is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return True


def validate_ip(value: Any) -> bool:
    if value is None or value == "":
        return True
    if not isinstance(value, str):
        return False
    try:
        ipaddress.ip_address(value)
    except ValueError:
        return False
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


def validate_profile(profile: dict[str, Any], schema: dict[str, Any], enums: dict[str, set[str]], allow_derived: bool) -> list[str]:
    errors: list[str] = []
    required = set(schema.get("required", []))
    properties = schema.get("properties", {})
    allowed_fields = set(properties) | QUALITY_FIELDS
    if allow_derived:
        allowed_fields.update(DERIVED_FIELDS)

    for field in sorted(required):
        if field not in profile or not is_non_empty(profile.get(field)):
            errors.append(f"missing required field: {field}")

    unknown_fields = sorted(set(profile) - allowed_fields)
    for field in unknown_fields:
        errors.append(f"unknown field not allowed by schema: {field}")

    for field, value in profile.items():
        if field not in properties:
            continue
        field_schema = properties[field]
        expected_type = field_schema.get("type")
        if expected_type is not None and not type_matches(value, expected_type):
            errors.append(f"invalid type for {field}: expected {expected_type}, got {type(value).__name__}")
        if field_schema.get("format") == "date" and not validate_date(value):
            errors.append(f"invalid date for {field}: expected YYYY-MM-DD")
        pattern = field_schema.get("pattern")
        if pattern and isinstance(value, str) and not re.match(pattern, value):
            errors.append(f"invalid format for {field}: does not match {pattern}")

    methods = profile.get("recovery_methods")
    method_enum = enums.get("recovery_method", set())
    if not isinstance(methods, list) or not methods:
        errors.append("recovery_methods must be a non-empty array")
    else:
        for method in methods:
            if method not in method_enum:
                errors.append(f"invalid recovery_method: {method}")

    family = profile.get("recovery_family")
    if family is not None and family not in enums.get("recovery_family", set()):
        errors.append(f"invalid recovery_family: {family}")

    source_type = profile.get("source_type")
    if source_type is not None and source_type not in enums.get("source_type", set()):
        errors.append(f"invalid source_type: {source_type}")

    confidence = profile.get("confidence_level")
    confidence_enum = enums.get("confidence_levels", set())
    if confidence is not None and confidence not in confidence_enum:
        errors.append(f"invalid confidence_level: {confidence}")

    source_evidence = profile.get("source_evidence")
    if not is_non_empty(source_evidence):
        errors.append("source_evidence must be non-empty")

    network_recovery = profile.get("network_recovery")
    if isinstance(network_recovery, dict):
        for field in ("default_ip",):
            if not validate_ip(network_recovery.get(field)):
                errors.append(f"invalid IP address in network_recovery.{field}: {network_recovery.get(field)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_path_args(parser)
    parser.add_argument("--strict-derived", action="store_true", help="Reject normalized_* and dedupe_key derived fields.")
    args = parser.parse_args()

    try:
        paths = collect_jsonl_paths(args.paths)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not paths:
        print("No JSONL files found.")
        return 0

    schema = load_schema()
    enums = load_enums()
    issues: list[Issue] = []
    checked = 0

    for path in paths:
        for record in iter_jsonl(path):
            checked += 1
            if record.json_error:
                issues.append((str(path), record.line_number, f"invalid JSONL: {record.json_error}"))
                continue
            assert record.data is not None
            for error in validate_profile(record.data, schema, enums, allow_derived=not args.strict_derived):
                issues.append((str(path), record.line_number, error))

    print(f"Checked {checked} JSONL records across {len(paths)} file(s).")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for path, line_number, message in issues:
            print(f"{path}:{line_number}: {message}")
        return 1

    print("No validation issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
