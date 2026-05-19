# ASUS RT-AX86U Official Baseline Live Session

Date: 2026-05-17
Status: closed live note
Device role: ASUS RT-AX86U official baseline / Rescue Mode reference device candidate
Primary goal: capture official normal-state baseline and firmware-source evidence before any Rescue Mode or firmware-upload test

## Guardrails

- Do not upload firmware, run ASUS Firmware Restoration, start TFTP transfer, or perform any write/recovery action in Phase 1.
- Do not generate a final profile from this note.
- Do not merge RT-AX86U behavior with RT-AC86U behavior.
- RT-AC86U may be used only as explicitly labeled comparison evidence.
- Treat Rescue Mode entry, Web recovery, TFTP transfer, firmware write, post-upload wait, DHCP return, and configuration retention as separate claims.
- If signals conflict or timing becomes guesswork, stop and create an incident candidate instead of tuning parameters.
- Keep firmware binaries private/local. Record only official URL, version, filename, size, checksum status, and model/region applicability.
- Do not record serial number, MAC address, default Wi-Fi password, admin password, WAN account details, or private local paths.

## Current Known State From User

- Vendor: ASUS
- Model: RT-AX86U
- Device condition: user-owned primary router, in daily use for about 4 months; user reports strong performance and stable/pleasant daily operation.
- Edition / appearance: red Gundam / Zaku-themed edition per user description and label branding.
- Current firmware family from user: official ASUSWRT-Merlin firmware, unmodified.
- Current production role: normally the user's primary router, but temporarily replaced by an H3C NX30 Pro for this test window.
- Intended scope: official normal baseline first; Rescue Mode entry observation later; no firmware upload or write test in Phase 1.
- Related comparison source: `runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json` is RT-AC86U evidence only and must not be treated as RT-AX86U fact.
- Risk boundary: because this is normally the user's primary production router, firmware upload, restore, factory reset, or destructive write tests still require explicit owner confirmation. During the current test window, low-risk and moderate-risk observation can proceed faster than prior reference devices because the active Mac/router path has been moved to an H3C NX30 Pro.

## Session Hypothesis

RT-AX86U should be tested as an independent ASUS reference device for Rescue Mode and possible Passive TFTP PUT behavior. The first useful output is a clean official-state baseline and firmware-source manifest, not a profile and not proof of RT-AX86U recovery support.

## Phase 1 - Official Baseline Only

### 1. Physical Label / Power Baseline

Record non-sensitive label facts only.

- [x] Model exactly as printed: `RT-AX86U`; label also describes it as `Wireless-AX5700 Dual-band Gigabit Router`.
- [x] Hardware version / revision, if printed: `H/W Ver.: 1.0`.
- [x] Region / market marking, if printed: multiple regulatory marks visible; made in Vietnam; Gundam/Zaku edition branding visible. Exact sales region not concluded from label alone.
- [x] Power input rating on router label: `19V 2.37A or 19.5V 2.31A`.
- [ ] Power adapter output rating:
- [x] Label photo/video saved privately: user provided `IMG_7218.jpg`; sensitive identifiers intentionally not transcribed.
- [x] LAN port numbering / physical layout noted: rear ports visible in photo; a `2.5G Port` label is visible. Full LAN/WAN port order still needs a clearer rear-port photo or direct observation before using it for recovery guidance.

Do not transcribe:

- serial number
- MAC address
- default Wi-Fi password
- default SSID if it contains device-specific identifiers
- WPS PIN or other device-specific onboarding secrets

Notes:

- Label-visible default Wi-Fi network name, MAC address, PIN code, serial number, QR code contents, and barcode contents are intentionally not recorded.
- Label-visible firmware string appears to be stock label/manufacturing information, not necessarily the currently installed runtime firmware. Current firmware must be confirmed from the live Web UI because the user reports official ASUSWRT-Merlin is installed.

### 2. Official Admin UI Baseline

Use the router's normal official admin UI only. Do not enter Rescue Mode in this phase.

- [x] Admin UI reachable: yes, normal ASUSWRT-Merlin Web UI reachable.
- [x] Admin UI URL / management IP: `http://192.168.50.1/` observed, including `/index.asp`, `/Advanced_FirmwareUpgrade...`, `/Advanced_LAN_Content.asp`, and `/Advanced_DHCP_Content.asp`.
- [x] Login state / setup state: logged in to normal admin UI; no setup wizard or recovery page observed.
- [x] Current firmware version: `3004.388.11`.
- [x] Hardware version shown in UI: model shown as `RT-AX86U`; hardware revision not shown in System Info screenshot.
- [x] ASUSWRT / ASUSWRT-Merlin / other firmware family: ASUSWRT-Merlin shown in UI header; user describes it as official Merlin, unmodified.
- [x] Language / region shown in UI: Simplified Chinese UI selected.
- [x] Router mode / AP mode, if visible: operation mode shown as wireless router.
- [x] LAN IP: `192.168.50.1`.
- [x] DHCP server enabled: yes.
- [x] DHCP range: `192.168.50.2` - `192.168.50.254`.
- [x] DHCP lease time: `86400` seconds.
- [x] Default gateway field: blank in DHCP server page.
- [x] DNS fields, if visible: DNS server 1 and DNS server 2 blank in DHCP server page; router-IP advertising option enabled.
- [x] Firmware upgrade page reachable: yes.
- [x] Online upgrade prompt: firmware page shows scheduled check for new firmware availability enabled; no newer-version result captured yet.
- [ ] Latest version offered by UI:
- [x] Auto-update setting, if visible: security upgrade toggle shown ON; scheduled firmware availability check set to yes.
- [x] Configuration backup/export option found: yes, restore/export/upload settings tab exists.
- [x] Configuration backup saved privately before any update/write decision: yes, user confirmed Merlin backup was exported and saved.

Notes:

- Current WAN/upstream state in this temporary setup: router reports internet connected and a private WAN IP in the `192.168.66.0/24` range. This is temporary upstream context via the replacement H3C path, not recovery evidence.
- Current Mac Wi-Fi client state from macOS network settings: DHCP address `192.168.50.79`, subnet mask `255.255.255.0`, router `192.168.50.1`.
- UI shows normal runtime health panels including traffic, CPU cores, RAM, and Ethernet interface widgets. These confirm normal admin access but are not recovery-mode evidence.
- SSID, custom router hostname suffix, and any identifiers derived from MAC/default label values are intentionally not transcribed.
- System Info page confirms:
  - Model: `RT-AX86U`.
  - Firmware version: `3004.388.11`.
  - Firmware build: `Fri Dec 26 17:25:33 UTC 2025`.
  - Bootloader: `0.0.0.6`.
  - Uptime at capture: about 7 days 18 hours 32 minutes.
  - CPU: `BCM490x - B53 ARMv8 revision 0`, 4 cores at 1800 MHz.
  - Memory: total about 912.07 MB; no swap.
  - Internal storage indicators: NVRAM and JFFS usage visible.
  - Temperatures at capture: 2.4 GHz 48 C, 5 GHz 51 C, CPU 70 C.
  - Hardware acceleration: Runner enabled, Flow Cache enabled.
  - Wireless clients: 5 GHz clients associated/authenticated; 2.4 GHz no clients at capture.
- Wireless driver version and full feature-token list were visible but are not transcribed unless needed later; they are verbose runtime diagnostics, not recovery-entry facts.

### 3. Official Firmware Source Manifest

Use official ASUS sources only. Do not commit firmware binaries to this repo.

| Firmware role | Version | Official page URL | Download filename | Extension | Size | Checksum available | Checksum checked | Model/hardware/region match | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current installed | 3004.388.11 | https://www.asuswrt-merlin.net/download | `RT-AX86U_3004_388.11_0.zip` | `.zip` containing firmware image | 74.6 MB | SHA256 listed for extracted `.w` image | not locally checked | UI-confirmed on RT-AX86U | Currently installed; SourceForge release directory lists the matching release |
| latest offered by UI | 3004.388.11 | https://www.asuswrt-merlin.net/download | `RT-AX86U_3004_388.11_0.zip` | `.zip` containing firmware image | 74.6 MB | SHA256 listed for extracted `.w` image | not locally checked | UI-offered/current for this device | Firmware page did not show a newer captured version |
| latest listed on ASUS support page |  |  |  |  |  |  |  |  | Source-manifest only |

Official page context:

- [x] ASUS support/download page title: Asuswrt-Merlin Download page plus SourceForge `RT-AX86U/Release` directory.
- [x] Page model selector confirms exact `RT-AX86U`: SourceForge directory contains `RT-AX86U` release folder and `RT-AX86U_3004_388.11_0.zip`.
- [ ] Hardware/revision selector exists:
- [ ] Region/market applicability visible:
- [x] Release notes visible: not on captured SourceForge directory page; changelog links exist on the Merlin site navigation.
- [x] Checksum/hash visible: Merlin download page lists SHA256 for `RT-AX86U_3004_388.11_0_pureubi.w`: `2c5afe57302544311fac5c3b537179b184066d93f3fad015b3c084214b9dd925`.
- [x] Firmware archive requires extraction: release file is a `.zip`; firmware image inside should be used for manual upload/restoration, not the zip itself.
- [x] Download page links ASUS Firmware Restoration: firmware upgrade page instructs users to download ASUS Firmware Restoration from the ASUS download center if firmware/security upgrade fails and the router enters emergency mode.
- [ ] Separate official Rescue Mode / Firmware Restoration article found:

Notes:

- Firmware upgrade page states that during firmware/security upgrade, configuration parameters will keep their settings.
- Firmware upgrade page states that if upgrade fails, RT-AX86U will automatically enter emergency mode and the front LED will indicate that state.
- Firmware upgrade page points to `https://www.asuswrt-merlin.net/download/` for latest Merlin firmware downloads.
- Manual firmware update/upload entry is visible for the RT-AX86U AiMesh router entry.
- SourceForge RT-AX86U release directory lists `RT-AX86U_3004_388.11_0.zip`, modified 2025-12-26, size 74.6 MB.

### 4. Backup / Update Gate

Before any official update, firmware upload, restoration action, or recovery-mode write test, answer this gate explicitly.

- [x] Is current configuration worth preserving? yes, this is normally the user's primary router.
- [x] Is backup/export available in UI? yes.
- [x] Backup created and kept private/local: yes, user confirmed Merlin configuration backup was exported and saved locally; backup file not committed.
- [ ] Does the UI warn about region/model/hardware mismatch?
- [x] Does the UI warn not to power off during update? not directly captured in the visible screenshots; firmware page does warn about upgrade failure/emergency mode and points to Firmware Restoration.
- [ ] Decision: no update/write action in Phase 1.

Gate decision notes:

- Phase 1 is information collection only. If the device offers an official online update, record it but do not start it until the backup decision is explicit.
- The backup gate is satisfied for observation and Rescue Mode entry planning. It does not approve firmware upload, restoration, factory reset, or other write actions.

## Phase 2 - Rescue Mode Entry Observation Only

Do not start this phase until Phase 1 is filled enough to preserve the official baseline.

- [x] Phase 1 reviewed before Rescue Mode entry: official normal-state baseline, Merlin source manifest, backup gate, front LED baseline, and rear-port layout are recorded enough to proceed to entry-only observation.
- [x] Recovery observation plan selected: Rescue Mode entry observation only, no firmware upload.
- [x] No firmware upload planned: yes.
- [x] Stop conditions reviewed: no firmware upload, no ASUS Firmware Restoration action, no factory reset, and no profile claim during this phase.

Observation fields to fill later:

- [x] Power-off wait duration: about 10 seconds before recovery-entry attempt.
- [x] Cable path: Mac wired Ethernet to RT-AX86U LAN1; WAN and other LAN clients not part of the observation.
- [x] LAN port used: LAN1.
- [ ] Mac wired interface:
- [ ] Wi-Fi kept available:
- [ ] Wired route/IP ownership confirmed:
- [x] Static IP used, if any: Mac-side static recovery subnet was planned as `192.168.1.10/24`; exact interface ownership still to confirm from Mac network state.
- [x] Button used: Reset.
- [x] Hold duration: user began holding Reset while inserting power at video time about 9 seconds; exact release time not recorded in this note.
- [x] LED sequence:
  - Video time about 13 seconds: LAN1 white LED became lit.
  - Power LED changed from solid on to slow flashing.
  - Later LAN1 LED flashed while power LED continued slow flashing.
  - Observation ended after seamless transition from TTL=100 replies to TTL=64 replies.
- [ ] Mac link-up timing:
- [x] Ping target: `192.168.1.1`.
- [x] Ping replied: yes.
- [x] TTL observed: TTL=100 first observed at video time about 16 seconds; continuous TTL=100 replies lasted about 162 seconds; then replies transitioned to TTL=64.
- [x] Web probe attempted: yes, `192.168.1.1` Web access attempted during TTL=100 window.
- [x] Web probe result: did not open / no Web recovery page observed.
- [ ] TFTP transfer attempted: no
- [ ] ASUS Firmware Restoration attempted: no

Notes:

- Phase 2 should prove only entry/readiness signals. It should not prove upload, write, post-upload behavior, DHCP return, or configuration retention.
- Normal front LED baseline from photo: power, 5 GHz, 2.4 GHz, and Internet LEDs lit; 2.5G and LAN1-LAN4 LEDs appear off; WPS appears off.
- Rear port layout from photo, left to right: DC input, power switch, reset button, two USB 3.0 ports, 2.5G port, blue WAN port, then yellow LAN ports 1-4. Photo labels LAN1-LAN4 clearly enough for Phase 2 port selection.
- Prior RT-AC86U observation suggested LAN1 mattered on that model, but RT-AX86U must independently verify whether LAN1 is required for Rescue Mode entry or TFTP readiness.
- Interpretation from this observation:
  - LAN1 + Reset-held power-on successfully reached a recovery-like state on this RT-AX86U unit.
  - TTL=100 plus slow-flashing power LED is a strong Rescue Mode entry/readiness signal for this unit.
  - Web recovery is not supported or not exposed in this observed state.
  - The long TTL=100 window may support a TFTP workflow, but TFTP direction is still unverified. Do not classify as active TFTP server, passive TFTP PUT, ASUS Firmware Restoration success, firmware write success, or post-upload recovery from this observation alone.
  - TTL=64 transition likely indicates the device left the recovery bootloader/window and returned toward normal boot, but this needs admin/DHCP follow-up before making a normal-boot conclusion.

### Passive Capture Direction Probe - No Transfer

Date/time: 2026-05-17 around 19:14 local time

- [x] Wireshark capture started on the corresponding wired interface before entry observation.
- [x] Capture filter: none.
- [x] Display filters to review after capture: `tftp`, `udp.port == 69`, and `arp or icmp or udp.port == 69 or bootp or dhcp`.
- [x] TFTP command/tool executed: no.
- [x] Firmware upload attempted: no.
- [x] ASUS Firmware Restoration executed: no.
- [x] Ping target: `192.168.1.1`.
- [x] TTL=100 observed: yes.
- [x] TTL=100 duration: observed from ping sequence around 231 through 648, more than 5 minutes, without natural transition to TTL=64 before user paused the test.
- [x] User paused test: yes.
- [x] Display-filter review, `tftp`: no packets.
- [x] Display-filter review, `udp.port == 69`: no packets.
- [x] Display-filter review, non-ICMP subset: ARP only in copied summary; no DHCP/BOOTP or TFTP records reported.
- [x] ARP observations:
  - Mac-side Ugreen adapter ARPed for `192.168.1.1`; router responded that `192.168.1.1` is at the ASUS MAC.
  - Router ARPed for `192.168.1.10`; Mac responded with the Ugreen adapter MAC.
  - Additional Mac ARP probes/announcements for `192.168.1.10` and probes for `169.254.255.255` were observed around the 47-49 second range.
  - Later ARP refreshes for `192.168.1.1` at about 196.7s and 343.3s were answered by the router.

Interpretation:

- This run confirms that the RT-AX86U Rescue Mode / recovery-like TTL=100 window can persist for more than 5 minutes under the observed setup.
- The prior 162-second TTL=100 duration should not be treated as a fixed timeout.
- Timing variability is now an observation, not a parameter to tune.
- No router-initiated TFTP RRQ was observed in passive capture during this run.
- Active TFTP Server direction is not supported by this capture.
- Passive TFTP PUT remains untested because no WRQ/PUT command was sent.
- The capture confirms bidirectional L2/L3 presence between Mac `192.168.1.10` and router `192.168.1.1`; lack of TFTP packets is therefore not explained by total link failure.

Next proposed test, not yet executed:

- Use the local POC App / harness to send a controlled Passive TFTP PUT to `192.168.1.1` from Mac `192.168.1.10`.
- Prefer the POC App over macOS interactive `tftp` because it can preserve structured transfer metadata: start timing, ACK source port, duration, bytes sent, block count, rollover behavior, and error message.
- If a real firmware image is selected, this becomes a firmware write test and requires explicit owner confirmation.
- If the goal is only protocol acceptance, consider a non-firmware WRQ probe first; if the goal is write confirmation, use a model-matched Merlin firmware image with recorded filename, extracted image hash, and post-upload observation plan.

### POC App Passive TFTP PUT - Firmware Upload

Runtime attempt:

- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`

Observed from POC App log:

- Target device under test: RT-AX86U, despite the POC UI/log still using R7000 wording.
- Router recovery IP / TFTP server: `192.168.1.1:69`.
- Mac bind IP: `192.168.1.10`.
- Firmware image filename: `388102.w`.
- Firmware image size: 86,900,756 bytes.
- WRQ filename: `388102.w`.
- TFTP mode: `octet`.
- WRQ attempt #1 accepted immediately.
- ACK block 0 received from `192.168.1.1:69`.
- Server replied from initial port `69`; no ephemeral server port observed.
- Upload completed: 86,900,756 bytes in 39.956 seconds, about 2123.94 KiB/s.
- Block number rollover observed twice.
- Final DATA block: 38657 after two rollovers, consistent with 169,729 total 512-byte blocks for the 86,900,756-byte image.
- POC App post-upload instruction: wait several minutes before power cycling.

Interpretation:

- This proves Passive TFTP PUT transfer compatibility for this RT-AX86U unit in the observed Rescue Mode state.
- The transfer result does not yet prove firmware write completion, downgrade success, post-upload reboot behavior, DHCP return, admin UI return, or configuration retention.
- Post-upload evidence must be recorded separately before changing the runtime attempt outcome to success.
- Post-upload wait observation:
  - After upload completion and more than 5 minutes of waiting, front LEDs showed only LAN1 white solid; other LEDs were off per user report.
  - Mac wired interface was changed from static recovery IP to DHCP and waited about 1 minute.
  - DHCP did not return; Mac received only a self-assigned `169.254.x.x` address with no router/gateway/DNS.
  - This is evidence against immediate DHCP return after upload. It does not yet prove failure, because manual power cycle has not been tested in this AX86U post-upload state.
  - User notes this post-upload state matches the prior RT-AC86U observed behavior: after firmware upload, only LAN1 white LED remained on and DHCP was not available before the next transition.
  - Scope boundary: this comparison supports an ASUS-family post-upload hypothesis, but it does not yet prove RT-AX86U manual power-cycle behavior, DHCP return, firmware-version change, or configuration retention.
- Manual power-cycle follow-up:
  - After normal power cycle, Mac DHCP returned on the normal LAN.
  - Mac received `192.168.50.5`, subnet `255.255.255.0`, router `192.168.50.1`, DNS `192.168.50.1`.
  - Admin UI reopened at `192.168.50.1`.
  - Firmware version displayed in UI: `3004.388.10_2`.
  - Configuration appeared retained by visual inspection; LAN/admin IP and themed Merlin UI remained consistent with the pre-test state.
  - Stability follow-up: admin UI remained stable, firmware page continued to show `3004.388.10_2`, DHCP settings stayed unchanged, Wi-Fi settings were retained, WAN connectivity was working, and the pre-existing JFFS ShellCrash installation remained usable.
  - Result for this runtime attempt: successful Passive TFTP PUT downgrade plus post-upload power-cycle recovery.
  - Configuration-retention boundary: user reports prior RT-AC86U repeated tests behaved inconsistently, with about 3-4 tests including at least one case where configuration was cleared. Therefore this RT-AX86U single retained-config result must be recorded as this-run outcome only, not as a controllable or guaranteed ASUS behavior.

### Normal Web UI Upgrade Back To Current Merlin

Date/time: 2026-05-17 around 20:05-20:09 local time

Scope:

- This is a normal Web UI firmware upgrade baseline after the TFTP downgrade test.
- It is not Rescue Mode evidence and should not be mixed with TFTP recovery behavior.

Observed:

- Firmware before Web UI upgrade: `3004.388.10_2`.
- Firmware file used: `RT-AX86U_3004_388.11_0_pureubi.w`.
- Upgrade target: `3004.388.11`.
- UI displayed firmware upgrade progress and estimated the process would take about 3 minutes.
- Owner observed total upgrade time around 2-3 minutes.
- Owner observed Web UI transfer/progress felt much slower than the TFTP transfer.
- Network interruption was short; after the progress completed, network appeared immediately usable.
- No additional power cycle was needed after the Web UI upgrade; network was usable when the upgrade flow completed.
- Owner interpretation: the UI's 3-minute estimate likely includes upload/write time inside the router, not only file transfer.
- Firmware after Web UI upgrade: `3004.388.11`.
- Configuration after Web UI upgrade: visually normal/retained.
- Wi-Fi, WAN, and existing JFFS ShellCrash installation remained usable.

Interpretation:

- Normal Merlin Web UI upgrade from `3004.388.10_2` back to `3004.388.11` succeeded.
- This confirms the router returned cleanly to the original current firmware after the recovery experiment.
- It does not add evidence about Rescue Mode, TFTP direction, or post-upload recovery semantics.

## RT-AC86U Comparison Boundary

RT-AC86U observed comparison evidence exists, but it is not RT-AX86U evidence.

Comparison source:

- `runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json`
- `reports/asus_rt_ac86u_observation_guardrails_2026-05-13.md`
- `reports/asus_rt_ac86u_reference_validation_owner_checklist.md`

RT-AC86U comparison facts that require fresh RT-AX86U verification before reuse:

- Rescue Mode entry button, LAN port, hold duration, and LED pattern.
- Recovery IP and Mac static IP.
- Passive TFTP PUT direction.
- ACK source port behavior.
- Firmware filename or file extension acceptance.
- Post-upload wait duration.
- Whether manual power cycle is required.
- DHCP return gateway/admin URL.
- Configuration retained/reset/unknown outcome.

## Evidence Mapping

Use these buckets after each phase:

| Observation type | Destination |
| --- | --- |
| Official normal-state facts | This live session note |
| Official firmware source facts | This live session note / future source index if needed |
| Rescue Mode entry-only signal | This live session note first |
| Upload or transfer test | Runtime attempt only after explicit approval |
| Failed or unstable timing | Incident candidate |
| Reproducible reviewed behavior | Profile candidate only after review |

## Open Questions

- [x] Does RT-AX86U normal firmware UI expose model/hardware/region clearly enough for source matching? Model and firmware family were visible; hardware revision came from label, not System Info.
- [x] Does ASUS/Merlin provide checksum/hash for the RT-AX86U firmware package? Merlin page provided SHA256 for the extracted `.w`; local checksum was not checked in this session.
- [x] Does the official page point users to Web UI upload, ASUS Firmware Restoration, or both? Web UI manual upload exists; firmware page points to ASUS Firmware Restoration if upgrade fails/emergency mode occurs.
- [x] Is Rescue Mode reachable without starting any transfer? Yes, LAN1 + Reset-held power-on reached TTL=100 / slow-flashing power LED state.
- [x] Does Rescue Mode expose Web, TFTP, ASUS Firmware Restoration, or a combination of paths? Web was not observed; active RRQ was not observed; Passive TFTP PUT was verified through the POC App. ASUS Firmware Restoration GUI itself was not tested.

## Session Closeout

Date/time: 2026-05-17 evening

- Device returned to normal daily-use firmware: `3004.388.11`.
- Normal Web UI upgrade back to current Merlin succeeded after the TFTP downgrade.
- Network was usable after Web UI upgrade without another power cycle.
- Owner reports backend/admin UI, firmware page, DHCP, Wi-Fi, WAN, and existing JFFS ShellCrash remained normal.
- Follow-up from a separate code/app session: `/tmp/ShellCrash/CrashCore.check` was no longer present after router testing. Interpretation: temporary `/tmp` runtime state was likely cleared during reboot/upgrade/recovery transitions. This does not contradict the observed JFFS ShellCrash installation/configuration being usable; treat `/tmp` runtime files separately from persistent JFFS configuration.
- This RT-AX86U is ready to resume primary-router use.
- No further device testing is recommended unless a future product-blocking question requires it.
- Future work should be documentation/profile-candidate review and App wording/tooling updates, not more hardware tests on this unit.
