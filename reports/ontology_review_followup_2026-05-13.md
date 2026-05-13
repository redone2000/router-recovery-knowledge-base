# Ontology Review Follow-Up

Date: 2026-05-13
Prepared by: Codex

## Decision

Apply Claude Code's minor ontology review recommendations before processing OpenClaw workflow evidence.

## Changes

Schema:

- Added `observation_only` and `blocked_gates` to incidents.
- Added `confidence` and `observation_only` to workflows.
- Added `linked_workflows`, `blocking_incidents`, and `observation_only_groups` to profiles.

Data:

- Linked ASUS RT-AC86U profile to `passive-tftp-put` and `post-upload-phase`.
- Linked R7000 profile to `passive-tftp-put` and its blocking incident.
- Marked the R7000 incident as `observation_only: true`.
- Added blocked gates to the R7000 incident.
- Added workflow confidence fields.

Tooling:

- Added `tools/validate_system_links.py` to validate profile/incident/workflow cross-links and gate rules.

## Safety Boundaries

- No `reviewed/` data was written.
- No `final/` data was written.
- R7000 remains blocked.
- ASUS remains incoming pending Owner confirmation.
