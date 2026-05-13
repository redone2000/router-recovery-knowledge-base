# Recovery Priority Strategy Decision

Date: 2026-05-13
Prepared by: Codex

## Decision

Adopt Recovery Opportunity Priority as the ordering rule for knowledge production.

The project will not prioritize work by market share, number of models covered, or opportunistic source availability alone. Brand and model ordering must be explicit to prevent uncontrolled long-tail profile expansion.

## Rationale

Router recovery knowledge has unbounded model count and high tacit-knowledge variance. Without priority discipline, the project is likely to accumulate partial profiles, repeated tutorials, weak evidence, and unstable workflow abstractions.

The higher-leverage path is:

```text
workflow abstraction
  -> brand recovery world
  -> reference device
  -> family expansion
  -> long-tail profile
```

## Brand Order

Stage 1 brand priority:

1. TP-Link
2. ASUS
3. NETGEAR

This is not a market ranking. It is a recovery knowledge-production ranking.

## Reference Devices

| Brand | Reference Direction | Current Rule |
| --- | --- | --- |
| TP-Link | Archer AX55 | Web Recovery and Archer AX applicability first |
| ASUS | AX86U-class Rescue Mode family | RT-AC86U lab data remains observed evidence |
| NETGEAR | RAX40 | Use modern NETGEAR as reference; keep R7000 as incident/research until reproducible |

## Operational Impact

OpenClaw tasks should be phrased as coverage gaps:

- missing Web Recovery evidence for TP-Link Archer AX family
- missing ASUS Rescue Mode timing or post-upload evidence
- missing NETGEAR NMRP/TFTP orchestration evidence

OpenClaw should not receive broad tasks like "collect more models" or "expand all TP-Link profiles."

## Files Updated

- `docs/recovery_priority_strategy.md`
- `docs/recovery_knowledge_system_architecture.md`
- `WORKFLOW.md`
- `RULES.md`

## Gate Rule

A candidate device may enter profile preparation only when it supports one of these goals:

- validates a reference workflow
- fills a known workflow evidence gap
- confirms or rejects a brand-system assumption
- resolves an open incident
- provides model-specific evidence for an already prioritized family

Otherwise, it remains outside the queue.
