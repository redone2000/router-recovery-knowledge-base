# Claude Code Stage 1 TP-Link / ASUS Workflow Evidence Batch 2 Review

You are the Knowledge Architect / Schema Reviewer for the Router Recovery Knowledge project.

## Agent Identity Gate

This task is intended only for: Claude Code.

If you are not this agent, stop immediately and reply only:

WRONG_AGENT_TASK
Expected agent: Claude Code
Your role: [your actual role if known]
No action performed.

Do not reinterpret, adapt, or partially execute this task if your agent identity does not match.

## Current Stage

Stage 1 workflow evidence-quality review.

The project is collecting official TP-Link / ASUS workflow evidence to strengthen reusable workflow abstractions before profile expansion.

## Scope

Review only.

Do not browse the web.
Do not collect new sources.
Do not generate profiles.
Do not edit workflow files.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/data/workflow_source_index.stage1.tplink-asus-batch2.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_tplink_asus_official_workflow_evidence_batch2_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/tplink-asus-batch2/tplink-faq-3062.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/tplink-asus-batch2/tplink-faq-3186.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/tplink-asus-batch2/tplink-faq-2954.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/tplink-asus-batch2/asus-faq-1033090.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/web_recovery.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/post_upload_phase.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/passive_tftp_put.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_workflow.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/validate_workflow_source_index.py`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_priority_strategy.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/evidence_lifecycle.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`

## Facts Already Established By Codex Review

- OpenClaw found four official TP-Link / ASUS workflow evidence sources.
- Codex accepted all four as source-index evidence.
- Codex corrected `tftp_recovery` to `active_tftp_server` because `tftp_recovery` is not a project workflow enum.
- TP-Link FAQ 3186 includes both Web Recovery and Active TFTP evidence.
- TP-Link FAQ 2954 is Active TFTP evidence because the computer runs TFTP server software and the device retrieves `recovery.bin`.
- ASUS FAQ 1033090 supports Rescue Mode and Post-upload Phase abstraction for Lyra series only.
- No source is profile-generation eligible.

Treat these as claims to verify against local files. If you disagree, request corrections.

## Review Questions

1. Are all four indexed rows correctly classified by workflow target and applicability scope?
2. Is `active_tftp_server` the correct workflow target for TP-Link FAQ 3186 and FAQ 2954?
3. Does this batch justify drafting an `active_tftp_server` workflow file, or should it remain indexed only?
4. Does ASUS FAQ 1033090 justify updating `post_upload_phase` or `web/rescue` workflow language?
5. Does TP-Link FAQ 3062 strengthen Web Recovery enough to update `web_recovery.json`?
6. Are any profile-pollution risks present from series-level evidence?
7. Should `rescue_mode` become its own workflow file later, or remain embedded in brand workflows for now?
8. What workflow JSON changes, if any, should Codex make after review?
9. What additional evidence is required before model or family expansion?
10. Should TP-Link / ASUS official workflow indexing continue, or pause after this batch?

## Expected Review Posture

Be strict about not turning series-level evidence into model guidance.

Prefer controlled workflow refinement only if it improves reusable abstraction without implying App-ready profile guidance.

## Output Format

# Claude Code Stage 1 TP-Link / ASUS Workflow Evidence Batch 2 Review

Task ID: stage1-tplink-asus-workflow-evidence-batch2-review
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `WORKFLOW_EVIDENCE_ACCEPTED_INDEX_ONLY`
- `WORKFLOW_EVIDENCE_ACCEPTED_WORKFLOW_UPDATES_ALLOWED`
- `REQUEST_WORKFLOW_SOURCE_INDEX_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Source-by-Source Review

### workflow-src-stage1-tplink-asus-batch2-001

- workflow target:
- applicability scope:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-tplink-asus-batch2-002

- workflow target:
- applicability scope:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-tplink-asus-batch2-003

- workflow target:
- applicability scope:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-tplink-asus-batch2-004

- workflow target:
- applicability scope:
- decision:
- issues:
- allowed use:
- prohibited use:

## 3. Workflow Impact

### web_recovery

- evidence impact:
- whether update is allowed:
- required wording guardrails:

### active_tftp_server

- evidence impact:
- whether workflow draft is allowed:
- required wording guardrails:

### rescue_mode

- evidence impact:
- whether workflow draft is allowed:
- required wording guardrails:

### post_upload_phase

- evidence impact:
- whether update is allowed:
- required wording guardrails:

## 4. Profile Pollution Risk

- series-level evidence risk:
- TFTP direction risk:
- firmware filename risk:
- whether any profile generation is allowed:
- whether any reviewed/final movement is allowed:

## 5. Tooling / Schema Feedback

- workflow source index validation:
- workflow schema:
- missing workflow files:
- recommended changes:

## 6. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to keep this batch
- whether Codex should update workflow JSON files
- whether Codex should draft `active_tftp_server.json`
- whether TP-Link / ASUS official indexing should continue
- whether model expansion remains paused

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming profile generation:
- no reviewed writes:
- no final writes:
- no profile approval:
