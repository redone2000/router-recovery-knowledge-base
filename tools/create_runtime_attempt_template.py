#!/usr/bin/env python3
"""Create a blank App runtime attempt JSON template for lab testing."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date

from profile_utils import repo_path, safe_write_text


def slug(value: str) -> str:
    cleaned = []
    for char in value.lower():
        if char.isalnum():
            cleaned.append(char)
        else:
            cleaned.append("-")
    return "-".join(part for part in "".join(cleaned).split("-") if part)


def build_template(vendor: str, model: str, workflow: str, profile_id: str | None, attempt_date: str) -> dict:
    attempt_id = f"{slug(vendor)}-{slug(model)}-{slug(workflow)}-{attempt_date}"
    return {
        "attempt_id": attempt_id,
        "status": "draft",
        "created_date": attempt_date,
        "profile_id": profile_id,
        "workflow_ids": [workflow],
        "device": {
            "vendor": vendor,
            "model": model,
            "hardware_version": "unknown",
            "firmware_version_before": "unknown",
            "firmware_version_after": "unknown",
            "serial_number_recorded": False,
        },
        "firmware_file": {
            "source_type": "official_vendor_page",
            "official_download_page_url": None,
            "local_path_recorded": False,
            "filename_recorded": None,
            "extension": None,
            "size_bytes": None,
            "appears_compressed": None,
            "checksum_algorithm": None,
            "checksum_status": "not_checked",
            "model_match_confirmed_by_user": None,
        },
        "macos_preflight": {
            "wired_interface_selected": None,
            "wifi_available_during_recovery": True,
            "wired_route_confirmed": None,
            "local_network_permission": "not_checked",
            "file_picker_authorized": None,
            "static_ip_set": None,
            "client_ip": None,
            "client_cidr": None,
            "notes": None,
        },
        "recovery_entry": {
            "method": None,
            "button": None,
            "hold_seconds_observed": None,
            "lan_port_used": None,
            "led_state_observed": None,
            "user_confirmed_recovery_mode": None,
        },
        "readiness_observations": {
            "ping_replied": None,
            "ttl_observed": None,
            "service_probe_attempted": None,
            "service_probe_result": "not_attempted",
            "readiness_signal_strength": "unknown",
            "notes": None,
        },
        "transfer": {
            "method": "unknown",
            "tftp_direction": "unknown",
            "mac_role": "unknown",
            "router_role": "unknown",
            "started": False,
            "completed": False,
            "duration_seconds": None,
            "bytes_sent": None,
            "block_count": None,
            "ack_source_port": None,
            "server_uses_ephemeral_port_observed": None,
            "required_filename": None,
            "first_packet_timing": None,
            "retry_pattern": None,
            "retry_effect": "not_tested",
            "error_category": "unknown",
            "error_message": None,
        },
        "post_upload": {
            "wait_completed": None,
            "wait_seconds_actual": None,
            "power_cycle_performed": None,
            "dhcp_restored": None,
            "gateway_detected": None,
            "admin_ui_opened": None,
            "notes": None,
        },
        "outcome": {
            "result": "unknown",
            "firmware_version_after_observed": None,
            "configuration_state": "unknown",
            "incident_candidate": None,
            "incident_reason": None,
        },
        "privacy": {
            "local_only_by_default": True,
            "user_export_approved": False,
            "private_paths_redacted": True,
            "serials_redacted": True,
        },
        "notes": "Draft runtime attempt template. Fill from lab notes before using as evidence.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vendor", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--profile-id", default=None)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    template = build_template(args.vendor, args.model, args.workflow, args.profile_id, args.date)
    try:
        safe_write_text(repo_path(args.output), json.dumps(template, indent=2, ensure_ascii=False) + "\n")
    except FileExistsError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote runtime attempt template: {repo_path(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
