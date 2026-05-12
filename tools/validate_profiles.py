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

from profile_utils import LEGACY_DERIVED_FIELDS, add_common_path_args, collect_jsonl_paths, iter_jsonl, load_enums, load_schema


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
    allowed_fields = set(properties)
    if allow_derived:
        allowed_fields.update(LEGACY_DERIVED_FIELDS)

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
    elif not isinstance(source_evidence, list):
        errors.append("source_evidence must be an array")
    else:
        evidence_supported_fields: set[str] = set()
        for index, evidence in enumerate(source_evidence):
            if not isinstance(evidence, dict):
                errors.append(f"source_evidence[{index}] must be an object")
                continue
            evidence_source_type = evidence.get("source_type")
            if evidence_source_type not in enums.get("source_type", set()):
                errors.append(f"invalid source_evidence[{index}].source_type: {evidence_source_type}")
            if not is_non_empty(evidence.get("snippet")):
                errors.append(f"source_evidence[{index}].snippet must be non-empty")
            if not is_non_empty(evidence.get("source_url")) and not is_non_empty(evidence.get("source_document")):
                errors.append(f"source_evidence[{index}] must include source_url or source_document")
            supports_fields = evidence.get("supports_fields")
            if isinstance(supports_fields, list):
                evidence_supported_fields.update(str(field) for field in supports_fields)

        if isinstance(methods, list):
            for method in methods:
                if method not in evidence_supported_fields and "recovery_methods" not in evidence_supported_fields:
                    errors.append(f"missing source_evidence support for recovery method: {method}")

    network_recovery = profile.get("network_recovery")
    if isinstance(network_recovery, dict):
        for field in ("default_ip", "client_static_ip"):
            if not validate_ip(network_recovery.get(field)):
                errors.append(f"invalid IP address in network_recovery.{field}: {network_recovery.get(field)}")
        passive = network_recovery.get("passive_tftp_from_router")
        active = network_recovery.get("active_tftp_to_router")
        if passive is True and active is True:
            errors.append("network_recovery.passive_tftp_from_router and active_tftp_to_router cannot both be true")
        if isinstance(methods, list) and ("tftp_active" in methods or "tftp_passive" in methods):
            if passive is None and active is None:
                errors.append("TFTP recovery method listed but both TFTP direction fields are unknown")
            if "tftp_passive" in methods and passive is not True:
                errors.append("tftp_passive listed but network_recovery.passive_tftp_from_router is not true")
            if "tftp_active" in methods and active is not True:
                errors.append("tftp_active listed but network_recovery.active_tftp_to_router is not true")
    elif isinstance(methods, list) and ("tftp_active" in methods or "tftp_passive" in methods):
        errors.append("TFTP recovery method listed but network_recovery is missing")

    if confidence in {"high", "verified"}:
        if profile.get("hardware_version") == "unknown":
            errors.append("confidence_level cannot be high or verified when hardware_version is unknown")
        if profile.get("firmware_version") == "unknown":
            errors.append("confidence_level cannot be high or verified when firmware_version is unknown")

    method_detail_requirements = {
        "uart_serial": "uart_details",
        "web_ui": "web_recovery",
        "button_reset": "button_recovery",
    }
    if isinstance(methods, list):
        for method, detail_field in method_detail_requirements.items():
            if method in methods and not is_non_empty(profile.get(detail_field)):
                errors.append(f"{method} listed but {detail_field} is missing or empty")

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
