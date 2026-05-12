# OpenClaw Stage 1 Source-List Proposal Task

You are the Evidence Collector / Queue Executor for the Router Recovery Knowledge project.

## Current Stage

Stage 1 source-list proposal only.

## Important Limits

This is still not real collection. Do not access websites, search, open links, download materials, or generate incoming profiles.

You may only design a source-list proposal for the approved candidate models.

## Approved Candidate Models

1. ASUS RT-AX86U
2. NETGEAR R7000
3. Xiaomi AX3600
4. TP-Link Archer AX55

## Owner Planning Signal

- TP-Link FAQ 1482: `https://www.tp-link.com/us/support/faq/1482/`
- This is only an Archer AX series planning signal.
- It is not AX55 model-specific profile evidence.
- During future real collection, AX55 model-specific and hardware-version-specific sources must be verified before generating any incoming profile.

## Allowed Output

- Source search plan for each candidate model
- Expected source types
- Future search query suggestions
- Questions that must be verified later
- Stop conditions
- Source types not recommended for first real collection
- Risk notes

## Disallowed Actions

- no web fetching
- no source collection
- no page opening
- no search
- no downloading
- no incoming profiles
- no reviewed/final writes
- no recovery method claims
- no IP addresses
- no firmware filenames
- no TFTP direction claims
- no source evidence snippets
- no confidence assignment
- no inferred recovery facts
- no router IP access
- no TFTP/UDP packets
- no network scanning

## Special Rules

You may write that future collection should prioritize `official_documentation`, `vendor_support_forum`, `verified_community_guide`, `third_party_repository`, or `community_forum_post`.

You must not write that any source has already proved anything.

You may suggest future search queries, but must not perform the searches.

You may write that hardware version splits must be verified, but must not claim that a split exists unless it is already established by owner-provided context.

Do not populate any of these profile fields:

- `recovery_methods`
- `network_recovery`
- `source_evidence`
- `confidence_level`

## Output Format

# OpenClaw Stage 1 Source-List Proposal

Task ID: stage1-source-list-proposal
Date:
Scope: source-list proposal only, no collection

## Candidate Source Plans

Output one JSON block for each of the four approved candidates.

Use this structure:

```json
{
  "queue_id": "wq-stage1-proposed-001",
  "vendor": "ASUS",
  "model": "RT-AX86U",
  "source_plan_status": "proposed_only",
  "expected_source_types": ["official_documentation", "vendor_support_forum", "third_party_repository", "verified_community_guide"],
  "future_search_queries": [
    "ASUS RT-AX86U firmware recovery official",
    "ASUS RT-AX86U rescue mode official support",
    "ASUS RT-AX86U hardware version firmware recovery"
  ],
  "must_verify": [
    "model-specific official page",
    "hardware version applicability",
    "firmware version applicability",
    "whether any recovery instructions are official or community-only",
    "whether source explicitly states recovery direction before any TFTP fields are set"
  ],
  "stop_conditions": [
    "only generic recovery article found",
    "hardware version unclear",
    "source requires login",
    "source gives recovery method without direct evidence",
    "sources conflict"
  ],
  "disallowed_outputs": [
    "recovery_methods",
    "network_recovery",
    "source_evidence",
    "confidence_level",
    "IP addresses",
    "firmware filenames",
    "TFTP direction"
  ],
  "risk_notes": [
    "Planning notes only; no recovery facts asserted."
  ]
}
```

## Excluded Source Types For First Real Collection

Explain which source types should not be prioritized in the first real collection batch, such as:

- `social_media`
- `ai_generated`
- `unknown`
- paywalled/private sources
- sources requiring login

## Safety Confirmation

Answer yes/no for each item:

- no web fetching:
- no source collection:
- no page opening:
- no search:
- no downloading:
- no incoming profiles:
- no reviewed/final writes:
- no recovery method claims:
- no IP addresses:
- no firmware filenames:
- no TFTP direction claims:
- no source evidence snippets:
- no confidence assignment:
- no inferred recovery facts:
- no router IP access:
- no TFTP/UDP packets:
- no network scanning:

## Required Owner Decisions

List any decisions required from the owner.

## Next Recommended Task

You may only recommend:

- Codex reviews source-list proposal
- Owner approves first real collection scope
- OpenClaw waits for explicit approval before real collection
