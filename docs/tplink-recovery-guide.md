# TP-Link Recovery Guide

TP-Link routers may expose web recovery, TFTP recovery, normal setup pages, or ordinary firmware upgrade pages depending on the model and state. Reaching a page at a recovery IP is useful evidence, but it is not the same as completed firmware recovery.

## Common TP-Link Recovery Paths

Possible paths include:

- web recovery page at a fixed local IP
- TFTP recovery for specific models
- normal web UI firmware upgrade
- factory-reset setup flow

Treat each path separately. A page asking you to create an administrator password is usually setup or factory-reset behavior, not proof of firmware recovery mode.

For common page-entry and upload boundary problems, see [TP-Link Web Recovery Troubleshooting](tplink-web-recovery-troubleshooting.md).

## Web Recovery Checklist

1. Confirm exact model, hardware version, and region.
2. Download firmware from the matching official support page.
3. Connect by Ethernet.
4. Set the computer static IP for the expected recovery subnet.
5. Enter recovery mode using the model-specific button sequence.
6. Open the expected recovery IP in a browser.
7. Upload only the correct firmware file.
8. Wait for write and reboot behavior.
9. Confirm completion only after the router boots and becomes usable.

## TFTP Recovery Checklist

If the model uses TFTP, confirm:

- computer static IP
- router recovery IP
- required filename, if any
- whether the router is TFTP client or TFTP server
- whether the firmware file needs to be renamed

Do not assume TP-Link recovery direction from brand alone.

## Firmware Selection Risks

TP-Link hardware revisions matter. A firmware image for one region or hardware revision may be rejected or unsafe for another.

Check:

- label on the router
- model string in the web UI, if available
- official support page
- file name and release notes
- OpenWrt device page, if recovering an OpenWrt installation

## Evidence Boundary

This project separates:

- recovery page entry
- firmware upload
- firmware acceptance
- completed reboot
- usable admin or network state

Do not report a recovery as complete until the final usable state is confirmed.

## Related Tool

Router Recovery for macOS can help keep recovery attempts organized, especially when users need to preserve IP settings, firmware choice, and result boundaries.
