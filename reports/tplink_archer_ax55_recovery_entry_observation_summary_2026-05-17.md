# TP-Link Archer AX55 Recovery Entry Observation Summary

Date: 2026-05-17
Prepared by: Codex
Status: observation summary, not profile promotion

## Scope

Device observed:

- Vendor: TP-Link
- Model: Archer AX55
- Physical label: Archer AX55(CA), Ver: 1.0
- Hardware version in UI: Archer AX55 v1.0
- Firmware during recovery-entry observation: 1.5.11 Build 20251119 rel.49503(4341)

Primary records:

- `lab_tests/live_sessions/tplink_archer_ax55_v1_official_baseline_2026-05-15.md`
- `runtime_attempts/tplink_archer_ax55_official_online_update_2026-05-16.json`
- `runtime_attempts/tplink_archer_ax55_recovery_entry_observation_2026-05-17.json`

## Decision

AX55 now has enough owner-lab evidence to record a model-specific recovery-entry observation for the tested unit.

Do not generate a recovery profile yet.

## Confirmed Observations

Official online update baseline:

- Official Web UI online update succeeded.
- Firmware changed from `1.3.1 Build 20240129 rel.57815(4341)` to `1.5.11 Build 20251119 rel.49503(4341)`.
- Admin IP stayed `192.168.0.1`.
- DHCP stayed enabled with range `192.168.0.2 - 192.168.0.253`.
- Lease time stayed 120 minutes.
- Configuration was retained per user confirmation.
- Upgrade progress reaching 100% did not mean the router was immediately usable.
- Admin login page returned about 3m35s after upgrade confirmation.
- Overnight check on 2026-05-17 showed admin UI, firmware page, and DHCP settings still normal.

Recovery-entry observation:

- WPS power-on attempt did not enter recovery; the router returned to normal admin UI.
- Reset power-on attempt succeeded.
- Successful entry sequence observed:
  - power unplugged at 0:04
  - Reset held and power connected at 0:14
  - middle orange LED lit at 0:20
  - Reset released after about 6 seconds of powered hold
  - ping responded at 0:29
  - `http://192.168.0.1` opened the recovery page
- Mac static IP `192.168.0.10/24` was used for the successful page access.
- Recovery page title/text observed: `Firmware Upgrade`, with local firmware file picker, disabled Upgrade button until file selection, 0% progress bar, and warnings not to power off and to choose the correct firmware.
- No firmware was uploaded during this observation.
- After observing the recovery page without upload, power-cycle return to normal admin UI took about 147 seconds.

## Source Relationship

TP-Link FAQ 1482 remains a series-level Archer AX source, not AX55-specific proof by itself.

The owner-lab observation now confirms that this physical AX55(CA) v1.0 unit can enter a browser-based recovery page using the Reset path described as an alternative in the FAQ.

Observed match:

- static PC IP: `192.168.0.10/24`
- recovery page IP: `192.168.0.1`
- direct browser-based firmware upload page
- orange middle LED as recovery signal

Observed model-specific detail:

- WPS path did not work in the tested attempt.
- Reset path worked.

## Not Confirmed

These must remain unknown:

- whether the page accepts the current official firmware file
- whether upload/write succeeds
- whether post-upload recovery preserves configuration
- whether post-upload requires manual power cycle
- whether TFTP is involved
- TFTP direction, if any
- TTL during recovery entry
- exact LAN-port sensitivity
- whether the behavior applies to other AX55 hardware or regions
- whether the behavior applies to all Archer AX models

## Product Guidance Implications

Safe guidance candidates for the tested unit:

- Use direct Ethernet and static client IP `192.168.0.10/24` before attempting the recovery page.
- Try `http://192.168.0.1` after the middle orange LED appears.
- For this observed AX55(CA) unit, Reset-on-power was the successful entry method.
- Do not treat WPS failure as proof that recovery is unavailable.
- Do not treat ping alone as success; the decisive signal is the recovery page.
- Do not power off during actual firmware upload/write.

Copy caution:

- "Progress 100%" and "ping reachable" should never be used alone as completion proof.
- A page appearing is only recovery-entry success, not firmware recovery success.

## Recommendation

Stop AX55 testing here for this session.

The next useful work is a separate, explicitly approved upload/acceptance test using an official firmware `.bin` that matches the device region and hardware version. That test should require:

- official firmware source rechecked
- exact file name and size recorded
- checksum status recorded if available
- configuration backup confirmed
- camera recording
- no third-party firmware
- explicit user confirmation before clicking Upgrade

Until then, AX55 should remain at `recovery-entry observed` status, not `recovery success`.

