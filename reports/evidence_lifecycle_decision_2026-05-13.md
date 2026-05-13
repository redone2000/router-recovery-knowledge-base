# Evidence Lifecycle Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Add a formal evidence lifecycle to connect source index, incident, workflow, profile, reviewed, and final stages.

## Files Updated

- `docs/evidence_lifecycle.md`
- `WORKFLOW.md`
- `RULES.md`

## Why

The project now has separate evidence objects:

- source indexes
- incidents
- workflows
- incoming profiles
- reviewed/final profile states

Without a lifecycle document, future agents may incorrectly treat incidents or draft workflows as App-ready profile guidance.

## Current Gate Results

- R7000 remains blocked from reviewed profile promotion because the TFTP path did not reproduce locally.
- ASUS RT-AC86U remains incoming until Owner confirmation allows reviewed-candidate migration.
- Workflow documents remain draft ontology artifacts.

## Safety Boundaries

- No `reviewed/` data was written.
- No `final/` data was written.
- No new source collection was started.
