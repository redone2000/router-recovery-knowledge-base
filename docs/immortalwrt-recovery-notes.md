# ImmortalWrt Recovery Notes

ImmortalWrt recovery is closely related to OpenWrt recovery, but it should not be treated as a universal substitute for OpenWrt, stock firmware, or vendor recovery instructions.

The safest approach is to start from the exact device and firmware family, then decide whether the right path is ImmortalWrt sysupgrade, ImmortalWrt factory image, OpenWrt guidance, vendor web recovery, vendor TFTP recovery, failsafe, or serial console recovery.

## Relationship To OpenWrt

Many ImmortalWrt concepts are inherited from or aligned with the OpenWrt ecosystem:

- device targets and subtargets matter
- factory and sysupgrade image types matter
- failsafe is useful only when the installed system boots far enough
- vendor recovery remains device-specific
- hardware revision and flash layout can change what is safe

This overlap does not mean every OpenWrt image can be replaced by an ImmortalWrt image, or the reverse.

## First Identify The Current State

Before choosing a recovery path, determine which state the device is in:

- stock vendor firmware still boots
- ImmortalWrt boots but configuration is broken
- OpenWrt boots but configuration is broken
- firmware does not boot, but vendor recovery mode appears
- bootloader TFTP or web recovery appears
- only serial console access is available
- hardware fault or power issue is suspected

The recovery method follows from the state. Do not start with a firmware file and work backward.

## Firmware Image Boundaries

Common image categories:

- ImmortalWrt factory image
- ImmortalWrt sysupgrade image
- OpenWrt factory image
- OpenWrt sysupgrade image
- vendor stock firmware
- vendor recovery-specific file

General rule:

- Use factory images only when the device guide says they are appropriate for installing from stock or a compatible recovery path.
- Use sysupgrade images only when upgrading an already-running compatible OpenWrt-like system.
- Use vendor stock firmware when the vendor recovery path requires vendor firmware.

Do not assume a vendor recovery page accepts an ImmortalWrt image. Some vendor recovery modes validate headers, model IDs, region IDs, or file formats.

## Failsafe Boundary

ImmortalWrt failsafe is useful when the installed system still boots far enough to expose a minimal recovery environment.

Failsafe may help with:

- bad network configuration
- firewall lockout
- package or service changes that broke access
- configuration reset

Failsafe usually does not help when:

- the firmware image cannot boot
- bootloader recovery is required
- the wrong image was flashed and the system never starts
- Ethernet never comes up
- the device needs serial console or vendor recovery

See [OpenWrt Failsafe Guide](openwrt-failsafe-guide.md) for the shared concept boundary.

## Vendor Recovery Still Matters

Many devices that run ImmortalWrt still depend on vendor-specific recovery behavior:

- TP-Link web recovery
- ASUS Rescue Mode
- NETGEAR TFTP or NMRP-related workflows
- device-specific TFTP filename requirements
- vendor stock firmware validation

ImmortalWrt support for a device does not prove that the vendor recovery path accepts an ImmortalWrt image.

## What To Record

For an ImmortalWrt recovery report, record:

- exact vendor and model
- hardware version and region
- current firmware family
- target firmware family
- target/subtarget if known
- image type: factory, sysupgrade, or vendor stock
- image source URL
- filename and file size
- checksum if available
- recovery method used
- router IP and computer IP
- upload or sysupgrade result
- final boot and management state

These details are more useful than a broad claim like "ImmortalWrt recovery worked."

## Common Mistakes

- using sysupgrade from stock firmware
- using factory image from an already-running system without checking the device guide
- mixing OpenWrt and ImmortalWrt images without confirming compatibility
- treating vendor recovery as if it accepts every `.bin`
- assuming failsafe is available when firmware does not boot
- ignoring hardware revision or region
- calling upload success a completed recovery

## Evidence Boundary

This project can document ImmortalWrt recovery concepts before it has model-specific ImmortalWrt recovery profiles. Concept guidance is not the same as device guidance.

For model-specific claims, evidence should identify the exact device, firmware family, image type, recovery method, and final usable state.

## Related Tool

Router Recovery for macOS can help preserve recovery attempt details, especially around IP settings, firmware files, and result boundaries. ImmortalWrt image choice still requires checking the relevant upstream device documentation.
