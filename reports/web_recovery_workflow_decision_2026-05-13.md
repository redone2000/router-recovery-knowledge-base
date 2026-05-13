# Web Recovery Workflow Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Add a draft Web Recovery workflow before expanding TP-Link/AX model coverage.

## Files Added

- `workflows/web_recovery.json`

## Why

TP-Link FAQ 1482 provides a useful series-level signal for browser-based recovery, but it is not sufficient to generate an Archer AX55 profile.

The correct use is workflow abstraction:

- client network preparation
- recovery mode entry
- recovery page availability
- firmware upload
- post-upload handoff

## Safety Boundary

The workflow explicitly preserves the source scope boundary:

- TP-Link FAQ 1482 is used as series-level workflow evidence only.
- It does not unblock AX55 profile generation.
- It does not write `reviewed/` or `final/`.

## Next Recommended Work

- Regenerate SEO keyword candidates from the new workflow.
- Use Web Recovery workflow as the structure for future TP-Link source indexing tasks.
