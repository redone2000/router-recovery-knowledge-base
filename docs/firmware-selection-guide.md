# Firmware Selection Guide

Firmware selection is one of the highest-risk parts of router recovery. A recovery method can be correct while the firmware file is wrong.

## Identify the Device Exactly

Before downloading firmware, confirm:

- vendor
- model
- hardware version
- region
- current firmware family
- target firmware family

Examples of values that matter:

- `Archer AX55 v1` is not necessarily the same as another AX55 hardware revision.
- stock ASUSWRT and ASUSWRT-Merlin may use related but distinct release paths.
- NETGEAR `.chk` files may be model-specific.

## Factory vs Sysupgrade

For OpenWrt and ImmortalWrt:

- `factory` images are usually for installing from stock firmware.
- `sysupgrade` images are usually for upgrading an already-running OpenWrt or ImmortalWrt system.

Using the wrong type can fail or cause a harder recovery problem.

Do not assume OpenWrt and ImmortalWrt images are interchangeable. Match the firmware family, device target, hardware revision, and upstream device page before flashing.

## Region and Hardware Version

Some vendors publish separate firmware for regions or hardware versions. If the label, web UI, and download page disagree, stop and resolve the mismatch before flashing.

Useful checks:

- device bottom label
- current web UI model string
- vendor support page
- OpenWrt device page
- firmware filename and release notes

## Recovery Firmware May Differ From Normal Upgrade Firmware

Some recovery modes require a renamed file, a stripped header, or a vendor-specific format. Do not assume that a normal web UI update file is accepted by bootloader recovery.

## Red Flags

- model name is close but not exact
- hardware version is unknown
- firmware source is a mirror with no vendor or upstream reference
- file was recommended without region or revision details
- recovery page accepts upload but router never boots

## Minimum Record To Keep

For each attempt, record:

- downloaded firmware URL
- filename
- file size
- checksum if available
- model and hardware version
- recovery method
- result after waiting and rebooting

These details make future troubleshooting much easier.
