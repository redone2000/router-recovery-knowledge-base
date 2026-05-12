# Stage 0 Schema Governance Decision

Date: 2026-05-12
Prepared by: Codex

## Decision

Claude Code returned `REQUEST CHANGES`. Codex accepts the finding and keeps the project in Stage 0. Stage 1 collection is blocked until schema, evidence policy, and validation tooling are aligned.

## Adopted Policies

- `source_evidence` is a top-level required field.
- `hardware_version` is a required field. Use `unknown` when sources do not identify the hardware revision.
- TFTP direction requires direct evidence. Do not infer `passive_tftp_from_router` or `active_tftp_to_router` from vendor, model, chipset, or recovery family.
- If a source only says "TFTP recovery" without server/client direction, both TFTP direction fields remain null and confidence is capped at `medium`.
- Tool-derived normalization belongs under `tool_metadata`, not as manually authored top-level profile fields.
- JSONL is the operating format for local batch processing.
- `final/` remains owner-controlled and must not be written by agents or automated tools.

## Owner Decisions Applied

- Normalized fields are tool metadata, not human-authored profile fields.
- JSONL is supported as the default local processing format.
- Evidence snippets should be short and attributable; avoid long copyrighted excerpts.
- `risk_warnings` is included as an optional user-facing field.
- TFTP inference policy is strict: direct evidence required.
- Deprecation fields are included as optional lifecycle metadata.

## Stage 1 Gate

OpenClaw remains on standby. Before collection begins, OpenClaw should receive a queue/source-index design task only. Real profile collection starts after owner confirmation that Stage 0 governance is acceptable.
