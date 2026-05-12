# Source Scope Policy

Date: 2026-05-12
Prepared by: Codex

## Purpose

Some official sources describe a vendor family or router series rather than one exact model. TP-Link FAQ 1482 is the current example: it discusses Archer AX series recovery guidance, but does not by itself prove model-specific behavior for `Archer AX55`.

The project should preserve such sources in the source index, but must not turn them directly into model-level recovery profiles.

## Applicability Scope

Every source index entry should classify source scope:

- `vendor_level`: applies to a vendor broadly
- `series_level`: applies to a product series or family
- `model_level`: applies to one exact model
- `hardware_version_level`: applies to one exact model and hardware revision
- `firmware_version_level`: applies to one exact model/hardware scope and firmware version
- `unknown`: scope cannot be determined

## Profile Generation Rule

`vendor_level`, `series_level`, and `unknown` sources may be indexed, but default to:

```json
{
  "profile_generation_allowed": false
}
```

They need `profile_generation_blockers`, such as:

- `series_level_source_not_model_specific`
- `model_specific_applicability_unknown`
- `hardware_version_scope_unknown`
- `firmware_version_scope_unknown`

## Use In App Profiles

Model recovery profiles must remain model/hardware-version oriented. A series-level source can support a profile only after model-specific applicability is confirmed by another source or a human reviewer.

Do not create an incoming profile from a series-level source alone.

## TP-Link FAQ 1482 Handling

TP-Link FAQ 1482 should be indexed as a series-level official source for Archer AX planning. It should not be treated as direct `Archer AX55` profile evidence unless future collection confirms AX55-specific applicability.
