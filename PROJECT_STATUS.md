# Project Status

Last updated: 2026-05-26
Owner timezone: Asia/Shanghai
Repository: `/Users/YiYuan/Projects/router-recovery-knowledge`

## Current Stage

The project is in Stage 1: reference-device evidence and App-upgrade preparation.

The active goal is no longer to collect as many router profiles as possible. The current goal is to build a reliable Recovery Knowledge System that can support the macOS App with evidence-bound workflows, runtime attempt records, incidents, and reviewed profile candidates.

Model expansion remains paused. Work should focus on the three reference directions:

| Priority | Reference direction | Current status |
| --- | --- | --- |
| 1 | TP-Link Archer AX55 | Official baseline and recovery-entry observation exist. Firmware upload recovery is not tested. |
| 2 | ASUS RT-AC86U / RT-AX86U | RT-AC86U incoming draft exists. RT-AX86U reviewed candidate, App export draft, and App integration slice spec exist; final remains prohibited. |
| 3 | NETGEAR RAX40 / RAX40v2 | Official App/Web management baseline exists. Recovery method remains research-only. R7000 remains blocked incident context. |

## Completed Work

### Governance and Evidence System

- Stage 0 schema governance was established.
- Evidence lifecycle is defined: source -> incident -> pattern -> workflow -> incoming -> reviewed -> final.
- Source scope rules are in place: brand/series/workflow-level evidence cannot generate model profiles without model-specific validation.
- `reviewed/` and `final/` are protected gates. `final/` must not be written by agents.
- Runtime observations are separated from model profiles.
- Incidents preserve failed, ambiguous, or timing-sensitive observations without polluting profiles.

### Schemas and Tooling

Implemented or extended:

- `schema/recovery_profile.schema.json`
- `schema/recovery_incident.schema.json`
- `schema/recovery_workflow.schema.json`
- `schema/app_runtime_attempt.schema.json`
- `schema/model_hypothesis.schema.json`
- `tools/validate_profiles.py`
- `tools/validate_incidents.py`
- `tools/validate_workflows.py`
- `tools/validate_runtime_attempts.py`
- `tools/validate_model_hypotheses.py`
- `tools/validate_system_links.py`
- `tools/create_runtime_attempt_template.py`
- `tools/create_incident_from_runtime_attempt.py`
- `tools/export_app_profile.py`
- `tools/report_system_status.py`

Latest validation results on 2026-05-19:

```text
python3 tools/validate_runtime_attempts.py runtime_attempts
Checked 8 runtime attempt file(s).
No validation issues found.

python3 tools/validate_profiles.py incoming
Checked 2 JSONL records across 2 file(s).
No validation issues found.

python3 tools/validate_incidents.py incidents
Checked 1 incident file(s).
No incident validation issues found.

python3 tools/validate_system_links.py
Checked 2 profile(s), 1 incident(s), 3 workflow(s).
No system link validation issues found.
```

### Workflow and Architecture Docs

Important design docs are in place:

- `docs/recovery_knowledge_system_architecture.md`
- `docs/recovery_language.md`
- `docs/evidence_lifecycle.md`
- `docs/recovery_priority_strategy.md`
- `docs/reference_device_validation_process.md`
- `docs/reference_device_app_upgrade_plan.md`
- `docs/reference_device_lab_test_protocol.md`
- `docs/app_recovery_runtime_workflow.md`
- `docs/app_upgrade_field_contract.md`
- `docs/recovery_hygiene_defaults.md`

### AI-Assisted Model Expansion

The repository now has a separate `model_hypotheses/` layer for outward model expansion.

Purpose:

- let AI agents collect candidate model evidence and workflow hypotheses
- preserve missing-proof lists before any profile drafting
- prevent AI-generated breadth from polluting `incoming/`, `reviewed/`, or `final/`

Current queue:

- `model_hypotheses/asus-expansion-seeds.jsonl`
- `model_hypotheses/tplink-expansion-seeds.jsonl`
- `model_hypotheses/netgear-expansion-seeds.jsonl`

Current notable states:

- ASUS RT-AX86U Pro has official source evidence indexed, but remains insufficient for `incoming/` because TFTP direction, recovery IP, post-upload behavior, hardware revision scope, and firmware scope remain unproven.
- ASUS RT-AC86U mirrors the existing incoming profile evidence and remains Owner-gated for any reviewed migration.
- NETGEAR R7000 remains blocked.
- Other added candidates remain research seeds with `suspected_workflows=["unknown"]`.

Tooling and prompts:

- `schema/model_hypothesis.schema.json`
- `tools/validate_model_hypotheses.py`
- `prompts/agent_tasks/claude_stage1_model_hypothesis_expansion_review.md`
- `reports/claude_stage1_model_hypothesis_expansion_review_2026-05-26.md`
- `reports/asus_rt_ax86u_pro_source_probe_2026-05-26.md`

### Latest Local Commits

- `4bfe41c Add 2026-05 reference device evidence batch`
- `1c108f2 Add RT-AX86U candidate review prompt`
- `5d93b4d Update handoff for RT-AX86U review step`

These commits were pushed to `origin/main` on 2026-05-26.

### Reference Device Work

#### TP-Link Archer AX55

Current status: recovery-entry observed, no recovery upload success yet.

Evidence recorded:

- Official normal baseline exists.
- Device observed as Archer AX55(CA), Ver 1.0 / UI hardware Archer AX55 v1.0.
- Official Web UI online update succeeded from `1.3.1 Build 20240129 rel.57815(4341)` to `1.5.11 Build 20251119 rel.49503(4341)`.
- Admin returned at `192.168.0.1`.
- DHCP remained enabled: `192.168.0.2` - `192.168.0.253`.
- Recovery entry observation succeeded with Reset-held power-on.
- WPS-held power-on did not enter recovery in the observed attempt.
- Recovery page opened at `http://192.168.0.1`.
- Mac static IP used: `192.168.0.10/24`.
- No firmware was uploaded in the recovery-entry observation.

Boundary:

- This proves recovery-page entry for the tested AX55(CA) v1.0 unit.
- It does not prove firmware acceptance, write success, post-upload behavior, TFTP direction, or broader AX55 applicability.

#### ASUS RT-AC86U

Current status: incoming draft exists, reviewed/final not approved.

Evidence:

- Owner-lab observations support Rescue Mode and Passive TFTP PUT for the tested unit.
- Critical post-upload behavior was observed: upload completion is not recovery completion; wait and manual power-cycle behavior matters.
- Configuration retention was mixed across attempts, so App/profile language must not promise retained or reset configuration.

Boundary:

- `incoming/asus-rt-ac86u-unknown-unknown.jsonl` remains incoming only.
- Firmware/hardware applicability remains unknown.
- Confidence cannot exceed medium without broader scope evidence.

#### ASUS RT-AX86U

Current status: reviewed candidate, App-facing draft export, and App integration slice spec exist. None are final.

Evidence recorded:

- Official baseline captured for RT-AX86U H/W Ver. 1.0.
- Firmware family: ASUSWRT-Merlin, official/unmodified per owner.
- Baseline firmware: `3004.388.11`.
- Rescue Mode entry observed with Reset-held power-on, LAN1, slow-flashing power LED, and `TTL=100` at `192.168.1.1`.
- Web recovery page was not observed during `TTL=100`.
- Passive capture with no transfer showed no router-initiated TFTP RRQ.
- Passive TFTP PUT succeeded with Mac/App as TFTP client and router as TFTP server.
- WRQ attempt #1 was accepted immediately.
- ACK block 0 came from `192.168.1.1:69`; no ephemeral server port was observed.
- Firmware image `388102.w`, size `86,900,756` bytes, transferred in about 40 seconds.
- Firmware changed from `3004.388.11` to `3004.388.10_2`.
- After upload and more than 5 minutes of waiting, DHCP did not return until normal power cycle.
- After power cycle, DHCP/admin returned at `192.168.50.1`.
- Configuration appeared retained in this single attempt.
- Device was later returned to `3004.388.11` through normal Web UI upgrade.

Boundary:

- This is not final profile evidence yet.
- RT-AX86U and RT-AC86U must not be merged.
- LAN1 requirement, ACK port behavior, power-cycle requirement, and configuration retention are observation-only until reviewed.
- Incoming draft: `incoming/asus-rt-ax86u-1-0-merlin.jsonl`.
- Reviewed candidate: `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`.
- App export draft: `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`.
- App integration slice: `reports/rt_ax86u_app_integration_slice_2026-05-26.md`.
- App project prompt: `prompts/router_recovery_app_rt_ax86u_integration_prompt.md`.
- Prepared prompt: `prompts/agent_tasks/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`.
- Review report: `reports/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`.
- Migration plan: `reports/asus_rt_ax86u_reviewed_candidate_migration_plan.md`.
- Codex draft review: `reports/codex_asus_rt_ax86u_incoming_draft_review_2026-05-26.md`.

#### NETGEAR R7000

Current status: blocked, incident-only.

Evidence:

- Official TFTP sources exist, including macOS TFTP guidance.
- Owner test did not successfully complete R7000 TFTP recovery.
- Incident records `TTL=100` visibility with TFTP PUT timeout and easier success through nmrpflash context.

Boundary:

- R7000 must not move to reviewed or final.
- Treat as timing-sensitive incident and NETGEAR orchestration research.

#### NETGEAR RAX40v2

Current status: official baseline and App/Web management restoration observations exist. Recovery is not validated.

Evidence recorded:

- Device observed as RAX40v2.
- Official Nighthawk App online update succeeded from `1.0.2.82` to `1.0.17.142`.
- Browser setup path initially showed stale/404 behavior.
- Official App "set up a new router" flow restored browser local admin UI.
- Final browser admin firmware shown as `V1.0.17.142_2.0.100`.
- LAN IP: `192.168.1.1`.
- DHCP range: `192.168.1.2` - `192.168.1.254`.
- Backup/export option exists and a private backup was saved.

Boundary:

- This is official management/update baseline, not Recovery Mode, Web Recovery, TFTP, or NMRP proof.

## Key Design Decisions

1. Model profile is a parameterized workflow instance, not the primary unit of knowledge production.
2. Workflow and incident layers must mature before long-tail model expansion.
3. Evidence must preserve scope: cross-brand, brand, series, model, hardware version, firmware version, and observation-only are separate.
4. TFTP direction must be explicit. Do not infer active/passive from brand or model.
5. Runtime attempt data belongs in `runtime_attempts/`, not directly in profile fields.
6. Failed or ambiguous tests are valuable incidents, not wasted work.
7. Upload complete is not recovery complete.
8. Ping/TTL is a supporting signal, not proof of recovery readiness or completion.
9. Configuration retention must not be promised unless specifically verified and scoped.
10. Firmware binaries, local paths, serial numbers, MAC addresses, admin passwords, Wi-Fi passwords, and backups stay private/local.
11. Wi-Fi does not have to be disabled by default because the App may rely on network access; instead confirm wired route/service priority.
12. Recovery hygiene defaults are recommendations, not universal facts. Profile evidence overrides them.

## Remaining Tasks

### Near-Term

- Communicate RT-AX86U App integration through `prompts/router_recovery_app_rt_ax86u_integration_prompt.md`; do not directly modify the App project from this knowledge-system thread.
- Keep the RT-AX86U App integration slice as future-build input only while the App project is in App Review waiting mode.
- Use `model_hypotheses/` for AI-assisted outward model expansion; do not generate `incoming/` profiles directly from AI research.
- Run `python3 tools/validate_model_hypotheses.py model_hypotheses` whenever hypothesis records change.
- Do not write `final/` without explicit Owner approval.
- Keep AX55 at recovery-entry observed until an explicit firmware upload/acceptance test is approved.
- Keep RAX40 at official baseline until a recovery-specific test is planned.
- Keep R7000 blocked.
- Update App copy and implementation model to include the upload-complete vs recovery-complete state split.
- Fix any POC App wording that still hardcodes `R7000` in generic TFTP flows.

### Before Next Live Tests

- Reconfirm official firmware source, hardware version, region, file extension, and checksum availability.
- Confirm configuration backup exists and remains private.
- Start from the reference device lab protocol.
- Record wired interface, wired route ownership, static IP, LED timing, ping/TTL, service response, transfer behavior, post-upload wait, DHCP return, admin UI, firmware version, and configuration state.
- Use runtime attempt templates first; create incidents for failures or timing ambiguity.

### Later

- Build App integration around a small reference-device slice.
- Generate App-ready profile exports only from reviewed candidates.
- Add stronger cross-validation for observed-only groups and blocked gates.
- Consider NMRP workflow only after stronger evidence or lab success exists.
- Resume official source indexing only when a specific workflow gap is defined.

## Risks

- RT-AX86U reviewed candidate, App export draft, and App integration slice exist, but none are final.
- AX86U evidence is strong but disruptive-device testing should stop unless a product-blocking question remains.
- AX55 recovery entry could be mistaken for recovery success; no upload was performed.
- RAX40 normal App/Web recovery of management access could be mistaken for router firmware recovery; it is not.
- R7000 has tempting official TFTP evidence but unresolved timing behavior; promoting it would pollute profiles.
- Hygiene defaults can become folklore if phrased as universal facts.
- App copy must not label transfer completion as success.
- Firmware source handling remains high risk because wrong region/hardware firmware can damage devices or void warranty.

## Important Files

### Root / Handoff

- `PROJECT_STATUS.md`
- `HANDOFF.md`
- `prompts/new_thread_start_prompt.md`

### Docs

- `docs/recovery_knowledge_system_architecture.md`
- `docs/recovery_language.md`
- `docs/evidence_lifecycle.md`
- `docs/recovery_priority_strategy.md`
- `docs/reference_device_app_upgrade_plan.md`
- `docs/reference_device_lab_test_protocol.md`
- `docs/recovery_hygiene_defaults.md`
- `docs/app_recovery_runtime_workflow.md`
- `docs/app_upgrade_field_contract.md`

### Schemas and Tools

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

### Current Data

- `incoming/asus-rt-ax86u-1-0-merlin.jsonl`
- `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`
- `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`
- `incoming/asus-rt-ac86u-unknown-unknown.jsonl`
- `incoming/netgear-r7000-unknown-unknown.jsonl`
- `incidents/lab/netgear_r7000_ttl100_tftp_timeout_2026-05-13.json`
- `runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json`
- `app_exports/examples/asus_rt_ac86u_app_profile_draft.json`

### Committed 2026-05 Reference-Device Evidence Batch

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

### Prepared External Review Prompt

- `prompts/agent_tasks/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`

### Completed External Review And Plan

- `reports/claude_stage1_asus_rt_ax86u_reviewed_candidate_review.md`
- `reports/asus_rt_ax86u_reviewed_candidate_migration_plan.md`

## Recommended Next Step

Use this App integration slice as the next App implementation input:

```text
reports/rt_ax86u_app_integration_slice_2026-05-26.md
```

Recommended sequence:

1. Load `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`.
2. Keep `production_allowed=false` and `final_allowed=false`.
3. Preserve observation-only warnings in App UI.
4. Preserve upload-complete-vs-recovery-complete copy in the post-upload flow.
5. Do not write `final/`.
6. Keep AX55, RAX40, and R7000 blocked at their current evidence gates until the next planned lab tests.
