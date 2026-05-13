# Recovery Knowledge Architecture Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Adopt a layered Recovery Knowledge System architecture before expanding model coverage.

The project will treat model profiles as parameterized workflow instances, not isolated articles.

## Rationale

Recent work exposed two risks:

- R7000: official TFTP support exists, but local recovery did not reproduce clearly. This shows that workflow timing and orchestration can block a theoretically correct profile.
- ASUS RT-AC86U: lab testing revealed post-upload behavior that was not represented in the original schema. This shows that real tests can correct the abstraction layer.

The right architecture is therefore dual-track:

- abstraction layer: foundations, workflows, brand systems, shared vocabulary
- evidence layer: source index, incidents, lab observations, incoming/reviewed/final profiles

## Files Added

- `docs/recovery_knowledge_system_architecture.md`
- `docs/recovery_language.md`

## Immediate Policy

- Do not expand model coverage today.
- Keep R7000 paused.
- Continue ASUS RT-AC86U only through Owner confirmation and reviewed-candidate gate.
- Define an incident schema before recording more R7000 timing tests.

## Next Recommended Work

1. Create `schema/recovery_incident.schema.json`.
2. Create the first R7000 timing incident from lab notes if Owner wants to preserve the failed test.
3. Draft workflow documents for:
   - Passive TFTP PUT
   - Post-upload phase
   - Web Recovery
