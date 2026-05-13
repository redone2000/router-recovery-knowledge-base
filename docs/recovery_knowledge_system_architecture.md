# Recovery Knowledge System Architecture

Date: 2026-05-13
Status: Stage 1 governance draft

## Core Decision

Router Recovery Knowledge is not a model-count database.

It is a recovery knowledge system built from two tracks:

- abstraction layer: reusable recovery concepts, workflows, brand systems, and language
- evidence layer: model profiles, lab observations, incidents, source indexes, and review decisions

Both tracks are required.

If the project only creates model profiles, it will become fragmented and repetitive. If it only creates abstract workflows, it will become plausible but wrong in real recovery situations.

## Why This Architecture Exists

Router recovery knowledge is unusually prone to fragmentation:

- a forum comment mentions a timing trick
- a vendor article describes only the happy path
- a YouTube video shows an LED state
- a lab test reveals a post-upload power cycle
- a user report finds one LAN port works better

These pieces are valuable, but they are not equal to reviewed profile guidance.

The system must preserve these fragments without letting them become unsupported final instructions.

## Layer 1: Recovery Foundations

Foundations are cross-brand concepts that explain how recovery works.

Examples:

- What is Recovery Mode?
- Why static IP may be required
- Why Wi-Fi should be disabled during wired recovery
- Why upload completion may not mean recovery completion
- Why ping is not a sufficient success/failure signal
- How to think about recovery windows
- Why firmware format and hardware version matter

Primary use:

- App onboarding
- panic-entry explanations
- AI assistant grounding
- support docs
- SEO entry content

## Layer 2: Recovery Workflows

Workflows are reusable execution patterns.

Examples:

- Web Recovery Workflow
- Passive TFTP / TFTP PUT Workflow
- Active TFTP / router-pulls-firmware Workflow
- ASUS Rescue Mode Workflow
- NETGEAR NMRP Workflow
- Post-upload phase Workflow

Model profiles should be treated as parameterized instances of workflows.

Example:

```text
Passive TFTP PUT Workflow
  -> ASUS RT-AC86U
     -> rescue IP, client IP, file type, LAN port, post-upload behavior
  -> NETGEAR R7000
     -> official support exists, but local timing remains unresolved
```

## Layer 3: Brand Recovery Systems

Brand systems describe vendor-specific recovery behavior and terminology.

Examples:

- ASUS Recovery World
  - Rescue Mode
  - ASUS `.w` firmware
  - reset-hold-power-on choreography
  - post-upload behavior
- TP-Link Recovery World
  - Archer AX web recovery
  - series-level versus model-level applicability
- NETGEAR Recovery World
  - TFTP PUT
  - NMRP
  - timing/orchestration sensitivity

Brand systems help avoid duplicating the same explanation across many model profiles.

## Layer 4: Model Profiles

Model profiles are structured, evidence-backed parameter sets.

They should contain stable profile facts such as:

- model and hardware version scope
- recovery method
- recovery IP
- client IP requirements
- firmware file type
- required LAN port
- recovery entry method
- post-upload behavior
- risk warnings
- source evidence

Model profiles are not the place for raw speculation or unresolved failed attempts.

Current rule:

- `incoming/`: draft profile candidates
- `reviewed/`: reviewed candidates only after explicit approval
- `final/`: never written automatically

## Layer 5: Recovery Incidents

Incidents record success/failure cases, timing clues, and tacit knowledge.

They are the right place for observations like:

- TTL=100 but WRQ timeout
- manual `put` timing is hard to catch
- LAN1 appears more reliable
- wait after upload before power cycle
- recovery page responds only after a second LED phase
- NMRP appears more stable than TFTP for a given device

Incident data should not automatically become model profile guidance.

Pipeline:

```text
incident -> pattern -> hypothesis -> lab validation -> profile update
```

## Panic Entry Layer

Users often enter the recovery system through symptoms, not model names.

Examples:

| Panic Symptom | Likely Knowledge Path |
| --- | --- |
| 192.168.1.1 does not open | Recovery Preparation / IP assignment |
| TFTP timeout | Passive TFTP Workflow / Recovery Window |
| Upload finished but nothing happens | Post-upload phase |
| Recovery page does not open | Web Recovery Workflow |
| TTL=100 | Recovery Window / readiness signal |

This layer should guide App onboarding, website content, and AI assistant routing.

## Relationship Graph

```text
panic symptom
  -> recovery foundation
  -> recovery workflow
  -> brand recovery system
  -> model profile
  -> incident evidence / lab observation
```

The graph is bidirectional:

- abstract workflow guides what profile fields are needed
- lab observations and incidents correct the workflow

## Current Project Implications

### R7000

R7000 should not move to `reviewed/` right now.

It has official TFTP support evidence, but local testing did not reproduce a clear success. The likely unresolved variable is timing/orchestration around the TFTP WRQ window.

Current status:

- keep source index
- keep incoming draft as historical candidate
- pause reviewed migration
- capture future tests as incidents or lab retests

### ASUS RT-AC86U

ASUS RT-AC86U is a strong example of the evidence layer improving the abstraction layer.

The observed post-upload power-cycle requirement forced the schema to represent the post-upload phase explicitly.

Current status:

- keep incoming draft
- reviewed-candidate migration requires Owner confirmation
- keep observed fields marked `observation_only`

### OpenClaw

OpenClaw should not only collect model-specific profile facts.

Future tasks may also collect:

- workflow evidence
- panic symptom evidence
- brand system evidence
- source material that explains failure modes

OpenClaw must still avoid inference and must not generate final guidance.

## Non-Goals

- Do not chase large model coverage before the workflow and incident layers exist.
- Do not create a second manual source of truth for App export profiles.
- Do not treat a single incident as final profile guidance.
- Do not hide failed lab tests; failed tests are useful incident evidence.

## Next Architecture Tasks

1. Create `docs/recovery_language.md`.
2. Define an incident schema before recording more R7000 timing tests.
3. Create workflow documents for:
   - Passive TFTP PUT
   - Web Recovery
   - Post-upload phase
4. Later, build an export tool that generates App-friendly JSON from reviewed/final profiles plus workflow metadata.
