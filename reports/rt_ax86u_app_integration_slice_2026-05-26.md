# RT-AX86U App Integration Slice

Date: 2026-05-26
Status: implementation slice spec, not App code

## Decision

Use the reviewed RT-AX86U App export as the first App integration slice input.

Source export:

```text
app_exports/examples/asus_rt_ax86u_app_profile_draft.json
```

This export is an implementation aid only:

- `production_allowed=false`
- `final_allowed=false`
- `review_required=true`
- source profile status is `reviewed`, not `final`

Do not present this as general RT-AX86U production guidance.

## Product Goal

Build a guided App flow that proves the runtime architecture can consume a reviewed candidate without flattening or losing evidence boundaries.

The goal is not to support more models.

## Minimum Flow

### 1. Device Selection

Use:

- `device_selection.profile_id`
- `device_selection.vendor`
- `device_selection.model`
- `device_selection.hardware_version`
- `device_selection.firmware_version`
- `device_selection.confidence_level`
- `export_metadata.source_profile_status`

Required UI behavior:

- Show `RT-AX86U` and `H/W Ver. 1.0`.
- Show firmware scope as unknown / tested evidence only, not all firmware.
- Show reviewed-candidate status, not final status.

Stop line:

- Do not show "officially supported" or "final".

### 2. Risk And Scope Confirmation

Use:

- `risk_and_scope.known_issues`
- `risk_and_scope.risk_warnings`
- `risk_and_scope.observation_only_groups`
- `risk_and_scope.review_notes`

Required UI behavior:

- User must acknowledge scope before recovery starts.
- Observation-only groups must remain visible as tested-unit behavior.

Mandatory warnings:

- Upload completion is not recovery completion.
- Configuration retention is not guaranteed.
- Stock ASUSWRT behavior is unknown.
- Other hardware revisions, regions, and firmware variants are unknown.
- Active TFTP is not supported by this evidence.
- Web Recovery was not observed in the tested state.

### 3. Firmware Preparation

Use:

- `firmware_preparation.official_download_page_url`
- `firmware_preparation.official_download_page_model`
- `firmware_preparation.file_type`
- `firmware_preparation.checksum_available`
- `firmware_preparation.checksum_algorithms`
- `firmware_preparation.version_selection_guidance`
- `firmware_preparation.risk_warning`
- `firmware_preparation.binary_stored`

Required UI behavior:

- Direct user to official ASUSWRT-Merlin download page.
- Require model-match confirmation for RT-AX86U.
- Require extracted `.w` firmware image.
- Store filename/extension/size/checksum status in runtime attempt only.
- Never persist local firmware path in shared/exported records.

Stop line:

- Do not store firmware binaries or private local paths.

### 4. macOS Preflight

Use:

- `macos_preflight.client_ip_assignment`
- `macos_preflight.client_static_ip`
- `macos_preflight.client_static_cidr`
- `macos_preflight.default_subnet`
- `macos_preflight.local_network_permission_warning`
- `macos_preflight.file_picker_required`
- `macos_preflight.wired_interface_required`
- `macos_preflight.wired_service_priority_or_route_check_required`

Runtime fields to capture:

- `macos_preflight.wired_interface_selected`
- `macos_preflight.wifi_available_during_recovery`
- `macos_preflight.wired_route_confirmed`
- `macos_preflight.local_network_permission`
- `macos_preflight.file_picker_authorized`
- `macos_preflight.static_ip_set`
- `macos_preflight.client_ip`
- `macos_preflight.client_cidr`

Required UI behavior:

- Confirm wired Ethernet interface before transfer.
- Confirm static IP `192.168.1.10/24`.
- Confirm wired route ownership before sending TFTP.
- Treat Local Network permission denial as a first-class error path.

### 5. Recovery Entry And Readiness

Use:

- `physical_setup.required_lan_port`
- `physical_setup.button_name`
- `physical_setup.entry_method`
- `physical_setup.led_indicator`
- `readiness.recovery_ip`
- `readiness.expected_ttl`
- `readiness.ping_signal_strength`
- `readiness.readiness_warning`

Required UI behavior:

- Guide Reset-held power-on.
- Recommend LAN1 as observed guidance, not a universal requirement.
- Treat TTL=100 as a supporting readiness signal only.
- Require at least LED/context plus network signal before transfer.

Stop line:

- Do not label ping or TTL alone as recovery success.

### 6. Transfer Execution

Use:

- `transfer.recovery_methods`
- `transfer.passive_tftp_from_router`
- `transfer.active_tftp_to_router`
- `transfer.listen_port`
- `transfer.tftp_mode`
- `transfer.filename_required`
- `transfer.accepted_filename_examples`
- `transfer.server_uses_ephemeral_port`
- `transfer.port_behavior`
- `transfer.ack_source_port`
- `transfer.client_behavior_requirement`

Runtime fields to capture:

- `transfer.method`
- `transfer.tftp_direction`
- `transfer.mac_role`
- `transfer.router_role`
- `transfer.started`
- `transfer.completed`
- `transfer.duration_seconds`
- `transfer.bytes_sent`
- `transfer.block_count`
- `transfer.ack_source_port`
- `transfer.server_uses_ephemeral_port_observed`
- `transfer.error_category`
- `transfer.error_message`

Required UI behavior:

- Use Passive TFTP PUT only.
- Mac/App role is TFTP client.
- Router role is TFTP server.
- Send WRQ/PUT to `192.168.1.1:69`.
- Follow the server ACK source port.

Stop line:

- Do not implement router-pulls-firmware / active TFTP for this profile.

### 7. Post-Upload Phase

Use:

- `post_upload.wait_seconds`
- `post_upload.power_cycle_required`
- `post_upload.dhcp_after_power_cycle`
- `post_upload.gateway_ip_as_admin_url`
- `post_upload.user_warning_after_upload`

Required UI behavior:

- Transfer completion must lead to `transfer_complete`, not `recovery_success`.
- Show a post-upload wait state.
- After wait, guide normal power cycle if the user continues.
- Then guide Mac Ethernet back to DHCP.
- Use detected DHCP gateway as admin URL.

Required copy:

```text
Firmware upload finished, but recovery is not complete.
Wait several minutes before any power action.
```

Stop line:

- Do not power-cycle immediately at transfer completion.

### 8. Outcome And Attempt Export

Use:

- `outcome_guidance.config_retention_observed`
- `outcome_guidance.do_not_infer_config_state_from_transfer_success`
- `runtime_attempt_mapping.schema`
- `runtime_attempt_mapping.local_only_by_default`
- `runtime_attempt_mapping.private_paths_redacted`
- `runtime_attempt_mapping.serials_redacted`

Required UI behavior:

- Ask user to verify firmware version in admin UI.
- Ask user to check LAN/DHCP, Wi-Fi, WAN, and add-ons.
- Record configuration state as observed by user, not inferred.
- Runtime attempt stays local/private unless user explicitly exports it.

Stop line:

- Do not claim retained configuration as guaranteed.

## Minimum Acceptance Criteria

The App integration slice is acceptable when:

1. It can load `asus_rt_ax86u_app_profile_draft.json`.
2. It refuses to treat the profile as final.
3. It displays all risk warnings or a complete user-acknowledged summary.
4. It captures runtime fields required by `schema/app_runtime_attempt.schema.json`.
5. It preserves upload-complete vs recovery-complete state separation.
6. It records post-upload wait, power cycle, DHCP return, admin UI check, and firmware verification separately.
7. It can export a redacted runtime attempt JSON that passes `tools/validate_runtime_attempts.py`.
8. It does not write or modify model profiles from runtime results.

## Not In Scope

- AX55 user-facing recovery flow.
- RAX40/R7000 recovery flow.
- `final/` profile publication.
- Automatic firmware download.
- Storing firmware binary or local path.
- Promising configuration retention.
- Generalizing RT-AX86U behavior to stock ASUSWRT or other hardware revisions.

## Next Implementation Input

Use this file plus:

- `app_exports/examples/asus_rt_ax86u_app_profile_draft.json`
- `schema/app_runtime_attempt.schema.json`
- `docs/app_upgrade_field_contract.md`
- `docs/app_recovery_runtime_workflow.md`
