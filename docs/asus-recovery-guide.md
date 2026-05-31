# ASUS Recovery Guide

ASUS routers often expose Rescue Mode or Firmware Restoration behavior, but exact recovery details vary by model, hardware revision, firmware family, and observed device state.

## Common ASUS Recovery Signals

Possible signals include:

- slow flashing power LED
- ping response from a recovery IP such as `192.168.1.1`
- vendor Firmware Restoration utility guidance
- TFTP transfer behavior
- web recovery behavior on some models

These signals are not universal. A signal should be tied to a specific model and observation.

For source boundaries and public evidence links, see [ASUS Firmware Restoration Evidence Links](asus-firmware-restoration-evidence-links.md).

## TFTP Direction Must Be Proven

Some ASUS recovery attempts behave as passive TFTP: the router acts as a TFTP server, and the computer uploads firmware as a client.

Do not assume this for every ASUS model. Confirm with official documentation, tool behavior, or packet evidence.

## Firmware Family Matters

Before attempting recovery, identify whether the router is running or targeting:

- stock ASUSWRT
- ASUSWRT-Merlin
- vendor restoration firmware
- another third-party build

Firmware family changes can affect filenames, compatibility, and expected post-upload behavior.

## Recovery Is Not Complete At Upload

For ASUS-style rescue workflows, transfer completion is only one stage. The router may need time to write flash and may not return DHCP or admin UI immediately.

Record:

- whether TFTP transfer completed
- how long you waited
- whether DHCP returned
- whether the admin UI returned
- whether a manual power cycle was needed
- firmware version before and after

## Current Evidence Boundary

This project keeps ASUS device observations conservative. For example, one model or firmware-family result should not be generalized to all ASUS routers, and configuration retention should not be promised from a single attempt.

## Related Tool

Router Recovery for macOS can guide supported ASUS-oriented TFTP recovery workflows and preserve local attempt details. This public guide remains the source for evidence boundaries and manual understanding.
