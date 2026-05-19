# Prompt: Integrate AX55 Web Recovery Entry Evidence Into Main App

Use this prompt in the main-app integration session.

```text
We need to integrate the latest TP-Link Archer AX55 reference-device findings from the private router-recovery-knowledge repository into the main Router Recovery app.

Source repository:
https://github.com/redone2000/router-recovery-knowledge

Read these files first:

1. Handoff:
https://github.com/redone2000/router-recovery-knowledge/blob/codex/ax55-web-recovery-entry-handoff/handoffs/main_app_ax55_web_recovery_entry_handoff_2026-05-19.md

2. Observation summary:
https://github.com/redone2000/router-recovery-knowledge/blob/codex/ax55-web-recovery-entry-handoff/reports/tplink_archer_ax55_recovery_entry_observation_summary_2026-05-17.md

3. Structured official-update runtime attempt:
https://github.com/redone2000/router-recovery-knowledge/blob/codex/ax55-web-recovery-entry-handoff/runtime_attempts/tplink_archer_ax55_official_online_update_2026-05-16.json

4. Structured recovery-entry runtime attempt:
https://github.com/redone2000/router-recovery-knowledge/blob/codex/ax55-web-recovery-entry-handoff/runtime_attempts/tplink_archer_ax55_recovery_entry_observation_2026-05-17.json

5. Full live lab notes:
https://github.com/redone2000/router-recovery-knowledge/blob/codex/ax55-web-recovery-entry-handoff/lab_tests/live_sessions/tplink_archer_ax55_v1_official_baseline_2026-05-15.md

Task:

Apply the AX55 findings to the main app as staged, observation-backed guidance. The app should support the observed Web Recovery entry flow, but must not claim full recovery support.

Observed device scope:

- TP-Link Archer AX55
- Physical label: Archer AX55(CA), Ver: 1.0
- UI hardware version: Archer AX55 v1.0
- Firmware observed: 1.5.11 Build 20251119 rel.49503(4341)

Confirmed facts to integrate:

- Normal admin IP: 192.168.0.1
- Normal DHCP range: 192.168.0.2 - 192.168.0.253
- Mac/client static IP for recovery-page access: 192.168.0.10/24
- Recovery URL: http://192.168.0.1
- Successful recovery entry method: hold Reset while powering on
- Observed powered hold time: about 6 seconds
- LED signal: middle orange LED
- Ping responded around 29 seconds
- Browser opened Firmware Upgrade recovery page
- WPS power-on attempt failed in the tested attempt
- No firmware upload was performed
- TFTP was not observed or tested
- After recovery-page observation without upload, power-cycle return to normal admin UI took about 147 seconds
- Official online update showed that 100% progress is not completion; admin page returned about 3m35s after confirmation

Required app behavior:

- Treat this as support level: recovery_entry_observed
- Add a stop gate before firmware upload
- Do not label page access as recovery success
- Do not default this flow to TFTP
- Do not claim upload acceptance, write success, config retention after recovery upload, or broad AX55 compatibility
- Keep TP-Link FAQ 1482 as series-level background only; the tested facts come from the AX55 owner-lab runtime records

Recommended user-facing copy:

"This AX55 flow has been observed only up to the recovery upload page. Do not treat page access as a completed recovery."

"Set Ethernet to 192.168.0.10/24, connect directly to the router, then enter recovery mode before opening http://192.168.0.1."

"For the observed AX55(CA) v1.0 unit, holding Reset while powering on reached the recovery page. WPS did not work in the tested attempt."

"If the Firmware Upgrade page appears, stop here unless you intentionally want to run a separate official-firmware upload test."

"100% progress is not proof that the router is usable. Keep waiting until the admin page or network returns."

Implementation expectation:

Read the source files, inspect the main app's existing device/profile/workflow model, then implement the smallest safe change that makes this AX55 entry guidance available without overclaiming full recovery. Add tests or fixtures if the app has them. Do not modify unrelated ASUS/NETGEAR behavior.
```

