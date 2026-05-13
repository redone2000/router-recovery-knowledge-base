# Claude Code Stage 1 NETGEAR NMRP Workflow Evidence Review

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

Stage 1 workflow evidence-quality review for NETGEAR NMRP.

The project is collecting workflow evidence, not generating model profiles.

## Scope

Review only.

Do not browse the web.
Do not collect new sources.
Do not generate profiles.
Do not draft `workflows/nmrp.json`.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/data/workflow_source_index.stage1.netgear-nmrp.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_netgear_nmrp_workflow_evidence_indexing_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/netgear-nmrp/nmrpflash_github_docs.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/netgear-nmrp/reddit_nmrpflash_wndr3400_guide.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/incidents/lab/netgear_r7000_ttl100_tftp_timeout_2026-05-13.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/passive_tftp_put.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_priority_strategy.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/evidence_lifecycle.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/validate_workflow_source_index.py`

## Facts Already Established By Codex Review

- OpenClaw reported three candidate NMRP sources.
- Codex indexed the nmrpflash GitHub repository as `third_party_repository`, not official documentation.
- Codex retained the Reddit WNDR3400 source as `social_media` and `indexed_context_only`, not as a verified community guide.
- Codex did not index the DD-WRT forum PDF attachment because it was not stable text evidence in this batch.
- No source is profile-generation eligible.
- R7000 remains blocked by an unresolved lab incident and is not approved for reviewed/final movement.

Treat these as claims to verify against local files. If you disagree, request corrections.

## Review Questions

1. Is `workflow-src-stage1-netgear-nmrp-001` correctly classified as `third_party_repository` and brand-level workflow evidence?
2. Is `workflow_update_allowed=true` appropriate for the nmrpflash source, or should it remain index-only until more evidence exists?
3. Is `workflow-src-stage1-netgear-nmrp-002` correctly downgraded to `social_media` and `indexed_context_only`?
4. Was it correct not to index the DD-WRT PDF attachment?
5. Does the current evidence justify drafting a new `nmrp` workflow later?
6. If a future NMRP workflow is allowed, what mandatory guardrails should it include?
7. Does any evidence affect the existing R7000 blocked status?
8. Does NMRP evidence suggest a better future lab retest plan for R7000?
9. Are the workflow source-index validation rules sufficient for NMRP sources?
10. Should OpenClaw collect additional official NETGEAR documentation before any workflow draft?

## Expected Review Posture

Be strict about evidence type and workflow/profile separation.

The main risk is turning third-party tool documentation or social-media reports into App-ready NETGEAR recovery guidance too early.

## Output Format

# Claude Code Stage 1 NETGEAR NMRP Workflow Evidence Review

Task ID: stage1-netgear-nmrp-workflow-evidence-review
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `NMRP_EVIDENCE_ACCEPTED_INDEX_ONLY`
- `NMRP_EVIDENCE_ACCEPTED_WORKFLOW_DRAFT_ALLOWED`
- `REQUEST_NMRP_SOURCE_INDEX_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Source Review

### workflow-src-stage1-netgear-nmrp-001

- source type:
- applicability scope:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-netgear-nmrp-002

- source type:
- applicability scope:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

### workflow-src-stage1-netgear-nmrp-003

- indexed:
- decision:
- reason:
- future requirements:

## 3. NMRP Workflow Readiness

- current readiness:
- whether `workflows/nmrp.json` may be drafted:
- required guardrails:
- required evidence before App guidance:
- evidence still missing:

## 4. R7000 Incident Impact

- does this unblock R7000:
- does this change profile gate:
- lab retest implications:
- recommended next R7000 action:

## 5. Tooling / Schema Feedback

- validate_workflow_source_index.py:
- workflow schema:
- missing fields:
- recommended changes:

## 6. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to keep the NMRP source index
- whether Codex should draft NMRP workflow now or wait
- whether OpenClaw should continue NMRP source indexing
- whether R7000 remains blocked
- what exact next task should be done

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming profile generation:
- no reviewed writes:
- no final writes:
- no profile approval:
