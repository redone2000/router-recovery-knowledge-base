# TP-Link FAQ 3186 EAP Recovery Mode Source Note

URL: https://www.tp-link.com/us/support/faq/3186/
Title: How to use the Recovery Mode to recover the firmware for EAP
Workflow target: Web Recovery / Active TFTP Server
Applicability scope: series_level (listed EAP Access Point models)
Source type: official_documentation

## Evidence Topics

- Recovery Mode for listed EAP models
- model-dependent static client IP requirements
- HTTP-only recovery page behavior
- official firmware file requirement
- TFTP path where PC acts as TFTP server and EAP acts as TFTP client
- TFTP filename requirement for selected models
- manual timing/retry sensitivity during reset-hold entry

## Evidence Gaps

- Series/listed-model evidence only
- Hardware-version scope remains unknown
- Not all EAP models support the same recovery methods
- Partial model applicability needs separate model-level validation before profile use

## Profile Boundary

This source can support Web Recovery and Active TFTP workflow abstraction. It must not generate model-specific EAP profile guidance without model-level evidence and reviewer approval.
