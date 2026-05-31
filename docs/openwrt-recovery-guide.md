# OpenWrt Recovery Guide

OpenWrt and ImmortalWrt recovery depends on the device, bootloader, firmware format, and vendor recovery path. There is no single universal OpenWrt recovery method.

For ImmortalWrt-specific firmware and recovery boundaries, see [ImmortalWrt Recovery Notes](immortalwrt-recovery-notes.md).

## First Decision: Recovery Path

Most devices fall into one of these paths:

- vendor web recovery page
- vendor TFTP recovery
- bootloader recovery through serial console
- OpenWrt failsafe mode
- normal vendor web UI flash back to stock

The right path depends on whether the router still boots, whether Ethernet works, and whether the bootloader still exposes recovery behavior.

## Firmware File Types

Common firmware types include:

- vendor stock firmware
- OpenWrt factory image
- OpenWrt sysupgrade image
- ImmortalWrt factory image
- ImmortalWrt sysupgrade image
- device-specific formats such as `.trx`, `.chk`, or `.bin`

Use a factory image when installing OpenWrt from stock firmware if the device guide requires it. Use a sysupgrade image for upgrading an already-running OpenWrt system. Do not assume the two are interchangeable.

## Safe Recovery Checklist

1. Identify the exact model and hardware revision.
2. Read the OpenWrt device page and vendor recovery instructions.
3. Confirm whether recovery needs stock firmware or an OpenWrt factory image.
4. Set a static IP only after confirming the expected recovery subnet.
5. Use Ethernet, not Wi-Fi.
6. Keep notes of each attempt, including IP addresses and error messages.
7. Treat success as confirmed only when the router boots and the admin interface or SSH becomes reachable.

## Failsafe Is Not the Same as Bootloader Recovery

OpenWrt failsafe mode is useful when OpenWrt still boots far enough to start a minimal system. It is not the same as vendor TFTP recovery or bootloader recovery.

If the device cannot boot OpenWrt at all, you may need a vendor recovery mode, serial console, or hardware-level procedure.

## Common OpenWrt Recovery Risks

- using sysupgrade image from stock firmware
- using a factory image on the wrong hardware revision
- flashing firmware for a different region
- losing track of whether the device is in failsafe, recovery mode, or normal setup mode
- assuming ping response means firmware recovery is ready

## Related Tool

Router Recovery for macOS can help with guided TFTP-oriented recovery attempts and local records. OpenWrt-specific flashing decisions still require checking the OpenWrt device page and vendor documentation.
