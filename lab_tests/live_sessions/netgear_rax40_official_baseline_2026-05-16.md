# NETGEAR RAX40 Official Baseline Live Session

Date: 2026-05-16
Status: active live note
Device role: NETGEAR RAX40 official baseline / recovery-entry observation reference device
Primary goal: capture official device state, firmware-source baseline, and recovery-direction signals before any firmware upload or profile claim

## Guardrails

- Do not flash OpenWrt, third-party firmware, or any firmware image during Phase 1.
- Do not claim RAX40 support from this session.
- Do not generate a final profile from this note.
- Treat official normal state, Recovery Mode, NMRP, TFTP, post-upload behavior, and DHCP return as separate claims.
- Keep R7000 evidence as incident context only unless RAX40 observations independently reproduce a pattern.
- If signals conflict or timing becomes guesswork, stop and create an incident candidate instead of tuning timing.
- Keep firmware binaries private/local. Record only source URL, version, filename, size, checksum status, and model/hardware applicability.
- Do not record serial number, MAC address, default Wi-Fi password, admin password, WAN account details, or private local paths.

## Current Known State From User

- Vendor: NETGEAR
- Model: RAX40v2, printed on label as NETGEAR Nighthawk AX4 / AX3000 4-Stream WiFi Router
- Device condition: second-hand unit arrived; live baseline collection not started in this note yet.
- Intended scope: official baseline first; recovery entry observation later; no dangerous flashing in this phase.
- LAN port marking observation: the port labeled `LAN 1` is on the far side from the WAN port, not the LAN port nearest the WAN port.
- Label/regulatory observation: Chinese-language label with China regulatory markings observed; made in Vietnam.
- Initial normal-boot anomaly: DHCP did not provide an IP before reset; after reset, DHCP provided an IP and the browser reached the NETGEAR setup start page.
- Official app setup path: Nighthawk app reached router settings and identified the unit as `RAX40v2`.
- Post-update access anomaly: default Wi-Fi password from the label can join the wireless network, but browser backend authentication/management is still not available.
- App management limitation: current Nighthawk app view exposes only limited settings and does not provide enough baseline/admin controls.
- Client IP confirmation: phone/client is confirmed to be receiving an IP from the RAX40 network while browser access still redirects to 404 behavior.
- Admin recovery after setup: after the official App "set up a new router" flow, the browser local admin UI became reachable.

## Session Hypothesis

RAX40 is a modern NETGEAR reference target for deciding whether NETGEAR recovery needs orchestration around NMRP, TFTP, or another recovery path. The useful first output is a clean official-state baseline and source manifest, not a profile and not proof of RAX40 recovery support.

## Phase 1 - Official Baseline Only

### 1. Physical Label / Power Baseline

Record non-sensitive label facts only.

- [x] Model exactly as printed: NETGEAR Nighthawk AX4 / AX3000 4-Stream WiFi Router, model `RAX40v2`
- [x] Hardware version / revision, if printed: `v2` appears as part of the printed model identifier `RAX40v2`
- [x] Region / market marking, if printed: Chinese-language regulatory label and China regulatory marks observed
- [x] Power input rating: 12V DC, 2.5A
- [ ] Power adapter output rating:
- [x] Label photo/video saved privately:
- [x] LAN port numbering / physical layout noted: `LAN 1` is physically farthest from the WAN port.

Do not transcribe:

- serial number
- MAC address
- default Wi-Fi password / network key
- default SSID if it contains device-specific identifiers

Notes:

- This matters for later recovery-entry tests. Use the router's printed `LAN 1` label as the primary port identity; do not assume "LAN1" means the LAN port nearest WAN on this model.
- Label also prints a router-login URL and default credential fields, plus SSID, Wi-Fi password, serial number, and MAC. These sensitive or device-specific values are intentionally not transcribed into the repo.
- The device should be treated as `RAX40v2` for source matching and later observations, not generic `RAX40`.

### 2. Official Admin UI Baseline

Use the router's normal official admin UI only. Do not enter recovery mode in this phase.

- [x] Admin UI reachable: yes, full browser admin UI reachable after official App new-router setup flow
- [x] Admin UI URL / management IP: `http://192.168.1.1/start.htm`
- [x] Login state / setup state: browser local admin UI reachable; earlier setup fallback and `192.168.1.1/start.htm` paths reached stale/broken 404 until App new-router setup completed
- [x] Current firmware version: before app update `v1.0.2.82`; after app update `1.0.17.142`
- [x] Hardware version shown in UI: `RAX40v2`
- [x] Language / region shown in UI: Chinese setup page text observed
- [ ] Router mode / AP mode, if visible:
- [x] Router mode / AP mode, if visible: Router mode selected; AP mode and bridge mode options visible but not selected
- [x] LAN IP: `192.168.1.1`
- [x] DHCP server enabled: yes
- [x] DHCP range: `192.168.1.2` - `192.168.1.254`
- [ ] DHCP lease time:
- [ ] Default gateway field:
- [ ] DNS fields, if visible:
- [x] Firmware upgrade page reachable: Nighthawk app detected a new firmware version
- [x] Online upgrade prompt: before update, app showed update available and estimated about 3 minutes depending on Internet speed; after update, app reports firmware is current
- [x] Latest version offered by UI: `1.0.17.142`; update completed successfully via Nighthawk app
- [x] Auto-update setting, if visible: enabled
- [x] Configuration backup/export option found: yes, browser admin UI backup/export works after App new-router setup restored local admin access
- [x] Configuration backup saved privately before recovery testing: `NETGEAR_RAX40v2.cfg`, kept local/private and not committed

Notes:

- Before reset, DHCP did not provide an IP. This is recorded as an arrival-state anomaly for this second-hand unit, not as a recovery-mode signal.
- After reset, DHCP succeeded enough for the browser to reach `192.168.1.1/start.htm`.
- The visible page asks the user to download/use the Nighthawk app for quick setup and includes a fallback link for users without a compatible smartphone.
- Clicking the no-compatible-smartphone fallback opened `https://www.routerlogin.net/genie_index.htm`, which returned `Server Error` / `404 - File or directory not found`.
- The 404 is recorded as a broken or stale normal-setup fallback path, not as evidence of recovery behavior.
- Retrying the `192.168.1.1` path also redirected to the same `routerlogin.net/genie_index.htm` 404.
- Retrying `http://192.168.1.1/start.htm` later also redirected to the same 404, so the browser setup path is currently blocked after the initial setup prompt.
- Directly opening `https://www.routerlogin.net` loaded the public NETGEAR Router Login website instead of the local router admin/setup UI.
- For this session, `routerlogin.net` should not be treated as a reliable local-management endpoint. Prefer explicit `192.168.1.1` observations and record redirects separately.
- Next low-risk path: use the official Nighthawk app only for minimum setup/admin access, with no firmware update or recovery action.
- Nighthawk app router settings screen confirms:
  - Router name: `RAX40v2`
  - Hardware version: `RAX40v2`
  - Firmware version before update: `v1.0.2.82`
  - Firmware version after update: `v1.0.17.142`
  - Hardware type text before update: `NIGHTHAWK`
  - Hardware type text after update: `Router`
  - Router LAN/admin IP: `192.168.1.1`
- Nighthawk app Internet-port screen shows:
  - External/upstream IP address: `192.168.66.157`
  - Upstream gateway: `192.168.66.1`
  - Subnet mask: `255.255.255.0`
  - DNS: `192.168.66.1`
  - WAN type: DHCP
- The app-visible serial number and MAC addresses are intentionally not transcribed into this repo.
- Firmware update prompt showed current firmware `1.0.2.82` and available firmware `1.0.17.142`.
- Official Nighthawk app update completed successfully; firmware reached `1.0.17.142`.
- Post-update app check reports the firmware is current and no newer firmware is available.
- DHCP was maintained after the update.
- Default Wi-Fi credentials from the physical label still allow joining the wireless network after reset/update.
- Browser access remained abnormal after the update: `192.168.1.1` is still not normal, and both `192.168.1.1`/routerlogin behavior and `routerlogin.net` still lead to 404 behavior.
- Backend authentication/management is still not available from the browser path.
- The App currently exposes limited settings only; no sufficient backup/export or full admin baseline controls have been found.
- Phone/client is confirmed to be on the RAX40-provided network/IP, so the browser 404 is less likely to be a simple wrong-Wi-Fi/wrong-network mistake.
- User is attempting the official App "set up a new router" path as a controlled re-initialization check.
- Official App "set up a new router" flow restored browser local admin UI access.
- Browser admin UI after setup shows:
  - Firmware version: `V1.0.17.142_2.0.100`
  - GUI/interface language version: `V1.0.17.140_21.46.1`
  - Router label: `Nighthawk RAX40v2`
  - Basic and Advanced tabs are available.
  - Internet status: good.
  - Connected devices: 1-2 during observation window.
  - Dynamic QoS: off.
  - ReadySHARE / USB status: no USB drive.
  - Guest network: disabled.
- LAN settings page confirms:
  - LAN IP: `192.168.1.1`
  - Subnet mask: `255.255.255.0`
  - RIP direction: both
  - RIP version: disabled
  - DHCP server enabled
  - DHCP range: `192.168.1.2` - `192.168.1.254`
- Backup settings page confirms:
  - Backup current settings action exists.
  - Restore saved settings from file action exists.
  - Factory-default erase action exists.
- Router upgrade page confirms:
  - Online firmware check says no newer firmware is available.
  - Manual firmware upload UI exists.
  - Automatic firmware upgrade is enabled.
- Advanced settings page confirms selectable operating modes:
  - Router mode selected.
  - AP mode available.
  - Bridge mode available.
- Screenshot-visible Wi-Fi SSID/password details are intentionally not transcribed.
- Configuration backup after clean official setup:
  - Filename: `NETGEAR_RAX40v2.cfg`
  - Size: 14,747 bytes
  - File type: zip archive data
  - Archive contents: one file, `acos_backup.cfg`
  - SHA-256: `3a407f2fe38b89138b32c86045efcc79f246f888cae88b4a345e7aac2d673a45`
  - Handling: local/private only; do not commit the backup or transcribe sensitive config contents.
- Interpretation: official app update success, Wi-Fi join success, and browser local-management restoration are separate observations. The update alone did not fix the stale/broken browser setup/admin path; the App new-router setup flow did.
- This page is an official normal setup/start page, not a Recovery Mode page and not evidence of Web Recovery/TFTP/NMRP behavior.

### 3. Official Firmware Source Manifest

Use official NETGEAR sources only. Do not commit firmware binaries to this repo.

| Firmware role | Version | Official page URL | Download filename | Extension | Size | Checksum available | Checksum checked | Model/hardware/region match | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| arrival firmware | 1.0.2.82 |  |  |  |  |  |  | app-confirmed on RAX40v2 | UI-confirmed arrival baseline before app update |
| app online update target | 1.0.17.142 |  |  |  |  |  |  | app offered for RAX40v2 | Installed successfully via official Nighthawk app |
| current after update | 1.0.17.142 |  |  |  |  |  |  | app-confirmed on RAX40v2 | DHCP maintained; browser management path still abnormal |
| latest listed on official download page |  |  |  |  |  |  |  |  | Source-manifest only |

Official page context:

- [ ] NETGEAR support/download page title:
- [ ] Page model selector or product page confirms RAX40:
- [ ] Hardware version selector exists:
- [ ] Region/market applicability visible:
- [ ] Release notes visible:
- [ ] Checksum/hash visible:
- [ ] Firmware archive requires extraction:
- [ ] Download page includes recovery instructions:
- [ ] Separate official recovery article found:

Notes:

-

### 4. Backup / Update Gate

Before any official update, answer this gate explicitly.

- [x] Is current configuration worth preserving? yes, at least enough to preserve/reset baseline before any update
- [x] Is backup/export available in UI? yes
- [x] Backup created and kept private/local: `NETGEAR_RAX40v2.cfg`
- [ ] Does the UI warn about region/model/hardware mismatch?
- [ ] Does the UI warn not to power off during update?
- [x] Decision: official Nighthawk app online update performed after browser setup path was blocked and no more visible parameters were reachable

Gate decision notes:

- The app offered an update from `1.0.2.82` to `1.0.17.142`.
- Because browser setup was blocked and no more visible parameters were reachable before update, the official Nighthawk app online update was allowed as a separate baseline event. The device had just been reset and no meaningful user configuration had been built yet.

### 5. Official App Online Update Capture Plan

Only use this if choosing the official Nighthawk app update path. This remains official-update baseline evidence, not recovery-mode evidence.

- [ ] Video captures both phone app screen and router front LEDs in the same frame when possible.
- [x] Before tapping update, capture current/available firmware versions: `1.0.2.82` -> `1.0.17.142`.
- [x] Start time: relative `0s`, app update started.
- [x] App download/update progress states:
  - `0s`: app update started; app page says do not unplug router or power off, and says router will reboot after firmware update completes.
  - `2m19s`: app reports it is rebooting the router and says reboot may take about 3 minutes.
  - `4m01s`: app reports update succeeded.
- [x] Router LED changes during update:
  - `0s`: visible front LEDs were lit, including power, Internet/cloud, 2.4 GHz, 5 GHz, LAN 1, and lower status LEDs.
  - `2m19s`: visible front LEDs still appeared lit similarly while app reported rebooting.
  - `4m01s`: power and Internet/cloud LEDs appeared amber/red, 2.4 GHz and 5 GHz LEDs were lit, lower status LED remained lit, and app reported update success.
- [ ] Approximate time of any Wi-Fi/DHCP/client disconnect:
- [x] Approximate time App reconnects or reports completion: `4m01s` from update start, app reports update success.
- [x] Firmware version after update: `v1.0.17.142`
- [x] App update check after update: firmware is current; no newer firmware available
- [x] DHCP after update: maintained
- [x] Browser `192.168.1.1` behavior after update: still abnormal / not normal local admin access
- [x] Browser `routerlogin.net` behavior after update: still 404 behavior
- [x] Configuration retained/reset/unknown: app-visible router name and LAN IP remained present; detailed configuration retention not fully assessed

Capture cautions:

- Do not record admin password, NETGEAR account credentials, serial number, MAC address, or Wi-Fi password in the video frame if avoidable.
- Do not power off during update.
- Do not treat 100% progress as completion until the app/router/admin access returns.

## Phase 2 - Recovery Entry Observation Only

Do not start this phase until Phase 1 is filled enough to preserve the official baseline.

- [x] Phase 1 reviewed before recovery entry: official firmware updated, browser admin UI restored, configuration backup saved privately
- [x] Recovery observation plan selected: low-risk entry observation only, no firmware upload
- [x] No firmware upload planned: yes
- [x] Stop conditions reviewed: yes

Observation fields to fill later:

- [ ] Power-off wait duration:
- [ ] Cable path:
- [ ] LAN port used:
- [ ] Mac wired interface:
- [ ] Wi-Fi kept available:
- [ ] Wired route/IP ownership confirmed:
- [ ] Static IP used, if any:
- [ ] Button used:
- [ ] Hold duration:
- [ ] LED sequence:
- [ ] Recovery IP attempted:
- [ ] Ping response:
- [ ] TTL:
- [ ] Web recovery page reachable:
- [ ] Web recovery URL:
- [ ] TFTP packets observed:
- [ ] TFTP direction, if observed:
- [ ] NMRP-like discovery observed:
- [ ] Stop reason:

### Phase 2A - Low-Risk Entry Observation Plan

Goal: identify whether RAX40v2 exposes a visible recovery/setup/recovery-like state and what signals appear. Do not upload firmware and do not try to force success.

Preparation:

- [ ] Confirm config backup remains available locally: `NETGEAR_RAX40v2.cfg`.
- [ ] Keep official admin baseline screenshot/video private.
- [ ] Mac connected directly to the router by Ethernet.
- [ ] Disconnect WAN if the goal is pure recovery-entry observation; keep Wi-Fi/phone available only for notes/timer if needed.
- [ ] Use printed `LAN 1` first, even though it is physically farthest from WAN.
- [ ] Record if a second port comparison is needed later: printed `LAN 1` vs LAN port nearest WAN.
- [ ] Keep firmware file out of this phase.

Suggested passive observation commands/tools:

- [ ] Continuous ping to `192.168.1.1`.
- [ ] Optional packet capture on the wired interface with broad capture first, then inspect for ARP, ICMP, HTTP, TFTP, or NMRP-like traffic.
- [ ] Browser probe only after a stable IP/ping signal appears: `http://192.168.1.1/`.

Entry attempt A:

- [ ] Power off duration:
- [ ] Button used:
- [ ] Hold duration:
- [ ] Release timing:
- [ ] LED sequence:
- [ ] LAN port:
- [ ] Mac IP before entry:
- [ ] Mac IP during entry:
- [ ] Ping result:
- [ ] TTL:
- [ ] Web page response:
- [ ] Packet signals:
- [ ] Return-to-normal result:

Stop rules:

- Stop after one clean observation attempt if the device returns to normal and signals are understandable.
- Stop after two ambiguous attempts with the same setup.
- Stop immediately if the router enters an unknown LED loop, DHCP does not return, or admin access does not recover.
- If ping appears but no service-specific signal appears, record that as a signal mismatch; do not tune timing repeatedly.

### Phase 2A - 2026-05-17 Execution Checklist

Status: in progress

Scope: recovery-entry observation only. No firmware upload, no factory reset from UI, no NMRP/TFTP transfer.

Pre-check before touching buttons:

- [x] Browser admin UI reachable at `192.168.1.1/start.htm`.
- [x] Firmware still shows `V1.0.17.142_2.0.100`.
- [x] Config backup file still exists privately: `NETGEAR_RAX40v2.cfg`.
- [x] Current normal DHCP/client state recorded.
- [x] Printed `LAN 1` selected for first attempt.
- [x] WAN disconnected for the observation attempt.
- [x] Firmware file not selected or prepared for upload.

Attempt 1 - printed `LAN 1`, observation only:

- [x] Mac/client connection: Mac direct Ethernet to printed `LAN 1`
- [x] Power-off duration: about 10 seconds; at relative `12s`, reset was held while power was reconnected
- [x] Button used: reset
- [x] Button hold timing: reset held from relative `12s` to `28s`
- [x] Button release timing: released at relative `28s` when power LED was amber blinking
- [x] LED sequence:
  - `12s`: power reconnected while holding reset; power LED was solid white
  - `16s`: power LED changed to amber flashing
  - `28s`: power LED amber blinking; reset released
  - `33s`: power LED still amber flashing
  - `36s`: printed `LAN 1` white LED lit; ping responded once with `ttl=100`
  - `52s`: printed `LAN 1` white LED went off
  - `1m06s`: printed `LAN 1` white LED lit again; ping responses returned with `ttl=64`; Wi-Fi white LEDs lit
- [ ] Link/DHCP state during entry:
- [x] Ping target: `192.168.1.1`
- [x] Ping first response time: relative `36s`, one reply observed
- [x] TTL observed: one `ttl=100` reply during short early window; later normal replies returned with `ttl=64`
- [ ] Browser response at `http://192.168.1.1/`:
- [x] Browser response at `http://192.168.1.1/start.htm`: Nighthawk App quick-setup prompt page appeared after the attempt, similar to the earlier setup/start page
- [x] Browser setup fallback behavior: clicking the no-compatible-smartphone / click-here fallback now opens `http://192.168.1.1/ads_start.htm`, showing NETGEAR terms and conditions with an agreement checkbox/button; it no longer jumps to the old `genie_index.htm` 404 in this state
- [x] Browser setup agreement result: after clicking agree on `ads_start.htm`, the browser redirected to `https://www.routerlogin.net/genie_index.htm` and returned `Server Error` / `404 - File or directory not found`
- [ ] Packet/capture signals, if any:
- [ ] Return-to-normal method:
- [x] Return-to-normal time: normal ping behavior returned around relative `1m06s`
- [x] Post-attempt admin UI reachable: no; browser reached the Nighthawk App setup prompt instead of the full admin UI; Nighthawk app also reported the router is not set up
- [x] Stop/continue decision: stop after one observation and classify the `ttl=100` response as a short bootloader/recovery-like signal; do not tune timing or upload firmware

Interpretation placeholder:

- Recovery entry confirmed: not fully confirmed; reset-on-power produced a short recovery-like `ttl=100` signal
- Recovery service type observed: none observed yet
- TFTP direction observed: none
- NMRP-like signal observed: not checked / not observed
- Incident candidate: yes, normal-setup regression candidate
- Reason: `ttl=100` was transient and appeared only once before normal `ttl=64` boot returned; after the attempt, `start.htm` showed the Nighthawk App quick-setup prompt instead of the full admin UI, and the Nighthawk app reported the router is not set up. This suggests the reset-on-power sequence altered setup/admin state, not just exposed a harmless observation window.
- Setup fallback note: yesterday, the click-here fallback led to `routerlogin.net/genie_index.htm` 404. After the device was updated and setup state changed, the same fallback now reaches local `ads_start.htm` terms page. This suggests the earlier 404 was state/firmware/setup-path dependent, not necessarily a permanently broken link.
- Setup agreement result note: the local terms page itself loads, but agreeing still redirects to the stale/broken `routerlogin.net/genie_index.htm` 404 path. This means the browser setup flow remains broken after the reset-on-power setup regression.
- Official support check on 2026-05-17:
  - NETGEAR's RAX40v2 user manual documents web-browser access and says the NETGEAR installation assistant runs on devices with a web browser.
  - NETGEAR's web-interface installation KB explicitly applies to `RAX40v2` and says the app recommendation page should allow clicking the no-compatible-smartphone link, after which a welcome page should display.
  - Therefore this observed `ads_start.htm` -> `routerlogin.net/genie_index.htm` 404 is not explained by "RAX40v2 does not support web setup" in official docs. It is better treated as a broken setup redirect/state anomaly on this unit/firmware path.
- Recovery from setup regression:
  - Official Nighthawk app was used to complete setup again after the reset-on-power attempt.
  - Browser admin pages became accessible again after App setup.
  - Saved configuration backup was not restored because the basic state after App setup was effectively consistent with the prior baseline.
  - Keep `NETGEAR_RAX40v2.cfg` as private rollback evidence, but do not treat backup restore as performed.
  - Post-restore browser check shows router status and LAN IP settings reachable again.
  - Firmware remains `V1.0.17.142_2.0.100`.
  - LAN/DHCP baseline remains consistent: DHCP enabled, range `192.168.1.2` - `192.168.1.254`.
  - Mac Ethernet DHCP confirmation after restore:
    - Client IP: `192.168.1.2`
    - Subnet mask: `255.255.255.0`
    - Router/gateway: `192.168.1.1`
    - DNS server: `192.168.1.1`

## Open Questions

- Does the normal admin UI identify this unit as RAX40 with a visible hardware revision?
- Does the normal admin UI identify this unit as `RAX40v2`, matching the printed label?
- Does the official download page have RAX40 hardware/region variants that matter?
- Does NETGEAR publish checksums for the relevant firmware package?
- Does the admin UI offer an online update, and is it a safer source than manual download?
- Does a configuration backup need to be captured before any official update or recovery entry test?
- Is the eventual recovery direction Web, NMRP, passive TFTP PUT, active TFTP server, or mixed?
- Are ping/TTL signals potentially misleading before a service-specific response appears?
- Does RAX40 recovery behavior prefer the printed `LAN 1`, the port nearest WAN, any LAN port, or another port? This must be observed, not inferred from hygiene defaults.

## Output Decision Log

- Runtime attempt record needed: not yet. Phase 1 is baseline/source capture only; app-based setup access is recorded as normal baseline evidence.
- Runtime attempt record needed: yes for official app online update baseline, created at `runtime_attempts/netgear_rax40v2_official_app_online_update_2026-05-16.json`.
- Incident candidate needed: no for now. Browser setup/admin anomaly resolved after official App new-router setup; keep it as a baseline note, not an incident, unless it recurs.
- Profile update candidate: no.
- Workflow update candidate: unknown.
- App issue/task found: unknown.
- Next action: complete Phase 1 official baseline fields from label, admin UI, and official download page evidence.

## App Guidance Candidate

Status: candidate only; not profile guidance yet.

Observation:

- After a reset-on-power recovery-entry observation, RAX40v2 returned to normal `ttl=64` boot but entered an unconfigured/setup state.
- Browser setup flow showed the Nighthawk App prompt, then `ads_start.htm`, but clicking agree redirected to `routerlogin.net/genie_index.htm` and returned 404.
- The official Nighthawk app was the practical path to restore local admin access in the earlier setup sequence.
- Official docs indicate RAX40v2 should support web-interface setup, so the 404 should be treated as a broken setup redirect/state anomaly rather than as a designed no-web-support behavior.

Potential App guidance:

- If a user completes NETGEAR recovery or reset-like recovery entry and then sees a NETGEAR setup prompt or `routerlogin.net/genie_index.htm` 404, do not tell the user to retry firmware recovery immediately.
- First suggest confirming the router has booted normally and the client has a DHCP lease from the router.
- Then suggest using the official Nighthawk app to complete minimum initial setup and restore local admin access.
- Only return to recovery troubleshooting if DHCP/admin/App access cannot be restored.

Risk:

- This is currently based on one RAX40v2 lab observation. Keep it as incident/app-guidance candidate until repeated or supported by additional evidence.

## Phase 2B - Passive Service Probe Plan

Date: 2026-05-18
Status: stopped after two attempts

Scope: observe services/signals during the already observed short `ttl=100` window. Do not upload firmware, do not run a recovery transfer, and do not tune timing repeatedly.

Goal:

- Determine whether the short `ttl=100` window exposes any service-specific recovery signal.
- Separate bootloader ICMP visibility from actual Web/TFTP/NMRP readiness.
- Preserve the setup-regression lesson from 2026-05-17.

Preconditions:

- [ ] Browser admin UI reachable before test.
- [ ] Firmware still `V1.0.17.142_2.0.100`.
- [ ] Mac Ethernet DHCP normal: `192.168.1.2` / gateway `192.168.1.1`.
- [ ] Config backup still saved privately.
- [ ] WAN disconnected for the attempt.
- [ ] Printed `LAN 1` used first.
- [ ] No firmware file selected.

Observation tools:

- [ ] Continuous ping to `192.168.1.1`.
- [ ] Browser page pre-opened to `http://192.168.1.1/`, manually refreshed only when `ttl=100` appears.
- [ ] Optional packet capture on wired interface if available, broad capture first.
- [ ] Optional passive UDP/TFTP watch only; no upload and no firmware transfer.

Attempt outline:

- [ ] Power off for about 10 seconds.
- [ ] Hold reset while reconnecting power.
- [ ] Release on amber blinking power LED, matching the 2026-05-17 attempt.
- [ ] When `ttl=100` appears, immediately note timestamp and try one browser refresh.
- [ ] Do not click upload/restore/update even if a page appears.
- [ ] Let device return to normal boot.
- [ ] Confirm whether setup regression happens again.

Fields to capture:

- [x] Time of first `ttl=100` response: not observed in two controlled attempts
- [x] Number of `ttl=100` replies: 0 across two attempts
- [ ] HTTP/browser response during `ttl=100`: not applicable; no `ttl=100` observed
- [ ] Any UDP/TFTP packet observed:
- [ ] Any NMRP-like traffic observed:
- [ ] Time normal `ttl=64` returns:
- [ ] Whether full admin UI remains available:
- [ ] Whether App setup is required again:

Result:

- Two Phase 2B attempts did not reproduce the 2026-05-17 one-time `ttl=100` reply.
- No service-specific probe should be inferred because the target `ttl=100` window was not observed.
- Stop condition reached: repeated attempts did not reproduce the signal, so do not continue tuning button timing in this session.

Interpretation:

- The 2026-05-17 `ttl=100` signal is currently a non-reproducible recovery-like observation, not a stable entry method.
- Treat this as incident-candidate evidence around unstable reset-on-power behavior, not as profile guidance.
- Do not claim RAX40v2 exposes a reliable TFTP/Web/NMRP recovery window from current evidence.

Stop rules:

- Stop after one controlled attempt if setup regression repeats.
- Stop if `ttl=100` appears but no service-specific signal appears; do not keep tuning release timing.
- Stop if admin UI does not recover normally.
- Convert to incident candidate if setup regression repeats or service signals conflict.

## Official Firmware / TFTP Evidence Check

Date: 2026-05-18
Status: source check complete; lab validation not complete

Official firmware paths:

- RAX40v2 user manual documents normal firmware update from the router Web UI: `ADVANCED > Administration > Router Update`.
- The manual also documents manual firmware upload from the Web UI after downloading and unzipping firmware from NETGEAR Download Center. The expected firmware file extension is `.img` or `.chk`.
- NETGEAR RAX40v2 firmware release article links official firmware package `RAX40v2-V1.0.4.100_2.0.64.zip` as an example older package and says to follow the user manual for update instructions.

Official TFTP evidence:

- NETGEAR's official Windows TFTP-client article says TFTP can be used when a router is bricked, does not boot properly, has blinking/solid amber power LED, firmware update fails, web UI is inaccessible, or DHCP is not assigning addresses.
- The official Windows TFTP-client article lists `RAX40v2` in its applies-to model list.
- NETGEAR's official macOS TFTP article also lists `RAX40v2` in its applies-to list and gives the macOS flow:
  - download and extract official firmware
  - direct Ethernet connection
  - static client IP `192.168.1.10/24`, router `192.168.1.1`
  - macOS terminal `tftp 192.168.1.1`, `binary`, then prepare `put <firmware file name>`
  - power off for 10 seconds, power on, wait for power LED to light orange and flash
  - execute `put`
  - wait about 4 minutes after successful upload

Current interpretation:

- Officially, RAX40v2 is included in NETGEAR's TFTP recovery guidance.
- Locally, this lab has not yet reproduced a stable `ttl=100` window or any service-specific TFTP/Web/NMRP response.
- Do not promote RAX40v2 to "TFTP verified" from source evidence alone.
- The next useful test, if performed later, should be a controlled macOS TFTP-readiness probe or packet capture around the official "orange flashing power LED" state, not repeated arbitrary reset timing.

## Phase 2C - TFTP Readiness Probe

Date: 2026-05-18
Status: stopped

Scope: local POC readiness test only; no successful TFTP response observed.

Observation:

- User tested with the local POC after considering that the router might not respond to ICMP but could still respond to TFTP.
- Result: no response observed.

Interpretation:

- Current local evidence does not show TFTP readiness on RAX40v2.
- This does not disprove official NETGEAR TFTP support, because timing/interface/state/tool behavior may still be wrong.
- Stop condition reached for this session: do not keep tuning TFTP timing without new evidence.

Next candidate:

- Test NMRP on a later session because prior NETGEAR work suggested NMRP can be simpler/reliable on some NETGEAR devices.
- Keep NMRP findings at runtime/incident level until repeatable and clearly separated from official TFTP evidence.
