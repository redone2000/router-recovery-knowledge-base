# Contributing

Thank you for helping improve router recovery documentation.

This project is conservative by design. Recovery instructions can affect real hardware, so claims need clear evidence and careful wording.

## Good Contributions

- Official recovery documentation links
- Device-specific recovery observations
- Failed recovery attempts with useful timing or network details
- Corrections for hardware version, region, firmware file, or IP address details
- Troubleshooting notes that explain what was observed and what remains unknown

## Evidence Requirements

When submitting a recovery claim, include as much of the following as possible:

- Vendor and model
- Hardware version or region, if visible
- Firmware version before and after the attempt
- Recovery method used
- Computer IP address and router IP address
- Whether the router acted as TFTP server or TFTP client
- Logs, packet capture notes, screenshots, or terminal output
- Official documentation URL, if available

## Wording Rules

- Say "observed on this device" instead of "works for all models" unless broad evidence exists.
- Say "upload completed" only when the transfer completed.
- Say "recovery completed" only when the router booted and became usable again.
- Mark unknown TFTP direction as unknown.
- Do not infer behavior from `TTL=100` alone.
- Do not recommend firmware files without checking model, hardware version, and region.

## Sensitive Information

Do not submit:

- serial numbers
- MAC addresses
- passwords
- private network screenshots with unrelated personal information
- vendor account credentials
- proprietary firmware contents

## Commercial App Boundary

Router Recovery for macOS is a separate commercial app. This repository is for public recovery knowledge, documentation, schemas, and maintenance tooling. Contributions to this repository do not require using the app.
