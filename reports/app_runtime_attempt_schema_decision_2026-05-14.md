# App Runtime Attempt Schema Decision

Date: 2026-05-14
Scope: App upgrade support and reference-device validation

## Decision

Create `schema/app_runtime_attempt.schema.json` as a separate local runtime record format.

Runtime attempts are not recovery profiles. They record one App-guided recovery attempt and may later produce an incident candidate or profile refinement after review.

## Why This Is Needed

The App needs to record state that should not live in model profiles:

- selected local firmware file metadata
- selected wired interface
- Local Network permission state
- file picker authorization
- live recovery readiness observations
- transfer progress and error category
- post-upload power-cycle and DHCP result
- final outcome

Keeping this separate prevents profile pollution while allowing real App testing to produce structured feedback.

## Safety Boundary

Runtime attempt records are local/private by default.

Required safeguards:

- `privacy.local_only_by_default: true`
- `privacy.private_paths_redacted: true`
- `privacy.serials_redacted: true`
- `firmware_file.local_path_recorded: false`

The validator enforces these safeguards for shared/exported examples.

## Reference Device Use

The schema should be pressure-tested by the three reference-device directions:

- RT-AC86U / ASUS Rescue Mode: richest current success-path sample
- TP-Link AX55: Web Recovery and beginner panic-flow coverage
- NETGEAR RAX40: orchestration/timing-sensitive attempt capture

Failed or ambiguous attempts should become incident candidates, not profile updates.

## Implemented Files

- `schema/app_runtime_attempt.schema.json`
- `runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json`
- `tools/validate_runtime_attempts.py`

## Verification

Commands:

```text
python3 tools/validate_runtime_attempts.py runtime_attempts/examples
python3 tools/validate_profiles.py incoming
python3 tools/validate_incidents.py
```

All passed.
