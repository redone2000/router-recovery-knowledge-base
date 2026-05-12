# OpenClaw Stage 1 Gap-Focused Source Index Batch 2 Task

You are the Evidence Collector / Queue Executor for the Router Recovery Knowledge project.

## Agent Identity Gate

This task is intended only for: OpenClaw.

If you are not this agent, stop immediately and reply only:

WRONG_AGENT_TASK
Expected agent: OpenClaw
Your role: [your actual role if known]
No action performed.

Do not reinterpret, adapt, or partially execute this task if your agent identity does not match.

## Current Stage

Stage 1 source indexing only, batch 2.

## Scope

This task allows public web fetching for gap-focused source indexing only.

Do not generate profiles.
Do not write `incoming/`, `reviewed/`, or `final/`.

## Background

Claude Code reviewed batch 1 and returned:

`SOURCE_INDEX_ACCEPTED_PROFILE_PREP_BLOCKED`

Current gaps:

1. TP-Link Archer AX55 needs model-specific recovery evidence.
2. NETGEAR R7000 needs hardware/firmware applicability and macOS workflow mapping.

Review file:

`/Users/YiYuan/Projects/router-recovery-knowledge/reports/claude_stage1_evidence_quality_review_batch1.md`

Existing source index:

`/Users/YiYuan/Projects/router-recovery-knowledge/data/source_index.stage1.batch1.jsonl`

Source scope policy:

`/Users/YiYuan/Projects/router-recovery-knowledge/reports/source_scope_policy.md`

## Approved Gap Targets

### Target A: TP-Link Archer AX55

Goal:

Find model-specific public recovery documentation for `TP-Link Archer AX55`.

Must verify:

- exact model applicability
- hardware-version applicability
- firmware-version applicability
- whether any recovery procedure is official or community-only
- whether any TFTP direction is explicitly stated before recording TFTP-specific claims

Stop if:

- only generic Archer AX series guidance is found
- source does not mention Archer AX55 or exact model page
- source requires login
- source gives recovery method without direct evidence
- source conflicts with batch 1

### Target B: NETGEAR R7000

Goal:

Find public evidence for:

- R7000 hardware-version applicability for the indexed NETGEAR TFTP recovery source
- firmware-version applicability
- macOS-compatible workflow mapping, preferably official or high-quality public source

Must verify:

- exact model applicability
- whether the source is official or community-only
- whether macOS instructions are direct, generic, or need mapping from Windows-only guidance
- whether any TFTP direction is explicitly stated before recording TFTP-specific claims

Stop if:

- only generic NETGEAR router guidance is found
- source does not mention R7000 or exact model page
- source requires login
- source gives recovery method without direct evidence
- source conflicts with batch 1

## Allowed Writes

Prefer returning proposed file contents in your response rather than writing files.

If file output is explicitly allowed by the owner, only these paths are allowed:

- `data/source_index.stage1.batch2.jsonl`
- `reports/openclaw_stage1_gap_source_index_batch2.md`
- `sources/stage1/batch2/*.md`

Do not write any other path.

## Disallowed Actions

- no `incoming/` writes
- no `reviewed/` writes
- no `final/` writes
- no profile generation
- no confidence assignment
- no inferred recovery facts
- no guessed IP addresses
- no guessed firmware filenames
- no guessed TFTP direction
- no router IP access
- no TFTP/UDP packets
- no network scanning
- no private, paywalled, or login-required source use
- no merging source claims into a profile

## Allowed Sources

Use only public sources. Prioritize:

1. `official_documentation`
2. `vendor_support_forum`
3. `verified_community_guide`
4. `third_party_repository`
5. `community_forum_post`

Do not use:

- `social_media`
- `ai_generated`
- `unknown`
- private sources
- paywalled sources
- login-required sources

## Required Source Index Fields

Each source index row must include:

- `source_id`
- `queue_id`
- `status`
- `source_type`
- `source_url`
- `source_document`
- `vendor`
- `applicability_scope`
- `series`
- `model`
- `hardware_version`
- `firmware_version`
- `applies_to_candidate_model`
- `applicability_notes`
- `profile_generation_allowed`
- `profile_generation_blockers`
- `recovery_methods_claimed`
- `tftp_direction_claimed`
- `contains_macos_guidance`
- `evidence_snippets`
- `evidence_gaps`
- `conflicts`
- `collector_notes`
- `extracted_date`

## Field Rules

### applicability_scope

Use one of:

- `vendor_level`
- `series_level`
- `model_level`
- `hardware_version_level`
- `firmware_version_level`
- `unknown`

### applies_to_candidate_model

Use one of:

- `true`
- `false`
- `"unknown"`

### profile_generation_allowed

Use `false` unless the source is model-level or more specific and all blocking applicability issues are resolved.

For this batch, prefer conservative `false` when uncertain.

### tftp_direction_claimed

Use one of:

- `"tftp_passive"`
- `"tftp_active"`
- `"unknown"`
- `null`

Only use `tftp_passive` or `tftp_active` if the source explicitly states who acts as server/client or gives equivalent direct instructions.

If the source only says "TFTP recovery" without direction, use `"unknown"` or `null` and add `tftp_direction_unclear`.

### contains_macos_guidance

Use boolean:

- `true`: source contains direct macOS guidance
- `false`: source does not contain direct macOS guidance

### recovery_methods_claimed

Only use existing enum values from `schema/enums.md` if the source explicitly claims a method.

Allowed recovery method enum values:

- `tftp_passive`
- `tftp_active`
- `uart_serial`
- `web_ui`
- `button_reset`
- `usb_storage`
- `sd_card`
- `ssh_cli`
- `telnet_cli`
- `jtag`
- `nand_programmer`
- `auto_recovery`
- `other`

If the source is too generic or ambiguous, use an empty array and add an evidence gap.

### evidence_snippets

Use short excerpts or concise summaries only.

Avoid long copyrighted excerpts.

Do not turn snippets into final app instructions.

## Batch Limits

- Maximum 2 candidate models.
- Maximum 3 new sources per candidate model.
- Stop after indexing at most 6 total new sources.
- If source quality is poor, stop early and report evidence gaps.

## Required Output

Return the following sections in your response.

# OpenClaw Stage 1 Gap Source Index Batch 2 Report

Task ID: stage1-gap-source-index-batch2
Date:
Scope: gap-focused source indexing only

## Source Index JSONL

Provide the full proposed contents of `data/source_index.stage1.batch2.jsonl` as a JSONL code block.

Each line must be one valid JSON object.

## Source Notes

If needed, provide proposed source note files under `sources/stage1/batch2/` as markdown code blocks.

Keep source notes short. Include source URL, title, scope classification, what gap it addresses, and remaining evidence gaps. Do not copy full pages.

## Batch Report

Include:

- sources indexed by target
- which gap each source addresses
- source types used
- applicability scope distribution
- evidence gaps remaining
- conflicts
- sources skipped and why
- whether any source is model-specific
- whether any source includes direct macOS guidance
- whether any source is profile-generation eligible

## Safety Confirmation

Answer yes/no:

- no incoming writes:
- no reviewed writes:
- no final writes:
- no profile generation:
- no confidence assignment:
- no inferred recovery facts:
- no guessed IP addresses:
- no guessed firmware filenames:
- no guessed TFTP direction:
- no router IP access:
- no TFTP/UDP packets:
- no network scanning:
- only public sources used:
- source count within limit:

## Required Owner Decisions

List anything the owner must decide before profile generation.

## Next Recommended Task

You may only recommend:

- Codex reviews source index batch 2
- Claude Code reviews evidence quality
- Owner approves or rejects profile-generation preparation

Do not recommend generating incoming profiles unless owner explicitly approves after Codex and Claude review.
