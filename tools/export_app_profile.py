#!/usr/bin/env python3
"""Export a recovery profile into an App-facing implementation draft."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from profile_utils import iter_jsonl, repo_path, safe_write_text


DEFAULT_PROFILE_ID = "asus-rt-ac86u-unknown-unknown"
DEFAULT_INPUT = "incoming/asus-rt-ac86u-unknown-unknown.jsonl"


def load_profile(path: Path, profile_id: str) -> dict[str, Any]:
    for record in iter_jsonl(path):
        if record.json_error:
            raise ValueError(f"{path}:{record.line_number}: invalid JSONL: {record.json_error}")
        if record.data and record.data.get("id") == profile_id:
            return record.data
    raise ValueError(f"profile not found: {profile_id} in {path}")


def pick(profile: dict[str, Any], field: str) -> Any:
    value: Any = profile
    for part in field.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def build_export(profile: dict[str, Any]) -> dict[str, Any]:
    network = profile.get("network_recovery") if isinstance(profile.get("network_recovery"), dict) else {}
    button = profile.get("button_recovery") if isinstance(profile.get("button_recovery"), dict) else {}
    firmware_source = profile.get("firmware_source") if isinstance(profile.get("firmware_source"), dict) else {}
    firmware_details = profile.get("firmware_details") if isinstance(profile.get("firmware_details"), dict) else {}
    tftp = profile.get("tftp_details") if isinstance(profile.get("tftp_details"), dict) else {}
    post_upload = profile.get("post_upload_behavior") if isinstance(profile.get("post_upload_behavior"), dict) else {}
    outcomes = profile.get("observed_outcomes") if isinstance(profile.get("observed_outcomes"), dict) else {}

    return {
        "export_metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "export_type": "app_profile_implementation_draft",
            "source_profile_id": profile.get("id"),
            "source_profile_status": "incoming",
            "production_allowed": False,
            "final_allowed": False,
            "review_required": True,
            "notes": "Generated for App upgrade integration testing only. This is not final guidance.",
        },
        "device_selection": {
            "profile_id": profile.get("id"),
            "vendor": profile.get("vendor"),
            "model": profile.get("model"),
            "hardware_version": profile.get("hardware_version"),
            "firmware_version": profile.get("firmware_version"),
            "applies_to_all_firmware_versions": profile.get("applies_to_all_firmware_versions"),
            "device_type": profile.get("device_type"),
            "confidence_level": profile.get("confidence_level"),
            "tags": profile.get("tags") or [],
        },
        "risk_and_scope": {
            "known_issues": profile.get("known_issues") or [],
            "risk_warnings": profile.get("risk_warnings") or [],
            "observation_only_groups": profile.get("observation_only_groups") or [],
            "source_evidence_count": len(profile.get("source_evidence") or []),
            "review_notes": profile.get("review_notes"),
        },
        "firmware_preparation": {
            "official_download_page_url": firmware_source.get("official_download_page_url"),
            "official_download_page_region": firmware_source.get("official_download_page_region"),
            "official_download_page_model": firmware_source.get("official_download_page_model"),
            "source_type": firmware_source.get("source_type"),
            "file_type": firmware_details.get("file_type"),
            "official_format": firmware_details.get("official_format"),
            "checksum_available": firmware_source.get("checksum_available"),
            "checksum_algorithms": firmware_source.get("checksum_algorithms") or [],
            "version_selection_guidance": firmware_source.get("version_selection_guidance"),
            "risk_warning": firmware_source.get("risk_warning"),
            "binary_stored": firmware_source.get("binary_stored"),
        },
        "macos_preflight": {
            "client_ip_assignment": network.get("client_ip_assignment"),
            "client_static_ip": network.get("client_static_ip"),
            "client_static_cidr": network.get("client_static_cidr"),
            "default_subnet": network.get("default_subnet"),
            "local_network_permission_warning": "Initial macOS Local Network permission denial can appear as sendto() No route to host.",
            "file_picker_required": True,
            "wired_interface_required": True,
            "wifi_can_remain_available": True,
            "wired_service_priority_or_route_check_required": True,
        },
        "physical_setup": {
            "required_lan_port": network.get("required_lan_port"),
            "button_name": button.get("button_name"),
            "entry_method": button.get("entry_method"),
            "press_duration_seconds_min": button.get("press_duration_seconds_min"),
            "press_duration_seconds_max": button.get("press_duration_seconds_max"),
            "led_indicator": button.get("led_indicator"),
        },
        "readiness": {
            "recovery_ip": network.get("default_ip"),
            "expected_ttl": network.get("rescue_ping_ttl"),
            "ping_signal_strength": "weak",
            "readiness_warning": "Ping and TTL can support readiness but must not be the sole success or failure signal.",
        },
        "transfer": {
            "recovery_methods": profile.get("recovery_methods") or [],
            "passive_tftp_from_router": network.get("passive_tftp_from_router"),
            "active_tftp_to_router": network.get("active_tftp_to_router"),
            "runtime_tftp_direction_field": "transfer.tftp_direction",
            "runtime_role_fields": ["transfer.mac_role", "transfer.router_role"],
            "listen_port": network.get("listen_port"),
            "tftp_mode": tftp.get("mode"),
            "filename_required": tftp.get("filename_required"),
            "accepted_filename_examples": tftp.get("accepted_filename_examples") or [],
            "server_uses_ephemeral_port": tftp.get("server_uses_ephemeral_port"),
            "port_behavior": tftp.get("port_behavior"),
            "ack_source_port": tftp.get("ack_source_port"),
            "client_behavior_requirement": tftp.get("client_behavior_requirement"),
        },
        "post_upload": {
            "wait_seconds": post_upload.get("wait_seconds"),
            "power_cycle_required": post_upload.get("power_cycle_required"),
            "dhcp_after_power_cycle": post_upload.get("dhcp_after_power_cycle"),
            "gateway_ip_as_admin_url": post_upload.get("gateway_ip_as_admin_url"),
            "user_warning_after_upload": post_upload.get("user_warning_after_upload"),
        },
        "outcome_guidance": {
            "config_retention_observed": outcomes.get("config_retention_observed"),
            "factory_reset_observed": outcomes.get("factory_reset_observed"),
            "firmware_downgrade_supported": outcomes.get("firmware_downgrade_supported"),
            "known_recovery_variants": outcomes.get("known_recovery_variants") or [],
            "do_not_infer_config_state_from_transfer_success": True,
        },
        "runtime_attempt_mapping": {
            "schema": "schema/app_runtime_attempt.schema.json",
            "recommended_export_for_internal_testing": True,
            "local_only_by_default": True,
            "private_paths_redacted": True,
            "serials_redacted": True,
        },
        "stop_lines": [
            "Do not present this export as final production guidance.",
            "Do not generalize RT-AC86U observations to RT-AX86U or other ASUS models.",
            "Do not claim all hardware or firmware versions are covered.",
            "Do not store firmware binaries or private local file paths.",
            "Do not infer configuration retention or factory reset from transfer success.",
        ],
        "source_trace": [
            {
                "source_type": evidence.get("source_type"),
                "source_url": evidence.get("source_url"),
                "source_document": evidence.get("source_document"),
                "supports_fields": evidence.get("supports_fields") or [],
                "notes": evidence.get("notes"),
            }
            for evidence in profile.get("source_evidence") or []
            if isinstance(evidence, dict)
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-id", default=DEFAULT_PROFILE_ID)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default="app_exports/examples/asus_rt_ac86u_app_profile_draft.json")
    args = parser.parse_args()

    try:
        profile = load_profile(repo_path(args.input), args.profile_id)
        exported = build_export(profile)
        safe_write_text(repo_path(args.output), json.dumps(exported, indent=2, ensure_ascii=False) + "\n")
    except (ValueError, FileExistsError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote App profile export: {repo_path(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
