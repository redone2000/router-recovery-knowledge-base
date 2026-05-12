# OpenClaw Stage 1 Source-List Proposal Review

Date: 2026-05-12
Prepared by: Codex

## Decision

Accepted with minor corrections.

OpenClaw stayed within the source-list proposal boundary. It did not report source collection, did not include recovery methods, did not include IP addresses, did not include firmware filenames, did not assign confidence, and did not generate profile data.

## Files Added

- `data/stage1_source_plan.proposed.jsonl`

This is a proposed source-search plan only. It is not source evidence, not an incoming profile, and not a source index.

## Corrections Applied

- Reworded the Xiaomi bilingual query to avoid over-specific Chinese phrasing that could imply a recovery fact.
- Preserved TP-Link FAQ 1482 as a planning signal only, not AX55-specific evidence.
- Adjusted source-type guidance: `personal_testing` is not something OpenClaw should perform, but documented hands-on testing may be high-value evidence later if owner-provided and reviewable.
- Adjusted source-type guidance: `firmware_analysis` and `bootloader_dump` are not first-batch ordinary collection priorities, but may be high-confidence expert evidence in a later specialist workflow.

## Source Type Guidance For First Real Collection

Prioritize:

- `official_documentation`
- `vendor_support_forum`
- `verified_community_guide`
- `third_party_repository`
- `community_forum_post` only when higher-quality sources are unavailable or when used as a secondary corroborating source

Do not prioritize:

- `social_media`
- `ai_generated`
- `unknown`
- paywalled/private sources
- sources requiring login

Defer to later specialist review:

- `personal_testing`
- `security_research_paper`
- `firmware_analysis`
- `bootloader_dump`

## Owner Decision Needed

Approve whether the first real collection batch should use all four candidates:

1. ASUS RT-AX86U
2. NETGEAR R7000
3. Xiaomi AX3600
4. TP-Link Archer AX55

Codex recommendation: approve all four for a first controlled collection pass, but cap OpenClaw to source indexing only before any incoming profile generation.

## Next Step

If owner approves, prepare an OpenClaw task file for `Stage 1 source indexing only`.

That next task may allow web fetching of public sources, but should still prohibit:

- writing `final/`
- writing `reviewed/`
- generating incoming profiles until source index review passes
- router IP access
- TFTP/UDP packets
- network scanning
- guessing IP addresses, firmware filenames, or TFTP direction
