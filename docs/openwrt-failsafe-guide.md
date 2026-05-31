# OpenWrt Failsafe Guide

OpenWrt failsafe mode is a recovery path for routers that can still boot far enough to start OpenWrt's minimal recovery environment. It is not the same as vendor bootloader recovery, TFTP recovery, or serial console recovery.

Use failsafe when OpenWrt is installed and the router still reaches the early boot stage, but normal network access, firewall rules, configuration, or package changes prevent regular use.

## When Failsafe Is Relevant

Failsafe may help when:

- the router still powers on and boots OpenWrt
- configuration changes broke network access
- firewall rules locked you out
- DHCP or static IP settings were misconfigured
- a package or service change broke normal management access
- you need to reset configuration without reflashing firmware

Failsafe usually does not help when:

- the bootloader cannot start firmware
- the firmware image is invalid for the device
- flash write failed before a bootable system existed
- Ethernet never becomes usable
- the device needs vendor TFTP or web recovery
- hardware is damaged

## Failsafe vs Bootloader Recovery

OpenWrt failsafe is an operating-system-level recovery environment. Vendor recovery modes are usually bootloader-level workflows.

Keep these separate:

- OpenWrt failsafe: recover or reset a broken OpenWrt configuration.
- Vendor TFTP recovery: send firmware through a bootloader recovery path.
- Vendor web recovery: upload firmware through a recovery web page.
- Serial console recovery: interact with the bootloader or early system console.

Using the wrong mental model can waste time. If the router is not booting OpenWrt at all, failsafe may never appear.

## General Failsafe Workflow

Exact button timing and network behavior are device-specific. Check the OpenWrt device page before acting.

Typical flow:

1. Connect the computer directly to the router with Ethernet.
2. Start the router and watch for the failsafe trigger window.
3. Press the required button according to the device page.
4. Assign the computer an IP in the expected subnet if needed.
5. Connect using the documented failsafe method.
6. Decide whether to inspect configuration, reset configuration, or reboot.
7. Confirm normal boot and network access after changes.

## What To Record

For useful troubleshooting, record:

- model and hardware version
- OpenWrt or ImmortalWrt version
- button sequence used
- LED behavior
- computer IP address
- router IP address
- whether failsafe prompt or access appeared
- commands used
- final result after reboot

## Common Mistakes

- assuming failsafe exists on every device
- confusing vendor recovery mode with OpenWrt failsafe
- using a sysupgrade image when a vendor recovery workflow expects another format
- treating ping response as proof that failsafe is available
- resetting configuration before preserving useful evidence

## Related Tool

Router Recovery for macOS focuses on guided recovery attempt records and TFTP-oriented workflows. OpenWrt failsafe decisions still require checking the upstream OpenWrt device documentation.
