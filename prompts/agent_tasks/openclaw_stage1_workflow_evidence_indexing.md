# OpenClaw Stage 1 Workflow Evidence Indexing Task

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

This is not model profile collection.

## Scope

This task allows public web fetching for workflow-level evidence indexing only.

Do not generate profiles.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.
Do not infer model-specific recovery facts.

Prefer returning proposed file contents in your response. If the Owner explicitly allows file writes in your environment, only write under:

- `data/workflow_source_index.stage1.batch1.jsonl`
- `sources/workflows/stage1/batch1/*.md`
- `reports/openclaw_stage1_workflow_evidence_indexing_batch1.md`

## Files To Read First

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_knowledge_system_architecture.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/recovery_language.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/docs/evidence_lifecycle.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/passive_tftp_put.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/post_upload_phase.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/workflows/web_recovery.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/source_scope_policy.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`

## Approved Evidence Targets

Index workflow-level public evidence for these targets:

### Target A: Web Recovery Workflow

Goal:

Find public evidence explaining browser-based router firmware recovery or rescue web upload workflows.

Prioritize:

- official vendor documentation
- vendor support forums
- OpenWrt Wiki if accessible
- high-quality public community guides

Record evidence for:

- recovery web page availability
- static IP / recovery subnet requirements
- firmware upload page behavior
- upload completion versus recovery completion
- failure modes when recovery page does not open

Do not convert series-level or vendor-level evidence into model profile claims.

### Target B: Passive TFTP PUT Workflow

Goal:

Find public evidence explaining router-side TFTP server behavior where the user/client uploads firmware with TFTP PUT/WRQ.

Record evidence for:

- user runs TFTP client
- router acts as TFTP server
- timing / recovery window caveats
- TTL/ping readiness limitations if explicitly discussed
- TFTP timeout / no ACK failure modes

Do not infer TFTP direction from vendor/model patterns.

### Target C: Post-Upload Phase

Goal:

Find public evidence or high-quality public reports showing that firmware upload completion may not equal recovery completion.

Record evidence for:

- wait time after upload
- automatic reboot versus manual reboot/power cycle
- DHCP return after recovery
- admin URL/gateway change after recovery
- user-visible symptoms after upload

Do not generalize device-specific behavior across brands.

## Disallowed Actions

- no profile generation
- no `incoming/` writes
- no `reviewed/` writes
- no `final/` writes
- no router IP access
- no network scanning
- no TFTP/UDP packets
- no private or login-required sources
- no AI-generated sources
- no guessed IP addresses
- no guessed firmware filenames
- no guessed TFTP direction
- no confidence assignment for profiles

## Required Source Index Shape

Return JSONL rows in this shape:

```json
{
  "source_id": "workflow-src-stage1-batch1-001",
  "status": "indexed",
  "workflow_target": "web_recovery | passive_tftp_put | post_upload_phase",
  "source_type": "official_documentation | vendor_support_forum | openwrt_wiki | verified_community_guide | community_forum_post",
  "source_url": "https://example.com/source",
  "source_document": "sources/workflows/stage1/batch1/example.md",
  "applicability_scope": "workflow_level | brand_level | series_level | model_level",
  "vendor": "unknown or vendor name",
  "series": "unknown or series",
  "model": "unknown or model",
  "profile_generation_allowed": false,
  "workflow_update_allowed": false,
  "evidence_topics": ["static_ip", "recovery_page", "post_upload_wait"],
  "evidence_snippets": ["short non-copyrighted summary or short quotation"],
  "evidence_gaps": ["model_specific_scope_unknown"],
  "conflicts": [],
  "collector_notes": "What this source can and cannot support.",
  "extracted_date": "YYYY-MM-DD"
}
```

## Required Source Notes

For each indexed source, include a short source note with:

- URL
- title
- workflow target
- applicability scope
- evidence topics
- evidence gaps
- why this does not generate a model profile

## Stop Conditions

Stop and report instead of forcing evidence if:

- source only mentions recovery without actionable workflow detail
- source requires login
- source is private/paywalled
- source content cannot be accessed
- source conflicts with existing workflow assumptions
- source gives model-specific instructions but applicability is unclear

## Output Format

# OpenClaw Stage 1 Workflow Evidence Indexing Batch 1

Task ID: stage1-workflow-evidence-indexing-batch1
Date:
Scope: workflow source indexing only, no profile generation

## 1. Source Index JSONL

Provide JSONL rows.

## 2. Source Notes

Provide proposed source note paths and content summaries.

## 3. Batch Report

- sources indexed by workflow:
- source types used:
- applicability scope distribution:
- evidence topics found:
- evidence gaps:
- conflicts:
- skipped sources and why:
- whether any source is profile-generation eligible: must be `0`
- whether any source suggests workflow update: yes/no with explanation

## 4. Safety Confirmation

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
