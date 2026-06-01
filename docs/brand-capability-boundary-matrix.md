# Brand Capability Boundary Matrix

Date: 2026-06-01
Status: Working governance note

This document defines how brand and device research should support the Router Recovery macOS app without turning this repository into an unlimited model list.

The goal is to expand recovery capability boundaries, not to claim broad device support before evidence exists.

## Core Rule

Device and brand work should answer one of these questions:

- What can the app safely guide?
- What should remain public documentation only?
- What is still research-only?
- Which reference device would reduce the most uncertainty?

Do not expand by market-share lists, search-result lists, or model count.

## Capability Boundary Levels

| Level | Meaning | App use |
| --- | --- | --- |
| App-guidable | Evidence is strong enough for guided in-app steps with visible warnings | Allowed |
| App-assisted | The app can help record settings, logs, or attempts, but should not promise the workflow | Allowed with conservative copy |
| Documentation-only | Useful public explanation, but not enough for guided app behavior | Do not convert to in-app instructions |
| Research-only | Hypothesis, source gap, or conflicting evidence | Do not use in user-facing guidance |
| Blocked | Evidence conflict or failed reproduction creates meaningful user risk | Do not promote |

## Current Brand Matrix

| Brand / family | Current public value | App-guidable boundary | Documentation-only boundary | Research-only or blocked boundary | Reference devices |
| --- | --- | --- | --- | --- | --- |
| ASUS | Rescue Mode, Firmware Restoration, passive TFTP, post-upload wait behavior | Observed ASUS passive TFTP flows may inform cautious app copy when model-specific evidence exists | ASUS Rescue Mode and Firmware Restoration concepts can be documented at brand/workflow level | Do not generalize RT-AC86U or RT-AX86U behavior to all ASUS routers; do not claim stock ASUSWRT behavior from Merlin-only evidence | RT-AX86U, RT-AC86U |
| TP-Link | Web Recovery, Emergency Mode, active TFTP examples, firmware filename constraints | App may support recording and checklist guidance when model-specific IP, filename, and method evidence exists | Series-level Omada/EAP/Pharos evidence can explain TP-Link recovery patterns | Archer AX family behavior stays limited until model-specific recovery evidence is collected; region and hardware version are high-risk gaps | Archer AX55, then AX72 / AX23 |
| NETGEAR | TFTP timing risk, NMRP boundary, legacy recovery complexity | App should primarily assist with logging, IP setup records, and result separation until method evidence is stronger | Public docs can explain official TFTP vs community NMRP boundary | R7000 TFTP remains timing-sensitive and should not be promoted as a stable app-guided path; NMRP is not official unless source evidence proves it | RAX40, R7000 as incident/legacy case |
| OpenWrt / ImmortalWrt | Failsafe, firmware selection, sysupgrade vs factory image boundaries | App can provide general recovery records and cautionary checklists, not device-universal OpenWrt recovery promises | Failsafe vs bootloader/TFTP distinctions are strong public documentation topics | Do not treat OpenWrt support as proof that vendor recovery, TFTP direction, or firmware image format is known for a device | Device-specific OpenWrt pages, not one universal model |

## Testing Priority

Test a concrete model only when it satisfies at least one gate:

- It validates a recovery workflow used by the app.
- It resolves an evidence conflict.
- It represents a priority brand family.
- It has official documentation that needs lab boundary confirmation.
- It can improve user-visible safety copy, such as TFTP direction, wait time, power-cycle timing, or recovery completion criteria.

Do not buy or test devices only to increase model count.

## Near-Term Test Candidates

| Priority | Candidate | Why it matters | Do not claim until proven |
| --- | --- | --- | --- |
| 1 | ASUS RT-AX86U / RT-AC86U comparison | Validates ASUS Rescue Mode, passive TFTP, and post-upload behavior boundaries | All ASUS models behave the same |
| 2 | TP-Link Archer AX55 | Anchors Archer AX family Web Recovery or TFTP behavior for a common consumer line | All Archer AX models share the same recovery method |
| 3 | NETGEAR RAX40 | Modern NETGEAR reference for TFTP/NMRP/orchestration research | NMRP is official, or TFTP is stable across NETGEAR |
| 4 | NETGEAR R7000 retest | Preserves legacy timing-sensitive incident knowledge | Official TFTP documentation is enough for stable app guidance |

## App Guidance Implications

The app should prefer capability-based language:

- "Set Mac IP and record recovery attempt details"
- "Transfer completed; wait before judging recovery"
- "Confirm router boot and admin access before calling recovery complete"
- "This model requires verification before guided recovery can be considered reliable"

The app should avoid unsupported language:

- "Supported ASUS routers"
- "Works for all TP-Link Archer models"
- "NETGEAR NMRP recovery is official"
- "Upload completed, recovery successful"
- "TTL=100 means TFTP is ready"

## Evidence Needed Before Stronger App Guidance

For any model-specific guided path, collect:

- exact model and hardware version
- firmware family and version before the attempt
- recovery entry method and LED behavior
- router IP and Mac static IP requirements
- TFTP direction or web recovery page behavior
- firmware filename or file-type requirements
- transfer result
- post-upload wait behavior
- final boot and admin-access result
- whether a manual power cycle was used
- official source links, packet notes, logs, or screenshots with sensitive data removed

## Maintenance Use

Use this matrix during weekly maintenance to decide:

1. whether a user report can become public documentation
2. whether a model candidate belongs in `incoming/`
3. whether a lab test should be scheduled
4. whether app copy can be strengthened
5. whether a claim must stay documentation-only or research-only

If a proposed device does not improve a capability boundary, defer it.
