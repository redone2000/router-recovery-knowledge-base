# ASUS RT-AC86U Reviewed-Candidate Migration Plan

Date: 2026-05-14
Status: prepared, not executed

## Candidate

```text
incoming/asus-rt-ac86u-unknown-unknown.jsonl
```

## Current Decision

Migration is prepared but not authorized.

The profile is ready for Owner confirmation, but it is not yet approved for `reviewed/` movement.

## Preconditions Already Met

- `tools/validate_profiles.py incoming` passes.
- `tools/validate_system_links.py` passes.
- `tools/report_reference_validation.py` reports:
  - `ready_for_owner_confirmation: true`
  - `ready_for_reviewed_migration: false`
  - `migration_requires_owner_confirmation: true`
  - `final_write_allowed: false`
- No blocking incidents are linked to the RT-AC86U profile.
- `reviewed/` and `final/` currently contain no profile files.

## Preconditions Still Required

Explicit Owner confirmation of all checklist items in:

```text
reports/asus_rt_ac86u_reference_validation_owner_checklist.md
```

Required confirmation wording:

```text
RT-AC86U checklist 11 items confirmed. Approve reviewed-candidate migration only. Do not write final.
```

Equivalent clear confirmation is acceptable.

## Migration Scope

Allowed after Owner confirmation:

- create reviewed-candidate copy under `reviewed/`
- preserve the incoming file unless Owner explicitly asks to move rather than copy
- add lifecycle decision record
- run validators with reviewed allowed

Forbidden:

- do not write `final/`
- do not raise confidence above `medium`
- do not fill hardware version or firmware version
- do not set `applies_to_all_firmware_versions` to true
- do not remove observation-only labels
- do not remove risk warnings
- do not generalize this profile to other ASUS models

## Fields To Preserve Exactly

These values must remain unchanged:

| Field | Required Value |
| --- | --- |
| `hardware_version` | `unknown` |
| `firmware_version` | `unknown` |
| `applies_to_all_firmware_versions` | `null` |
| `confidence_level` | `medium` |
| `source_type` | `personal_testing` |
| `blocking_incidents` | `[]` |

Observation-only groups must remain:

- `button_recovery`
- `network_recovery`
- `tftp_details`
- `firmware_details`
- `post_upload_behavior`
- `observed_outcomes`

## Proposed Reviewed File

Recommended reviewed-candidate path:

```text
reviewed/asus-rt-ac86u-unknown-unknown.jsonl
```

The reviewed copy should update only review metadata:

- `reviewed_by`: `owner`
- `reviewed_date`: current date
- `review_notes`: explicitly state reviewed-candidate status, observed-only scope, and final prohibition

No other profile facts should change.

## Proposed Lifecycle Decision

Append a decision to:

```text
data/profile_lifecycle_decisions.jsonl
```

Decision shape:

```json
{
  "decision_id": "decision-2026-05-14-asus-rt-ac86u-reviewed-candidate",
  "profile_id": "asus-rt-ac86u-unknown-unknown",
  "decision": "reviewed_candidate_allowed",
  "decision_scope": "incoming_to_reviewed",
  "reason": "Owner confirmed RT-AC86U lab observations and approved reviewed-candidate migration only. Hardware and firmware scope remain unknown; observed-only limits remain in force.",
  "decision_date": "2026-05-14",
  "decided_by": "owner",
  "next_allowed_action": "create_reviewed_candidate_only",
  "prohibited_actions": ["write_final", "raise_confidence", "generalize_to_other_asus_models", "remove_observation_only_labels"],
  "notes": "Reviewed-candidate status is not final App guidance."
}
```

## Validation Commands After Migration

Run:

```text
python3 tools/validate_profiles.py incoming reviewed
python3 tools/validate_system_links.py --allow-reviewed
python3 tools/report_reference_validation.py --output reports/asus_rt_ac86u_reference_validation_readiness_after_reviewed_2026-05-14.json
git diff --check
```

Do not run with `--allow-final` because `final/` must remain empty.

## Stop Conditions

Stop and do not migrate if:

- Owner confirmation is ambiguous
- any checklist item is rejected
- validation fails before migration
- reviewed copy would require factual changes
- any action would write `final/`
