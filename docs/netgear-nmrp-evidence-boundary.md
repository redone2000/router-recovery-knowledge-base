# NETGEAR NMRP Evidence Boundary

NMRP-based recovery can be useful for some NETGEAR devices, but this project treats it differently from official NETGEAR TFTP documentation.

This page explains the evidence boundary so NMRP context does not get promoted into unsupported model-specific recovery guidance.

## What NMRP Is In This Knowledge Base

NMRP is documented here as a NETGEAR-related recovery workflow used by third-party tooling such as `nmrpflash`.

It is not automatically treated as:

- official NETGEAR guidance
- a universal NETGEAR recovery method
- proof that a specific model can be recovered by NMRP
- proof that NMRP is safer than TFTP for every device
- a replacement for model-specific firmware checks

## Source Categories

### Official NETGEAR TFTP Sources

Official NETGEAR sources currently indexed here include:

- `https://kb.netgear.com/000059633/How-to-upload-firmware-to-a-NETGEAR-router-using-TFTP-client`
- `https://kb.netgear.com/000064624/How-do-I-upload-firmware-to-my-NETGEAR-router-using-TFTP-on-Apple-macOS`

These support passive TFTP upload evidence for listed models such as R7000, but hardware-version and firmware-version scope still matter.

They do not prove NMRP behavior.

### Third-Party NMRP Tooling

The main third-party source indexed here is:

- `https://github.com/jclehner/nmrpflash`

This source supports NMRP workflow understanding:

- interface selection
- computer-side recovery tool
- NMRP request/response orchestration
- firmware upload
- keep-alive and post-upload waiting behavior
- macOS support for the tool

Boundary:

- It is not official NETGEAR documentation.
- It is not enough to generate a model-specific recovery profile by itself.
- It does not replace exact firmware, hardware, and region checks.

### Community Reports

The indexed Reddit WNDR3400 report is retained as context only.

Boundary:

- single social-media report
- not independently verified in this project
- does not generalize to all NETGEAR devices
- does not support profile generation by itself

## R7000 Incident Boundary

This project has an R7000 lab incident where:

- official TFTP evidence exists
- `TTL=100` and ping were observable
- manual macOS TFTP PUT did not complete successfully in the observed timing window
- nmrpflash completed recovery easily in that test context

This is useful evidence, but it is still incident-level.

It does not prove:

- all R7000 units should use NMRP first
- official TFTP is wrong
- NMRP is an official NETGEAR method
- the local timing issue applies to every firmware or hardware revision

The safe conclusion is narrower:

```text
For the observed R7000 incident, manual TFTP timing was unreliable while nmrpflash succeeded. Keep R7000 blocked from reviewed guidance until recovery behavior is reproduced with stronger evidence.
```

## TFTP vs NMRP

Treat these as different workflows.

TFTP recovery often focuses on:

- static IP setup
- TFTP client/server direction
- firmware upload timing
- whether the router replies to WRQ or RRQ

NMRP recovery often involves:

- a dedicated recovery protocol
- interface selection
- automated timing/orchestration
- protocol-specific keep-alive behavior
- tool-specific firmware upload flow

Do not merge them into one generic "NETGEAR recovery" instruction.

## Evidence Needed For Model Guidance

Before publishing model-specific NMRP guidance, collect:

- exact model
- hardware version
- firmware version before recovery
- firmware file source URL
- filename and file type
- operating system and tool version
- network interface used
- command used
- timing notes
- upload result
- post-upload wait behavior
- final admin or network state
- independent confirmation or reproducible lab observation

## Safe Public Wording

Prefer:

```text
NMRP-based tools such as nmrpflash can be useful for some NETGEAR recovery workflows, but model-specific guidance needs stronger evidence and should be separated from official NETGEAR TFTP documentation.
```

Avoid:

```text
Use NMRP for all NETGEAR routers.
```

Avoid:

```text
NMRP is the official NETGEAR recovery method.
```

## Related Tool

Router Recovery for macOS can preserve NETGEAR recovery attempt details such as firmware choice, static IP, timing, and observed result. NMRP-specific guidance still needs model-level evidence and careful source labeling.
