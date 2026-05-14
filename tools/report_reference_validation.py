#!/usr/bin/env python3
"""Report reference-device validation readiness for an incoming profile."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from profile_utils import iter_jsonl, load_enums, load_schema, repo_path, safe_write_text
from validate_profiles import validate_profile


DEFAULT_PROFILE_ID = "asus-rt-ac86u-unknown-unknown"
DEFAULT_INPUT = "incoming/asus-rt-ac86u-unknown-unknown.jsonl"


def load_profile(path: Path, profile_id: str) -> dict[str, Any]:
    for record in iter_jsonl(path):
        if record.json_error:
            raise ValueError(f"{path}:{record.line_number}: invalid JSONL: {record.json_error}")
        if record.data and record.data.get("id") == profile_id:
            return record.data
    raise ValueError(f"profile not found: {profile_id} in {path}")


def check_rt_ac86u_guardrails(profile: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    if profile.get("confidence_level") != "medium":
        issues.append("confidence_level must remain medium for reviewed-candidate readiness")
    if profile.get("hardware_version") != "unknown":
        issues.append("hardware_version must remain unknown unless directly evidenced")
    if profile.get("firmware_version") != "unknown":
        issues.append("firmware_version must remain unknown unless directly evidenced")
    if profile.get("applies_to_all_firmware_versions") is not None:
        issues.append("applies_to_all_firmware_versions must remain null unless directly evidenced")

    expected_groups = {
        "button_recovery",
        "network_recovery",
        "tftp_details",
        "firmware_details",
        "post_upload_behavior",
        "observed_outcomes",
    }
    observed_groups = set(profile.get("observation_only_groups") or [])
    missing_groups = sorted(expected_groups - observed_groups)
    if missing_groups:
        issues.append(f"missing observation_only_groups: {', '.join(missing_groups)}")

    for field in expected_groups:
        value = profile.get(field)
        if isinstance(value, dict) and value.get("observation_only") is not True:
            issues.append(f"{field}.observation_only must be true")

    if profile.get("blocking_incidents"):
        issues.append("blocking_incidents must be empty before reviewed-candidate migration")

    firmware_source = profile.get("firmware_source") if isinstance(profile.get("firmware_source"), dict) else {}
    if not firmware_source.get("official_download_page_url"):
        issues.append("firmware_source.official_download_page_url is required before reviewed-candidate migration")
    if firmware_source.get("binary_stored") is not False:
        issues.append("firmware_source.binary_stored must be false")
    if not firmware_source.get("checksum_available"):
        issues.append("firmware_source.checksum_available should be true when the official page provides checksums")

    post_upload = profile.get("post_upload_behavior") if isinstance(profile.get("post_upload_behavior"), dict) else {}
    if post_upload.get("power_cycle_required") is not True:
        issues.append("post_upload_behavior.power_cycle_required must remain true")
    if post_upload.get("wait_seconds") != 180:
        issues.append("post_upload_behavior.wait_seconds should remain 180 unless new evidence changes it")
    if post_upload.get("dhcp_after_power_cycle") is not True:
        issues.append("post_upload_behavior.dhcp_after_power_cycle must remain true")
    if post_upload.get("gateway_ip_as_admin_url") is not True:
        issues.append("post_upload_behavior.gateway_ip_as_admin_url must remain true")

    warnings = " ".join(str(item).lower() for item in profile.get("risk_warnings") or [])
    for required_text in ("upload completion", "power", "configuration", "ping"):
        if required_text not in warnings:
            issues.append(f"risk_warnings must mention {required_text}")

    if profile.get("source_type") == "personal_testing":
        evidence = profile.get("source_evidence")
        if not isinstance(evidence, list) or len(evidence) < 2:
            issues.append("personal_testing reviewed-candidate readiness requires at least two source_evidence entries")

    return issues


def build_report(profile: dict[str, Any], schema_errors: list[str], guardrail_issues: list[str]) -> dict[str, Any]:
    owner_confirmation_required = [
        "lab observations are accurate for the tested RT-AC86U unit",
        "profile remains scoped to observed/tested behavior only",
        "hardware_version remains unknown",
        "firmware_version remains unknown",
        "applies_to_all_firmware_versions remains null",
        "confidence_level medium is acceptable for reviewed-candidate status",
        "post-upload warning and manual power-cycle behavior are accurate",
        "configuration outcome remains mixed/uncertain",
        "ping and previous LAN IP are not reliable failure signals",
        "official firmware source is identified and firmware binaries are not stored",
        "reviewed status is approved only as reviewed-candidate data, not final guidance",
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "profile_id": profile.get("id"),
        "input_file": DEFAULT_INPUT,
        "ready_for_owner_confirmation": not schema_errors and not guardrail_issues,
        "ready_for_reviewed_migration": False,
        "migration_requires_owner_confirmation": True,
        "final_write_allowed": False,
        "schema_errors": schema_errors,
        "guardrail_issues": guardrail_issues,
        "owner_confirmation_required": owner_confirmation_required,
        "preserve_fields": {
            "confidence_level": "medium",
            "hardware_version": "unknown",
            "firmware_version": "unknown",
            "applies_to_all_firmware_versions": None,
            "firmware_source.binary_stored": False,
            "observation_only_groups": profile.get("observation_only_groups"),
        },
        "next_action": "Owner must confirm the checklist before Codex prepares any reviewed-candidate migration.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-id", default=DEFAULT_PROFILE_ID)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default="reports/asus_rt_ac86u_reference_validation_readiness.json")
    args = parser.parse_args()

    try:
        profile = load_profile(repo_path(args.input), args.profile_id)
        schema = load_schema()
        enums = load_enums()
        schema_errors = validate_profile(profile, schema, enums, allow_derived=True)
        guardrail_issues = check_rt_ac86u_guardrails(profile)
        report = build_report(profile, schema_errors, guardrail_issues)
        safe_write_text(repo_path(args.output), json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    except (ValueError, FileExistsError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote reference validation report: {repo_path(args.output)}")
    print(f"Ready for owner confirmation: {report['ready_for_owner_confirmation']}")
    print(f"Ready for reviewed migration: {report['ready_for_reviewed_migration']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
