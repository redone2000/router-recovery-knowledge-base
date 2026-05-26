# ASUS RT-AX86U App Export Readiness

Date: 2026-05-26
Status: App-facing draft export generated from reviewed candidate

## Decision

`APP_EXPORT_DRAFT_READY_FOR_INTERNAL_APP_INTEGRATION`

The RT-AX86U reviewed candidate can produce an App-facing implementation draft, provided the App treats it as reviewed-candidate guidance and not final production guidance.

## Inputs

- `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`
- `tools/export_app_profile.py`
- `docs/app_upgrade_field_contract.md`
- `reports/app_copy_upload_complete_vs_recovery_complete_2026-05-17.md`

## Output

- `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`

## Tooling Change

`tools/export_app_profile.py` now accepts:

```text
--source-profile-status incoming|reviewed
```

This prevents reviewed-candidate exports from being mislabeled as `incoming`.

The export stop line was also generalized from RT-AC86U-specific wording to:

```text
Do not generalize observations from this profile to other ASUS models.
```

## Export Command

```text
python3 tools/export_app_profile.py \
  --profile-id asus-rt-ax86u-1-0-merlin \
  --input reviewed/asus-rt-ax86u-1-0-merlin.jsonl \
  --output app_exports/examples/asus_rt_ax86u_app_profile_draft.json \
  --source-profile-status reviewed
```

## Readiness Checks

The generated export preserves:

- `source_profile_status: reviewed`
- `production_allowed: false`
- `final_allowed: false`
- `review_required: true`
- `confidence_level: medium`
- `firmware_version: unknown`
- `applies_to_all_firmware_versions: false`
- observation-only groups
- post-upload wait and power-cycle guidance
- configuration-retention non-guarantee
- Passive TFTP only
- no Active TFTP claim
- no Web Recovery claim
- no firmware binaries or private local paths

## App Copy Requirements

The App must still show:

- Upload completion is not recovery completion.
- Wait several minutes before any power action.
- A normal power cycle may be required before DHCP/admin return.
- Configuration retention is not guaranteed.
- Ping/TTL is not enough by itself.
- This reviewed candidate is not final and must not be generalized to RT-AC86U, stock ASUSWRT, other hardware revisions, or other regions.

## Remaining Boundary

Do not write `final/`.

Do not call this App-ready production guidance until final publication is explicitly approved.
