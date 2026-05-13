# ASUS RT-AC86U Observation Guardrails

Date: 2026-05-13
Prepared by: Codex

## Decision

Claude Code accepted the ASUS RT-AC86U incoming draft as eligible for reviewed-candidate migration only after explicit Owner confirmation.

Codex did not migrate the draft to `reviewed/` in this step.

## Changes Applied Before Owner Gate

- Added `observation_only` to observed behavior field groups in the schema.
- Marked ASUS RT-AC86U observed field groups with `observation_only: true`.
- Added validator guardrails:
  - `personal_testing` profiles cannot use `high` or `verified` confidence.
  - Unknown hardware or firmware scope must be reflected in known issues or risk warnings.
  - Profiles requiring post-upload power cycle must include a prominent user warning.

## Owner Confirmation Still Required

Before reviewed-candidate migration, Owner must confirm:

- The lab observations are accurate for the tested RT-AC86U unit.
- `confidence_level: medium` is acceptable with unknown hardware/firmware scope.
- The profile should be treated as applicable only to tested units until broader scope is verified.

## Safety Boundaries

- No `reviewed/` write was performed.
- No `final/` write was performed.
- No new collection was started.
