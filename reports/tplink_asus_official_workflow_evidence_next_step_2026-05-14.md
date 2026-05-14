# TP-Link / ASUS Official Workflow Evidence Next Step

Date: 2026-05-14
Prepared by: Codex

## Decision

Return workflow evidence collection focus to TP-Link and ASUS.

NETGEAR NMRP remains research-only because official NETGEAR NMRP evidence was not found. The next higher-leverage work is to strengthen official-source evidence for Web Recovery, Rescue Mode, and Post-upload Phase using TP-Link and ASUS sources.

## Rationale

TP-Link and ASUS currently have stronger official-source paths:

- TP-Link has official Archer AX series Web Recovery evidence.
- ASUS has official Rescue Mode / Firmware Restoration evidence.
- Both brands can strengthen reusable workflow abstraction without needing model-profile generation.

This aligns with the Recovery Priority Strategy:

```text
Recovery Foundations
  -> Recovery Workflow Types
  -> Brand Recovery Worlds
  -> Reference Devices
  -> Family Expansion
```

## Task Prepared

OpenClaw task file:

`prompts/agent_tasks/openclaw_stage1_tplink_asus_official_workflow_evidence_batch2.md`

## Scope Boundary

The task is official-source workflow indexing only.

It must not:

- generate profiles
- write `incoming/`, `reviewed/`, or `final/`
- use community sources as substitutes
- infer model-specific facts
- duplicate already indexed sources unless materially new official content exists

## Expected Outcome

Either:

1. additional official TP-Link / ASUS workflow evidence is indexed, or
2. a clear no-additional-evidence result is recorded.

Both outcomes are useful for deciding when workflow documents are mature enough for controlled refinement.
