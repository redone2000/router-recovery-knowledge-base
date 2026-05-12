# OpenClaw Stage 1 Source Index Batch 1 Task

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

Stage 1 source indexing only, batch 1.

## Scope

This task allows public web fetching for source indexing only.

You may inspect public web pages for the two approved candidate models below, then output a source index report and JSONL records for Codex review.

This is not profile generation.

## Approved Batch 1 Candidate Models

1. TP-Link Archer AX55
2. NETGEAR R7000

## Allowed Writes

For this task, do not directly modify the repository unless explicitly instructed by the owner in your own execution environment. Prefer returning the proposed file contents in your response.

If file output is explicitly allowed by the owner, the only allowed paths are:

- `data/source_index.stage1.batch1.jsonl`
- `reports/openclaw_stage1_source_index_batch1.md`
- `sources/stage1/batch1/*.md`

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

## Source Scope Policy

Follow:

`/Users/YiYuan/Projects/router-recovery-knowledge/reports/source_scope_policy.md`

Key rule:

Series-level sources may be indexed but must not generate model-level profiles by themselves.

For example, TP-Link FAQ 1482 may be indexed as an Archer AX series source, but it is not by itself Archer AX55 model-specific evidence.

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

### profile_generation_blockers

Required when `profile_generation_allowed` is false.

Examples:

- `series_level_source_not_model_specific`
- `model_specific_applicability_unknown`
- `hardware_version_scope_unknown`
- `firmware_version_scope_unknown`
- `community_source_requires_corroboration`
- `tftp_direction_unclear`
- `firmware_filename_missing`
- `default_ip_missing`

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

Use short excerpts or concise summaries only. Avoid long copyrighted excerpts.

Do not turn snippets into final app instructions.

### TFTP Direction

Do not infer TFTP direction.

Only record `tftp_active` or `tftp_passive` when the source explicitly states who acts as server/client or provides equivalent direct instructions.

If the source only says "TFTP recovery" without direction, do not infer direction. Add `tftp_direction_unclear`.

## Batch Limits

- Maximum 2 candidate models.
- Maximum 3 sources per candidate model.
- Stop after indexing at most 6 total sources.
- If source quality is poor, stop early and report evidence gaps.

## Required Output

Return the following sections in your response.

# OpenClaw Stage 1 Source Index Batch 1 Report

Task ID: stage1-source-index-batch1
Date:
Scope: source indexing only

## Source Index JSONL

Provide the full proposed contents of `data/source_index.stage1.batch1.jsonl` as a JSONL code block.

Each line must be one valid JSON object.

## Source Notes

If needed, provide proposed source note files under `sources/stage1/batch1/` as markdown code blocks.

Keep source notes short. Include source URL, title, scope classification, and evidence gaps. Do not write full copied pages.

## Batch Report

Include:

- sources indexed by candidate
- source types used
- applicability scope distribution
- evidence gaps
- conflicts
- sources skipped and why
- whether any source is series-level only
- whether any source is model-specific
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

- Codex reviews source index batch
- Claude Code reviews evidence quality
- Owner approves or rejects profile-generation preparation

Do not recommend generating incoming profiles unless owner explicitly approves after Codex review.
