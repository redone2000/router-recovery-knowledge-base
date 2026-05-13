# Claude Code Stage 1 Ontology and Workflow Review

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

Stage 1 ontology / workflow architecture review.

The project has shifted from model-count collection toward a Recovery Knowledge System with source indexes, incidents, workflows, profiles, and evidence lifecycle gates.

## Scope

Review only.

Do not browse the web.
Do not collect new sources.
Do not generate or edit profiles.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_knowledge_system_architecture.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_language.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/evidence_lifecycle.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_incident.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_workflow.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_profile.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/passive_tftp_put.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/post_upload_phase.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/web_recovery.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/incidents/lab/netgear_r7000_ttl100_tftp_timeout_2026-05-13.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/data/profile_lifecycle_decisions.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/validate_incidents.py`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/validate_workflows.py`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/report_system_status.py`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/WORKFLOW.md`

## Review Questions

1. Does the ontology cleanly separate source index, incident, workflow, profile, reviewed, and final data?
2. Are incidents prevented from becoming profile guidance too early?
3. Are workflows correctly represented as reusable abstractions, not App-ready instructions?
4. Is `passive_tftp_put` correctly modeling weak readiness signals like TTL/ping?
5. Is `web_recovery` sufficiently conservative with series-level TP-Link evidence?
6. Is `post_upload_phase` correctly representing upload-complete versus recovery-complete distinction?
7. Does the incident schema capture reasoning path well enough: symptom, context, hypothesis, experiment, result, next action?
8. Are status values (`observed-only`, `unresolved`, `blocked`, `draft`) semantically clear?
9. Are validator rules sufficient to prevent R7000 from moving forward while blocked?
10. Are there fields missing for future App/SEO/AI assistant use?
11. Are any fields over-modeled or likely to create maintenance burden?
12. What should be fixed before Stage 1 broadens source collection again?

## Expected Review Posture

Be strict about preventing knowledge pollution.

The highest risk is that raw incident evidence or draft workflow language becomes user-facing recovery guidance without review.

Do not recommend expanding model coverage unless the ontology and gates are adequate.

## Output Format

# Claude Code Stage 1 Ontology and Workflow Review

Task ID: stage1-ontology-workflow-review
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `ONTOLOGY_APPROVED_FOR_CONTROLLED_WORKFLOW_EVIDENCE_INDEXING`
- `ONTOLOGY_APPROVED_WITH_CHANGES_BEFORE_COLLECTION`
- `REQUEST_ONTOLOGY_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Architecture Assessment

- source/index layer:
- incident layer:
- workflow layer:
- profile layer:
- reviewed/final gates:
- evidence lifecycle:

## 3. Schema Review

### recovery_incident.schema.json

- decision:
- missing fields:
- over-modeled fields:
- gate risks:

### recovery_workflow.schema.json

- decision:
- missing fields:
- over-modeled fields:
- gate risks:

### recovery_profile.schema.json integration

- decision:
- integration gaps:

## 4. Workflow Review

### passive_tftp_put

- decision:
- issues:
- required changes:

### post_upload_phase

- decision:
- issues:
- required changes:

### web_recovery

- decision:
- issues:
- required changes:

## 5. R7000 Incident / Gate Review

- is R7000 correctly blocked:
- is the incident useful:
- does the workflow capture the lesson:
- any required changes:

## 6. Tooling Review

- validate_incidents.py:
- validate_workflows.py:
- report_system_status.py:
- missing tooling:

## 7. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether ontology is ready for controlled workflow evidence indexing
- whether OpenClaw may index workflow evidence under strict limits
- what Codex should fix first
- whether model expansion should remain paused

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming writes:
- no reviewed writes:
- no final writes:
- no profile approval:
