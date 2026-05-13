#!/usr/bin/env python3
"""Validate cross-links and gate rules across profiles, incidents, and workflows."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from profile_utils import iter_jsonl, repo_path


def load_profiles(directory: str) -> dict[str, dict[str, Any]]:
    root = repo_path(directory)
    profiles: dict[str, dict[str, Any]] = {}
    if not root.exists():
        return profiles
    for path in sorted(root.glob("*.jsonl")):
        for record in iter_jsonl(path):
            if record.json_error or record.data is None:
                continue
            profile_id = record.data.get("id")
            if isinstance(profile_id, str):
                profile = dict(record.data)
                profile["_file"] = str(path.relative_to(repo_path(".")))
                profiles[profile_id] = profile
    return profiles


def load_json_objects(directory: str, key: str) -> dict[str, dict[str, Any]]:
    root = repo_path(directory)
    objects: dict[str, dict[str, Any]] = {}
    if not root.exists():
        return objects
    for path in sorted(root.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        object_id = data.get(key)
        if isinstance(object_id, str):
            item = dict(data)
            item["_file"] = str(path.relative_to(repo_path(".")))
            objects[object_id] = item
    return objects


def load_lifecycle_decisions() -> list[dict[str, Any]]:
    path = repo_path("data/profile_lifecycle_decisions.jsonl")
    if not path.exists():
        return []
    decisions: list[dict[str, Any]] = []
    for record in iter_jsonl(path):
        if record.json_error or record.data is None:
            continue
        decisions.append(dict(record.data))
    return decisions


def has_pause_decision(profile_id: str, decisions: list[dict[str, Any]]) -> bool:
    return any(decision.get("profile_id") == profile_id and decision.get("decision") in {"paused", "blocked"} for decision in decisions)


def listed_files(directory: str) -> list[Path]:
    root = repo_path(directory)
    if not root.exists():
        return []
    return [path for path in root.rglob("*") if path.is_file()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-reviewed", action="store_true", help="Allow reviewed/ files.")
    parser.add_argument("--allow-final", action="store_true", help="Allow final/ files.")
    args = parser.parse_args()

    incoming = load_profiles("incoming")
    reviewed = load_profiles("reviewed")
    final = load_profiles("final")
    profiles = {**incoming, **reviewed, **final}
    incidents = load_json_objects("incidents", "incident_id")
    workflows = load_json_objects("workflows", "workflow_id")
    decisions = load_lifecycle_decisions()
    issues: list[str] = []

    if listed_files("reviewed") and not args.allow_reviewed:
        issues.append("reviewed/ contains files but --allow-reviewed was not set")
    if listed_files("final") and not args.allow_final:
        issues.append("final/ contains files but --allow-final was not set")

    for incident_id, incident in incidents.items():
        linked_profile = incident.get("linked_profile_id")
        if linked_profile and linked_profile not in profiles:
            issues.append(f"incident {incident_id} links missing profile: {linked_profile}")
        if incident.get("profile_gate") == "blocked":
            if linked_profile and not has_pause_decision(str(linked_profile), decisions):
                issues.append(f"blocked incident {incident_id} lacks paused/blocked lifecycle decision for profile {linked_profile}")
            blocked_gates = incident.get("blocked_gates")
            if not isinstance(blocked_gates, list) or not blocked_gates:
                issues.append(f"blocked incident {incident_id} must include blocked_gates")

    for workflow_id, workflow in workflows.items():
        for incident_id in workflow.get("incident_links", []) if isinstance(workflow.get("incident_links"), list) else []:
            if incident_id not in incidents:
                issues.append(f"workflow {workflow_id} links missing incident: {incident_id}")
        for failure in workflow.get("failure_modes", []) if isinstance(workflow.get("failure_modes"), list) else []:
            if not isinstance(failure, dict):
                continue
            for incident_id in failure.get("linked_incidents", []) if isinstance(failure.get("linked_incidents"), list) else []:
                if incident_id not in incidents:
                    issues.append(f"workflow {workflow_id} failure {failure.get('failure_id')} links missing incident: {incident_id}")

    for profile_id, profile in profiles.items():
        for workflow_id in profile.get("linked_workflows", []) if isinstance(profile.get("linked_workflows"), list) else []:
            if workflow_id not in workflows:
                issues.append(f"profile {profile_id} links missing workflow: {workflow_id}")
        for incident_id in profile.get("blocking_incidents", []) if isinstance(profile.get("blocking_incidents"), list) else []:
            if incident_id not in incidents:
                issues.append(f"profile {profile_id} links missing blocking incident: {incident_id}")
        if profile_id in incoming and has_pause_decision(profile_id, decisions):
            blocking = profile.get("blocking_incidents")
            if not isinstance(blocking, list) or not blocking:
                issues.append(f"paused incoming profile {profile_id} must list blocking_incidents")
        if profile_id in reviewed or profile_id in final:
            for incident in incidents.values():
                if incident.get("linked_profile_id") == profile_id and incident.get("profile_gate") == "blocked":
                    issues.append(f"profile {profile_id} is reviewed/final but has blocked linked incident {incident.get('incident_id')}")

    print(f"Checked {len(profiles)} profile(s), {len(incidents)} incident(s), {len(workflows)} workflow(s).")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for issue in issues:
            print(issue)
        return 1
    print("No system link validation issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
