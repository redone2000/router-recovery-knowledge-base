# OpenClaw Stage 1 NETGEAR NMRP Workflow Evidence Indexing

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

The project is currently focused on Recovery Workflow Coverage Gaps, not broad model expansion.

This task targets the NETGEAR NMRP workflow gap.

## Scope

Source indexing only.

Allowed:

- collect public source references about NETGEAR NMRP recovery workflow
- create source-index style output in your report
- identify whether a source is official, community, GitHub documentation, or tool documentation
- identify evidence topics and evidence gaps
- identify whether a source is workflow-level, brand-level, series-level, or model-level

Forbidden:

- do not generate incoming profiles
- do not write `incoming/`
- do not write `reviewed/`
- do not write `final/`
- do not infer model-specific recovery facts
- do not access any real router IP
- do not run network scans
- do not send TFTP/UDP packets
- do not run NMRP traffic
- do not test against real hardware
- do not download firmware binaries
- do not claim App-ready guidance

## Target

Collect and index up to 4 public sources that explain NETGEAR NMRP recovery or NMRP-style recovery orchestration.

Preferred source priority:

1. official NETGEAR documentation, if available
2. nmrpflash project documentation, if publicly available
3. reputable community guides that explain NMRP workflow mechanics
4. forum posts only if they contain clear procedural or troubleshooting evidence

## Required Focus

Evidence topics to look for:

- whether NMRP is a NETGEAR-specific or NETGEAR-common recovery path
- how NMRP differs from passive TFTP PUT
- whether computer-side tooling sends discovery/recovery packets
- whether timing/orchestration is part of the recovery process
- whether model-specific applicability is explicit or unknown
- whether R7000 is discussed only as incident/research context, not as a reviewed profile

## Required Boundaries

Every indexed source must set:

- `profile_generation_allowed: false`
- `workflow_update_allowed: false` unless the source is strong enough to support workflow abstraction
- `applicability_scope` to one of:
  - `workflow_level`
  - `brand_level`
  - `series_level`
  - `model_level`
  - `unknown`

For any non-model-level source, include an evidence gap such as:

- `workflow_level_not_model_specific`
- `brand_level_not_model_specific`
- `series_level_not_model_specific`
- `applicability_scope_unknown`

Every `collector_notes` must explicitly state that profile generation is not allowed from this source without model-level evidence.

## Output Format

# OpenClaw Stage 1 NETGEAR NMRP Workflow Evidence Indexing

Task ID: stage1-netgear-nmrp-workflow-evidence-indexing
Date:
Scope: workflow source indexing only, no profile generation

## Source Index JSONL

Provide one JSON object per source with these fields:

```json
{
  "source_id": "workflow-src-stage1-netgear-nmrp-001",
  "status": "indexed",
  "workflow_target": "nmrp",
  "workflow_targets": ["nmrp"],
  "source_type": "official_documentation",
  "source_url": "https://example.invalid",
  "source_document": "sources/workflows/stage1/netgear-nmrp/example.md",
  "applicability_scope": "brand_level",
  "vendor": "NETGEAR",
  "series": "unknown",
  "model": "unknown",
  "profile_generation_allowed": false,
  "workflow_update_allowed": false,
  "evidence_topics": ["nmrp_orchestration", "computer_side_recovery_tool"],
  "evidence_snippets": ["short factual snippet or summary only"],
  "evidence_gaps": ["brand_level_not_model_specific", "model_specific_applicability_unknown"],
  "conflicts": [],
  "collector_notes": "Explain allowed use and explicitly state no profile generation is allowed without model-level evidence.",
  "extracted_date": "2026-05-13"
}
```

## Source Notes

For each source, provide:

- source title
- source URL
- source type
- workflow target
- applicability scope
- evidence topics
- evidence gaps
- why profile generation is blocked

## Batch Report

Include:

- sources indexed by source type
- applicability scope distribution
- evidence topics found
- evidence gaps remaining
- conflicts found
- skipped sources and why
- whether any source is profile-generation eligible
- whether any source suggests future NMRP workflow drafting

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
- no NMRP packets:
- no network scanning:
- no firmware binary downloads:
- only public sources used:
