# Claude Code Stage 1 Evidence Quality Review Batch 2

You are the Knowledge Architect / Schema Reviewer for the Router Recovery Knowledge project.

## Current Stage

Stage 1 evidence-quality review for gap-focused source index batch 2.

This batch is focused on whether NETGEAR R7000 now has enough official evidence to move toward incoming profile draft preparation.

## Scope

Review only.

Do not collect new sources.
Do not browse the web.
Do not generate incoming profiles.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/data/source_index.stage1.batch1.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/data/source_index.stage1.batch2.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_source_index_batch1_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_gap_source_index_batch2_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/claude_stage1_evidence_quality_review_batch1.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/source_scope_policy.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/stage1/batch1/netgear_kb_000059633.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/stage1/batch2/netgear_kb_000064624_macos.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_profile.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/enums.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`

## Facts Already Established By Codex Review

- NETGEAR KB 000064624 is an official NETGEAR macOS TFTP article.
- Its applies-to section lists R7000, so Codex corrected the source index from `vendor_level` to `model_level`.
- It supports `contains_macos_guidance=true`.
- It supports `tftp_direction_claimed=tftp_passive` because the Mac acts as a TFTP client and uploads firmware to the router.
- It does not resolve hardware-version or firmware-version applicability.
- `profile_generation_allowed` remains `false` in the source index.

Treat these as claims to verify against the local source notes and indexed data. If you disagree, request changes.

## Review Questions

1. Is `src-stage1-batch2-001` correctly classified as `model_level` for R7000?
2. Is `applies_to_candidate_model=true` justified?
3. Is `tftp_direction_claimed=tftp_passive` justified under the project TFTP evidence rules?
4. Does the combined NETGEAR evidence set now prove that R7000 supports official TFTP firmware recovery on macOS?
5. Are `hardware_version_scope_unknown` and `firmware_version_scope_unknown` still blocking issues?
6. With `hardware_version="unknown"` and `firmware_version="unknown"`, may Codex prepare an `incoming/` draft profile for human review, or must profile preparation remain blocked?
7. If an incoming draft is allowed later, what is the maximum allowed `confidence`?
8. What exact fields must be included or constrained in a safe R7000 incoming draft?
9. Is any additional official/model-specific source required before incoming profile draft preparation?
10. Should TP-Link Archer AX55 remain blocked and out of profile preparation?

## Expected Review Posture

Be strict, but do not over-block if the evidence is already sufficient for an `incoming/` draft clearly marked as unknown-scope and human-review-only.

Distinguish these decisions:

- source indexing accepted
- profile preparation planning allowed
- actual incoming profile generation allowed
- reviewed/final data approval

This task can only recommend whether profile preparation should be allowed. It must not approve reviewed/final data.

## Output Format

# Claude Code Stage 1 Evidence Quality Review Batch 2

Task ID: stage1-evidence-quality-review-batch2
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `SOURCE_INDEX_ACCEPTED_PROFILE_PREP_BLOCKED`
- `SOURCE_INDEX_ACCEPTED_PROFILE_DRAFT_ALLOWED_FOR_R7000`
- `REQUEST_SOURCE_INDEX_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Source Review

### src-stage1-batch2-001

- candidate:
- applicability_scope:
- applies_to_candidate_model:
- source_type:
- tftp_direction_claimed:
- contains_macos_guidance:
- profile_generation_allowed:
- decision:
- issues:
- required next evidence:

## 3. Combined NETGEAR R7000 Readiness

- current readiness:
- evidence supporting R7000 model applicability:
- evidence supporting macOS workflow:
- evidence supporting TFTP direction:
- remaining blockers:
- whether incoming draft is allowed:
- maximum confidence if draft is allowed:

## 4. TFTP Direction Judgment

State clearly:

- Is this App-side active TFTP server mode?
- Or is this Mac-side TFTP client upload mode?
- Which profile field/recovery family should be used?
- What evidence supports that decision?

## 5. Draft Profile Guardrails

If incoming draft preparation is allowed, list mandatory guardrails:

- hardware_version:
- firmware_version:
- recovery_method:
- TFTP direction:
- confidence maximum:
- source_evidence requirements:
- warning / limitation notes:
- fields that must remain unknown or omitted:

If draft preparation is not allowed, list the minimum evidence needed to unblock it.

## 6. TP-Link AX55 Status

- current readiness:
- reason:
- next required evidence:

## 7. Required Corrections

If any source index rows should be changed, list exact row IDs and field-level corrections.

Do not edit files.
Do not write `final/`.

## 8. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to keep the batch 2 source
- whether R7000 should advance toward incoming draft preparation
- whether OpenClaw should collect more sources first
- whether AX55 should stay blocked
- what Codex should do next

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming profile generation:
- no reviewed writes:
- no final writes:
- no profile approval:
