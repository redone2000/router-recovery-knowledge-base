# HANDOFF

Use this file as the startup context for a new Codex thread working on this repository.

Repository: `/Users/YiYuan/Projects/router-recovery-knowledge`
Last updated: 2026-05-26
Current mode: Stage 1 reference-device evidence and App-upgrade preparation

## Working Principle

This is a Recovery Knowledge System, not a router tutorial dump.

Prioritize:

1. evidence boundaries
2. runtime attempts
3. incidents
4. workflow maturity
5. reviewed profile candidates
6. App-ready exports

Do not prioritize broad model collection.

## Current Completion Summary

The repo has established:

- governance and evidence lifecycle
- schema/tooling for profiles, incidents, workflows, and runtime attempts
- reference-device strategy
- recovery hygiene defaults
- App runtime workflow mapping
- initial profile export path
- source/workflow indexing reviews from OpenClaw and Claude Code
- 2026-05 reference-device evidence batch committed locally
- RT-AX86U reviewed-candidate review prompt prepared
- RT-AX86U Claude Code review report saved
- RT-AX86U reviewed-candidate migration plan prepared, not executed
- Owner confirmed the RT-AX86U 9-item checklist on 2026-05-26
- RT-AX86U incoming candidate draft prepared
- RT-AX86U incoming candidate draft reviewed by Codex and accepted for reviewed-migration request
- Owner approved RT-AX86U reviewed-candidate migration only on 2026-05-26
- RT-AX86U reviewed-candidate copy prepared
- RT-AX86U App-facing implementation draft export generated

Validated on 2026-05-19 before the evidence-batch commit:

```text
python3 tools/validate_runtime_attempts.py runtime_attempts
python3 tools/validate_profiles.py incoming
python3 tools/validate_incidents.py incidents
python3 tools/validate_system_links.py
```

All passed.

## Current Device Gates

### TP-Link Archer AX55

Gate: recovery-entry observed only.

Facts:

- AX55(CA), Ver. 1.0 / UI Archer AX55 v1.0.
- Official Web UI online update succeeded to `1.5.11 Build 20251119 rel.49503(4341)`.
- Recovery page entry observed with Reset-held power-on.
- Recovery page opened at `192.168.0.1` using Mac static `192.168.0.10/24`.
- WPS-held power-on failed in the observed attempt.

Do not claim:

- firmware recovery success
- firmware acceptance
- post-upload behavior
- TFTP direction
- all AX55 variants behave the same

Next useful AX55 task:

- Plan an explicitly approved official firmware upload/acceptance test, or keep it blocked.

### ASUS RT-AC86U

Gate: incoming candidate only.

Facts:

- Lab-observed Rescue Mode and Passive TFTP PUT data exists.
- Incoming profile exists: `incoming/asus-rt-ac86u-unknown-unknown.jsonl`.
- Critical lesson: upload complete is not recovery complete.
- Post-upload wait and manual power-cycle behavior matter.
- Configuration retention is mixed across observations, so do not promise retention or reset.

Do not:

- write final
- raise confidence above medium
- assume all firmware/hardware variants are covered

### ASUS RT-AX86U

Gate: reviewed candidate only, not final.

Facts:

- H/W Ver. 1.0.
- ASUSWRT-Merlin `3004.388.11` baseline.
- Rescue Mode entry observed with Reset-held power-on, LAN1, slow flashing power LED, `TTL=100`.
- Web recovery was not observed.
- Passive TFTP PUT succeeded.
- Router acted as TFTP server; Mac/App acted as TFTP client.
- ACK block 0 came from `192.168.1.1:69`.
- No ephemeral TFTP server port observed.
- Firmware changed from `3004.388.11` to `3004.388.10_2`.
- DHCP/admin did not return until normal power cycle after waiting more than 5 minutes.
- Configuration appeared retained in that one attempt.
- Router was later returned to `3004.388.11` through normal Web UI upgrade.
- Incoming draft exists: `incoming/asus-rt-ax86u-1-0-merlin.jsonl`.
- Reviewed-candidate copy exists: `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`.

Do not:

- merge with RT-AC86U
- generalize to stock ASUSWRT
- promise configuration retention
- treat LAN1/power-cycle/ACK-port behavior as universal
- promote to final profile

Next useful AX86U task:

- Use the RT-AX86U App export as an internal implementation aid, while preserving observation-only warnings.

### NETGEAR R7000

Gate: blocked incident-only.

Facts:

- Official TFTP evidence exists.
- Lab test did not complete successfully.
- `TTL=100` did not guarantee successful TFTP PUT.
- NMRP/nmrpflash context is useful but official NETGEAR NMRP evidence was not found.

Do not:

- move to reviewed
- draft final profile
- treat NMRP as official NETGEAR method

### NETGEAR RAX40v2

Gate: official management/update baseline only.

Facts:

- RAX40v2 official Nighthawk App update succeeded.
- Firmware reached `V1.0.17.142_2.0.100`.
- Browser setup path had stale/404 behavior until official App new-router setup restored local admin UI.
- LAN `192.168.1.1`, DHCP `192.168.1.2` - `192.168.1.254`.

Do not:

- claim Recovery Mode
- claim TFTP
- claim NMRP
- generate profile

## Key Design Decisions

- Model profile = parameterized workflow instance.
- Workflow abstraction comes before long-tail model expansion.
- Runtime attempt records are separate from model profiles.
- Incidents are first-class evidence for failures and tacit knowledge.
- TFTP active/passive direction must be proven by packets, official documentation, or successful tool behavior.
- `TTL=100` is not enough by itself.
- Upload completion is not recovery completion.
- Manual power-cycle guidance must be profile/runtime-evidence based.
- Wi-Fi does not need to be disabled by default; confirm wired route/service ownership instead.
- Hygiene defaults are helpful recommendations, not universal facts.
- `reviewed/` and `final/` are protected; never write `final/`.
- Sensitive data stays out of the repo.

## Current Risks

- RT-AX86U reviewed candidate and App export draft exist, but neither is final.
- AX55 recovery page entry may be overread as recovery success.
- AX86U evidence is strong but still observation-only for many fields.
- RAX40 management recovery could be confused with firmware recovery.
- R7000 remains timing-sensitive and blocked.
- Firmware source/region mismatch remains high risk.
- App copy must not announce success at transfer completion.

## Important Files

Root:

- `PROJECT_STATUS.md`
- `HANDOFF.md`
- `prompts/new_thread_start_prompt.md`

Docs:

- `docs/recovery_knowledge_system_architecture.md`
- `docs/evidence_lifecycle.md`
- `docs/recovery_priority_strategy.md`
- `docs/reference_device_app_upgrade_plan.md`
- `docs/reference_device_lab_test_protocol.md`
- `docs/recovery_hygiene_defaults.md`
- `docs/app_recovery_runtime_workflow.md`
- `docs/app_upgrade_field_contract.md`

Schemas/tools:

- `schema/recovery_profile.schema.json`
- `schema/recovery_incident.schema.json`
- `schema/recovery_workflow.schema.json`
- `schema/app_runtime_attempt.schema.json`
- `tools/validate_runtime_attempts.py`
- `tools/validate_profiles.py`
- `tools/validate_incidents.py`
- `tools/validate_system_links.py`
- `tools/create_runtime_attempt_template.py`
- `tools/create_incident_from_runtime_attempt.py`
- `tools/export_app_profile.py`

Data:

- `incoming/asus-rt-ax86u-1-0-merlin.jsonl`
- `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`
- `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`
- `incoming/asus-rt-ac86u-unknown-unknown.jsonl`
- `incoming/netgear-r7000-unknown-unknown.jsonl`
- `incidents/lab/netgear_r7000_ttl100_tftp_timeout_2026-05-13.json`
- `runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json`
- `app_exports/examples/asus_rt_ac86u_app_profile_draft.json`

Committed 2026-05 reference-device evidence batch:

- `lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`
- `lab_tests/live_sessions/netgear_rax40_official_baseline_2026-05-16.md`
- `lab_tests/live_sessions/tplink_archer_ax55_v1_official_baseline_2026-05-15.md`
- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `runtime_attempts/netgear_rax40v2_official_app_online_update_2026-05-16.json`
- `runtime_attempts/tplink_archer_ax55_official_online_update_2026-05-16.json`
- `runtime_attempts/tplink_archer_ax55_recovery_entry_observation_2026-05-17.json`
- `reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md`
- `reports/asus_rt_ax86u_profile_candidate_guardrails_2026-05-17.md`
- `reports/tplink_archer_ax55_recovery_entry_observation_summary_2026-05-17.md`
- `reports/app_copy_upload_complete_vs_recovery_complete_2026-05-17.md`

Prepared review prompt:

- `prompts/agent_tasks/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`

Completed review and plan:

- `reports/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`
- `reports/asus_rt_ax86u_reviewed_candidate_migration_plan.md`
- `reports/codex_asus_rt_ax86u_incoming_draft_review_2026-05-26.md`
- `reports/asus_rt_ax86u_app_export_readiness_2026-05-26.md`

## Recommended Next Step

Use the RT-AX86U App export as the next App integration input:

- `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`
- `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`
- `reports/asus_rt_ax86u_app_export_readiness_2026-05-26.md`
- `docs/app_recovery_runtime_workflow.md`
- `docs/app_upgrade_field_contract.md`

Do not write `final/`. Do not remove observation-only warnings. Do not treat the export as production guidance.

Do not start new model expansion.

## New Session Prompt

Use this prompt to start a new Codex thread:

```text
You are working in /Users/YiYuan/Projects/router-recovery-knowledge.

Read AGENTS.md, PROJECT_STATUS.md, and HANDOFF.md first. Then inspect git status.

Goal: continue the router recovery knowledge project from Stage 1 reference-device evidence and App-upgrade preparation. Do not broaden into long-tail model collection.

Current priorities:
1. Protect evidence boundaries.
2. Use the RT-AX86U App export as internal App integration input only.
3. Keep AX55 at recovery-entry observed until firmware upload is explicitly approved.
4. Treat ASUS RT-AX86U as reviewed candidate only, not final.
5. Keep R7000 blocked as incident-only.
6. Treat RAX40v2 as official management/update baseline only, not recovery proof.

Before editing, run or inspect:
- git status --short
- python3 tools/validate_runtime_attempts.py runtime_attempts
- python3 tools/validate_profiles.py incoming
- python3 tools/validate_incidents.py incidents
- python3 tools/validate_system_links.py

Important rules:
- Never write final/.
- Do not write reviewed/ unless Owner explicitly approves the specific promotion.
- Do not infer TFTP direction.
- Do not treat ping/TTL as proof.
- Do not label upload completion as recovery success.
- Do not commit secrets, local paths, serials, MACs, Wi-Fi passwords, admin passwords, firmware binaries, or router backups.
- Keep runtime attempts, incidents, workflow evidence, and model profiles separate.

Recommended first task:
Use app_exports/examples/asus_rt_ax86u_app_profile_draft.json as internal App integration input, preserving observation-only warnings and upload-complete-vs-recovery-complete copy. Do not write final/.
```
