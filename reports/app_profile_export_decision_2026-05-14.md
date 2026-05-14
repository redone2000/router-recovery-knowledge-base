# App Profile Export Decision

Date: 2026-05-14
Scope: RT-AC86U App upgrade implementation draft

## Decision

Create an App-facing profile export for RT-AC86U as an implementation aid.

The export is generated from `incoming/asus-rt-ac86u-unknown-unknown.jsonl` and groups fields by App module rather than by raw profile schema structure.

## Output

Generated file:

```text
app_exports/examples/asus_rt_ac86u_app_profile_draft.json
```

Generator:

```text
tools/export_app_profile.py
```

## Boundary

The export is not:

- a reviewed profile
- a final profile
- production guidance
- proof of RT-AX86U behavior
- proof of broad RT-AC86U hardware or firmware-version applicability

The export is:

- an App integration draft
- a field grouping reference
- a way to test the first RT-AC86U implementation slice
- a bridge between profile data and runtime attempt capture

## Required App Warnings

The App must preserve these warnings:

- hardware version remains unknown
- firmware-version applicability remains unknown
- observations are tested-unit behavior
- upload completion is not recovery completion
- manual power cycle is required for the observed RT-AC86U path
- configuration may be retained or reset
- ping/TTL alone must not be treated as success or failure proof

## Next Use

Use this export to implement the first App slice:

1. RT-AC86U profile selection
2. official firmware page guidance
3. firmware file metadata capture
4. macOS preflight checklist
5. passive TFTP transfer flow
6. post-upload wait / power-cycle / DHCP return flow
7. runtime attempt JSON export
