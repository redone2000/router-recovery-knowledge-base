# Runtime To Incident Bridge Decision

Date: 2026-05-14
Scope: reference-device lab testing support

## Decision

Add a tool to generate incident candidates from filled App runtime attempt records.

## Rationale

Upcoming TFTP active/passive testing will likely produce high-value failed or ambiguous attempts:

- timing windows that are hard to catch
- ping/TTL before TFTP readiness
- active/passive direction surprises
- fixed filename requirements
- ACK source port differences
- macOS permission or route ownership issues
- post-upload behavior that differs from expectation

These should not directly mutate model profiles. They should first become incident candidates, then be reviewed.

## Implemented Tool

```text
tools/create_incident_from_runtime_attempt.py
```

Example:

```text
python3 tools/create_incident_from_runtime_attempt.py \
  --input runtime_attempts/templates/netgear_rax40_tftp_orchestration_template.json \
  --output incidents/lab/netgear-rax40-example-incident.json \
  --symptom "TTL visible but transfer service not ready"
```

## Default Gate

Generated incidents default to:

- `status: observed-only`
- `resolution: unresolved`
- `evidence_type: lab_observation`
- `confidence: medium`
- `profile_gate: blocked`
- `blocked_gates`: incoming-to-reviewed, reviewed-to-final, app-guidance

This keeps runtime observations from becoming App/profile guidance without review.

## Verification

The generator was tested against a temporary runtime attempt output under `/private/tmp`, then validated with:

```text
python3 tools/validate_incidents.py /private/tmp/asus_rt_ac86u_generated_incident_test.json
```

The temporary incident was not committed.
