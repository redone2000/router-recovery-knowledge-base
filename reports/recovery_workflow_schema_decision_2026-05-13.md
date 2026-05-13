# Recovery Workflow Schema Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Create a workflow layer between recovery foundations and model profiles.

Model profiles are now treated as parameterized instances of workflows rather than isolated tutorials.

## Files Added

- `schema/recovery_workflow.schema.json`
- `tools/validate_workflows.py`
- `workflows/passive_tftp_put.json`
- `workflows/post_upload_phase.json`

## Initial Workflows

### Passive TFTP PUT

Represents the workflow where the router acts as TFTP server and the user/App uploads firmware with a client.

This workflow explicitly records that TTL/ping is a weak readiness signal and links the R7000 timing incident as a failure mode.

### Post-Upload Phase

Represents the phase after firmware upload completes but before the router is usable again.

This workflow exists because ASUS RT-AC86U lab testing showed upload completion is not necessarily recovery completion and may require wait/power-cycle/DHCP steps.

## Safety Boundaries

- No model profile was promoted.
- No `reviewed/` data was written.
- No `final/` data was written.
- Workflows are draft ontology artifacts, not App-ready instructions by themselves.

## Next Work

- Add `docs/evidence_lifecycle.md`.
- Later add workflow documents for Web Recovery and Active TFTP.
- Build export tooling only after reviewed/final profile policy is clear.
