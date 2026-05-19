# Main App Handoff: TP-Link Archer AX55 Web Recovery Entry

Date: 2026-05-19
Prepared by: Codex
Repository: `redone2000/router-recovery-knowledge`
Branch target: `main`
Status: ready for main-app integration planning

## Purpose

This handoff packages the TP-Link Archer AX55 work from the local reference-device session so another integration session can apply it to the main application without needing this physical device.

This is not a final compatibility profile. It is a tested recovery-entry baseline for one physical unit.

## Remote Files To Use

Use these repository files as the source of truth:

- `lab_tests/live_sessions/tplink_archer_ax55_v1_official_baseline_2026-05-15.md`
- `runtime_attempts/tplink_archer_ax55_official_online_update_2026-05-16.json`
- `runtime_attempts/tplink_archer_ax55_recovery_entry_observation_2026-05-17.json`
- `reports/tplink_archer_ax55_recovery_entry_observation_summary_2026-05-17.md`
- `handoffs/main_app_ax55_web_recovery_entry_handoff_2026-05-19.md`
- `prompts/main_app_ax55_web_recovery_entry_integration_prompt_2026-05-19.md`

Expected remote URL pattern after push:

```text
https://github.com/redone2000/router-recovery-knowledge/blob/main/<path>
```

## Device Scope

Observed device:

- Vendor: TP-Link
- Model: Archer AX55
- Physical label: Archer AX55(CA), Ver: 1.0
- UI hardware version: Archer AX55 v1.0
- Firmware after official update: `1.5.11 Build 20251119 rel.49503(4341)`
- Normal admin IP: `192.168.0.1`
- Normal DHCP range: `192.168.0.2 - 192.168.0.253`

Scope boundary:

- Treat this as tested-unit evidence for AX55(CA) v1.0.
- Do not generalize to all AX55 hardware/regions.
- Do not generalize to all Archer AX models.
- Do not claim full firmware recovery success.

## Confirmed For App Integration

Official update baseline:

- Official Web UI online update succeeded.
- Firmware changed from `1.3.1 Build 20240129 rel.57815(4341)` to `1.5.11 Build 20251119 rel.49503(4341)`.
- Configuration was retained.
- DHCP range and admin IP were retained.
- Upgrade progress reached 100% before the router was usable.
- Admin login page returned about 3m35s after upgrade confirmation.
- Overnight admin/DHCP/firmware check remained normal.

Recovery entry baseline:

- Mac Ethernet static IP `192.168.0.10/24` worked for recovery-page access.
- Recovery page IP: `http://192.168.0.1`
- Successful entry method:
  - power unplugged
  - hold Reset
  - connect power while holding Reset
  - middle orange LED appeared after about 6 seconds of powered hold
  - release Reset
  - ping responded around 29 seconds
  - browser opened `Firmware Upgrade` recovery page
- WPS power-on attempt did not enter recovery in the tested attempt.
- Recovery page showed:
  - title/text: `Firmware Upgrade`
  - local firmware file picker
  - disabled Upgrade button until file selection
  - 0% progress bar
  - warning not to power off
  - warning to choose the correct firmware
- No firmware was uploaded.
- After observing the page without upload, unplug/replug returned to normal admin UI in about 147 seconds.

## Do Not Integrate As Claims

Do not add claims that:

- firmware upload was accepted
- firmware write succeeded through the recovery page
- configuration is retained after recovery-page upload
- post-upload reboot behavior is known for AX55 recovery
- TFTP is involved
- TFTP direction is known
- TTL behavior is known
- LAN-port sensitivity is known
- WPS never works
- AX55 is fully supported

## Recommended App Behavior

Add AX55 as an observation-backed Web Recovery entry flow only, if the app has a concept of staged support or lab-observed guidance.

Recommended states:

- `prepare_static_ip`
- `enter_recovery_mode`
- `probe_recovery_page`
- `recovery_page_observed`
- `stop_before_upload`
- `unsupported_until_upload_tested`

Recommended UX copy:

```text
This AX55 flow has been observed only up to the recovery upload page. Do not treat page access as a completed recovery.
```

```text
Set Ethernet to 192.168.0.10/24, connect directly to the router, then enter recovery mode before opening http://192.168.0.1.
```

```text
For the observed AX55(CA) v1.0 unit, holding Reset while powering on reached the recovery page. WPS did not work in the tested attempt.
```

```text
If the Firmware Upgrade page appears, stop here unless you intentionally want to run a separate official-firmware upload test.
```

Progress/wait copy:

```text
100% progress is not proof that the router is usable. Keep waiting until the admin page or network returns.
```

## Integration Shape

If the main app supports per-device metadata, suggested values:

```json
{
  "vendor": "TP-Link",
  "model": "Archer AX55",
  "hardware_scope": "observed: CA label, v1.0",
  "firmware_scope": "observed: 1.5.11 Build 20251119 rel.49503(4341)",
  "support_level": "recovery_entry_observed",
  "recovery_type": "web_recovery",
  "client_static_ip": "192.168.0.10",
  "client_cidr": "192.168.0.10/24",
  "recovery_url": "http://192.168.0.1",
  "entry_button": "Reset",
  "entry_hold_seconds_observed": 6,
  "entry_led_observed": "middle orange LED",
  "recovery_page_title": "Firmware Upgrade",
  "upload_tested": false,
  "tftp_tested": false,
  "profile_generation_allowed": false
}
```

## Suggested Integration Tasks

1. Add an AX55 staged device entry only if the app can label it as `recovery_entry_observed`.
2. Add a TP-Link Web Recovery preparation screen using static IP `192.168.0.10/24` and target `http://192.168.0.1`.
3. Add explicit copy that reaching the upload page is not recovery success.
4. Add a stop gate before any firmware upload.
5. Ensure the app does not route this flow into TFTP by default.
6. Keep generic Archer AX FAQ evidence separate from AX55 tested-unit facts.
7. Add a future task for official `.bin` upload/acceptance testing only after explicit user confirmation.

## Validation Commands Used

```text
python3 tools/validate_runtime_attempts.py runtime_attempts
python3 tools/validate_system_links.py
```

Both passed before handoff creation.

