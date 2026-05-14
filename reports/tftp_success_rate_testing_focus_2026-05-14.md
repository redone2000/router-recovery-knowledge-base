# TFTP Success-Rate Testing Focus

Date: 2026-05-14
Scope: reference-device lab preparation

## Decision

The upcoming reference-device tests should focus on full TFTP active/passive scenarios and the small operational details that improve recovery success rate.

The purpose is not just to confirm whether a router can be recovered. The purpose is to discover and structure details that make the App more likely to guide ordinary users through recovery successfully.

## Key Details To Capture

- TFTP direction: router-as-server versus router-as-client
- Mac/App role: TFTP client versus TFTP server
- first WRQ/RRQ timing relative to power-on, LED state, and ping/TTL
- whether ping/TTL appears before TFTP is ready
- ACK source port behavior
- ephemeral port switching or fixed port 69 behavior
- required filename and whether renaming is needed
- whether retrying helps or hurts
- LAN port reliability
- Wi-Fi/multiple-interface interference
- macOS Local Network permission failure mode
- post-upload wait, reboot, and power-cycle behavior

## App Impact

These observations should feed:

- preflight order
- transfer screen state machine
- retry strategy
- error category mapping
- post-upload guidance
- incident capture defaults

They should not become broad model profile claims until reviewed.

## Updated Files

- `docs/reference_device_lab_test_protocol.md`
- `lab_tests/reference_devices/tplink_archer_ax55_lab_prep.md`
- `lab_tests/reference_devices/asus_rt_ax86u_rt_ac86u_lab_prep.md`
- `lab_tests/reference_devices/netgear_rax40_lab_prep.md`
- `lab_tests/runtime_attempt_quick_note_template.md`
