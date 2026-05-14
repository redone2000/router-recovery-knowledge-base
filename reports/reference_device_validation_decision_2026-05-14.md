# Reference Device Validation Decision

Date: 2026-05-14
Prepared by: Codex

## Decision

Pause Stage 1 official workflow evidence search and move to reference device validation process design.

The first validation candidate is:

```text
incoming/asus-rt-ac86u-unknown-unknown.jsonl
```

## Why

Claude Code reviewed the ASUS Rescue gap-search evidence and recommended pausing further official evidence search for now.

The project has enough indexed workflow evidence to define the next gate:

```text
incoming profile candidate
  -> reference device validation
  -> reviewed candidate
```

This does not mean `final/` is unlocked.

## Current RT-AC86U Status

- location: `incoming/`
- source type: `personal_testing`
- confidence level: `medium`
- hardware version: `unknown`
- firmware version: `unknown`
- applies to all firmware versions: `null`
- observed-only groups: present
- reviewed candidate: not yet
- final data: prohibited

## Required Before Reviewed Promotion

1. Run profile and system-link validators.
2. Confirm no blocking incidents are linked.
3. Confirm all personal-testing evidence is accurately represented.
4. Confirm hardware/firmware scope remains unknown unless directly evidenced.
5. Confirm post-upload power-cycle warnings remain prominent.
6. Receive explicit Owner confirmation that reviewed-candidate promotion is allowed.
7. Record a lifecycle decision.

## Non-Goals

- Do not expand new models.
- Do not continue broad official source searching.
- Do not write `final/`.
- Do not generalize RT-AC86U observations to all ASUS routers.

## Next Task

Prepare an Owner review checklist for RT-AC86U reference device validation. The checklist should be short, concrete, and limited to the minimum confirmations needed before any `reviewed/` movement.
