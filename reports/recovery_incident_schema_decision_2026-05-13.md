# Recovery Incident Schema Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Create a separate incident layer for recovery success/failure observations and tacit recovery knowledge.

Incidents are not profiles and must not be treated as reviewed or final model guidance.

## Files Added

- `schema/recovery_incident.schema.json`
- `tools/validate_incidents.py`
- `incidents/lab/netgear_r7000_ttl100_tftp_timeout_2026-05-13.json`

## First Incident

The first incident records the R7000 lab observation:

- TTL=100 visible
- ping reachable during recovery window
- manual macOS TFTP PUT timed out or received no ACK
- official NETGEAR TFTP source path exists
- nmrpflash completed recovery easily
- R7000 profile gate remains blocked

Status:

- `status`: `observed-only`
- `resolution`: `unresolved`
- `profile_gate`: `blocked`

## Why This Matters

The R7000 case is not a stable profile, but it is valuable evidence.

It pressure-tests the incident schema with a real, ambiguous recovery case where official documentation exists but lab reproduction is unresolved.

## Safety Boundaries

- No `reviewed/` data was written.
- No `final/` data was written.
- The incident does not unblock R7000 profile promotion.
- Any future profile change requires successful retest or stronger timing/orchestration evidence.
