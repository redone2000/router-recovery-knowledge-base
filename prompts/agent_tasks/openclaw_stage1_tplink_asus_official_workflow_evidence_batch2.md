# OpenClaw Stage 1 TP-Link / ASUS Official Workflow Evidence Batch 2

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

Stage 1 controlled workflow evidence indexing.

The project is returning focus to official-source evidence for TP-Link and ASUS because these brands currently have stronger official workflow evidence than NETGEAR NMRP.

## Scope

Official-source workflow evidence indexing only.

Allowed source types:

- `official_documentation`
- `vendor_support_forum`

Forbidden source types for this task:

- third-party repositories
- Reddit/social media
- generic community forum posts
- YouTube/video-only sources
- OpenWrt/DD-WRT/Tomato community docs
- firmware binaries

Forbidden actions:

- do not generate incoming profiles
- do not write `incoming/`
- do not write `reviewed/`
- do not write `final/`
- do not infer model-specific recovery facts
- do not access any real router IP
- do not run network scans
- do not send TFTP/UDP packets
- do not download firmware binaries
- do not use community sources as substitutes if official evidence is not found

## Existing Evidence To Avoid Duplicating

These sources are already indexed. Do not re-index them unless you find materially new official content on the same page:

- TP-Link FAQ 1482: `https://www.tp-link.com/us/support/faq/1482/`
- ASUS FAQ 1000814: `https://www.asus.com/ca-en/support/faq/1000814/`
- TP-Link FAQ 2571: `https://www.tp-link.com/us/support/faq/2571/`

You may reference them in the batch report as existing context, but do not count them as new sources.

## Search Goal

Find up to 4 additional official TP-Link or ASUS sources that strengthen one of these workflow evidence gaps:

### TP-Link

- Archer AX Web Recovery applicability
- recovery page / emergency web server behavior
- static IP requirements for recovery
- hardware version / region matching requirements for recovery
- post-upload wait or reboot behavior after recovery upload

### ASUS

- Rescue Mode / Firmware Restoration workflow
- static IP and recovery web page behavior
- post-upload wait / reboot / power-cycle guidance
- model or family applicability for Rescue Mode
- firmware format / file matching requirements

## Required Boundaries

Every accepted source must set:

- `profile_generation_allowed: false`
- `workflow_update_allowed: false` unless the source is strong official workflow evidence

For non-model-level sources, include one of these evidence gaps:

- `brand_level_not_model_specific`
- `series_level_not_model_specific`
- `applicability_scope_unknown`

Every `collector_notes` must explicitly state that profile generation is not allowed without model-level evidence and reviewer approval.

If a source is model-level, it still must not generate a profile. Mark whether it is useful for reference-device planning only.

## Output Format

# OpenClaw Stage 1 TP-Link / ASUS Official Workflow Evidence Batch 2

Task ID: stage1-tplink-asus-official-workflow-evidence-batch2
Date:
Scope: official workflow source indexing only, no profile generation

## Search Result

Choose one:

- `OFFICIAL_WORKFLOW_EVIDENCE_FOUND`
- `NO_ADDITIONAL_OFFICIAL_WORKFLOW_EVIDENCE_FOUND`
- `BLOCKED`

Brief summary.

## Source Index JSONL

Provide one JSON object per accepted source:

```json
{
  "source_id": "workflow-src-stage1-tplink-asus-batch2-001",
  "status": "indexed",
  "workflow_target": "web_recovery",
  "workflow_targets": ["web_recovery"],
  "source_type": "official_documentation",
  "source_url": "https://example.com",
  "source_document": "sources/workflows/stage1/tplink-asus-batch2/example.md",
  "applicability_scope": "brand_level",
  "vendor": "TP-Link",
  "series": "unknown",
  "model": "unknown",
  "profile_generation_allowed": false,
  "workflow_update_allowed": false,
  "evidence_topics": ["static_ip_requirement", "recovery_page_behavior"],
  "evidence_snippets": ["short factual snippet only"],
  "evidence_gaps": ["brand_level_not_model_specific"],
  "conflicts": [],
  "collector_notes": "No profile generation is allowed without model-level evidence and reviewer approval.",
  "extracted_date": "2026-05-14"
}
```

## Source Notes

For each accepted source, provide:

- title
- URL
- source type
- vendor
- workflow target
- applicability scope
- evidence topics
- evidence gaps
- why profile generation is blocked

## Sources Checked But Not Indexed

List official TP-Link / ASUS pages checked but not indexed, with reason:

- duplicate of existing indexed source
- no recovery workflow content
- firmware download page only
- marketing/product page only
- inaccessible
- requires login

## Batch Report

Include:

- accepted source count
- source count by vendor
- source count by workflow target
- applicability scope distribution
- evidence topics strengthened
- evidence gaps remaining
- conflicts found
- whether any source is profile-generation eligible
- whether any source suggests future workflow refinement

## Safety Confirmation

Answer yes/no:

- no incoming writes:
- no reviewed writes:
- no final writes:
- no profile generation:
- no confidence assignment:
- no inferred model facts:
- no router IP access:
- no TFTP/UDP packets:
- no network scanning:
- no firmware binary downloads:
- only official TP-Link / ASUS sources used:
