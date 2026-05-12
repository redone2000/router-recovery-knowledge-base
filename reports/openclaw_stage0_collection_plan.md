# OpenClaw Stage 0 Collection Plan

## Scope

This stage only defines collection templates and handoff rules. It does not perform real collection, web access, source retrieval, or incoming profile generation. All examples are placeholders for Stage 1 planning.

## Allowed Sources For Future Stage 1

Future Stage 1 collection may use these public source classes, in priority order:

1. Official vendor documentation (`official_documentation`)
2. Vendor support forum (`vendor_support_forum`)
3. OpenWrt Wiki (`verified_community_guide` or `third_party_repository`, depending on page quality)
4. GitHub repository documentation (`third_party_repository`)
5. Verified community guide (`verified_community_guide`)
6. Community forum post (`community_forum_post`)
7. Other public sources, only when owner-approved and mapped to an existing `source_type`

## Disallowed Actions

- no network scanning
- no router IP access
- no TFTP/UDP packets
- no final writes
- no reviewed writes
- no inferred unclear fields
- no real collection during Stage 0
- no generation of real `incoming/` profiles during Stage 0

## Work Queue Design

`data/work_queue.template.jsonl` defines future collection tasks. The file is template-only and must not be treated as a real Stage 1 queue.

| Field | Meaning |
|-------|---------|
| `queue_id` | Unique queue item ID |
| `status` | Queue status; Stage 0 templates use `template_only` |
| `priority` | Lower number means higher priority |
| `vendor` | Target vendor placeholder or real vendor in Stage 1 |
| `model` | Target model placeholder or real model in Stage 1 |
| `hardware_version_hint` | Known or suspected hardware revision; use `unknown` if not identified |
| `firmware_version_hint` | Known firmware scope; use `unknown` if not identified |
| `target_sources` | Candidate public source URLs or placeholders |
| `collection_goal` | Narrow collection goal for the queue item |
| `allowed_source_types` | Values mapped to `schema/enums.md` `source_type` values |
| `disallowed_actions` | Item-level safety constraints |
| `evidence_requirements` | Required evidence before profile generation |
| `stop_conditions` | Conditions that stop collection and create an evidence gap |
| `owner_notes` | Owner or coordinator notes |

## Source Index Design

`data/source_index.template.jsonl` defines how future collected sources will be indexed before profile generation. The file is template-only and must not be treated as real collected evidence.

| Field | Meaning |
|-------|---------|
| `source_id` | Unique source index ID |
| `queue_id` | Related work queue ID |
| `status` | Source processing status; Stage 0 templates use `template_only` |
| `source_type` | Existing `source_type` enum value |
| `source_url` | Public source URL, or placeholder in templates |
| `source_document` | Local source document path or placeholder |
| `vendor` | Vendor covered by the source |
| `applicability_scope` | Source applicability level: `vendor_level`, `series_level`, `model_level`, `hardware_version_level`, `firmware_version_level`, or `unknown` |
| `series` | Series/family named by the source, such as an AX series, or null when not applicable |
| `model` | Model covered by the source, or `unknown` when the source is not model-specific |
| `hardware_version` | Hardware revision stated by source, or `unknown` |
| `firmware_version` | Firmware version stated by source, or `unknown` |
| `applies_to_candidate_model` | Whether this source directly applies to the candidate model: true, false, or `unknown` |
| `applicability_notes` | Notes explaining source scope and any model/hardware/firmware applicability uncertainty |
| `profile_generation_allowed` | Boolean gate for whether this source can contribute directly to profile generation |
| `profile_generation_blockers` | Reasons this source must not generate a profile yet |
| `recovery_methods_claimed` | Existing `recovery_method` enum values claimed by source |
| `evidence_snippets` | Placeholder or short attributable evidence snippets |
| `evidence_gaps` | Missing or ambiguous facts that block profile confidence |
| `conflicts` | Conflicts against other sources |
| `collector_notes` | Collector notes without unsupported inference |
| `extracted_date` | Extraction date in ISO date format |

## Evidence Gap Rules

Stop and mark `evidence_gap` when any of these conditions appears:

- source is vendor-level or series-level and not model-specific
- source applicability to the candidate model is unknown
- TFTP direction unclear
- hardware version mentioned but not mapped
- firmware filename missing
- default IP missing
- conflicting sources
- source has no actionable recovery steps
- source only says "TFTP recovery" without direction
- source requires login, payment, device access, or non-public material

## Incoming Profile Preconditions

Before a future incoming profile may be generated:

- vendor and model are identified
- source applicability is model-level or more specific, or a reviewer has confirmed that a series-level source applies to the exact model and hardware scope
- `hardware_version` is identified or set to `unknown`
- at least one `recovery_method` is supported by direct evidence
- each claimed recovery method has at least one `source_evidence` entry
- no guessed IP, firmware filename, hardware version, firmware version, or TFTP direction is present
- confidence is no higher than the evidence allows
- ambiguous TFTP direction is represented as null direction fields plus an evidence gap

## Batch Limits For Stage 1

- Each Stage 1 batch should include at most 3-5 models.
- Each model should use at most 3-5 sources in the first pass.
- Each batch must be validated and reviewed before expanding the next batch.

## Handoff Report Format

```md
# OpenClaw Stage Report

Task ID:
Date:
Allowed Scope:
Files Written:

## Queue Status
- queued:
- processed:
- blocked:
- skipped:

## Sources Indexed
- official_documentation:
- vendor_support_forum:
- verified_community_guide:
- third_party_repository:
- community_forum_post:
- other:

## Evidence Gaps
1. queue_id:
   missing:
   reason:
   recommended next step:

## Safety Confirmation
- no network scanning:
- no router IP access:
- no TFTP/UDP packets:
- no final writes:
- no reviewed writes:
- no real collection:
- no inferred unclear fields:

## Required Owner Decisions

## Next Recommended Task
```
