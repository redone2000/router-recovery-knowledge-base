# App Copy: Upload Complete vs Recovery Complete

Date: 2026-05-17
Prepared by: Codex
Status: App copy / workflow guidance draft

## Decision

The App must separate these states:

1. firmware transfer/upload completed
2. router is writing or transitioning
3. user wait period completed
4. manual power action, if required
5. DHCP returned
6. admin UI opened
7. firmware version verified
8. configuration state checked

Do not label a recovery attempt successful at step 1.

## Why

ASUS RT-AX86U lab evidence showed:

- Passive TFTP PUT completed successfully in about 40 seconds.
- After upload completion and more than 5 minutes of waiting, DHCP had not returned.
- Router front state was only LAN1 white LED solid with other LEDs off.
- A normal power cycle was needed before DHCP/admin UI returned.
- Firmware write success was only confirmed after admin UI showed the downgraded version.

ASUS RT-AC86U comparison evidence also showed upload completion and post-upload recovery are separate.

## Runtime State Labels

Recommended internal state names:

- `transfer_ready`
- `transfer_in_progress`
- `transfer_complete`
- `post_upload_wait`
- `awaiting_power_cycle`
- `return_to_dhcp`
- `admin_ui_check`
- `version_verified`
- `configuration_check`
- `recovery_success`
- `incident_candidate`

## User-Facing Copy

### Transfer Complete

Use:

```text
Firmware upload finished. The router may still be writing firmware.
Do not unplug power yet.
```

Avoid:

```text
Recovery complete.
```

### Post-Upload Wait

Use:

```text
Wait several minutes before the next step. During this phase, the router may not provide DHCP or open its admin page.
```

Avoid:

```text
If the page does not open now, the recovery failed.
```

### Manual Power Cycle

Use when profile/runtime evidence supports it:

```text
Now power the router off, wait 10 seconds, then power it on normally. Do not hold Reset.
```

Avoid:

```text
Power cycle immediately after upload.
```

### Return To DHCP

Use:

```text
Set the Mac Ethernet adapter back to DHCP. Wait for a router/gateway address, then open the gateway in your browser.
```

### Version Verification

Use:

```text
Open the router admin page and confirm the firmware version. This is the evidence that the write completed.
```

### Configuration State

Use:

```text
Check Wi-Fi, LAN/DHCP, WAN, and any add-ons you rely on. Configuration may be retained, reset, or changed depending on the device and attempt.
```

Avoid:

```text
Your settings will be preserved.
```

## Profile Copy Warnings

For ASUS RT-AX86U candidate guidance:

- "Observed on one RT-AX86U unit with ASUSWRT-Merlin."
- "Use official, model-matched firmware."
- "Use the extracted `.w` firmware image, not the `.zip` archive."
- "TTL=100 and slow-flashing power LED are readiness signals, not recovery success."
- "TFTP upload completion is only the transfer phase."
- "Manual power cycle may be required after waiting."
- "Configuration retention is not guaranteed."

## Product Follow-Up

The POC App should stop using `R7000` wording in generic TFTP flows.

The UI should derive labels from the selected device/profile or use neutral wording such as:

- "Target router"
- "Recovery window"
- "TFTP server"
- "Selected device"

Do not hardcode a model name in shared recovery workflow text.
