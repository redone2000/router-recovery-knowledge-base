# Codex ASUS RT-AX86U Incoming Draft Review

Date: 2026-05-26
Scope: local review of `incoming/asus-rt-ax86u-1-0-merlin.jsonl`
Status: incoming draft accepted for reviewed-candidate migration request

## Executive Decision

`INCOMING_DRAFT_ACCEPTED_REVIEWED_MIGRATION_REQUEST_ALLOWED`

The RT-AX86U incoming draft matches the Owner-confirmed 9-item checklist, the Claude Code review, and the migration plan. It is suitable to present to Owner for explicit reviewed-candidate migration approval.

This is not final approval.

## Files Reviewed

- `incoming/asus-rt-ax86u-1-0-merlin.jsonl`
- `reports/asus_rt_ax86u_reviewed_candidate_migration_plan.md`
- `reports/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`
- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`

## Checks Performed

Validation commands passed:

```text
python3 tools/validate_runtime_attempts.py runtime_attempts
python3 tools/validate_profiles.py incoming
python3 tools/validate_incidents.py incidents
python3 tools/validate_system_links.py
git diff --check
```

Manual boundary checks:

- `confidence_level` remains `medium`.
- `source_type` remains `personal_testing`.
- `hardware_version` is `1.0`.
- `firmware_version` is `unknown`; tested versions are preserved only in evidence and firmware details.
- `applies_to_all_firmware_versions` is `false`.
- `recovery_methods` includes only `tftp_passive`.
- `firmware_source.binary_stored` is `false`.
- `reviewed_by` and `reviewed_date` remain null.
- No `reviewed/` or `final/` file was written.

## Field Review

### Scope

Accepted.

The draft scopes the profile to ASUS RT-AX86U H/W Ver. 1.0 and ASUSWRT-Merlin evidence, without claiming broad firmware, stock ASUSWRT, region, or all-hardware applicability.

### TFTP Direction

Accepted.

The draft records Passive TFTP PUT only:

- router acts as TFTP server
- Mac/App acts as TFTP client
- router IP `192.168.1.1`
- observed ACK source port `69`
- no active TFTP / router-pulls-firmware support claimed

### Observation-Only Groups

Accepted.

All required groups remain marked observation-only:

- `button_recovery`
- `network_recovery`
- `tftp_details`
- `firmware_details`
- `post_upload_behavior`
- `observed_outcomes`

### Post-Upload Behavior

Accepted.

The draft correctly separates upload completion from recovery completion. It records the observed post-upload wait and normal power-cycle requirement without claiming universal behavior.

### Configuration Retention

Accepted.

The draft records retained configuration as a single observed RT-AX86U outcome, while warning that configuration retention is not guaranteed.

### Web Recovery

Accepted.

The draft says Web Recovery was not observed in the tested TTL=100 state. It does not claim Web Recovery is impossible across all states.

### Firmware Source

Accepted.

The draft uses source metadata only and does not store binaries, local paths, or private artifacts. It warns to use model-matched official ASUSWRT-Merlin firmware and extract the `.w` image.

## Correction Made During Review

The first local draft put tested firmware versions in top-level `firmware_version`. That was too strong for this evidence scope.

The draft was corrected to:

```json
"firmware_version": "unknown"
```

Tested versions remain in `source_evidence`, `firmware_details.known_successful_versions`, and notes.

## Remaining Gate

The next action requires explicit Owner approval for reviewed-candidate migration.

Suggested approval wording:

```text
Approve RT-AX86U reviewed-candidate migration only. Do not write final.
```

If approved, allowed actions are:

- create `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`
- update only review metadata and lifecycle decision records
- run validators with reviewed allowed

Still forbidden:

- writing `final/`
- raising confidence above `medium`
- removing observation-only labels
- removing warnings
- generalizing to RT-AC86U, stock ASUSWRT, other hardware revisions, or other regions

## Recommendation

Ask Owner whether to approve reviewed-candidate migration only.

No more RT-AX86U device testing is needed for this gate.
