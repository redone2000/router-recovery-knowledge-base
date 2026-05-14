# Claude Code Stage 1 ASUS Rescue Gap Search Review

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

- `/Users/YiYuan/Projects/router-recovery-knowledge/data/workflow_source_index.stage1.gap-search.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/openclaw_stage1_active_tftp_asus_rescue_official_gap_search_review.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/workflows/stage1/gap-search/asus-faq-1030642.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/post_upload_phase.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/evidence_lifecycle.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/tools/validate_workflow_source_index.py`

## Facts Already Established By Codex Review

- OpenClaw found one official ASUS source: ASUS FAQ 1030642.
- Codex classified it as `brand_level` rather than strict `series_level`, because the article is ASUS router Rescue Mode guidance using RT-AC68U as an example.
- Codex set `workflow_targets` to `["rescue_mode", "post_upload_phase"]`.
- Codex did not create profile data.
- No official non-TP-Link Active TFTP source was found.
- No official hardware-version-specific recovery behavior difference source was found.

Treat these as claims to verify against local files. If you disagree, request corrections.

## Review Questions

1. Is `brand_level` the correct applicability scope for ASUS FAQ 1030642?
2. Are `rescue_mode` and `post_upload_phase` correct workflow targets?
3. Is this source sufficient to update any workflow JSON now, or should it remain index-only?
4. Does it affect the existing ASUS RT-AC86U observed profile candidate?
5. Does it allow RT-AC68U profile generation?
6. Should the negative results for non-TP-Link Active TFTP and hardware-version behavior differences be treated as stopping conditions for now?

## Output Format

# Claude Code Stage 1 ASUS Rescue Gap Search Review

Task ID: stage1-asus-rescue-gap-search-review
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `ASUS_RESCUE_EVIDENCE_ACCEPTED_INDEX_ONLY`
- `ASUS_RESCUE_EVIDENCE_ACCEPTED_WORKFLOW_UPDATES_ALLOWED`
- `REQUEST_SOURCE_INDEX_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Source Review

### workflow-src-stage1-gap-search-001

- source type:
- applicability scope:
- workflow targets:
- profile_generation_allowed:
- workflow_update_allowed:
- decision:
- issues:
- allowed use:
- prohibited use:

## 3. Workflow / Profile Impact

- rescue_mode:
- post_upload_phase:
- ASUS RT-AC86U incoming candidate:
- RT-AC68U profile generation:
- reviewed/final gates:

## 4. Negative Gap Results

- non-TP-Link Active TFTP:
- hardware-version recovery differences:
- whether to continue searching now:

## 5. Recommendation To Owner

- whether to keep this source index
- whether Codex should update workflow files
- whether OpenClaw should continue official gap search
- what the next useful project task should be

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming profile generation:
- no reviewed writes:
- no final writes:
- no profile approval:
