# Reference Device App Upgrade Plan

Date: 2026-05-14
Status: Stage 1 execution plan

## Purpose

The next project phase should use a small set of reference devices to validate whether the recovery knowledge system is sufficient for a real App version upgrade.

This replaces arbitrary model expansion with a closed loop:

```text
reference device knowledge
  -> App upgrade implementation
  -> lab or user testing
  -> runtime attempt / incident capture
  -> profile, workflow, or schema refinement
```

## Core Decision

Focus on three reference directions first:

| Priority | Brand | Reference Device | Primary Workflow Goal | Current Gate |
| --- | --- | --- | --- | --- |
| 1 | TP-Link | Archer AX55 | Web Recovery / official firmware source / beginner panic flow | Source gaps remain; no profile generation |
| 2 | ASUS | RT-AX86U target family, with RT-AC86U lab profile as current observed sample | Rescue Mode / Passive TFTP PUT / post-upload phase | RT-AC86U incoming candidate exists; AX86U must not inherit AC86U facts without evidence |
| 3 | NETGEAR | RAX40 preferred modern reference | NETGEAR orchestration / NMRP-vs-TFTP decision / timing capture | R7000 remains incident-only; do not promote |

## Why These Three

### TP-Link Archer AX55

Purpose:

- validate Web Recovery flow for beginner users
- test official-source and series/model applicability boundaries
- stress the App's "recovery page does not open" and "static IP setup" guidance

Primary App value:

- lowest-friction panic recovery path
- likely useful for many users
- good test for firmware-source and web-upload UX

Current evidence state:

- TP-Link official workflow evidence exists at series/workflow level
- AX55 model-specific recovery evidence remains insufficient
- no incoming profile should be generated yet

Next work:

- collect or lab-confirm AX55 model-specific recovery page behavior
- capture required static IP, recovery page URL, button entry, firmware format, post-upload behavior
- record failed attempts as incidents rather than filling profile guesses

### ASUS RT-AX86U / RT-AC86U

Purpose:

- validate Rescue Mode and Passive TFTP PUT guidance
- verify post-upload behavior, especially wait and power-cycle requirements
- test App runtime handling for macOS permissions, static IP, firmware selection, TFTP transfer, and DHCP return

Primary App value:

- strong enthusiast/router recovery reference
- exercises the most complex App-guided flow currently available
- RT-AC86U already exposed critical post-upload behavior that common docs can miss

Current evidence state:

- RT-AC86U incoming profile exists and is lab-observed
- RT-AC86U can support App workflow design and runtime schema work
- RT-AX86U should be treated as a separate target unless directly tested or evidenced

Next work:

- use RT-AC86U to validate App runtime coverage
- if RT-AX86U is the intended reference device, create separate queue/source/lab artifacts for RT-AX86U
- do not copy RT-AC86U LAN port, timing, ACK port, or power-cycle behavior into RT-AX86U without evidence

### NETGEAR RAX40

Purpose:

- move NETGEAR work away from R7000 legacy timing uncertainty
- validate modern NETGEAR recovery orchestration
- decide whether App guidance should prioritize NMRP, TFTP, or another flow for modern NETGEAR devices

Primary App value:

- tests timing-sensitive recovery where simple profile fields may not be enough
- forces runtime attempt and incident capture design
- helps classify NETGEAR as an orchestration-heavy recovery world

Current evidence state:

- R7000 TFTP is unresolved and should remain incident-only
- NMRP evidence is research-only and not official-workflow-ready
- RAX40 should begin as a reference target, not a profile

Next work:

- create RAX40 source-list and lab-test plan only
- do not draft a RAX40 profile until a recovery method is reproduced or strongly evidenced
- capture failures as incidents with timing, LED, packet, and tool behavior

## App Upgrade Validation Matrix

Each reference device should be used to validate these App capabilities:

| Capability | TP-Link AX55 | ASUS RT-AC86U / RT-AX86U | NETGEAR RAX40 |
| --- | --- | --- | --- |
| Device/profile selection | Required | Required | Required |
| Official firmware source guidance | Required | Required | Required |
| Firmware file validation | Required | Required | Required |
| Wired interface preflight | Required | Required | Required |
| Static IP guidance | Likely | Required | Unknown |
| DHCP return guidance | Unknown | Required | Unknown |
| Recovery mode entry timer | Required | Required | Likely |
| LED/state cue capture | Required | Required | Required |
| Web recovery upload | Primary | Possible/brand context | Unknown |
| Passive TFTP PUT | Unknown | Primary | Possible/research |
| Active TFTP server | Possible in TP-Link families, not AX55-proven | No | Unknown |
| NMRP/orchestration | No | No | Research target |
| Transfer error mapping | Medium | High | High |
| Post-upload wait model | Required | Required | Required |
| Manual power-cycle model | Unknown | Required for RT-AC86U observed unit | Unknown |
| Incident capture | Required | Required | Required |

## Deliverables Per Reference Device

For each reference device, produce these artifacts in order:

1. `source index`
   - official source pages
   - applicability scope
   - explicit evidence gaps
   - no profile generation unless model-specific evidence is sufficient

2. `app field coverage report`
   - which runtime steps are supported
   - which steps are unknown
   - which unknowns block App guidance

3. `lab test plan`
   - exact device state to test
   - firmware source
   - network setup
   - recovery entry method
   - packet/log capture expectations
   - stop conditions

4. `runtime attempt record`
   - success or failure
   - timing
   - LED/ping/service observations
   - transfer behavior
   - post-upload behavior
   - outcome classification

5. `profile or incident update`
   - successful reproducible facts may update incoming/reviewed candidates
   - unresolved or failed behavior becomes incident data

## Gates

Allowed now:

- reference-device planning
- official source indexing
- App runtime coverage reports
- lab test plans
- incident capture from failed or partial tests
- RT-AC86U App workflow validation based on existing incoming profile

Not allowed yet:

- long-tail model expansion
- automatic profile generation from workflow-level sources
- copying RT-AC86U facts into RT-AX86U
- moving R7000 to reviewed
- writing `final/`
- publishing App guidance that hides unknown hardware/firmware scope

## Recommended Immediate Sequence

1. Create an App runtime attempt schema.
2. Use RT-AC86U to pressure-test that schema because it has the richest current evidence.
3. Prepare AX55 official/model-specific evidence and lab plan for Web Recovery.
4. Prepare RAX40 source-list and lab plan only after AX55/ASUS runtime flow has stabilized.

This keeps the App upgrade grounded in real device behavior while preventing profile sprawl.

The first App implementation slice should follow the module-level field contract in `docs/app_upgrade_field_contract.md`.
