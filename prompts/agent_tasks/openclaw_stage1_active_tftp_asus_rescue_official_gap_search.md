# OpenClaw Stage 1 Active TFTP / ASUS Rescue Official Gap Search

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

The previous TP-Link / ASUS official evidence batch was accepted as index-only. Do not generate workflow files or profiles.

## Scope

Official-source gap search only.

Allowed source types:

- `official_documentation`
- `vendor_support_forum`

Forbidden source types:

- third-party repositories
- Reddit/social media
- generic community forum posts
- video-only sources
- OpenWrt/DD-WRT/Tomato docs
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

## Search Goals

Find up to 3 official sources total that fill one of these gaps:

1. Official non-TP-Link Active TFTP recovery documentation
   - user computer runs TFTP server
   - device acts as TFTP client and retrieves firmware
   - source must explicitly state or clearly instruct this direction

2. Official ASUS non-Lyra Rescue Mode documentation
   - Rescue Mode entry behavior
   - static IP / Firmware Restoration / LED state / post-upload behavior
   - must be official ASUS documentation

3. Official hardware-version recovery behavior difference
   - same model or family has different recovery behavior by hardware version
   - official source must explicitly distinguish versions

If no official source is found for a gap, report the negative result. Do not substitute community evidence.

## Existing Sources To Avoid Duplicating

Do not re-index these:

- TP-Link FAQ 1482
- ASUS FAQ 1000814
- TP-Link FAQ 2571
- TP-Link FAQ 3062
- TP-Link FAQ 3186
- TP-Link FAQ 2954
- ASUS FAQ 1033090

## Output Format

# OpenClaw Stage 1 Active TFTP / ASUS Rescue Official Gap Search

Task ID: stage1-active-tftp-asus-rescue-official-gap-search
Date:
Scope: official source indexing only, no profile generation

## Search Result

Choose one:

- `OFFICIAL_GAP_EVIDENCE_FOUND`
- `NO_ADDITIONAL_OFFICIAL_GAP_EVIDENCE_FOUND`
- `BLOCKED`

Brief summary.

## Source Index JSONL

Only include accepted official sources:

```json
{
  "source_id": "workflow-src-stage1-gap-search-001",
  "status": "indexed",
  "workflow_target": "active_tftp_server",
  "workflow_targets": ["active_tftp_server"],
  "source_type": "official_documentation",
  "source_url": "https://example.com",
  "source_document": "sources/workflows/stage1/gap-search/example.md",
  "applicability_scope": "brand_level",
  "vendor": "EXAMPLE_VENDOR",
  "series": "unknown",
  "model": "unknown",
  "profile_generation_allowed": false,
  "workflow_update_allowed": false,
  "independent_source_count": 1,
  "evidence_topics": ["active_tftp_server_device_client"],
  "evidence_snippets": ["short factual snippet only"],
  "evidence_gaps": ["brand_level_not_model_specific"],
  "conflicts": [],
  "collector_notes": "No profile generation is allowed without model-level evidence and reviewer approval.",
  "extracted_date": "2026-05-14"
}
```

## Sources Checked But Not Indexed

List official pages checked but not indexed, with reason:

- duplicate
- no recovery workflow content
- no TFTP direction evidence
- firmware download page only
- inaccessible
- requires login

## Batch Report

Include:

- accepted source count
- which gap each source addresses
- source count by vendor
- source count by workflow target
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
- only official sources used:
