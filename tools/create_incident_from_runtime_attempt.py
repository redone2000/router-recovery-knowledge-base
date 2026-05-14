#!/usr/bin/env python3
"""Create an incident candidate from an App runtime attempt JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from profile_utils import repo_path, safe_write_text


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def slug(value: str) -> str:
    cleaned = []
    for char in value.lower():
        if char.isalnum():
            cleaned.append(char)
        else:
            cleaned.append("-")
    return "-".join(part for part in "".join(cleaned).split("-") if part)


def compact(value: Any, fallback: str = "unknown") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text if text else fallback


def observed_signals(attempt: dict[str, Any]) -> list[str]:
    readiness = attempt.get("readiness_observations") if isinstance(attempt.get("readiness_observations"), dict) else {}
    transfer = attempt.get("transfer") if isinstance(attempt.get("transfer"), dict) else {}
    post_upload = attempt.get("post_upload") if isinstance(attempt.get("post_upload"), dict) else {}

    signals: list[str] = []
    if readiness.get("ping_replied") is not None:
        signals.append(f"ping_replied={readiness.get('ping_replied')}")
    if readiness.get("ttl_observed") is not None:
        signals.append(f"ttl_observed={readiness.get('ttl_observed')}")
    if readiness.get("service_probe_result"):
        signals.append(f"service_probe_result={readiness.get('service_probe_result')}")
    if transfer.get("method"):
        signals.append(f"transfer_method={transfer.get('method')}")
    if transfer.get("tftp_direction"):
        signals.append(f"tftp_direction={transfer.get('tftp_direction')}")
    if transfer.get("ack_source_port") is not None:
        signals.append(f"ack_source_port={transfer.get('ack_source_port')}")
    if transfer.get("error_category"):
        signals.append(f"error_category={transfer.get('error_category')}")
    if post_upload.get("gateway_detected"):
        signals.append(f"gateway_detected={post_upload.get('gateway_detected')}")
    return signals or ["runtime attempt captured but no specific signal was recorded"]


def build_incident(attempt: dict[str, Any], symptom: str, created_by: str) -> dict[str, Any]:
    device = attempt.get("device") if isinstance(attempt.get("device"), dict) else {}
    transfer = attempt.get("transfer") if isinstance(attempt.get("transfer"), dict) else {}
    macos = attempt.get("macos_preflight") if isinstance(attempt.get("macos_preflight"), dict) else {}
    outcome = attempt.get("outcome") if isinstance(attempt.get("outcome"), dict) else {}

    vendor = compact(device.get("vendor"))
    model = compact(device.get("model"))
    attempt_id = compact(attempt.get("attempt_id"), "runtime-attempt")
    incident_id = f"{slug(vendor)}-{slug(model)}-{slug(symptom)[:40]}-{slug(compact(attempt.get('created_date')))}"

    workflow_ids = attempt.get("workflow_ids") if isinstance(attempt.get("workflow_ids"), list) else []
    linked_workflow = compact(workflow_ids[0], "unknown") if workflow_ids else "unknown"

    error_category = compact(transfer.get("error_category"))
    error_message = compact(transfer.get("error_message"), "no explicit error message recorded")

    failed_pattern = (
        f"{compact(transfer.get('method'))} attempt completed={transfer.get('completed')} "
        f"with error_category={error_category}; error_message={error_message}"
    )

    return {
        "incident_id": incident_id,
        "status": "observed-only",
        "observation_only": True,
        "resolution": "unresolved",
        "evidence_type": "lab_observation",
        "confidence": "medium",
        "profile_gate": "blocked",
        "blocked_gates": ["incoming_to_reviewed", "reviewed_to_final", "app_guidance"],
        "linked_profile_id": attempt.get("profile_id"),
        "linked_workflow": linked_workflow,
        "vendor": vendor,
        "model": model,
        "hardware_version": compact(device.get("hardware_version")),
        "firmware_version": compact(device.get("firmware_version_before")),
        "symptom": symptom,
        "context": {
            "client_os": "macOS",
            "client_tool": compact(transfer.get("method")),
            "connection": "direct wired recovery attempt",
            "client_ip_assignment": "static" if macos.get("static_ip_set") is True else "unknown",
            "official_path_exists": None,
            "notes": f"Generated from runtime attempt {attempt_id}.",
        },
        "observed_signals": observed_signals(attempt),
        "failed_patterns": [failed_pattern],
        "successful_patterns": [],
        "hypotheses": [
            "Runtime attempt indicates a recovery detail needs review before profile or App guidance promotion",
            "TFTP direction, timing, interface routing, firmware acceptance, or post-upload behavior may require additional testing",
        ],
        "experiments": [
            {
                "name": "runtime-attempt",
                "method": f"Executed App/lab runtime attempt {attempt_id}",
                "result": f"Outcome result={compact(outcome.get('result'))}; transfer completed={transfer.get('completed')}",
                "notes": attempt.get("notes"),
            }
        ],
        "results": [
            "Do not promote this behavior to profile guidance without review",
            "Use this incident to refine App preflight, transfer timing, error mapping, or post-upload guidance",
        ],
        "next_actions": [
            "Review packet/log evidence if available",
            "Repeat with controlled setup if the behavior affects user guidance",
            "Update runtime attempt, incident, workflow, or profile only after review",
        ],
        "source_refs": [],
        "created_date": compact(attempt.get("created_date")),
        "created_by": created_by,
        "notes": "Generated incident candidate from runtime attempt. Review and edit before treating as evidence.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Runtime attempt JSON file")
    parser.add_argument("--output", required=True, help="Incident JSON output path")
    parser.add_argument("--symptom", required=True, help="Short symptom summary")
    parser.add_argument("--created-by", default="owner-lab-observation")
    args = parser.parse_args()

    try:
        attempt = load_json(repo_path(args.input))
        if not isinstance(attempt, dict):
            raise ValueError("runtime attempt must be a JSON object")
        incident = build_incident(attempt, args.symptom, args.created_by)
        safe_write_text(repo_path(args.output), json.dumps(incident, indent=2, ensure_ascii=False) + "\n")
    except (OSError, ValueError, FileExistsError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote incident candidate: {repo_path(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
