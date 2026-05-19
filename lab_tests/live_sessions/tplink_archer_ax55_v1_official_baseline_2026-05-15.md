# TP-Link Archer AX55 v1 Official Baseline Live Session

Date: 2026-05-15
Status: active live note
Device role: TP-Link Web Recovery / TFTP direction baseline reference device
Primary goal: capture official-firmware baseline and recovery-entry behavior before any third-party firmware experiment

## Guardrails

- Do not flash OpenWrt, ImmortalWrt, Breed, U-Boot, or other third-party firmware in this session.
- Do not generalize AX55 observations to all TP-Link devices.
- Treat Web Recovery, active TFTP server, passive TFTP PUT, DHCP return, and post-upload recovery as separate claims.
- Record unknowns explicitly instead of filling guesses.
- Keep firmware binaries private/local; record only source URL, filename, version, size, checksum, and region/hardware applicability in this repo.
- Do not record serial numbers, passwords, WAN details, or private local paths.

## Current Known State From User

- Vendor: TP-Link
- Model: Archer AX55
- Hardware version: v1.0
- Label region / market marking: Archer AX55(CA), Ver: 1.0 observed on physical device label.
- UI product label: AX3000 4-Stream Wi-Fi 6 Router
- Region / UI: Traditional Chinese UI observed; Simplified Chinese not available in language list; user observed roughly 20-30 language options.
- Current firmware before session: 1.3.1 Build 20240129 rel.57815(4341)
- Upgrade offered by Web UI: 1.5.11 Build 20251119 rel.49503
- Current operating state: official firmware running normally
- Admin UI URL observed: `http://192.168.0.1/webpages/index.html#/firmware`
- Evidence screenshots:
  - `截屏2026-05-15 21.36.52.png`: firmware page showing firmware version, hardware version, and online upgrade offer.
  - `截屏2026-05-15 21.38.56.png`: DHCP server page showing LAN DHCP range and gateway.
  - `截屏2026-05-15 21.39.55.png`: update message popup.
  - `IMG_7185.jpg`: device label photo. Sensitive serial number, MAC address, default SSID, and default wireless password are intentionally not transcribed.

## Session Hypothesis

AX55 v1 should be treated as a TP-Link reference device for Web Recovery / TFTP direction discovery. The first useful output is not a model profile. The first useful output is a clean official baseline plus controlled recovery-mode observations.

## Step 0 - Before Touching Recovery

- [ ] Screenshot or screen recording saved privately for current Web UI firmware page.
- [x] Current firmware version confirmed from device UI: 1.3.1 Build 20240129 rel.57815(4341)
- [x] Hardware version confirmed from UI: Archer AX55 v1.0
- [x] Hardware / market marking confirmed from label: Archer AX55(CA), Ver: 1.0.
- [x] Region / firmware channel confirmed if visible: exact firmware channel not shown in UI; physical label indicates CA market; Traditional Chinese UI available, Simplified Chinese not available.
- [x] LAN default IP recorded: 192.168.0.1
- [x] DHCP default range recorded: 192.168.0.2 - 192.168.0.253
- [x] Admin UI URL recorded: http://192.168.0.1/
- [ ] WAN disconnected/not relevant:
- [x] Firmware auto-upgrade prompt behavior recorded: firmware page offers online upgrade from 1.3.1 Build 20240129 rel.57815(4341) to 1.5.11 Build 20251119 rel.49503; auto-update toggle is off.
- [x] Configuration backup saved before upgrade: `backup-Archer AX55-2026-05-15.bin` kept private/local, not committed to repo.

Notes:

- DHCP lease time shown as 120 minutes.
- Default gateway field shown as 192.168.0.1.
- Primary DNS and secondary DNS fields are blank.
- The UI uses marketing label `AX3000 4-Stream Wi-Fi 6 Router`; the model/hardware identity should be anchored to `Archer AX55 v1.0`.
- Browser marks the admin UI as not secure because it is HTTP on the local router admin page.
- Physical label shows `Archer AX55(CA)` and `Ver:1.0`, supporting the user's initial Canada-version assessment.
- Physical label also shows `Default Access: http://tplinkwifi.net`.
- Do not export serial number, MAC address, default SSID, or default wireless password from the label photo.

## Step 1 - Official Firmware Archive Manifest

Use official TP-Link sources only. Do not commit firmware binaries to this repo.

| Firmware role | Version/build | Official page URL | Download filename | Size | Checksum available | Checksum checked | Region/hardware match | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current | 1.3.1 Build 20240129 rel.57815(4341) |  |  |  |  |  | UI-confirmed on Archer AX55 v1.0 | Currently installed |
| latest offered | 1.5.11 Build 20251119 rel.49503 | TP-Link US Download Center page observed from screenshot | Archer AX55(US)_V1_1.5.11 Build 20251119 | 38.76 MB | not visible in screenshot | not checked | uncertain: US page, device region not yet confirmed | Online upgrade message available in device UI; US page notes firmware cannot be downgraded to previous version |
| regional latest visible | 1.3.5 Build 20241211 | TP-Link Hong Kong / Traditional Chinese Download Center page observed from screenshot | Archer AX55(US)_V1_1.3.5 Build 20241211 | 37.44 MB | not visible in screenshot | not checked | closer regional fit: HK Traditional Chinese page, but filename still `(US)_V1` | Published date 2025-07-17 on HK page; latest visible on HK page screenshot |
| historical | 1.3.3 Build 20240628 | TP-Link Hong Kong / Traditional Chinese Download Center page observed from screenshot | Archer AX55(US)_V1_1.3.3 Build 20240628 | 38.23 MB | not visible in screenshot | not checked | closer regional fit: HK Traditional Chinese page, but filename still `(US)_V1` | Published date 2024-09-18 |
| historical | 1.3.2 Build 20240325 | TP-Link Hong Kong / Traditional Chinese Download Center page observed from screenshot | Archer AX55(US)_V1_1.3.2 Build 20240325 | 37.60 MB | not visible in screenshot | not checked | closer regional fit: HK Traditional Chinese page, but filename still `(US)_V1` | Published date 2024-05-07; page notes firmware cannot be downgraded to previous version |

Observed official page context from user screenshot:

- Page title: `Download for Archer AX55 V1`
- Site footer/location selector: `United States / English`
- Hardware selector: `V1`
- Product label: `AX3000 Dual Band Gigabit Wi-Fi 6 Router Archer AX55`
- Manual links visible:
  - `Archer AX55(US)_V1_Datasheet`
  - `Archer AX55(US)_V1_User Guide`
  - `Archer AX55(US)_V1_Quick Installation Guide`
- Upgrade warning visible: use firmware from the local TP-Link official website for the purchase location, or the warranty may not be applied.
- Upgrade warning visible: verify hardware version; wrong firmware upgrade may damage the device and void warranty.
- Upgrade warning visible: do not turn off power during upgrade.
- Upgrade guidance visible: wired connection recommended during upgrade.
- Extraction guidance visible: use decompression software before upgrading if the firmware download is compressed.

US page firmware details visible:

- `Archer AX55(US)_V1_1.5.11 Build 20251119`
  - Published date: 2025-12-17
  - Language: Multi-language
  - File size: 38.76 MB
  - New features/enhancements: Added support for Ad Filtering; enhanced system stability and security.
  - Bug fixes: Resolved several minor bugs with EasyMesh.
  - Note: This firmware cannot be downgraded to the previous version.
- `Archer AX55(US)_V1_1.3.5 Build 20241211`
  - Published date: 2025-04-17
  - Language: Multi-language
  - File size: 37.44 MB
  - New features/enhancements: Added EasyMesh R2 traffic separation feature; implemented EasyMesh R3 functionality including DPP and encrypted communication.
  - Bug fixes: Fixed EasyMesh UI inconsistency after switching from router mode to AP mode; fixed guest-network IP assignment issue in AP mode.
- `Archer AX55(US)_V1_1.3.3 Build 20240628`
  - Published date: 2024-09-18
  - Language: Multi-language
  - File size: 38.23 MB
  - Modifications: added EasyMesh satellite/client binding; support for CAC channel availability check; client exception/approved websites in Web Protection; HomeShield EU functionality; VPN configuration process optimized.

Hong Kong / Traditional Chinese page context from user screenshot:

- Page title: `下載 Archer AX55 V1`
- Site footer/location selector: `Hong Kong, China / 繁體中文 | English`
- Hardware selector: `V1`
- Product label: `AX3000 雙頻 Wi-Fi 6+ EasyMesh 路由器 Archer AX55`
- Manual links visible:
  - `Archer AX55(US)_V1_Datasheet`
  - `Archer AX55(US)_V1_Quick Installation Guide`
  - `Archer AX55(US)_V1_User Guide`
- The visible firmware list does not show `1.5.11 Build 20251119`, even though the router Web UI offers it online.
- The visible firmware filenames still use `(US)_V1`, despite the page being the Hong Kong / Traditional Chinese site.

Hong Kong / Traditional Chinese page firmware details visible:

- `Archer AX55(US)_V1_1.3.5 Build 20241211`
  - Published date: 2025-07-17
  - Language: Multi-language
  - File size: 37.44 MB
  - New features/enhancements and bug fixes match the US page screenshot at a high level.
- `Archer AX55(US)_V1_1.3.3 Build 20240628`
  - Published date: 2024-09-18
  - Language: Multi-language
  - File size: 38.23 MB
  - Modifications match the US page screenshot at a high level.
- `Archer AX55(US)_V1_1.3.2 Build 20240325`
  - Published date: 2024-05-07
  - Language: Multi-language
  - File size: 37.60 MB
  - New features include ECO mode, DoH/DoT, OpenVPN Server, third-party VPN Client quick setup, multiple selection in whitelist, EasyMesh AP mode, Ethernet Backhaul, satellite router management via web UI, network isolation in AP mode, UI language options, USB sharing optimizations, Wi-Fi schedule enhancements, and stability enhancements.
  - Bug fixes include Tether lag for Family/Security options and Smart Connect being automatically disabled in specific operations.
  - Note: This firmware cannot be downgraded to the previous version.

Important interpretation:

- The device UI offered the same latest build as the US page, which is useful supporting evidence.
- The current installed build `1.3.1 Build 20240129 rel.57815(4341)` is not visible in either the US or Hong Kong screenshot sections shown by the user.
- The Hong Kong / Traditional Chinese page is a closer regional/language match to the device UI than the US page, but the device's online upgrade offer is newer than the HK page's visible firmware list.
- Because TP-Link warns to use purchase-region firmware, manual upgrade/recovery file selection should remain cautious. The physical label now points to CA market, while the US and HK pages shown both list `(US)_V1` firmware filenames.
- For official-to-official upgrade baseline, the router Web UI online upgrade path appears safer than manually selecting a downloaded package from a page whose list does not exactly match the device UI offer.

## Step 2 - Official Firmware Update Baseline

Only perform official-to-official upgrade if the firmware source and region/hardware match are clear.

- [x] Upgrade started from official Web UI: yes.
- [x] Upgrade source: online UI.
- [x] Start time: 2026-05-16 around 08:27 local time from photo evidence.
- [x] UI progress behavior: confirmation dialog, loading spinner, download progress, then upgrade progress, then login screen.
- [x] Router LED behavior: LEDs visible in photos remained lit during the captured early download/upgrade sequence; no obvious all-off state captured in the submitted images.
- [ ] Ping behavior during upgrade:
- [ ] TTL observations during upgrade:
- [ ] Time until reboot: not directly captured; inferred reboot/session reset occurred before the 3m35s login-screen observation.
- [x] Time until admin UI reachable: login screen visible at about 3m35s after starting the captured sequence.
- [x] DHCP restored: DHCP server page reachable after upgrade; DHCP remains enabled.
- [x] Gateway/admin URL after upgrade: 192.168.0.1 admin page reachable and shows local-password login screen.
- [x] Firmware version after upgrade: 1.5.11 Build 20251119 rel.49503(4341).
- [x] Configuration retained/reset/changed/unknown: retained per user confirmation; DHCP settings visible unchanged.
- [x] Notes: user captured key timepoints at 5s, 11s, 14s, 31s, 47s, and 3m35s, then supplied post-upgrade firmware and DHCP confirmation screenshots.

Captured upgrade timeline from user screenshots:

| Relative time | UI state | Router visible state | Interpretation |
| --- | --- | --- | --- |
| 5s | Upgrade confirmation dialog visible; message says the process may take about 3 minutes and router will reboot. | Several front LEDs lit. | User is confirming official online upgrade from the Web UI. |
| 11s | Firmware page still visible; upgrade button area shows loading spinner. | Several front LEDs lit. | Online upgrade request accepted; preparing or checking update. |
| 14s | Modal progress shown at 0%; text says `下載中...`; warning says do not operate router during firmware update. | Several front LEDs lit. | Firmware download phase started. |
| 31s | Modal text says `升級中...`; progress shown at 1%. | Several front LEDs lit. | Download phase completed and firmware upgrade/write phase started. |
| 47s | Modal progress shown at 100%; text says `升級中...`. | Several front LEDs lit. | Firmware upgrade/write progress reached 100%; reboot/session reset expected after this point. |
| 3m35s | Local password login screen visible at 192.168.0.1. | Several front LEDs lit. | Admin UI became reachable again; session required re-login after upgrade/reboot. |
| post-login confirmation | Firmware and DHCP pages visible after re-login. | Not captured in these screenshots. | Final firmware and retained DHCP settings confirmed after the upgrade. |

Official upgrade baseline interpretation:

- The Web UI's "about 3 minutes" warning is realistic for admin UI recovery, not just firmware download/write progress.
- Download phase completed between 14s and 31s, approximately 17 seconds from visible 0% download to upgrade-phase entry.
- Upgrade/write progress reached 100% by 47s, approximately 16 seconds after upgrade-phase entry.
- Progress reaching 100% did not mean the router was usable. The admin UI login screen was observed only around 3m35s.
- The observed recovery-to-login behavior supports an App/product warning such as: after online firmware update reaches 100%, keep waiting and do not power off until the admin page or network returns.
- Session reset/re-login after upgrade is normal in this observation and should not be treated as failure by itself.
- This is an official-update baseline, not a recovery-mode baseline. It should feed post-upload/wait-language guidance, but it does not prove Web Recovery or TFTP behavior.

Answered questions from this baseline:

- Official online upgrade path worked at least far enough to return the admin UI login page at `192.168.0.1`.
- The practical observed total time from upgrade confirmation to admin UI reachability was about 3m35s.
- The router remained physically powered and front LEDs were visible during submitted captured points.
- The upgrade required re-login after the router became reachable again.
- Manual downloaded firmware remains less preferred than Web UI online upgrade for this CA-labeled unit because visible US/HK download pages do not fully match the router's online-offered firmware list.

Still unanswered:

- Whether client DHCP lease renewal timing changed during the reboot window.
- Whether there was any ping/TTL transition during the reboot window.
- Exact moment of network drop or reboot, because the current evidence jumps from 47s upgrade progress to 3m35s login screen.

Post-upgrade confirmation:

- Firmware page at `192.168.0.1/webpages/index.html#/firmware` confirms:
  - Firmware version: `1.5.11 Build 20251119 rel.49503(4341)`
  - Hardware version: `Archer AX55 v1.0`
  - UI message: firmware is already the latest version.
- DHCP server page confirms:
  - DHCP server: enabled.
  - IP address range: `192.168.0.2 - 192.168.0.253`
  - Address lease time: 120 minutes.
  - Default gateway: `192.168.0.1`
  - Primary DNS / secondary DNS: blank.
- User confirmed other configuration was retained.

Official update baseline result:

- Result: success.
- Workflow: official Web UI online firmware update.
- Firmware before: `1.3.1 Build 20240129 rel.57815(4341)`.
- Firmware after: `1.5.11 Build 20251119 rel.49503(4341)`.
- Admin IP before/after: `192.168.0.1`.
- DHCP before/after: enabled, `192.168.0.2 - 192.168.0.253`, 120-minute lease.
- Configuration state: retained.
- Re-login required: yes.
- Approximate time from confirmation to admin UI login page: 3m35s.
- Evidence quality: strong for official update timing and post-update config retention; weak/absent for ping/TTL and exact reboot boundary.

Overnight stability check:

- Date/time: 2026-05-17 around 10:46 local time.
- Admin UI reachable at `192.168.0.1`.
- Firmware page still confirms `1.5.11 Build 20251119 rel.49503(4341)` and `Archer AX55 v1.0`.
- Firmware page reports the firmware is already the latest version.
- DHCP server remains enabled.
- DHCP range remains `192.168.0.2 - 192.168.0.253`.
- Lease time remains 120 minutes.
- Default gateway remains `192.168.0.1`.
- User assessment: visually normal.
- Interpretation: official online update remained stable overnight at the admin/DHCP/config-observation level.

Online upgrade message observed:

```text
New Features/Enhancements:
Added support for Ad Filtering.
Enhanced system stability and security.
```

## Step 3 - Recovery Entry Observation Only

No third-party upload. Avoid uploading anything unless we explicitly decide the file and risk boundary.

Structured draft record:

- `runtime_attempts/tplink_archer_ax55_recovery_entry_observation_2026-05-17.json`

Preflight plan:

- Observation goal: confirm whether AX55 v1 enters a recovery page/state, what IP/subnet it uses, and whether any TFTP direction signal appears.
- Do not upload firmware, even if an upload page appears.
- Do not use OpenWrt, ImmortalWrt, Breed, U-Boot, or any third-party file.
- Stop after a clear recovery page is observed, after a clear no-page/no-ping result is observed, or after 3 controlled entry attempts.
- If behavior differs by LAN port or timing, record it as an observation/incident candidate instead of guessing.

Official series-level source for this observation:

- Source: TP-Link FAQ 1482, `How to Recover a Bricked TP-Link Router`, last updated 2026-04-17.
- URL: `https://www.tp-link.com/us/support/faq/1482/`
- Existing repository classification: series-level Archer AX workflow evidence only, not AX55 model-specific profile evidence.
- Relevant Method 2 claims for Archer AX series:
  - Archer AX rescue mode may show only a single orange LED in the middle.
  - Entry method: power off, hold WPS button or Reset button on some models, power on, hold about 5 seconds until only the middle orange LED is lit.
  - PC should connect directly to a LAN port.
  - Static PC IP should be `192.168.0.10` with subnet mask `255.255.255.0`.
  - Rescue page should be opened at `192.168.0.1`.
  - Firmware file should be a `.bin` extracted from the official download.
  - After recovery, restore PC IP settings back to automatic.
- Boundary: use these claims to shape observation, not as proof that Archer AX55(CA) v1.0 on firmware `1.5.11 Build 20251119 rel.49503(4341)` behaves exactly this way.

Recommended first attempt:

- Start from current normal state: firmware `1.5.11 Build 20251119 rel.49503(4341)`, admin UI reachable at `192.168.0.1`.
- Keep direct Mac-to-router Ethernet if practical.
- Disconnect WAN and unrelated LAN clients if practical.
- Keep Wi-Fi available only for notes/chat if needed, but do not use Wi-Fi as proof that the router recovered.
- Record Mac wired interface name before power cycling.
- For the first controlled rescue-mode observation, set Mac Ethernet manually to `192.168.0.10/24` before entry, matching TP-Link FAQ 1482 Method 2.
- Try `http://192.168.0.1/` after entry. Do not upload firmware if the rescue page appears.
- If no page appears, record ping/TTL result for `192.168.0.1`.
- Film both screen and router LEDs if convenient.

Minimum data to send back after each attempt:

- Attempt number:
- LAN port used:
- Power-off duration:
- Button used:
- Hold duration:
- LED sequence:
- Mac IP before/after:
- URLs/IPs tried:
- Ping result and TTL, if checked:
- Web page result:
- Any packet/TFTP observation:
- Stop reason:

- [ ] Power-off wait duration:
- [ ] Cable path: Mac direct Ethernet / other:
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
- [ ] Page title/text summary:
- [ ] TFTP packets observed:
- [ ] TFTP direction, if observed:
- [ ] Required filename, if surfaced:
- [ ] Stop reason:

### Attempt 1 - WPS Power-On Entry

Result: failed to enter recovery mode; router returned to normal admin UI.

- Attempt number: 1
- Static IP used: Mac Ethernet set to `192.168.0.10/24`.
- Recovery IP attempted: `192.168.0.1`.
- Button used: WPS.
- Timeline:
  - 0:09: WPS held, then power connected.
  - Immediately after power-on: ping lost; power LED solid green; other LEDs not lit.
  - 0:28: WPS released while power LED still showed no change.
  - 0:54: power LED changed from solid to blinking at about 1-second interval.
  - 1:17: two green LEDs next to power LED turned on; power LED still blinking; ping still not reachable.
  - 2:03: Ethernet properties showed connected; Mac remained static `192.168.0.10`, not DHCP.
  - 2:12: LEDs unchanged; ping still not reachable; ping output alternated between normal ping attempts and `no route to host`; Ethernet still showed connected.
  - 2:47: ping became reachable; all visible router LEDs were on; opening `192.168.0.1` showed normal admin login page, not recovery page.
- Ping result: unreachable during early boot; reachable at about 2:47.
- TTL: not recorded.
- Web page result: normal management login page, not rescue/recovery page.
- TFTP packets observed: not recorded.
- Stop reason: observed normal boot/admin UI, not recovery mode.

Attempt 1 interpretation:

- TP-Link FAQ 1482 Method 2 WPS entry did not work on this AX55(CA) v1.0 unit with firmware `1.5.11 Build 20251119 rel.49503(4341)` under the tested timing.
- Releasing WPS at 28 seconds after power-on may still have allowed normal boot; no single orange/middle-LED rescue state was observed.
- The router's normal boot to ping/admin UI took about 2m47s in this test.
- `no route to host` during static-IP observation may indicate transient macOS route/link behavior while the Ethernet link was not fully usable; do not interpret it as router service state by itself.
- This is a negative observation for WPS-entry timing, not proof that AX55 lacks rescue mode.

### Attempt 2 - Reset Power-On Entry

Result: success; recovery firmware upload page appeared.

- Attempt number: 2
- Static IP used: Mac Ethernet set to `192.168.0.10/24`.
- Recovery IP attempted: `192.168.0.1`.
- Button used: Reset.
- Timeline:
  - 0:04: power unplugged.
  - 0:14: Reset held and power connected.
  - 0:20: middle orange LED lit; Reset released.
  - 0:29: ping responded.
  - Shortly after ping response: opening `192.168.0.1` showed recovery firmware upgrade page.
- Hold duration after power-on: about 6 seconds.
- LED sequence: middle orange LED appeared at about 6 seconds after power-on while Reset was held.
- Ping result: reachable at about 29 seconds.
- TTL: not recorded.
- Web page result: recovery page appeared at `http://192.168.0.1`.
- Page title/text summary: `Firmware Upgrade`; page asks user to choose a firmware file from local disk and click Upgrade; progress bar starts at 0%; tips warn not to power off and to choose the correct firmware file.
- TFTP packets observed: not recorded.
- Stop reason: recovery page observed; no firmware uploaded.

Attempt 2 interpretation:

- AX55(CA) v1.0 on firmware `1.5.11 Build 20251119 rel.49503(4341)` supports a browser-based recovery page at `192.168.0.1` when entered with Reset held during power-on.
- The successful entry method for this unit is Reset, not the WPS timing used in Attempt 1.
- The observed static client IP setup `192.168.0.10/24` matches TP-Link FAQ 1482 Method 2 and worked for page access.
- Recovery page readiness was observed quickly: ping by about 29 seconds, then HTTP recovery page.
- This proves Web Recovery page entry for this physical AX55 unit, but still does not prove firmware acceptance, post-upload behavior, TFTP direction, or broad AX55/Archer AX applicability.

Exit observation after Attempt 2:

- No firmware was uploaded.
- User unplugged power from the recovery page state and reconnected power.
- Ping responded again after about 147 seconds.
- Normal admin login page became accessible.
- Interpretation: after recovery-page observation without upload, power-cycle return to normal admin UI took about 2m27s.

## Open Questions

- Is AX55 v1 recovery primarily Web Recovery, active TFTP server, passive TFTP PUT, or mixed?
- Does Taiwan / Traditional Chinese firmware channel enforce region or header checks differently from US/EU docs?
- Does the official UI upgrade to 1.5.11 preserve configuration?
- Does recovery entry require a static client IP, and if so which subnet?
- Is ping/TTL present before the web page or TFTP service is actually ready?

## Output Decision Log

- Runtime attempt record needed: created at `runtime_attempts/tplink_archer_ax55_official_online_update_2026-05-16.json`.
- Incident candidate needed: no.
- Profile update candidate: no, this does not prove recovery-mode behavior.
- Workflow update candidate: yes, as supporting evidence for post-update/post-upload wait language.
- App issue/task found: product copy should warn that 100% progress is not completion; wait until admin/network returns.
- Next action: run observation-only Recovery Entry attempt using `runtime_attempts/tplink_archer_ax55_recovery_entry_observation_2026-05-17.json` as the structured draft.
