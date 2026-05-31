# TTL=100 Does Not Mean TFTP Is Ready

`TTL=100` is often treated as a shortcut for router recovery diagnosis. It can be a useful clue, but it is not proof that TFTP recovery is ready, correctly configured, or likely to succeed.

## What TTL Can Tell You

When a router replies to ping with `TTL=100`, it may indicate that the device is responding from an early bootloader or recovery-like state. On some routers, that timing window overlaps with firmware recovery behavior.

That is only a signal.

## What TTL Does Not Prove

`TTL=100` does not prove:

- the router is accepting TFTP traffic
- the router is a TFTP server
- the router is a TFTP client
- the expected IP address is correct
- the timing window is still open
- the firmware file is correct
- the firmware was accepted
- flash write succeeded
- recovery completed

Do not turn a ping observation into a recovery claim.

## Why TFTP Still Times Out

TFTP can time out even when ping replies appear.

Common reasons:

- wrong computer static IP
- wrong subnet
- wrong LAN port
- router is not in the right recovery mode
- recovery window closed before transfer started
- firewall blocks TFTP traffic
- TFTP direction is reversed
- required filename is missing or wrong
- firmware file is rejected after transfer

## Better Evidence

Stronger evidence includes:

- vendor recovery documentation
- packet capture showing RRQ or WRQ behavior
- TFTP logs showing the router IP and transfer direction
- successful transfer followed by observed flash/write/reboot behavior
- final boot into a usable admin or network state

For device-specific profiles, this project treats TTL as supporting context, not sufficient proof.

## Diagnostic Checklist

1. Confirm the expected recovery IP.
2. Confirm the computer static IP and subnet mask.
3. Confirm TFTP direction.
4. Start packet capture before power-on if possible.
5. Enter recovery mode using the model-specific sequence.
6. Start transfer inside the timing window.
7. Separate transfer success from completed recovery.

## Related Tool

Router Recovery for macOS can help preserve recovery attempt details, including IP choices, TFTP direction, and result boundaries. TTL interpretation still needs evidence from the actual device workflow.
