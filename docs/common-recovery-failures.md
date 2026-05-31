# Common Router Recovery Failures

Router recovery failures often look similar from the outside: the router pings, TFTP times out, upload finishes but nothing boots, or the web page returns after every reboot. The details matter.

## `TTL=100` Does Not Prove Recovery Is Ready

Many users treat `TTL=100` as proof that TFTP recovery will work. It is only a signal. It may indicate bootloader or recovery behavior, but it does not prove:

- correct firmware
- correct TFTP direction
- correct timing window
- successful flash write
- post-upload reboot behavior

Use `TTL=100` as a clue, not a success condition.

## TFTP Timeout

Likely causes:

- computer IP is on the wrong subnet
- firewall blocks TFTP
- router is not in recovery mode
- wrong LAN port
- TFTP direction is reversed
- recovery mode timing window was missed

What to check:

- static IP and subnet mask
- direct Ethernet connection
- packet capture or TFTP logs
- vendor-specific recovery button sequence
- whether your computer should be TFTP client or TFTP server

## Upload Completes But Router Does Not Recover

Likely causes:

- wrong firmware file
- firmware accepted for transfer but rejected for flashing
- flash write still in progress
- manual power cycle required after waiting
- recovery only restored setup mode, not previous configuration

Do not call this complete recovery until the router boots and becomes usable.

## Web Recovery Page Appears But Firmware Fails

Likely causes:

- wrong file type
- wrong hardware version
- browser cached a stale page
- router is in setup or factory-reset state, not firmware recovery
- region mismatch

For TP-Link-style web recovery, reaching a page is useful evidence of entry, but it does not prove firmware acceptance or completed recovery.

See [TP-Link Web Recovery Troubleshooting](tplink-web-recovery-troubleshooting.md) for TP-Link-specific page-entry and upload boundary examples.

## Wrong Subnet

Common examples:

- router expects `192.168.1.1`, computer should be `192.168.1.10`
- router expects `192.168.0.1`, computer should be `192.168.0.10`

Do not guess. Confirm from vendor documentation, OpenWrt device notes, or observed packets.

## Firewall and Local Network Permission

On macOS, local network permission and firewall state can affect recovery tools. If TFTP or web recovery fails unexpectedly, check whether the app or terminal process can bind to the required interface and receive local traffic.

## Recovery Checklist

- exact model and hardware version confirmed
- firmware source verified
- computer static IP set correctly
- Ethernet connected to correct port
- recovery mode entered with correct button sequence
- TFTP direction known
- transfer result separated from boot result
- final state recorded after enough wait time

## Related Tool

Router Recovery for macOS can help users keep recovery attempts organized, especially when IP settings, TFTP direction, and result boundaries are easy to confuse.
