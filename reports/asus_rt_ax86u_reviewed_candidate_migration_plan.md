# ASUS RT-AX86U Reviewed-Candidate Migration Plan

Date: 2026-05-26
Status: prepared, not executed

## Candidate

No profile draft exists yet.

Current evidence inputs:

- `lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`
- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md`
- `reports/asus_rt_ax86u_profile_candidate_guardrails_2026-05-17.md`
- `reports/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`

## Current Decision

Claude Code review accepted the evidence for a candidate profile draft after Owner confirmation.

This does not authorize:

- writing `final/`
- publishing an App-ready final profile
- generalizing RT-AX86U behavior to RT-AC86U
- generalizing Merlin behavior to stock ASUSWRT
- treating LAN1, ACK port behavior, power-cycle requirement, or configuration retention as universal

## Preconditions Already Met

- 2026-05 reference-device evidence batch is committed.
- RT-AX86U reviewed-candidate prompt is committed.
- Claude Code review report is saved under `reports/`.
- `tools/validate_runtime_attempts.py runtime_attempts` passes.
- `tools/validate_profiles.py incoming` passes.
- `tools/validate_incidents.py incidents` passes.
- `tools/validate_system_links.py` passes.

## Preconditions Still Required

Explicit Owner confirmation of all checklist items:

1. The live-session and runtime-attempt observations are accurate.
2. Any draft scope must be limited to ASUS RT-AX86U H/W Ver. 1.0 running ASUSWRT-Merlin, based on the tested evidence.
3. `confidence_level: medium` is acceptable for this candidate.
4. Configuration retention is not guaranteed and must remain observation-only.
5. Web Recovery is not supported by this evidence and must be represented as not observed or unknown, not as proven absent across all states.
6. Active TFTP / router-pulls-firmware is not supported by this evidence.
7. Passive TFTP PUT is supported by this evidence for the tested unit.
8. LAN1, ACK source port 69, fixed server port behavior, post-upload power cycle, and retained configuration must remain observation-only.
9. No final profile publication is approved.

Suggested confirmation wording:

```text
RT-AX86U checklist 9 items confirmed. Approve candidate draft preparation only. Do not write final.
```

Equivalent clear confirmation is acceptable.

## Allowed After Owner Confirmation

- Create an RT-AX86U candidate draft in `incoming/`.
- Preserve all observation-only boundaries.
- Add lifecycle decision record if the repo's existing lifecycle pattern requires it.
- Run validators after draft creation.

## Forbidden

- Do not write `final/`.
- Do not write `reviewed/` unless Owner explicitly approves reviewed-candidate migration after seeing the draft.
- Do not raise confidence above `medium`.
- Do not set `applies_to_all_firmware_versions` to true.
- Do not remove observation-only labels.
- Do not remove risk warnings.
- Do not store firmware binaries, firmware local paths, serial numbers, MAC addresses, Wi-Fi passwords, admin passwords, or router backups.
- Do not generalize this profile to RT-AC86U, stock ASUSWRT, other RT-AX86U hardware revisions, or other regional variants.

## Draft Field Direction

Recommended candidate identity:

```text
asus-rt-ax86u-1-0-merlin
```

Field constraints:

| Field | Required treatment |
| --- | --- |
| `vendor` | `ASUS` |
| `model` | `RT-AX86U` |
| `hardware_version` | `1.0` |
| `firmware_version` | keep specific tested versions in evidence/notes; do not imply all firmware |
| `applies_to_all_firmware_versions` | `false` |
| `confidence_level` | `medium` maximum |
| `source_type` | `personal_testing` |
| `recovery_methods` | include passive TFTP only |
| `firmware_source.binary_stored` | `false` |

Observation-only groups must include:

- `button_recovery`
- `network_recovery`
- `tftp_details`
- `firmware_details`
- `post_upload_behavior`
- `observed_outcomes`

## Mandatory Warnings

Any draft must warn:

- Upload completion is not recovery completion.
- Wait several minutes after upload before power action.
- Manual power cycle may be required after the wait.
- DHCP/admin UI may not return until after power cycle.
- Configuration retention is not guaranteed.
- Web Recovery was not observed.
- Active TFTP was not observed or supported by this evidence.
- LAN1 was tested, but other LAN ports were not evaluated.
- Use only model-matched official ASUSWRT-Merlin firmware for this evidence scope.
- Use extracted `.w` firmware image, not a `.zip` archive.

## Validation Commands After Draft Preparation

Run:

```text
python3 tools/validate_profiles.py incoming
python3 tools/validate_system_links.py
git diff --check
```

Do not run or rely on any `--allow-final` path because `final/` must remain untouched.

## Stop Conditions

Stop and do not draft if:

- Owner confirmation is ambiguous.
- Any checklist item is rejected.
- The draft would require weakening or hiding the observation-only boundaries.
- The draft would require writing `reviewed/` or `final/`.
- The draft would require new live router testing.
