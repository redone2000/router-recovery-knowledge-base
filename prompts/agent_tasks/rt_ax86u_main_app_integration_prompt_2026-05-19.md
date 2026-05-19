# Prompt: Integrate RT-AX86U Rescue/TFTP Findings Into Main App

Use this prompt in the main Router Recovery App integration session.

## Task

Integrate the ASUS RT-AX86U reference-device findings into the main App's guided recovery flow without re-running hardware tests.

Source repository is private:

```text
https://github.com/redone2000/router-recovery-knowledge
```

Use branch:

```text
codex-rt-ax86u-handoff
```

Read these files first:

- `reports/rt_ax86u_main_app_integration_handoff_2026-05-19.md`
- `lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`
- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md`
- `reports/asus_rt_ax86u_profile_candidate_guardrails_2026-05-17.md`
- `reports/app_copy_upload_complete_vs_recovery_complete_2026-05-17.md`

Remote links:

- https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/rt_ax86u_main_app_integration_handoff_2026-05-19.md
- https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md
- https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json
- https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md
- https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/asus_rt_ax86u_profile_candidate_guardrails_2026-05-17.md
- https://github.com/redone2000/router-recovery-knowledge/blob/codex-rt-ax86u-handoff/reports/app_copy_upload_complete_vs_recovery_complete_2026-05-17.md

## Evidence Summary

For the tested ASUS RT-AX86U unit:

- Rescue Mode entry: LAN1 + hold Reset while powering on.
- Recovery IP: `192.168.1.1`.
- Client static IP: `192.168.1.10/24`.
- Readiness signal: slow-flashing power LED plus TTL=100.
- Web Recovery page was not observed.
- Passive capture did not observe active TFTP RRQ.
- Passive TFTP PUT succeeded.
- WRQ accepted on first attempt.
- Router replied from `192.168.1.1:69`.
- ACK source port remained `69`.
- Transfer completed: 86,900,756 bytes in about 40 seconds.
- Upload completion did not restore DHCP.
- After waiting more than 5 minutes, only LAN1 white LED remained on and DHCP did not return.
- Normal power cycle restored DHCP/admin UI.
- Firmware write success was verified by downgrade to `3004.388.10_2`.
- Normal Web UI upgrade returned router to `3004.388.11`.
- Configuration was retained in this run but must not be promised.

## Implementation Guidance

Implement this as reviewed-candidate / observation-only behavior, not a final universal profile.

Main flow:

1. Firmware selection
   - Require model-matched official Merlin/ASUS firmware.
   - Tell user to use extracted `.w`, not `.zip`.
   - Record filename, size, checksum status, but not local path.

2. Network preparation
   - Direct Ethernet to LAN1.
   - Mac/App recovery IP: `192.168.1.10/24`.
   - Router recovery IP: `192.168.1.1`.

3. Rescue Mode entry
   - Hold Reset while powering on.
   - Wait for slow-flashing power LED and TTL=100.
   - Do not treat ping/TTL alone as recovery success.

4. Transfer
   - Passive TFTP PUT.
   - App is TFTP client.
   - Router is TFTP server.
   - Send WRQ/PUT to `192.168.1.1:69`.
   - Follow ACKs from source port `69`.
   - Log ACK block 0 source, bytes sent, block count, rollover count, duration, and errors.

5. Post-upload
   - Transfer complete is not recovery complete.
   - Wait several minutes after upload.
   - Do not power-cycle immediately at upload completion.
   - If DHCP does not return and the observed model guidance supports it, instruct a normal power cycle: power off, wait 10 seconds, power on without holding Reset.
   - Switch Mac back to DHCP.
   - Use DHCP gateway as admin URL.
   - Verify firmware version in admin UI.
   - Ask user to check LAN/DHCP, Wi-Fi, WAN, and add-ons.

## Required Copy Boundaries

Use:

```text
Firmware upload finished. The router may still be writing firmware. Do not unplug power yet.
```

Use:

```text
Wait several minutes before the next step. During this phase, the router may not provide DHCP or open its admin page.
```

Use:

```text
Open the router admin page and confirm the firmware version. This is the evidence that the write completed.
```

Avoid:

```text
Recovery complete.
```

at transfer completion.

Avoid:

```text
Your settings will be preserved.
```

Configuration retention is not guaranteed.

## POC App Wording Fix

Search the main App / POC code for hardcoded `R7000` in generic TFTP flow text.

Observed bad examples from the RT-AX86U run:

- `Waiting for R7000 recovery window...`
- `Target R7000 server=192.168.1.1:69`

Replace generic flow wording with neutral text:

- `Waiting for recovery window...`
- `Target router server=...`
- `Recovery window captured. Uploading firmware...`

If selected device/profile/model is available, show the selected model dynamically. Otherwise do not hardcode any model.

Do not change transfer logic while fixing wording.

## Stop Lines

Do not ask the user to retest RT-AX86U unless a specific implementation blocker requires a missing fact.

Do not claim:

- all RT-AX86U variants behave identically
- RT-AC86U and RT-AX86U share one profile
- Web Recovery is universally absent
- Active TFTP is impossible
- configuration will be retained
- upload completion means recovery completion

## Expected Output

At the end of the integration session, report:

- App files changed
- how RT-AX86U candidate behavior is represented
- UI/copy changes for upload-vs-recovery-complete
- `R7000` wording replacements
- tests/builds run
- any remaining gaps that require profile review, not hardware testing
