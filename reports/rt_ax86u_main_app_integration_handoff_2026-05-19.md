# RT-AX86U Main App Integration Handoff

Date: 2026-05-19
Prepared by: Codex
Status: handoff for main App integration
Branch: `codex-rt-ax86u-handoff`
Remote repository: `https://github.com/redone2000/router-recovery-knowledge` private

## Purpose

This handoff packages the ASUS RT-AX86U reference-device work so another session can integrate the findings into the main Router Recovery App without re-running device tests.

Do not perform more RT-AX86U device testing unless a future product-blocking question cannot be answered from these records.

## Remote Files To Read First

Use these files as the source of truth:

- [Live session note](https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md)
- [Runtime attempt JSON](https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json)
- [Observation summary](https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md)
- [Profile-candidate guardrails](https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/asus_rt_ax86u_profile_candidate_guardrails_2026-05-17.md)
- [App copy/state guidance](https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/app_copy_upload_complete_vs_recovery_complete_2026-05-17.md)
- [Integration prompt](https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/prompts/agent_tasks/rt_ax86u_main_app_integration_prompt_2026-05-19.md)

## What Was Proven

For the tested ASUS RT-AX86U unit:

- Normal admin baseline was captured on ASUSWRT-Merlin.
- Rescue Mode entry was observed with LAN1 + Reset-held power-on.
- `192.168.1.1` replied with TTL=100 in Rescue Mode.
- Web Recovery page was not observed.
- Passive capture did not observe active TFTP RRQ / router-pulls-firmware behavior.
- Passive TFTP PUT was verified using the local POC App.
- Router accepted WRQ on `192.168.1.1:69`.
- ACK source port stayed `69`; no ephemeral server port was observed.
- Firmware transfer completed: 86,900,756 bytes in about 40 seconds.
- Firmware write was verified by downgrade from `3004.388.11` to `3004.388.10_2`.
- Upload completion was not recovery completion.
- After upload and more than 5 minutes, DHCP had not returned and only LAN1 white LED remained on.
- Normal power cycle restored DHCP/admin UI.
- DHCP returned to normal LAN with gateway `192.168.50.1`.
- Configuration was retained in this run, but this must not be promised.
- Normal Web UI upgrade returned the router to `3004.388.11` without needing an extra power cycle.

## Integration Boundaries

Do not convert this evidence directly into a final production profile.

Safe integration target:

- reviewed-candidate logic
- App guided-flow behavior
- runtime attempt logging
- copy/state wording
- POC wording fix

Unsafe claims:

- all RT-AX86U variants behave identically
- RT-AX86U and RT-AC86U share one profile
- configuration will be retained
- Web Recovery is impossible on every firmware/state
- ping/TTL alone proves recovery success
- upload completion means recovery completion

## Main App Changes To Consider

Implement or review:

- Device/profile candidate for RT-AX86U as observation-only.
- Passive TFTP PUT flow:
  - Mac/App is TFTP client.
  - Router is TFTP server.
  - Recovery IP is `192.168.1.1`.
  - Mac static IP is `192.168.1.10/24`.
  - Use LAN1.
  - WRQ/PUT to port `69`.
  - Follow ACKs from source port `69`.
- UI states must separate:
  - transfer complete
  - post-upload wait
  - power-cycle step
  - DHCP return
  - admin UI check
  - firmware version verification
  - configuration check
- Warnings:
  - use the extracted `.w`, not `.zip`
  - firmware must be exact-model matched
  - configuration retention is not guaranteed
  - do not power-cycle immediately when upload completes

## POC App Wording Fix

The POC App log still used `R7000` wording during the RT-AX86U run. Fix generic/shared text so it does not hardcode a model name.

Use neutral text such as:

- `Waiting for recovery window...`
- `Target router server=...`
- `Recovery window captured. Uploading firmware...`

If the App has a selected device/profile, it may interpolate the actual selected model. Otherwise use neutral wording.

## Current Router State

The tested router has been returned to normal daily-use state:

- Firmware: `3004.388.11`
- Normal Web UI upgrade succeeded after the TFTP downgrade experiment.
- Network was usable after the Web UI upgrade without an additional power cycle.
- Admin UI, DHCP, Wi-Fi, WAN, and JFFS ShellCrash were reported normal.
- `/tmp/ShellCrash/CrashCore.check` was later missing; treat that as `/tmp` runtime cleanup, not persistent JFFS config loss.

## Verification Already Run

Runtime attempt validation:

```text
python3 tools/validate_runtime_attempts.py runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json
```

Result:

```text
No validation issues found.
```

## Recommended Next Step

Main App integration should start from the integration prompt in:

```text
prompts/agent_tasks/rt_ax86u_main_app_integration_prompt_2026-05-19.md
```

Do not ask the user to retest the router unless implementation is blocked by a specific missing fact.
