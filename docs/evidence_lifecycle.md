# Evidence Lifecycle

Date: 2026-05-13
Status: Stage 1 governance draft

## Purpose

This document defines how evidence moves through the Router Recovery Knowledge System.

The goal is to prevent raw observations, source fragments, or failed tests from becoming profile guidance too early.

## Core Lifecycle

```text
AI model hypothesis
  -> source / lab observation / user report
  -> source index or incident
  -> pattern candidate
  -> workflow update
  -> incoming profile
  -> reviewed candidate
  -> final profile
```

No stage automatically promotes to the next stage.

Every promotion requires an explicit gate decision.

`model_hypotheses/` is a pre-evidence queue. It may suggest what to research next, but it is not itself source evidence.

## Evidence Types

### Model Hypothesis Queue

Location:

- `model_hypotheses/`
- `schema/model_hypothesis.schema.json`

Purpose:

- let AI agents propose and audit candidate models
- classify suspected workflows only when evidence supports them
- preserve missing proof before any profile draft
- keep research seeds out of `incoming/`, `reviewed/`, and `final/`

Allowed outputs:

- hypothesis JSONL records
- source-gap reports
- blocked/deferred candidate notes
- exact JSONL proposals for Owner review

Disallowed outputs:

- automatic `incoming/` profile generation
- automatic App support claims
- inferred TFTP direction
- reviewed/final profile writes

Promotion from hypothesis to `incoming/` requires `hypothesis_status=ready_for_incoming_review`, `promotion_gate=ready_for_owner_review`, and explicit Owner approval.

### Source Index Evidence

Location:

- `data/source_index*.jsonl`
- `sources/`

Purpose:

- preserve source metadata
- classify applicability scope
- record evidence gaps
- prevent premature profile generation

Allowed outputs:

- source index rows
- source notes
- source review reports

Disallowed outputs:

- automatic `reviewed/` writes
- automatic `final/` writes
- model profile generation unless a gate explicitly allows it

### Incident Evidence

Location:

- `incidents/`
- `schema/recovery_incident.schema.json`

Purpose:

- preserve success/failure cases
- capture tacit recovery knowledge
- record hypotheses, experiments, results, and next actions
- block or inform profile gates

Incident evidence is not profile guidance.

Example:

```text
R7000 TTL=100 visible but TFTP PUT times out.
```

This is valuable evidence, but it blocks reviewed profile promotion until resolved.

### Workflow Evidence

Location:

- `workflows/`
- `schema/recovery_workflow.schema.json`

Purpose:

- model reusable recovery workflows
- identify phases and readiness signals
- connect failure modes to incidents
- define required profile parameters

Workflows are not model instructions by themselves. They require profile parameters and evidence.

### Profile Evidence

Location:

- `incoming/`
- `reviewed/`
- `final/`

Purpose:

- structured model-specific recovery candidate or approved data

Profiles must preserve source evidence and uncertainty.

## Gate Decisions

### Source Index -> Incoming Profile

Allowed only when:

- model applicability is established or explicitly unknown with review approval
- recovery method is directly evidenced
- TFTP direction is directly evidenced if TFTP is claimed
- evidence gaps are recorded
- confidence cap is clear

### Incident -> Pattern Candidate

Allowed when:

- multiple incidents show similar behavior, or
- one high-quality lab observation reveals an important workflow gap

Pattern candidates must remain outside final profile guidance until validated.

### Pattern Candidate -> Workflow Update

Allowed when:

- the pattern affects reusable workflow behavior
- the workflow can express the pattern without overgeneralizing it
- linked incidents remain traceable

Example:

R7000 timing failure updates Passive TFTP PUT workflow with:

```text
TTL/ping is a weak readiness signal.
```

### Incoming Profile -> Reviewed Candidate

Allowed only after:

- profile validation passes
- evidence review passes
- Owner or human reviewer confirms uncertainty boundaries
- paused or blocked lifecycle decisions are absent or resolved

Observed-only data may move to reviewed candidate only when clearly labeled.

### Reviewed Candidate -> Final Profile

Allowed only after:

- maintainer approval
- no unresolved blocking incidents
- source evidence is stable
- confidence is appropriate
- final data write is explicitly approved

Agents and tools must not write `final/` automatically.

## Status Semantics

### observed-only

The behavior was observed but must not be generalized.

Use for:

- lab observations
- tested-unit behavior
- timing clues
- one-off recovery outcomes

### unresolved

The incident or evidence question is not resolved.

Use when:

- tests failed
- timing is unclear
- a hypothesis exists but has not been verified

### blocked

The evidence actively prevents profile advancement.

Use when:

- lab testing contradicts or fails to reproduce expected behavior
- profile would mislead users
- key workflow uncertainty remains unresolved

### reviewed candidate

Human-reviewed candidate data, not final production data.

### final

Approved production data.

Only an explicit Owner/Maintainer decision may create final data.

## Current Examples

### NETGEAR R7000

Status:

- source evidence retained
- incoming profile paused
- incident recorded
- reviewed gate blocked

Reason:

Official TFTP path exists, but local lab testing did not reproduce a clear TFTP success. Timing/orchestration remains unresolved.

### ASUS RT-AC86U

Status:

- incoming profile retained
- Claude review passed
- Owner confirmation required before reviewed-candidate migration
- observed behavior groups marked `observation_only`

Reason:

High-quality local observation supports the draft, but hardware/firmware scope remains unknown and must be explicitly bounded.

## Agent Responsibilities

### OpenClaw

May produce:

- source index proposals
- source notes
- incident candidate reports if explicitly assigned

Must not:

- write `reviewed/`
- write `final/`
- infer missing recovery facts
- turn incidents into profile guidance

### Claude Code

May produce:

- schema reviews
- evidence-quality reviews
- profile gate recommendations
- workflow or incident review recommendations

Must not:

- collect new sources unless explicitly assigned
- write final data
- promote profiles without Owner gate

### Codex

May produce:

- tooling
- schema changes
- governance docs
- incoming drafts when gate allows
- reports
- validators

Must not:

- write `final/` automatically
- override Owner decisions
- convert unresolved incidents into reviewed profile guidance

## Validation Commands

Run these before committing related changes:

```bash
python3 tools/validate_model_hypotheses.py model_hypotheses
python3 tools/validate_profiles.py incoming
python3 tools/validate_incidents.py
python3 tools/validate_workflows.py
git diff --check
```

## Non-Goals

- Do not use incident count as a substitute for evidence quality.
- Do not promote a workflow because it sounds generally true.
- Do not expand model coverage before workflow and incident gates are clear.
- Do not hide failed tests; failed tests are recovery evidence.
