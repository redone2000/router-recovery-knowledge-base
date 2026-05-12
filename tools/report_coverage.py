#!/usr/bin/env python3
"""Generate local coverage and quality reports for router recovery profiles."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

from profile_utils import add_common_path_args, collect_jsonl_paths, dedupe_key, iter_jsonl, load_schema, repo_path, safe_write_text


def missing_fields(profile: dict[str, Any], required_fields: set[str]) -> list[str]:
    missing: list[str] = []
    for field in required_fields:
        value = profile.get(field)
        if value is None or value == "" or value == [] or value == {}:
            missing.append(field)
    if not profile.get("source_evidence"):
        missing.append("source_evidence")
    return sorted(missing)


def conflict_signature(profile: dict[str, Any]) -> dict[str, Any]:
    network = profile.get("network_recovery") if isinstance(profile.get("network_recovery"), dict) else {}
    return {
        "recovery_methods": sorted(profile.get("recovery_methods", [])) if isinstance(profile.get("recovery_methods"), list) else [],
        "default_ip": network.get("default_ip"),
        "default_subnet": network.get("default_subnet"),
        "tftp_filename": network.get("tftp_filename"),
    }


def build_report(paths: list[str]) -> dict[str, Any]:
    schema = load_schema()
    required_fields = set(schema.get("required", []))
    files = collect_jsonl_paths(paths)

    brands: Counter[str] = Counter()
    models_by_brand: dict[str, Counter[str]] = defaultdict(Counter)
    confidence: Counter[str] = Counter()
    missing: Counter[str] = Counter()
    malformed_records = 0
    total_records = 0
    duplicate_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for path in files:
        for record in iter_jsonl(path):
            total_records += 1
            if record.json_error or record.data is None:
                malformed_records += 1
                continue
            profile = record.data
            brand = str(profile.get("vendor") or "UNKNOWN")
            model = str(profile.get("model") or "UNKNOWN")
            brands[brand] += 1
            models_by_brand[brand][model] += 1
            confidence[str(profile.get("confidence_level") or "MISSING")] += 1
            for field in missing_fields(profile, required_fields):
                missing[field] += 1
            duplicate_groups[dedupe_key(profile)].append(
                {
                    "file": str(record.path),
                    "line": record.line_number,
                    "id": profile.get("id"),
                    "signature": conflict_signature(profile),
                }
            )

    conflicts = []
    duplicate_count = 0
    for key, entries in duplicate_groups.items():
        if len(entries) < 2:
            continue
        duplicate_count += len(entries)
        signatures = {json.dumps(entry["signature"], sort_keys=True) for entry in entries}
        if len(signatures) > 1:
            conflicts.append({"dedupe_key": key, "entries": entries})

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_files": [str(path) for path in files],
        "profile_count": total_records,
        "valid_json_object_count": total_records - malformed_records,
        "malformed_record_count": malformed_records,
        "brand_count": len(brands),
        "model_count": sum(len(models) for models in models_by_brand.values()),
        "brands": dict(sorted(brands.items())),
        "models_by_brand": {brand: dict(sorted(models.items())) for brand, models in sorted(models_by_brand.items())},
        "confidence_distribution": dict(sorted(confidence.items())),
        "missing_fields": dict(sorted(missing.items())),
        "duplicate_profile_record_count": duplicate_count,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_path_args(parser)
    parser.add_argument("--output", default="reports/coverage_report.json", help="Report path. Must not already exist.")
    args = parser.parse_args()

    try:
        report = build_report(args.paths)
        output_path = repo_path(args.output)
        safe_write_text(output_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    except (ValueError, FileExistsError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote coverage report: {output_path}")
    print(f"Profiles: {report['profile_count']}; brands: {report['brand_count']}; models: {report['model_count']}; conflicts: {report['conflict_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
