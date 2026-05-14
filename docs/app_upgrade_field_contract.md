# App Upgrade Field Contract

Date: 2026-05-14
Status: Stage 1 implementation contract draft

## Purpose

This document defines how the macOS App should consume recovery knowledge files during the next version upgrade.

It is intentionally module-based. The App should not read profile fields as a flat blob and improvise UI. Each App module should consume a bounded subset of profile fields and produce bounded runtime attempt fields.

## Source Layers

| Layer | File / schema | App role |
| --- | --- | --- |
| Model profile | `schema/recovery_profile.schema.json` | Evidence-backed guidance and default parameters |
| Runtime attempt | `schema/app_runtime_attempt.schema.json` | One local recovery attempt record |
| Incident | `schema/recovery_incident.schema.json` | Exportable success/failure/tacit knowledge candidate |
| Workflow docs | `docs/app_recovery_runtime_workflow.md` | UI flow and state-machine guidance |
| Hygiene defaults | `docs/recovery_hygiene_defaults.md` | Default preparation recommendations when not contradicted by profile evidence |

## App Modules

### 1. Device Selection

Consumes profile fields:

- `id`
- `vendor`
- `model`
- `hardware_version`
- `firmware_version`
- `applies_to_all_firmware_versions`
- `confidence_level`
- `tags`

Writes runtime fields:

- `profile_id`
- `workflow_ids`
- `device.vendor`
- `device.model`
- `device.hardware_version`
- `device.firmware_version_before`

UI rule:

- Show unknown hardware/firmware scope prominently.
- Do not present `unknown` as "all versions".

### 2. Risk And Scope Confirmation

Consumes profile fields:

- `known_issues`
- `risk_warnings`
- `observation_only_groups`
- `source_evidence`
- `review_notes`

Writes runtime fields:

- no dedicated field yet; user acknowledgement can be stored in App state
- future field may be `scope_acknowledged_by_user`

UI rule:

- Observed-only behavior must be labeled as tested-unit behavior.
- Never claim guaranteed recovery, guaranteed config retention, or guaranteed factory reset.

### 3. Firmware Source And Selection

Consumes profile fields:

- `firmware_source.official_download_page_url`
- `firmware_source.official_download_page_region`
- `firmware_source.official_download_page_model`
- `firmware_source.checksum_available`
- `firmware_source.checksum_algorithms`
- `firmware_source.version_selection_guidance`
- `firmware_source.risk_warning`
- `firmware_details.file_type`
- `firmware_details.official_format`

Writes runtime fields:

- `firmware_file.source_type`
- `firmware_file.official_download_page_url`
- `firmware_file.local_path_recorded`
- `firmware_file.filename_recorded`
- `firmware_file.extension`
- `firmware_file.size_bytes`
- `firmware_file.appears_compressed`
- `firmware_file.checksum_algorithm`
- `firmware_file.checksum_status`
- `firmware_file.model_match_confirmed_by_user`

UI rule:

- Store only metadata; do not persist private local paths in shared/exported records.
- Do not store firmware binaries.
- Prefer official support/download pages over direct binary URLs.

### 4. macOS Preflight

Consumes profile fields:

- `network_recovery.client_ip_assignment`
- `network_recovery.client_static_ip`
- `network_recovery.client_static_cidr`
- `network_recovery.default_subnet`
- relevant `known_issues`

Writes runtime fields:

- `macos_preflight.wired_interface_selected`
- `macos_preflight.wifi_disabled_or_warned`
- `macos_preflight.local_network_permission`
- `macos_preflight.file_picker_authorized`
- `macos_preflight.static_ip_set`
- `macos_preflight.client_ip`
- `macos_preflight.client_cidr`

UI rule:

- Treat Local Network permission and file-picker authorization as first-class preflight checks.
- If static IP setup is manual, record whether the user confirmed it.
- Apply recovery hygiene defaults: prefer direct Ethernet, disable or warn about Wi-Fi, disconnect other router cables, and confirm wired interface ownership unless profile evidence says otherwise.

### 5. Physical Setup

Consumes profile fields:

- `network_recovery.required_lan_port`
- `button_recovery.button_name`
- `button_recovery.entry_method`
- `button_recovery.press_duration_seconds_min`
- `button_recovery.press_duration_seconds_max`
- `button_recovery.led_indicator`

Writes runtime fields:

- `recovery_entry.method`
- `recovery_entry.button`
- `recovery_entry.hold_seconds_observed`
- `recovery_entry.lan_port_used`
- `recovery_entry.led_state_observed`
- `recovery_entry.user_confirmed_recovery_mode`

UI rule:

- Use timers and visual confirmations where possible.
- Do not advance automatically based only on elapsed time when LED/state confirmation is required.
- If the profile does not specify a better sequence, recommend powering off for about 10 seconds before holding the recovery button and reconnecting power.
- If the profile does not specify a port, start with LAN1 / the LAN port nearest WAN as a recommended default, not a universal fact.

### 6. Recovery Readiness

Consumes profile fields:

- `network_recovery.default_ip`
- `network_recovery.rescue_ping_ttl`
- `button_recovery.led_indicator`
- `risk_warnings`

Writes runtime fields:

- `readiness_observations.ping_replied`
- `readiness_observations.ttl_observed`
- `readiness_observations.service_probe_attempted`
- `readiness_observations.service_probe_result`
- `readiness_observations.readiness_signal_strength`

UI rule:

- Ping/TTL can support readiness but must not be the sole success/failure signal.
- Service probes should be workflow-specific and conservative.

### 7. Transfer Execution

Consumes profile fields:

- `recovery_methods`
- `network_recovery.passive_tftp_from_router`
- `network_recovery.active_tftp_to_router`
- `network_recovery.listen_port`
- `tftp_details.mode`
- `tftp_details.filename_required`
- `tftp_details.accepted_filename_examples`
- `tftp_details.server_uses_ephemeral_port`
- `tftp_details.port_behavior`
- `tftp_details.client_behavior_requirement`

Writes runtime fields:

- `transfer.method`
- `transfer.started`
- `transfer.completed`
- `transfer.duration_seconds`
- `transfer.bytes_sent`
- `transfer.block_count`
- `transfer.ack_source_port`
- `transfer.server_uses_ephemeral_port_observed`
- `transfer.error_category`
- `transfer.error_message`

UI rule:

- For passive TFTP, the client should follow the server ACK source port.
- If the observed behavior differs from the profile, keep the profile unchanged and record a runtime attempt or incident candidate.

### 8. Error Interpretation

Consumes profile fields:

- `known_issues`
- `risk_warnings`
- linked workflow failure modes
- linked incidents

Writes runtime fields:

- `transfer.error_category`
- `transfer.error_message`
- `outcome.incident_candidate`
- `outcome.incident_reason`

Initial error categories:

- `local_network_permission`
- `wrong_interface_or_ip`
- `recovery_window_missed`
- `firmware_rejected`
- `transfer_timeout`
- `link_interrupted`
- `unknown`

UI rule:

- Failed attempts should not mutate profiles directly.
- Repeated or high-signal failures should become incident candidates.

### 9. Post-Upload Phase

Consumes profile fields:

- `post_upload_behavior.wait_seconds`
- `post_upload_behavior.power_cycle_required`
- `post_upload_behavior.dhcp_after_power_cycle`
- `post_upload_behavior.gateway_ip_as_admin_url`
- `post_upload_behavior.user_warning_after_upload`

Writes runtime fields:

- `post_upload.wait_completed`
- `post_upload.wait_seconds_actual`
- `post_upload.power_cycle_performed`
- `post_upload.dhcp_restored`
- `post_upload.gateway_detected`
- `post_upload.admin_ui_opened`

UI rule:

- Upload completion is not recovery completion.
- If a profile says power cycle is required, the App must present it as an explicit step rather than a troubleshooting footnote.
- If the profile does not specify post-upload behavior, recommend waiting 2-3 minutes before judging failure unless there is a clear device-specific reason not to wait.

### 10. Outcome And Feedback

Consumes profile fields:

- `observed_outcomes.config_retention_observed`
- `observed_outcomes.factory_reset_observed`
- `observed_outcomes.firmware_downgrade_supported`
- `observed_outcomes.known_recovery_variants`
- `risk_warnings`

Writes runtime fields:

- `device.firmware_version_after`
- `outcome.result`
- `outcome.firmware_version_after_observed`
- `outcome.configuration_state`
- `outcome.incident_candidate`
- `outcome.incident_reason`

UI rule:

- Classify the outcome conservatively.
- Do not infer configuration retention or factory reset from transfer success.

### 11. Privacy And Export

Consumes profile fields:

- none required

Writes runtime fields:

- `privacy.local_only_by_default`
- `privacy.user_export_approved`
- `privacy.private_paths_redacted`
- `privacy.serials_redacted`

UI rule:

- Runtime attempts are local/private by default.
- Export requires explicit user approval.
- Private paths and serials must be redacted.

## Reference Device Coverage

| App module | TP-Link AX55 | ASUS RT-AC86U / RT-AX86U direction | NETGEAR RAX40 |
| --- | --- | --- | --- |
| Device selection | queue/reference only | RT-AC86U incoming exists; RT-AX86U separate | reference target only |
| Risk confirmation | pending profile | covered for RT-AC86U | pending |
| Firmware source | needs model-specific official source | covered for RT-AC86U | pending |
| macOS preflight | likely needed | needed and partly observed | likely needed |
| Physical setup | unknown | covered for RT-AC86U | unknown |
| Readiness | unknown | partially covered; ping weak | likely critical |
| Transfer | Web recovery target | passive TFTP covered for RT-AC86U | unresolved; likely orchestration-heavy |
| Error interpretation | pending incidents | initial taxonomy useful | critical |
| Post-upload | unknown | covered for RT-AC86U | unknown |
| Outcome feedback | pending | covered conceptually | pending |
| Privacy/export | generic App requirement | supported by runtime schema | supported by runtime schema |

## Immediate App Upgrade Slice

Recommended first implementation slice:

1. Device/profile selection for RT-AC86U only.
2. Firmware source and local file metadata capture.
3. macOS preflight checklist.
4. Passive TFTP transfer screen with progress and error category.
5. Post-upload wait / power-cycle / DHCP return flow.
6. Runtime attempt JSON export for internal testing.

Do not implement AX55 or RAX40 user-facing flows until their source/lab coverage improves.

For a generated RT-AC86U App-facing draft, see `app_exports/examples/asus_rt_ac86u_app_profile_draft.json`. This export is an implementation aid only and is not final production guidance.

## Stop Lines

- Do not use RT-AC86U fields for RT-AX86U without direct evidence.
- Do not publish R7000 App guidance from the unresolved TFTP incident.
- Do not turn runtime attempts into profile updates without review.
- Do not export local file paths, serial numbers, or private network details without explicit user approval and redaction.
