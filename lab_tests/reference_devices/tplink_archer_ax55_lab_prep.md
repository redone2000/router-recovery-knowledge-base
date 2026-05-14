# TP-Link Archer AX55 Lab Prep

Date: 2026-05-14
Status: pre-test plan
Reference role: Web Recovery / beginner panic flow

## Goal

Validate whether Archer AX55 can support an App-guided Web Recovery workflow.

This test should answer:

- Is recovery model-specific or only series-level?
- What static IP, recovery IP, and page URL are actually required?
- Which button/LED sequence reliably enters recovery mode?
- What firmware source and file format are accepted?
- What happens after upload: wait, reboot, DHCP, admin URL?

## Current Gate

No profile generation yet.

Known state:

- TP-Link official workflow evidence exists at series/workflow level.
- AX55 model-specific recovery behavior is not sufficiently verified.
- Any failed or ambiguous attempt should become an incident candidate.

## Pre-Test Checklist

- Confirm exact device label: `Archer AX55`
- Record hardware version if visible.
- Record region if visible on label or firmware page.
- If Web UI is reachable, record current firmware version.
- Open or save official AX55 firmware/support page.
- Download only from official TP-Link source.
- Record whether checksum is available.
- Prepare Ethernet cable and Mac wired adapter.
- Note Mac wired interface name.
- Decide whether Wi-Fi will be disabled or only warned.

## Firmware Preparation

Record:

- official download/support page URL
- firmware file extension
- whether the downloaded file is compressed
- whether extraction is required
- final selected firmware filename, without local path
- file size
- checksum status if available

Do not record private local file paths in exported runtime attempts.

## Recovery Entry Test

Record:

- power-off duration before test
- button used
- hold timing
- LED state sequence
- LAN port used
- whether recovery page appears
- recovery page URL/IP
- whether HTTP or HTTPS works
- whether ping responds and TTL, if checked

Do not assume Archer AX series instructions apply until AX55 behavior is observed.

## Web Recovery Test

If a recovery page is reachable, record:

- Mac static IP/cidr
- recovery page IP/URL
- upload form behavior
- accepted/rejected firmware file
- upload progress behavior
- immediate page result after upload
- wait time until reboot or reachable state
- DHCP behavior after recovery
- gateway/admin URL after recovery
- firmware version after recovery, if reachable
- whether configuration was retained/reset/unknown

## App Questions To Answer

- Can the App guide this as Web Recovery without TFTP?
- Does the App need to set or instruct a specific static IP?
- Is recovery page readiness detectable by HTTP probe?
- Is ping useful or irrelevant?
- Does the App need a post-upload wait timer?
- Does the App need manual power-cycle guidance?

## Stop Conditions

Stop and record an incident if:

- the page does not appear after 3 controlled entry attempts
- different LAN ports produce conflicting behavior
- firmware source/model match is uncertain
- upload page appears but rejects the official firmware
- post-upload state is unclear after a reasonable wait

## Expected Outputs

- one runtime attempt record for each meaningful attempt
- incident candidate for repeated failure or ambiguous state
- AX55 field coverage update
- no incoming profile unless model-specific behavior is confirmed and reviewed
