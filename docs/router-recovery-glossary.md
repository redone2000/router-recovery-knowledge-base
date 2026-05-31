# Router Recovery Glossary

This glossary defines common router recovery terms used across this knowledge base. The goal is to reduce ambiguity, especially around TFTP direction, firmware file choice, and what counts as completed recovery.

## Active TFTP

A recovery workflow where the router acts as a TFTP client and connects to a TFTP server running on the computer.

Typical evidence:

- vendor instructions tell the user to run a TFTP server
- router requests a specific filename from the computer
- packet capture shows an RRQ request from the router

Do not infer active TFTP from the brand alone.

## Bootloader

Early software that starts before the router's main firmware. Some recovery workflows happen in the bootloader before OpenWrt, stock firmware, or another operating system starts.

Bootloader behavior is device-specific. A bootloader recovery method for one model should not be generalized to another model without evidence.

## Bootloader Recovery

A recovery path exposed before the main firmware boots. Examples may include TFTP recovery, web recovery, serial console recovery, or vendor-specific tools.

Bootloader recovery is not the same as OpenWrt failsafe.

## Completed Recovery

A recovery attempt is complete only when the router has booted into a usable state after the firmware transfer or recovery action.

Useful completion signals:

- admin UI is reachable
- SSH or expected management interface works
- DHCP returns if expected
- firmware version can be confirmed
- network routing or local access behaves normally

Upload completion alone is not completed recovery.

## Device Profile

A structured record for one device or device variant. In this project, a profile should identify the vendor, model, hardware version, firmware context, recovery methods, evidence, and confidence boundaries.

Profiles should not be created from AI-generated guesses alone.

## Evidence Boundary

The line between what has been proven and what remains unknown.

Examples:

- Observing a recovery page proves entry, not firmware acceptance.
- Observing TFTP upload proves transfer, not completed recovery.
- Seeing `TTL=100` is a clue, not proof that TFTP is ready.

## Factory Image

An OpenWrt or ImmortalWrt image usually intended for installation from stock vendor firmware. The exact usage depends on the device page and vendor workflow.

Do not use a factory image only because it sounds like a reset image.

## Firmware Acceptance

The point where the router accepts a firmware file as valid for flashing. This may happen after upload, during validation, or after a write stage, depending on the device.

A web page or TFTP transfer can appear successful even when the firmware is later rejected.

## Firmware Selection

The process of choosing the correct firmware file for the exact model, hardware version, region, and recovery method.

Firmware selection mistakes are high risk. Similar model names are not enough.

## Hardware Version

A vendor-specific revision of a router model. Hardware version can affect firmware compatibility, recovery IP, button sequence, file format, and recovery behavior.

Always record hardware version when visible.

## ImmortalWrt

A router firmware distribution related to the OpenWrt ecosystem. Many recovery concepts overlap with OpenWrt, but device-specific documentation and firmware image type still matter.

Do not assume OpenWrt and ImmortalWrt files are interchangeable for every device.

## NMRP

A NETGEAR-related recovery protocol used by some community tools and workflows. This project treats NMRP guidance carefully because community recovery workflows and official vendor instructions may differ.

Do not present NMRP as an official method for a specific NETGEAR device unless the evidence supports that claim.

## OpenWrt Failsafe

An OpenWrt recovery mode for fixing broken OpenWrt configuration when the system still boots far enough to enter failsafe.

Failsafe is not vendor bootloader recovery and does not replace TFTP or web recovery when firmware cannot boot.

## Passive TFTP

A recovery workflow where the router runs a TFTP server and the computer acts as a TFTP client.

Typical evidence:

- instructions tell the user to connect to the router IP
- command uses `put firmware.bin`
- packet capture shows responses from router port `69`

Do not infer passive TFTP from the brand alone.

## Recovery IP

The IP address used by the router during recovery. It may differ from the normal LAN IP.

Common examples include `192.168.1.1` and `192.168.0.1`, but these are not universal.

## Recovery Method

A distinct path used to restore or repair a device.

Examples:

- OpenWrt failsafe
- web recovery
- passive TFTP
- active TFTP
- serial console recovery
- normal web UI firmware update

Different methods have different evidence requirements.

## Recovery Mode

A device state intended for repair or firmware recovery. The term is broad and vendor-specific.

Do not assume that every page, ping response, or LED pattern is recovery mode without supporting evidence.

## Region

A vendor or market-specific firmware variant. Region can affect firmware compatibility and update acceptance.

When the device label, web UI, and download page disagree, resolve the mismatch before flashing.

## Serial Console Recovery

A recovery path that uses a physical serial connection to inspect or control bootloader or early system behavior.

Serial work can be powerful but higher risk. It may require opening the device and should not be treated as a beginner default.

## Sysupgrade Image

An OpenWrt or ImmortalWrt image usually intended for upgrading an already-running OpenWrt-like system.

Do not assume a sysupgrade image is accepted by stock vendor firmware or vendor recovery pages.

## TFTP Client

The side that initiates a TFTP transfer request.

In active TFTP recovery, the router is often the client. In passive TFTP recovery, the computer is often the client.

## TFTP Direction

The direction of TFTP responsibility: which side is the client and which side is the server.

This is one of the most important recovery facts to verify. Ambiguous "TFTP recovery" instructions are not enough to prove direction.

## TFTP Server

The side that waits for TFTP requests.

In active TFTP recovery, the computer may be the server. In passive TFTP recovery, the router may be the server.

## TTL=100

A ping response value that may suggest early bootloader or recovery-like behavior on some routers.

TTL=100 is only a clue. It does not prove TFTP readiness, firmware acceptance, or completed recovery.

## Upload Complete

The network transfer finished. This can happen through TFTP or a web recovery page.

Upload complete does not prove firmware acceptance, flash write success, reboot success, or completed recovery.

## Web Recovery

A recovery method where the router exposes a local web page for firmware upload or repair.

Reaching a web page proves page entry, not necessarily firmware acceptance or completed recovery.

## Related Tool

Router Recovery for macOS can help preserve recovery attempt details. This glossary remains public documentation and does not require using the app.
