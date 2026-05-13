# Claude Code Stage 1 Workflow Evidence Quality Review Batch 1

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

The project is currently prioritizing Recovery Knowledge System structure over broad model expansion. Workflow evidence may support reusable workflow abstraction, but it must not become model-specific profile guidance without explicit model-level evidence.

## Scope

Review only.

Do not browse the web.
Do not collect new sources.
Do not generate incoming profiles.
Do not edit workflow files.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/data/workflow_source_index.stage1.batch1.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_workflow_evidence_indexing_batch1_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/batch1/tplink_faq_1482_web_recovery.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/batch1/asus_faq_1000814_rescue_mode.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/batch1/ubiquiti_edgerouter_tftp_recovery.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/batch1/tplink_faq_2571_post_upload.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/web_recovery.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/passive_tftp_put.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/post_upload_phase.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_knowledge_system_architecture.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/evidence_lifecycle.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_priority_strategy.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/WORKFLOW.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/validate_workflow_source_index.py`

## Facts Already Established By Codex Review

- OpenClaw stayed within workflow source-indexing scope and did not generate profiles.
- Codex accepted four workflow-level/context-level sources into `data/workflow_source_index.stage1.batch1.jsonl`.
- Codex did not accept the DD-WRT Wiki TFTP Flash entry into the index because the URL returned an inaccessible/error page during verification.
- TP-Link FAQ 1482 is treated as Archer AX series-level Web Recovery evidence, not Archer AX55 model evidence.
- ASUS FAQ 1000814 is treated as brand-level Web Recovery / Post-upload abstraction evidence, not model-specific ASUS evidence.
- Ubiquiti EdgeRouter TFTP Recovery is treated as Passive TFTP PUT workflow evidence because it explicitly describes the router running a TFTP server and the workstation using a TFTP client to upload.
- TP-Link FAQ 2571 is retained as `indexed_context_only` and `workflow_update_allowed=false` because it is about failed firmware update progress, not recovery-mode upload.
- No indexed source in this batch is profile-generation eligible.

Treat these as claims to verify against local files. If you disagree, request changes.

## Review Questions

1. Are all four indexed rows correctly classified by source type, workflow target, and applicability scope?
2. Is `workflow-src-stage1-batch1-001` safe to use for Web Recovery workflow abstraction only?
3. Is `workflow-src-stage1-batch1-002` safe to use for both Web Recovery and Post-upload workflow abstraction?
4. Is `workflow-src-stage1-batch1-003` strong enough evidence for the Passive TFTP PUT workflow pattern?
5. Is `workflow-src-stage1-batch1-005` correctly restricted to context-only status with `workflow_update_allowed=false`?
6. Should any workflow files be updated from this evidence, or should the evidence remain indexed without workflow modification?
7. Are there profile-pollution risks from series-level, brand-level, or context-only evidence?
8. Are the source notes sufficiently clear about why profile generation is blocked?
9. Is `validate_workflow_source_index.py` sufficient to prevent future workflow source indexes from allowing profile generation?
10. Does this batch comply with the Recovery Priority Strategy, especially collecting by workflow coverage gap rather than arbitrary model expansion?
11. What is the next safe OpenClaw task, if any?
12. Should model expansion remain paused?

## Expected Review Posture

Be strict about profile boundaries.

The highest risk is that workflow evidence becomes model-specific app guidance without model-level evidence.

Do not recommend broad model collection.

Prefer one of these outcomes:

- keep evidence indexed only
- allow narrow workflow-document updates
- request source-index corrections
- block further collection until tooling/rules are fixed

## Output Format

# Claude Code Stage 1 Workflow Evidence Quality Review Batch 1

Task ID: stage1-workflow-evidence-quality-review-batch1
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

### workflow-src-stage1-batch1-001

- workflow target:
- applicability scope:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-batch1-002

- workflow target:
- applicability scope:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-batch1-003

- workflow target:
- applicability scope:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-batch1-005

- workflow target:
- applicability scope:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

## 3. Workflow Impact

### web_recovery

- evidence impact:
- whether workflow update is allowed:
- required wording guardrails:

### passive_tftp_put

- evidence impact:
- whether workflow update is allowed:
- required wording guardrails:

### post_upload_phase

- evidence impact:
- whether workflow update is allowed:
- required wording guardrails:

## 4. Profile Pollution Risk

- series-level evidence risk:
- brand-level evidence risk:
- context-only evidence risk:
- whether any profile generation is allowed:
- whether any reviewed/final movement is allowed:

## 5. Tooling Review

- validate_workflow_source_index.py:
- missing validation rules:
- source note quality:
- report quality:

## 6. Recovery Priority Strategy Assessment

- does the batch align with workflow coverage gap collection:
- does it avoid arbitrary model expansion:
- does it support current brand priority:
- should model expansion remain paused:

## 7. Required Corrections

If any source index rows should be changed, list exact row IDs and field-level corrections.

Do not edit files.
Do not write `final/`.

## 8. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to keep this workflow source index batch
- whether Codex should update any workflow files
- whether OpenClaw should continue workflow evidence indexing
- what exact next OpenClaw task should be assigned, if any
- what Codex should fix next, if anything

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming profile generation:
- no reviewed writes:
- no final writes:
- no profile approval:
