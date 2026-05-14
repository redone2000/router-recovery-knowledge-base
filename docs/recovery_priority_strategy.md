# Recovery Priority Strategy

Date: 2026-05-13
Status: Stage 1 governance rule

## Core Decision

Recovery knowledge production must have explicit brand preference and device ordering.

The project must not expand by model count or market-share lists. Router models are effectively unbounded, and uncontrolled coverage creates schema drift, weak evidence, repeated content, and workflow confusion.

Production priority is based on Recovery Opportunity Priority.

## Recovery Opportunity Priority

Prioritize work by these factors:

| Factor | Priority |
| --- | --- |
| recovery user volume | very high |
| panic recovery likelihood | very high |
| workflow abstraction value | very high |
| recovery transparency | high |
| evidence collectability | high |
| beginner-user impact | high |
| SEO/search demand | high |

Market popularity alone is not sufficient. A device or brand is valuable when it improves recovery workflow understanding, panic-user guidance, or high-confidence profile generation.

## Brand Priority

Current Stage 1 priority order:

| Priority | Brand | Role |
| --- | --- | --- |
| 1 | TP-Link | global panic recovery and Web Recovery reference world |
| 2 | ASUS | enthusiast Rescue Mode and post-upload behavior reference world |
| 3 | NETGEAR | recovery orchestration, NMRP, TFTP timing, and legacy complexity research |

This order is not a final product ranking. It is a knowledge-production ranking.

## Reference Device Strategy

Use reference devices to stabilize workflows before expanding families.

| Brand | Reference Device | Purpose |
| --- | --- | --- |
| TP-Link | Archer AX55 | Web Recovery / Archer AX family applicability |
| ASUS | RT-AX86U / RT-AC86U family comparison | ASUS Rescue Mode and post-upload phase |
| NETGEAR | RAX40 | modern NETGEAR recovery orchestration and NMRP/TFTP comparison |

Existing lab data for ASUS RT-AC86U remains valid as observed evidence, but new ASUS production ordering should treat AX86U-class devices as the forward-looking reference family when available.

R7000 remains useful as an incident and legacy orchestration case, but it should not be treated as the primary NETGEAR reference profile while its TFTP recovery window is unresolved.

## Family Expansion Order

Expand only after a reference workflow is stable.

### TP-Link

Suggested sequence:

```text
AX55 -> AX72 -> AX23
```

Goal:

- validate Archer AX Web Recovery family behavior
- separate series-level evidence from model-level profile facts
- identify hardware-version and region constraints

### ASUS

Suggested sequence:

```text
AX86U -> AX58U -> AX88U
```

Goal:

- compare ASUS Rescue Mode behavior across enthusiast routers
- validate whether post-upload behavior generalizes
- preserve observed-only fields until broader evidence exists

### NETGEAR

Suggested sequence:

```text
RAX40 -> XR1000 -> WAX202
```

Goal:

- study modern NETGEAR recovery orchestration
- compare NMRP, TFTP, and web/discovery paths
- avoid over-promoting legacy timing-sensitive behavior from R7000

Stage 1 official-source search did not find NETGEAR documentation that mentions NMRP. Until official or lab-validated evidence exists, NMRP remains research-only and must not become App guidance or a reviewed workflow.

## Production Order

The project should produce knowledge in this order:

1. Recovery Foundations
2. Recovery Workflow Types
3. Brand Recovery Worlds
4. Reference Devices
5. Family Expansion
6. Long-tail Profiles

Long-tail profiles should not start until the relevant workflow and brand system are mature enough to absorb model-specific facts without duplicating article logic.

## OpenClaw Collection Rule

OpenClaw should collect by Recovery Workflow Coverage Gap, not by unlimited model hunting.

Examples of valid collection goals:

- missing Web Recovery evidence for TP-Link Archer AX family
- missing ASUS Rescue Mode timing evidence
- missing post-upload phase evidence for ASUS or TP-Link
- missing NETGEAR NMRP incident evidence
- missing source evidence that distinguishes TFTP from NMRP on modern NETGEAR devices

Examples of invalid collection goals:

- collect as many TP-Link models as possible
- generate one profile per search result
- expand to long-tail models before workflow gaps are closed
- infer family behavior from a single series-level source

## Gate Rule

A candidate device may enter profile preparation only when it supports one of these goals:

- validates a reference workflow
- fills a known workflow evidence gap
- confirms or rejects a brand-system assumption
- resolves an open incident
- provides model-specific evidence for an already prioritized family

Otherwise, it stays out of the queue.
