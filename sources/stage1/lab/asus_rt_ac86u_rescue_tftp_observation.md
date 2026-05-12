# ASUS RT-AC86U Rescue Mode TFTP Observation

Date: 2026-05-12
Source type: personal_testing
Device: ASUS RT-AC86U

## Scope

This is first-party lab observation supplied by the Owner for incoming profile drafting and schema evolution. It is not final data and must not be promoted to `reviewed/` or `final/` without human review.

## Observed Recovery Entry

- Ethernet cable connected to LAN1, the LAN port nearest the WAN port.
- Power off router.
- Hold reset button.
- Connect power while continuing to hold reset.
- Rescue Mode observed after about 10-20 seconds.
- Slow flashing power LED indicates Rescue Mode.
- In some phases the power LED may be off while LAN LED remains on.

## Observed Network State

- Rescue IP: `192.168.1.1`
- Mac static IP: `192.168.1.10/24`
- Observed rescue TTL: `100`
- Ping may respond but can be unstable across states; ping must not be the only success/failure signal.

## Observed TFTP Behavior

- macOS native `tftp` succeeded with WRQ upload in octet mode.
- Swift TFTP WRQ proof of concept succeeded.
- Sandboxed macOS app succeeded when App Sandbox, network client/server entitlements, file-picker access, and Local Network permission were available.
- Before Local Network permission was allowed, `sendto()` could fail with `No route to host`.
- Filename was not fixed in this test; `test.w` was accepted.
- No TFTP ERROR packet was observed.
- ACK sequence was standard.
- Server did not switch to an ephemeral transfer port in the observed RT-AC86U Rescue Mode runs; ACK packets came from `192.168.1.1:69` throughout.
- Client should follow the server ACK source port. If the server continues ACKing from port 69, continue sending to port 69.

## Observed Successful Transfers

Sample 1:

- Firmware file: `test.w`
- Size: `78,250,004 bytes`
- Transfer time: about `36 seconds`
- Blocks: `152,833`
- Block rollover: `2`
- Router entered subsequent flashing/recovery phase after upload.

Sample 2:

- Firmware before upload: `52334`
- Uploaded firmware: `52294`
- Final Web UI firmware: `52294`
- LAN before upload: `192.168.50.1`
- LAN after upload: `192.168.50.1`
- SSID, admin password, and DHCP settings were retained.
- Observed conclusion: Rescue/TFTP can perform downgrade or overwrite flashing and does not necessarily clear configuration.

Sample 3:

- LAN after upload returned to `192.168.50.1`
- Behavior appeared factory-reset-like or configuration was lost.
- Observed conclusion: TFTP success does not guarantee configuration retention or factory reset. Both outcomes were observed.

## Observed Post-Upload Requirement

- Do not treat upload completion as immediate recovery success.
- Wait about `3 minutes`.
- Manual power cycle was required in all local RT-AC86U test runs observed so far.
- After power cycle, switch the Mac wired network back to DHCP.
- Use the DHCP gateway IP as the Web UI/admin URL.

## User-Facing Warning

- Upload completion does not mean the router is immediately reachable.
- The router may retain configuration or may return to a factory-default-like state.
- If the old IP does not open, switch the Mac to DHCP and use the acquired gateway IP.
- In these RT-AC86U observations, wait about 3 minutes after upload, then unplug and reconnect power.
- Do not judge failure only by ping or the previous LAN IP.
