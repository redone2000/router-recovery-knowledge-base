# Claude Code Stage 1 Evidence Quality Review Batch 1

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

Stage 1 evidence-quality review for source index batch 1.

## Scope

Review the indexed sources and decide whether they are suitable for profile-preparation planning.

This task is review-only.

Do not collect new sources.
Do not browse the web.
Do not generate incoming profiles.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/data/source_index.stage1.batch1.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_source_index_batch1_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/source_scope_policy.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/stage1/batch1/tplink_faq_1482.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/stage1/batch1/tplink_archer_ax55_download.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/stage1/batch1/netgear_kb_000059633.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_profile.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`

## Review Questions

1. Is each source index row correctly classified by `applicability_scope`?
2. Are `profile_generation_allowed` and `profile_generation_blockers` correct?
3. Are the `recovery_methods_claimed` values justified by the source note and current evidence policy?
4. Are evidence snippets short enough and not app-ready instructions?
5. Is any source over-claiming applicability to the candidate model?
6. Does any source justify entering profile-preparation planning?
7. What extra source(s) are required before an incoming profile can be generated?
8. Is the TP-Link FAQ 1482 handling correct as series-level only?
9. Is the NETGEAR KB 000059633 handling correct as model-level for R7000 but still blocked?
10. Are there any schema/tooling gaps revealed by this batch?

## Expected Review Posture

Be strict. The project must not produce misleading recovery guidance.

Do not approve profile generation unless the evidence is clearly model-specific, scope-safe, and sufficient under current rules.

If evidence is useful but not profile-ready, mark it as source-index-ready only.

## Output Format

# Claude Code Stage 1 Evidence Quality Review Batch 1

Task ID: stage1-evidence-quality-review-batch1
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `SOURCE_INDEX_ACCEPTED_PROFILE_PREP_BLOCKED`
- `SOURCE_INDEX_ACCEPTED_PROFILE_PREP_ALLOWED_FOR_SELECTED`
- `REQUEST_SOURCE_INDEX_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Source-by-Source Review

For each source:

### source_id

- candidate:
- applicability_scope:
- source_type:
- profile_generation_allowed:
- decision:
- issues:
- required next evidence:

## 3. Candidate Readiness

For each candidate:

### TP-Link Archer AX55

- current readiness:
- strongest source:
- blockers:
- next required source:

### NETGEAR R7000

- current readiness:
- strongest source:
- blockers:
- next required source:

## 4. Evidence Policy Findings

- TFTP direction policy:
- series-level source handling:
- model-level source handling:
- source snippet quality:
- profile-generation blocker quality:

## 5. Required Corrections

If any source index rows should be changed, list exact row IDs and field-level corrections.

Do not edit `final/`.

## 6. Schema / Tooling Suggestions

List any schema or validation changes needed before profile preparation.

## 7. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to keep these sources
- whether to collect more sources
- whether any candidate should advance toward incoming profile preparation
- what OpenClaw should do next

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming profile generation:
- no reviewed writes:
- no final writes:
- no profile approval:
