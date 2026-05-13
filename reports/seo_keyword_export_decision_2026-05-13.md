# SEO Keyword Export Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Create a repeatable SEO keyword candidate export from the Recovery Knowledge System.

The export is a candidate layer only. It does not publish pages and does not convert incidents into user-facing recovery guidance.

## Files Added

- `tools/export_seo_keywords.py`
- `exports/seo_keyword_candidates.json`

## Inputs

The first export uses:

- `docs/recovery_language.md`
- `workflows/*.json`
- `incidents/**/*.json`

## Why

Recovery users often search by panic symptom or workflow failure, not by exact model.

The export turns ontology and incident evidence into SEO candidate language such as:

- TFTP timeout
- TTL=100 but upload fails
- firmware upload complete but router not working
- ping works but router page not opening
- NETGEAR R7000 TTL=100 visible but manual TFTP PUT receives no ACK or times out

## Safety Boundary

SEO candidates are not recovery instructions.

Any future page generated from these candidates must route into reviewed workflow/profile content and preserve uncertainty labels such as `observed-only`.
