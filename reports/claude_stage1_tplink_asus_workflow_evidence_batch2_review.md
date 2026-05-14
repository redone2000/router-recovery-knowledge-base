# Claude Code Stage 1 TP-Link / ASUS Workflow Evidence Batch 2 Review

Task ID: stage1-tplink-asus-workflow-evidence-batch2-review
Date: 2026-05-14
Scope: review only, no collection, no profile generation

## Executive Decision

`WORKFLOW_EVIDENCE_ACCEPTED_INDEX_ONLY`

All four indexed sources are correctly classified, properly bounded, and provide high-quality official evidence for workflow abstraction. No source is eligible for profile generation. Immediate workflow JSON updates are not required.

## Source Review

### workflow-src-stage1-tplink-asus-batch2-001

- workflow target: `web_recovery`
- applicability scope: `series_level` TP-Link Omada Gateway
- decision: accepted as valid official workflow evidence
- allowed use: Web Recovery abstraction, TP-Link Omada brand-system research, static IP pattern validation
- prohibited use: Omada model-specific profile parameters or model-validated guidance

### workflow-src-stage1-tplink-asus-batch2-002

- workflow targets: `web_recovery`, `active_tftp_server`
- applicability scope: `series_level` TP-Link EAP Access Point
- decision: accepted as valid official dual-workflow evidence
- allowed use: Web Recovery and Active TFTP Server abstraction, TFTP direction validation, EAP brand-system research
- prohibited use: EAP profile generation, generalizing filename requirements, or model-validated guidance

### workflow-src-stage1-tplink-asus-batch2-003

- workflow target: `active_tftp_server`
- applicability scope: `series_level` TP-Link Pharos Outdoor Products
- decision: accepted as valid official Active TFTP evidence
- allowed use: Active TFTP Server workflow definition validation and firmware filename pattern analysis
- prohibited use: Pharos profile generation or assuming `recovery.bin` is universal

### workflow-src-stage1-tplink-asus-batch2-004

- workflow targets: `rescue_mode`, `post_upload_phase`
- applicability scope: `series_level` ASUS Lyra Mesh WiFi
- decision: accepted as valid official workflow evidence
- allowed use: Rescue Mode abstraction, Post-upload Phase pattern validation, ASUS brand-system research
- prohibited use: generalizing Lyra behavior to all ASUS routers or generating Lyra profiles

## Workflow Impact

### web_recovery

Evidence is significantly strengthened by two additional official TP-Link series sources. Updates are optional but not required.

### active_tftp_server

Evidence is strong for TP-Link-specific Active TFTP Server behavior. Do not draft `active_tftp_server.json` yet; collect at least one additional official non-TP-Link source first.

### rescue_mode

ASUS Lyra evidence strengthens ASUS brand patterns, but Rescue Mode remains too brand-specific for a standalone workflow file.

### post_upload_phase

ASUS Lyra evidence incrementally strengthens post-upload phase patterns, but no immediate workflow update is required.

## Profile Pollution Risk

Risk remains low because all sources are series-level, profile generation is explicitly disabled, and evidence gaps are documented. No reviewed/final movement is allowed.

## Tooling / Schema Feedback

Claude recommended adding an optional `independent_source_count` field to workflow source index records to support maturity assessment.

Codex follow-up:

- `independent_source_count` is now required by the local workflow source-index validator.
- Existing workflow source-index rows should set `independent_source_count: 1`.

## Recommendation To Owner

Keep this batch. Do not update workflow JSON files now. Do not draft `active_tftp_server.json` yet. Continue limited official workflow evidence indexing only for:

1. non-TP-Link official Active TFTP recovery documentation
2. additional ASUS non-Lyra Rescue Mode documentation
3. official documentation distinguishing recovery behavior across hardware versions

Model expansion remains paused.

## Safety Confirmation

- no web browsing: yes
- no new source collection: yes
- no incoming profile generation: yes
- no reviewed writes: yes
- no final writes: yes
- no profile approval: yes
