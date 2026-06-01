# OpenWrt Failsafe vs TFTP Recovery

OpenWrt failsafe and TFTP recovery are often confused because both are used when a router is hard to access. They solve different problems.

Use OpenWrt failsafe when the router can still boot OpenWrt far enough to enter a minimal recovery environment. Use TFTP recovery when the normal firmware path is broken or when the vendor bootloader recovery workflow expects a firmware transfer.

## Quick Difference

| Question | OpenWrt failsafe | TFTP recovery |
| --- | --- | --- |
| Recovery layer | OpenWrt operating system | Bootloader or vendor recovery workflow |
| Main purpose | Fix or reset broken configuration | Reinstall or restore firmware |
| Typical cause | Bad network, firewall, password, package, or config change | Bad flash, invalid firmware, failed upgrade, vendor recovery |
| Firmware upload required | Usually no | Usually yes |
| Device-specific timing | Yes | Yes |
| Device-specific firmware file | Usually not for config reset | Yes |
| Success condition | Router boots OpenWrt normally after config fix or reset | Router accepts firmware, writes it, reboots, and becomes usable |

## Choose Failsafe When

OpenWrt failsafe is the better first attempt when:

- OpenWrt was installed and the device still appears to boot
- you changed LAN IP, DHCP, firewall, VLAN, bridge, or wireless settings
- you installed or removed packages and lost access
- the router is reachable only during early boot
- you want to reset configuration without reflashing firmware

Failsafe is not a universal unbrick method. It depends on OpenWrt reaching the stage where failsafe can be triggered.

## Choose TFTP Recovery When

TFTP recovery is more relevant when:

- the router does not boot OpenWrt far enough for failsafe
- a firmware upgrade failed before a usable system existed
- the vendor documents a TFTP recovery path
- the bootloader requests a firmware file from your computer
- the router exposes a TFTP server in recovery mode
- returning to vendor firmware or reinstalling firmware is required

TFTP recovery is not one workflow. The direction matters:

- Passive TFTP from router: the router runs a TFTP server and the computer uploads firmware.
- Active TFTP to router: the computer runs a TFTP server and the router requests a specific filename.

See [TFTP Recovery Guide](tftp-recovery-guide.md) for direction-specific notes.

## Common Wrong Turns

### Mistake: Treating Failsafe as Vendor Recovery

Failsafe is part of OpenWrt behavior. Vendor rescue modes are usually bootloader-level workflows. A router that cannot boot OpenWrt may never enter OpenWrt failsafe.

### Mistake: Treating TFTP Upload as Completed Recovery

A completed TFTP transfer only proves that the file moved across the network. It does not prove the router accepted the firmware, wrote flash successfully, rebooted, or became usable.

### Mistake: Assuming `TTL=100` Chooses the Method

`TTL=100` may be a useful signal, but it does not prove that failsafe is available or that TFTP is ready. Use it as evidence to investigate, not as a decision by itself.

See [TTL=100 Does Not Mean TFTP Is Ready](ttl-100-does-not-mean-tftp-ready.md).

### Mistake: Using the Wrong Firmware Image

OpenWrt sysupgrade images, factory images, vendor images, and bootloader recovery images may not be interchangeable. Always check model, hardware version, region, and recovery method before uploading firmware.

See [Firmware Selection Guide](firmware-selection-guide.md).

## Practical Decision Flow

1. Confirm the exact model, hardware version, and current firmware situation.
2. Ask whether OpenWrt still appears to boot.
3. If the likely issue is configuration, try OpenWrt failsafe first.
4. If OpenWrt does not boot far enough, look for the device-specific vendor or OpenWrt recovery method.
5. If TFTP is documented, identify the TFTP direction before transferring firmware.
6. Record upload result separately from final boot result.
7. Call recovery complete only after the router boots and becomes usable.

## What To Record

For either path, record:

- vendor, model, hardware version, and region
- firmware before the attempt
- method attempted: failsafe, TFTP client upload, TFTP server request, web recovery, or serial
- computer IP address and router IP address
- button timing and LED behavior
- transfer result, if any
- final boot result
- official source links or logs

These details make public recovery reports useful without overgeneralizing one device result.

## Source Notes

Start with upstream or vendor documentation before following forum summaries:

- OpenWrt failsafe, factory reset, and recovery mode: https://openwrt.org/docs/guide-user/troubleshooting/failsafe_and_factory_reset
- OpenWrt recovery methods index: https://openwrt.org/docs/guide-user/installation/recovery_methods/start

Device pages and vendor support pages may override general assumptions.
