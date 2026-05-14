# OpenClaw Stage 1 TP-Link / ASUS Official Workflow Evidence Batch 2 Review

Date: 2026-05-14
Prepared by: Codex

## Decision

Accepted with corrections.

OpenClaw found four useful official workflow evidence sources. All are correctly blocked from profile generation. Codex normalized workflow targets before indexing because `tftp_recovery` is not a project workflow enum.

## Corrections Applied

1. `workflow-src-stage1-tplink-asus-batch2-002` changed from `workflow_target: web_recovery,tftp_recovery` to primary `web_recovery` with `workflow_targets: ["web_recovery", "active_tftp_server"]`.
2. `workflow-src-stage1-tplink-asus-batch2-003` changed from `tftp_recovery` to `active_tftp_server`.
3. Source notes were added for all four accepted sources.
4. All rows keep `profile_generation_allowed=false`.

## Accepted Sources

### workflow-src-stage1-tplink-asus-batch2-001

- source: TP-Link FAQ 3062
- decision: accepted as series-level Web Recovery evidence
- allowed use: Omada Gateway Emergency Mode workflow abstraction
- prohibited use: model-specific profile generation

### workflow-src-stage1-tplink-asus-batch2-002

- source: TP-Link FAQ 3186
- decision: accepted as series-level Web Recovery and Active TFTP evidence
- allowed use: EAP recovery workflow abstraction and TFTP direction evidence
- prohibited use: profile generation for any listed EAP model without model-level review

### workflow-src-stage1-tplink-asus-batch2-003

- source: TP-Link FAQ 2954
- decision: accepted as series-level Active TFTP evidence
- allowed use: Pharos TFTP workflow abstraction
- prohibited use: model-specific Pharos profile generation

### workflow-src-stage1-tplink-asus-batch2-004

- source: ASUS FAQ 1033090
- decision: accepted as series-level ASUS Lyra Rescue Mode / Post-upload evidence
- allowed use: Rescue Mode and Post-upload workflow abstraction
- prohibited use: generalizing to all ASUS routers or generating Lyra profiles

## Workflow Impact

This batch strengthens official evidence for:

- Web Recovery
- Active TFTP / device-as-client recovery
- Rescue Mode
- Post-upload phase

Recommended next gate: Claude Code review before changing workflow JSON files.

## Profile Impact

Profile-generation eligible sources: 0.

No `incoming/`, `reviewed/`, or `final/` movement is allowed from this batch.

## Safety Confirmation

- no incoming writes: yes
- no reviewed writes: yes
- no final writes: yes
- no profile generation: yes
- no inferred model facts: yes
- no router IP access by Codex: yes
- no TFTP/UDP packets by Codex: yes
