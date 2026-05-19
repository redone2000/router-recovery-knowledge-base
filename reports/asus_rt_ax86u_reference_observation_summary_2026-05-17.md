# ASUS RT-AX86U Reference Observation Summary

Date: 2026-05-17
Prepared by: Codex
Status: observation summary, not profile promotion

## Scope

Device observed:

- Vendor: ASUS
- Model: RT-AX86U
- Hardware version: label `H/W Ver.: 1.0`
- Edition: red Gundam / Char's Zaku themed RT-AX86U
- Firmware family: ASUSWRT-Merlin, official/unmodified per owner
- Firmware before TFTP write test: `3004.388.11`
- Firmware after TFTP write test: `3004.388.10_2`

Primary records:

- `lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`
- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json` as comparison only

## Decision

RT-AX86U now has enough owner-lab evidence to record a model-specific Rescue Mode and Passive TFTP PUT recovery observation for the tested unit.

Do not generate a final profile yet.

Do not continue disruptive testing on this router unless a future product decision requires it. The device is normally the owner's primary router, and the useful uncertainty for this round has been resolved.

## Confirmed Observations

Official baseline:

- Normal admin UI was reachable at `192.168.50.1`.
- Device was running ASUSWRT-Merlin.
- Firmware before test was `3004.388.11`.
- Operation mode was wireless router.
- LAN IP was `192.168.50.1`.
- DHCP server was enabled.
- DHCP range was `192.168.50.2` - `192.168.50.254`.
- DHCP lease time was `86400` seconds.
- Configuration backup/export option existed.
- Owner exported and saved a Merlin configuration backup before write testing.
- Merlin download page used for firmware source: `https://www.asuswrt-merlin.net/download`.

Rescue Mode entry:

- Cable path: Mac wired Ethernet to RT-AX86U LAN1.
- Entry method: hold Reset while powering on.
- Recovery-like state was indicated by slow-flashing power LED and LAN1 activity.
- `192.168.1.1` replied with TTL=100.
- First observation saw TTL=100 for about 162 seconds before transition to TTL=64.
- Later passive capture observation saw TTL=100 persist for more than 5 minutes before user paused.
- Therefore the TTL=100 window duration should not be treated as a fixed timeout.

Web recovery:

- `http://192.168.1.1` did not open during TTL=100.
- No Web Recovery page was observed.

TFTP direction:

- Passive capture with no transfer showed no `tftp` packets and no `udp.port == 69` traffic.
- ARP showed bidirectional L2/L3 reachability between Mac `192.168.1.10` and router `192.168.1.1`.
- No router-initiated TFTP RRQ was observed.
- Active TFTP Server direction is not supported by this capture.

Passive TFTP PUT:

- POC App sent WRQ to `192.168.1.1:69` from Mac `192.168.1.10`.
- WRQ attempt #1 was accepted immediately.
- Router replied with ACK block 0 from `192.168.1.1:69`.
- ACK source port remained `69`; no ephemeral server port was observed.
- Firmware image filename used: `388102.w`.
- Firmware image size: 86,900,756 bytes.
- Transfer completed in about 39.956 seconds.
- Total block count: 169,729 512-byte blocks.
- Block number rollover was observed twice.

Post-upload behavior:

- Upload completion did not mean recovery completion.
- After upload completion and more than 5 minutes of waiting, the router showed only LAN1 white LED solid; other LEDs were off.
- Switching the Mac wired interface back to DHCP for about 1 minute did not restore DHCP.
- Mac received only a self-assigned `169.254.x.x` address before manual power cycle.
- After normal power cycle, DHCP returned on the normal LAN.
- Mac received `192.168.50.5` with router/DNS `192.168.50.1`.
- Admin UI reopened at `192.168.50.1`.
- Firmware version changed from `3004.388.11` to `3004.388.10_2`.
- Configuration appeared retained in this attempt.
- Follow-up checks showed admin UI, firmware page, DHCP page, Wi-Fi settings, WAN connectivity, and pre-existing JFFS ShellCrash installation remained usable.

Normal Web UI upgrade back to current firmware:

- After the TFTP downgrade, the owner upgraded normally from `3004.388.10_2` back to `3004.388.11` through the Web UI.
- Firmware file used: `RT-AX86U_3004_388.11_0_pureubi.w`.
- Upgrade took about 2-3 minutes.
- The Web UI progress felt slower than the TFTP transfer, and the UI's 3-minute estimate likely included router-side write time.
- Network interruption was short; after progress completed, the network appeared immediately usable.
- No additional power cycle was needed after the Web UI upgrade.
- Configuration remained normal after the Web UI upgrade.
- Wi-Fi, WAN, and existing JFFS ShellCrash installation remained usable.
- Separate follow-up observed `/tmp/ShellCrash/CrashCore.check` was no longer present after the router testing sequence. Treat this as likely `/tmp` runtime-state cleanup across reboot/upgrade/recovery transitions, not as evidence of persistent JFFS ShellCrash configuration loss.
- This is normal upgrade baseline evidence, not Rescue Mode or TFTP recovery evidence.

## Comparison With RT-AC86U

RT-AC86U is comparison evidence only, not RT-AX86U proof.

Observed similarity:

- Both RT-AC86U and this RT-AX86U attempt showed a post-upload state where only LAN1 white LED remained on and DHCP did not return before the next transition.
- Both require separating transfer completion from post-upload recovery completion.

Important boundary:

- Configuration retention is not controllable or guaranteed.
- Owner reports prior RT-AC86U repeated tests behaved inconsistently, with about 3-4 tests including at least one configuration-clear outcome.
- Therefore this RT-AX86U retained-configuration outcome is this-run evidence only, not an ASUS-family promise.

## Not Confirmed

These must remain unknown or unpromoted:

- Whether LAN1 is strictly required on RT-AX86U.
- Whether LAN2-LAN4 also work.
- Whether ASUS Firmware Restoration GUI behaves identically to the POC App.
- Whether official stock ASUSWRT behaves identically to ASUSWRT-Merlin.
- Whether other RT-AX86U hardware, region, or firmware variants behave identically.
- Whether configuration is retained across repeated RT-AX86U recovery attempts.
- Whether Web Recovery is absent in all states, or only absent in this observed state.
- Whether a different filename affects acceptance.
- Whether checksum-matched verification was performed locally for the uploaded `.w`.

## Product Guidance Implications

Safe guidance candidates for the tested unit:

- Use direct Ethernet to LAN1.
- Use Mac static IP `192.168.1.10/24`.
- Enter Rescue Mode by holding Reset during power-on.
- Treat slow-flashing power LED plus TTL=100 on `192.168.1.1` as a strong readiness signal.
- Use Passive TFTP PUT: Mac/App as TFTP client, router as TFTP server.
- Send WRQ/PUT to `192.168.1.1:69`.
- Follow ACKs from source port `69`.
- Do not expect Web Recovery from this observation.
- Do not wait indefinitely for DHCP after upload.
- After upload completes, wait several minutes, then a normal power cycle may be required before DHCP/admin UI return.
- After recovery, switch Mac back to DHCP and use the DHCP gateway as the admin URL.

Copy cautions:

- Do not say upload completion means firmware recovery is complete.
- Do not say ping/TTL alone proves TFTP readiness.
- Do not say configuration will be retained.
- Do not say all ASUS RT-AX86U variants behave the same.
- Do not say AC86U and AX86U share one profile.

## App / Tooling Follow-Up

The POC App succeeded but still labels the target as `R7000` in logs and UI text. That should be fixed before this flow is productized.

Useful App fields demonstrated by this attempt:

- selected local bind IP
- router recovery IP
- WRQ filename
- ACK block 0 source port
- server port behavior
- bytes sent
- block count
- block rollover count
- duration
- post-upload wait and DHCP return state

## Recommendation

Stop device testing here for this session.

Do not run more write tests, factory reset tests, or LAN-port matrix tests on this router now. The necessary reference-device questions for this round are answered:

- Rescue Mode entry observed.
- Web recovery not observed.
- Active TFTP RRQ not observed.
- Passive TFTP PUT verified.
- Firmware write verified by version downgrade.
- Post-upload manual power-cycle requirement observed.
- DHCP/admin return observed.
- Configuration retained in this run, with explicit non-guarantee warning.
- Normal Web UI upgrade back to `3004.388.11` observed after the recovery experiment.
- Device has returned to normal daily-use firmware and is suitable to resume primary-router use.

The next useful work is documentation and workflow refinement:

- create profile-candidate guardrails, not a final profile
- update App wording to separate upload completion from recovery completion
- fix POC App `R7000` wording before reuse
- consider a future low-risk recheck only if this router is already in a maintenance window
