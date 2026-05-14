# ASUS RT-AX86U / RT-AC86U Lab Prep

Date: 2026-05-14
Status: pre-test plan
Reference role: Rescue Mode / Passive TFTP PUT success-rate details / post-upload phase

## Goal

Use ASUS testing to validate the App's complex guided recovery flow:

- official firmware source
- macOS permissions
- static IP setup
- Rescue Mode entry
- Passive TFTP PUT transfer
- TFTP timing and ACK-port behavior
- transfer error mapping
- post-upload wait
- manual power-cycle handling
- DHCP return and admin URL discovery
- small details that materially improve success rate

## Current Gate

RT-AC86U:

- incoming profile exists
- lab-observed
- suitable for App workflow validation
- not final guidance

RT-AX86U:

- separate target
- must not inherit RT-AC86U facts without direct evidence
- create separate runtime attempts and incident/profile artifacts

## Pre-Test Checklist

- Confirm exact model: RT-AC86U or RT-AX86U.
- Record hardware version if visible.
- Record current firmware version if Web UI is reachable.
- Confirm official ASUS firmware/support page for the exact model.
- Record firmware file extension and checksum availability.
- Prepare Mac wired adapter and note interface name.
- Confirm Local Network permission behavior if using the App.
- Confirm file picker access to selected firmware.
- Decide whether Wi-Fi is disabled or warning-only.
- Prepare packet capture if available.

## Firmware Preparation

Record:

- official ASUS support/download page URL
- selected firmware version
- selected filename, without local path
- extension
- size
- checksum algorithm/status if available
- whether model match was confirmed by the tester

Do not reuse RT-AC86U firmware assumptions for RT-AX86U.

## Rescue Mode Entry

Record:

- LAN port used
- power-off duration
- button used
- hold seconds
- LED sequence
- when the Mac link becomes active
- whether ping responds
- TTL if ping responds
- whether ping behavior is stable or intermittent

For RT-AC86U, existing observation says LAN1 near WAN and slow flashing power LED, but retest should still record actual behavior.

## Passive TFTP PUT Test

Record:

- client tool: App / macOS `tftp` / Swift POC / other
- Mac static IP/cidr
- router recovery IP
- TFTP mode
- filename used
- first ACK timing
- ACK source port
- whether server switches to ephemeral port
- duration
- bytes sent
- block count
- error packet, if any

Success-rate details to test and record:

- whether sending WRQ immediately after TTL=100 differs from waiting 1-2 seconds
- whether repeated WRQ attempts improve success or create instability
- whether macOS `tftp`, Swift POC, and App behavior differ
- whether ACK source port remains fixed at 69 across multiple runs
- whether filename changes affect acceptance
- whether a different LAN port changes reliability
- whether Wi-Fi enabled/disabled changes routing or success
- whether Local Network permission failure can be detected before transfer

If ACK source port behavior differs from the profile, do not update profile directly. Record a runtime attempt and incident candidate.

## Post-Upload Test

Record:

- whether upload completed
- exact wait time before next action
- whether router reboots automatically
- whether manual power cycle is needed
- when Mac is switched back to DHCP
- DHCP IP/gateway result
- admin URL used
- firmware version after recovery
- configuration retained/reset/unknown

For RT-AC86U, manual power-cycle after about 3 minutes is currently a critical observed behavior. Retest should confirm or challenge it.

## App Questions To Answer

- Does the App preflight catch Local Network permission failures?
- Does the App clearly separate upload completion from recovery completion?
- Does the App handle fixed ACK source port 69 correctly?
- Does the App preserve enough transfer metadata for debugging?
- Does the App guide DHCP return and gateway discovery clearly?
- Does the App avoid promising configuration retention/reset?
- Does the App need a "TFTP ready but not yet safe" wait step after ping/TTL?

## Stop Conditions

Stop and record an incident if:

- Local Network permission blocks transfer
- no ACK appears after repeated controlled entries
- ACK port behavior differs from expected
- timing tuning becomes arbitrary rather than evidence-driven
- upload completes but post-upload state remains unclear
- RT-AX86U behavior diverges from RT-AC86U in any material way

## Expected Outputs

- runtime attempt record for each serious test
- incident candidate for any mismatch or failure
- RT-AC86U profile refinement only after review
- separate RT-AX86U source/profile path if tested
