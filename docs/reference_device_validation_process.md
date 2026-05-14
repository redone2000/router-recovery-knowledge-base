# Reference Device Validation Process

Date: 2026-05-14
Status: Stage 1 governance draft

## Purpose

Reference device validation is the process for deciding whether an `incoming/` profile candidate can become a `reviewed/` candidate.

It is not final approval.

The goal is to validate a small number of reference devices deeply enough to stabilize workflow abstractions and App guidance rules before expanding model coverage.

## Current First Candidate

First validation candidate:

```text
incoming/asus-rt-ac86u-unknown-unknown.jsonl
```

Reason:

- it is based on detailed Owner lab observation
- it exposed a critical post-upload phase requirement
- it is useful for ASUS Rescue Mode / Passive TFTP / Post-upload workflow research
- it has explicit observation-only groups and risk warnings

It must not move to `reviewed/` until Owner confirmation and review gates are complete.

## Validation Gates

### Gate 1: Schema And Tooling

Required:

- `tools/validate_profiles.py incoming`
- `tools/validate_system_links.py`
- no blocked incidents linked to the candidate
- no writes to `final/`

Pass criteria:

- no validation errors
- unknown hardware/firmware scope is explicit
- observed-only groups are marked

### Gate 2: Evidence Integrity

Required:

- each claimed recovery method has source evidence
- each source evidence item supports the listed fields
- personal-testing evidence is clearly marked
- source snippets do not overclaim beyond observation

Pass criteria:

- evidence supports the profile fields
- no AI-inferred IP, filename, timing, hardware version, firmware version, or TFTP direction
- source type limits confidence correctly

### Gate 3: Scope And Generalization

Required:

- hardware version scope reviewed
- firmware version scope reviewed
- observed-only behavior not generalized
- brand-level or workflow-level evidence kept separate from model profile facts

Pass criteria:

- `hardware_version: "unknown"` remains if not evidenced
- `firmware_version: "unknown"` remains if not evidenced
- `applies_to_all_firmware_versions` remains null unless directly evidenced
- all observed-only groups remain labeled

### Gate 4: App Guidance Safety

Required:

- risk warnings cover user-visible failure modes
- post-upload behavior is explicit
- ping and previous LAN IP limitations are documented
- configuration retention uncertainty is documented

Pass criteria:

- App guidance would not imply guaranteed success
- App guidance would not imply guaranteed config retention or factory reset
- App guidance would not recommend early retry/power-cycle unless profile evidence supports it

### Gate 5: Owner Confirmation

Required Owner confirmations:

- lab observations are accurate for the tested unit
- confidence level is acceptable with unknown hardware/firmware scope
- profile is applicable only to tested/observed units until broader evidence exists
- moving to `reviewed/` is approved as reviewed-candidate status, not final data

Pass criteria:

- explicit Owner approval recorded in a report or lifecycle decision
- no automatic final promotion

## Promotion Rule

Promotion from `incoming/` to `reviewed/` requires:

- all gates passed
- explicit Owner confirmation
- a lifecycle decision record
- no unresolved blocking incident

`final/` remains prohibited without a separate final approval process.

## Reviewed Candidate Requirements

If promoted, the reviewed candidate must preserve:

- `confidence_level: "medium"` maximum for personal testing with unknown scope
- `hardware_version: "unknown"` unless directly evidenced
- `firmware_version: "unknown"` unless directly evidenced
- `applies_to_all_firmware_versions: null`
- `observation_only_groups`
- risk warnings about post-upload wait, power cycle, ping unreliability, and mixed configuration retention

## Do Not Do

- Do not backfill unknown hardware or firmware values.
- Do not generalize RT-AC86U observations to all ASUS routers.
- Do not use official ASUS brand-level sources as proof of RT-AC86U macOS behavior.
- Do not write `final/`.
- Do not start long-tail model expansion before this validation process is exercised.
