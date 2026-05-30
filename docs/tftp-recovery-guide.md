# TFTP Recovery Guide

TFTP recovery is a common router firmware recovery method, but the word "TFTP" does not describe the full workflow. The most important question is direction: does the router wait for a TFTP client, or does the router fetch firmware from a TFTP server?

## Before You Start

Confirm these items first:

- exact router model
- hardware version and region
- correct firmware file for that model and hardware version
- recovery IP address
- computer static IP address
- Ethernet connection to the correct LAN port
- firewall and local network permissions
- whether the router runs a TFTP server or expects your computer to run one

Do not use a firmware file only because the filename looks similar. Router vendors often ship different firmware for hardware revisions, regions, and bootloader expectations.

## Two TFTP Recovery Directions

### Passive TFTP From Router

In this workflow, the router runs a TFTP server in recovery mode. Your computer acts as the TFTP client and uploads firmware to the router.

Typical signals:

- instructions tell you to connect to a router IP address
- the command uses `put firmware.bin`
- packet capture shows responses from router port `69`
- the router stays at a recovery IP such as `192.168.1.1`

### Active TFTP To Router

In this workflow, your computer runs a TFTP server. The router acts as a TFTP client and requests a specific filename.

Typical signals:

- instructions tell you to run a TFTP server on the computer
- the router looks for a specific filename
- the computer must use a specific static IP
- packet capture shows the router sending an RRQ request

## Basic Recovery Checklist

1. Disconnect other network paths that can confuse routing.
2. Connect the computer directly to the router with Ethernet.
3. Set the computer static IP according to the device guide.
4. Put the router into recovery mode using the vendor-specific button sequence.
5. Confirm the router responds at the expected IP.
6. Transfer the firmware using the correct TFTP direction.
7. Wait for the router to write firmware and reboot.
8. Confirm recovery only after the router boots and becomes usable.

## Upload Complete Is Not Recovery Complete

TFTP transfer completion means the file moved across the network. It does not prove the router accepted the firmware, wrote flash successfully, rebooted, or restored the admin interface.

After upload, some routers need several minutes. Some require a manual power cycle after the write process. Some reject firmware silently or return to recovery mode.

## Common Failure Patterns

- wrong static IP or subnet
- wrong firmware file
- hardware revision mismatch
- firewall blocks TFTP
- router is in normal setup mode, not recovery mode
- TFTP direction is reversed
- upload completes but firmware is not accepted
- ping `TTL=100` appears but TFTP still fails

See [Common Recovery Failures](common-recovery-failures.md) for troubleshooting details.

## Related Tool

The Router Recovery macOS app is a separate commercial tool for guided recovery workflows and local recovery attempt records. This guide remains usable without the app.
