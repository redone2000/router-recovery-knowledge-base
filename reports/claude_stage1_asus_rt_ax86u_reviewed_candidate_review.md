# Claude Code Stage 1 ASUS RT-AX86U Reviewed-Candidate Evidence Review

Task ID: stage1-asus-rt-ax86u-reviewed-candidate-review
Date: 2026-05-26
Scope: review only, no collection, no profile generation

## 1. Executive Decision

`CANDIDATE_EVIDENCE_ACCEPTED_PROFILE_DRAFT_ALLOWED_AFTER_OWNER_CONFIRMATION`

Summary: The provided owner-lab evidence for ASUS RT-AX86U (hardware v1.0, ASUSWRT-Merlin firmware) is sufficiently complete, consistent, and well-documented to support a reviewed-candidate profile draft after required owner confirmations are obtained. No additional device testing is required at this Stage 1 reference device milestone.

## 2. Evidence Assessment

- source_type judgment: `personal_testing` (all evidence comes from structured owner hands-on lab testing with complete runtime logs, live session notes, and observation records)
- confidence judgment: `medium` (single tested unit, no independent corroboration, but complete successful recovery test with detailed transfer and post-upload observations; aligns with confidence level rules for well-documented single personal testing)
- hardware/firmware scope judgment: Limited exclusively to ASUS RT-AX86U hardware revision 1.0 running official unmodified ASUSWRT-Merlin firmware. No evidence supports applicability to stock ASUSWRT, other hardware revisions, regional variants, or different firmware versions beyond those tested.
- TFTP direction judgment: `passive_tftp_put` is confirmed. Router acts as TFTP server; client sends WRQ/PUT to port 69. No router-initiated TFTP RRQ was observed in passive capture, ruling out active TFTP support in the tested state.
- Web Recovery judgment: Not observed in the tested recovery state. No evidence supports Web Recovery capability for this unit when TTL=100 is present.
- App-guidance readiness: Sufficient to build a guided recovery workflow for this specific unit, with required prominent warnings about generalization limits, post-upload step requirements, and non-guaranteed configuration retention.

## 3. Candidate Field Review

### profile identity / scope

- decision: accept with explicit scope limits
- notes:
  - Profile ID format: `asus-rt-ax86u-1.0-merlin` (follows required vendor-model-hardware-firmware pattern)
  - Core identity fields: Vendor = "ASUS", Model = "RT-AX86U", Hardware version = "1.0"
  - Recovery family = "asus" (aligns with ASUS proprietary recovery enum)
  - Recovery methods = `["tftp_passive"]` (confirmed by successful test)
  - `applies_to_all_firmware_versions = false` (only tested on 3004.388.11 -> 3004.388.10_2 downgrade)
  - Must include explicit scope warning that this profile only applies to the tested hardware/firmware combination.

### button_recovery

- decision: keep observation_only
- notes:
  - `entry_method = "reset_hold_power_on"` (observed)
  - `button_name = "reset"` (observed)
  - `led_indicator = "slow-flashing power LED plus LAN1 activity"` (observed)
  - `press_duration_seconds = null` (exact hold time not recorded in test)
  - `observation_only = true` (behavior only observed on this single unit; no evidence of general applicability across all RT-AX86U units)

### network_recovery

- decision: keep observation_only
- notes:
  - `passive_tftp_from_router = true` (confirmed by successful transfer, no router RRQ observed)
  - `active_tftp_to_router = false` (no RRQ observed in passive capture; no evidence of active TFTP support)
  - `default_ip = "192.168.1.1"` (observed)
  - `default_subnet = "255.255.255.0"` (inferred from client static IP configuration)
  - `client_static_ip = "192.168.1.10"` (observed)
  - `client_static_cidr = "192.168.1.10/24"` (observed)
  - `client_ip_assignment = "static"` (observed)
  - `listen_port = 69` (observed)
  - `required_lan_port = "LAN1"` (tested and worked, but no evidence other ports fail; keep as guidance not strict requirement)
  - `rescue_ping_ttl = 100` (observed strong readiness signal, but not definitive proof of recovery mode)
  - `observation_only = true` (all values observed on single unit only)

### tftp_details

- decision: keep observation_only
- notes:
  - `mode = "octet"` (observed in successful transfer)
  - `filename_required = null` (test used 388102.w, but no evidence other filenames are rejected)
  - `accepted_filename_examples = ["388102.w"]` (observed)
  - `server_uses_ephemeral_port = false` (ACKs observed from port 69 throughout entire transfer)
  - `port_behavior = "fixed_server_port"` (observed)
  - `ack_source_port = 69` (observed)
  - `block_rollover_observed = true` (observed twice during 86.9MB transfer)
  - `client_behavior_requirement = "Follow ACK source port 69 for transfer continuity"` (observed)
  - `observation_only = true` (behavior observed on single unit only)

### firmware_details / firmware_source

- decision: accept with explicit compatibility warnings
- notes:
  - `file_type = ".w"` (observed)
  - `official_format = true` (firmware from official ASUSWRT-Merlin download page)
  - `known_successful_versions = ["3004.388.11 -> 3004.388.10_2 downgrade", "3004.388.10_2 -> 3004.388.11 Web UI upgrade"]` (observed)
  - Firmware source fields:
    - `official_download_page_url = "https://www.asuswrt-merlin.net/download"` (observed)
    - `source_type = "official_vendor_download_page"`
    - `checksum_available = true` (SHA256 listed on download page, though not locally checked in test)
    - `binary_stored = false` (complies with schema requirement to store only metadata)
    - `version_selection_guidance = "Use official ASUSWRT-Merlin firmware explicitly for RT-AX86U hardware v1.0"`
    - `risk_warning = "Do not use stock ASUSWRT firmware or firmware for other RT-AX86U variants with this profile"`
  - `observation_only = true` (firmware compatibility observed on single unit only)

### post_upload_behavior

- decision: keep observation_only
- notes:
  - `wait_seconds = 300` (5 minutes observed before power cycle; no evidence shorter/longer waits work)
  - `power_cycle_required = true` (DHCP/admin UI did not return until after manual power cycle)
  - `dhcp_after_power_cycle = true` (DHCP returned on normal LAN after power cycle)
  - `gateway_ip_as_admin_url = true` (admin UI accessed at DHCP gateway 192.168.50.1 after recovery)
  - `user_warning_after_upload = "Upload completion does not equal recovery success. Wait 5 minutes, then manually power cycle the router. Set your Ethernet adapter back to DHCP after power cycle."`
  - `observation_only = true` (behavior observed on single unit only)

### observed_outcomes

- decision: keep observation_only
- notes:
  - `config_retention_observed = "retained"` (single test outcome; explicitly note no guarantee due to mixed ASUS device behavior)
  - `factory_reset_observed = false` (not observed in this test)
  - `firmware_downgrade_supported = true` (downgrade from 3004.388.11 to 3004.388.10_2 successful)
  - `known_recovery_variants = ["Configuration retained after TFTP recovery (single observation)", "Manual power cycle required after upload"]`
  - `observation_only = true` (outcomes observed on single unit only)

### risk_warnings / known_issues

- decision: accept all required mandatory warnings
- notes: Mandatory warnings to include:
  - This profile is only tested on ASUS RT-AX86U hardware v1.0 running ASUSWRT-Merlin firmware. Compatibility with other variants is not guaranteed.
  - Upload completion does not mean recovery is complete. Wait 5 minutes after upload before power cycling.
  - Manual power cycle is required after upload to restore DHCP and admin UI access.
  - Configuration retention is not guaranteed. Backup your configuration before recovery.
  - Web Recovery is not supported in the tested recovery state.
  - Active TFTP (router pulls firmware) is not supported. Use Passive TFTP PUT only.
  - Use only official ASUSWRT-Merlin firmware for RT-AX86U. Extract the .w file from the zip archive before upload.
  - LAN1 was used for testing, but other LAN ports may also work. Use LAN1 if you encounter issues.

## 4. RT-AC86U Comparison Boundary

- Which RT-AC86U facts may be used only as cautionary comparison:
  - Post-upload behavior similarity (both devices require manual power cycle after a wait period)
  - Mixed configuration retention outcomes (RT-AC86U has shown both retained and reset outcomes, so RT-AX86U configuration retention must not be guaranteed)
  - ASUS recovery family common TFTP behavior (fixed port 69 ACKs, passive PUT operation)
- Which RT-AC86U facts must not be imported into RT-AX86U fields:
  - LAN port requirements (RT-AC86U specifies "LAN1 nearest WAN"; RT-AX86U only tested LAN1, other ports not evaluated)
  - Button hold duration (RT-AC86U has 10-20s hold guidance; RT-AX86U exact hold time not recorded)
  - Firmware filename requirements (RT-AC86U uses "test.w" example; RT-AX86U uses "388102.w" but no evidence of filename enforcement)
  - Recovery applicability to stock firmware (RT-AC86U profile may support stock firmware; RT-AX86U only tested on Merlin)
- Whether mixed RT-AC86U configuration outcomes should affect RT-AX86U copy wording: Yes. RT-AX86U profile and App copy must explicitly state that configuration retention is not guaranteed, even though it was retained in the single RT-AX86U test, because ASUS devices show inconsistent behavior across models and test runs.

## 5. Critical App Guidance

- Should the App show upload completion as only transfer completion? Yes. Explicitly display: "Firmware upload finished. The router may still be writing firmware. Do not unplug power yet."
- Should the App require a post-upload wait before any power action? Yes. Enforce a mandatory 5-minute wait period before allowing the user to proceed to the power cycle step.
- Should the App show a manual power-cycle step, and if so with what wording strength? Yes. Strong mandatory wording: "Now power off the router, wait 10 seconds, then power it on normally. Do not hold the reset button during this process."
- Should the App warn that DHCP/admin may not return until after power cycle? Yes. Explicitly state: "DHCP and admin UI access will not be available until after you manually power cycle the router."
- Should the App warn that configuration retention is not guaranteed? Yes. Show this warning both before recovery starts and after recovery completes.
- Mandatory user-facing warnings:
  1. Pre-recovery: "Backup your configuration before proceeding. Recovery may retain or erase your settings."
  2. Pre-recovery: "This profile is only tested on ASUS RT-AX86U hardware v1.0 running ASUSWRT-Merlin firmware. Use at your own risk on other variants."
  3. Pre-recovery: "Use only official ASUSWRT-Merlin firmware for RT-AX86U. Extract the .w file from the zip archive before upload."
  4. Post-upload: "Upload complete. Wait 5 minutes before power cycling. Do not unplug the router during this time."
  5. Post-wait: "Now manually power cycle the router. DHCP and admin UI will return after boot."
  6. Post-recovery: "Verify your firmware version and configuration after recovery completes."

## 6. Reviewed-Candidate Gate

- can prepare reviewed-candidate draft after Owner confirmation: Yes
- required Owner confirmations:
  1. Confirm all observed facts in the live session and runtime attempt record are accurate.
  2. Confirm the profile scope is limited exclusively to RT-AX86U hardware v1.0 running ASUSWRT-Merlin firmware.
  3. Confirm confidence level "medium" is acceptable for this candidate profile.
  4. Confirm configuration retention is not guaranteed and must be marked as observation-only.
  5. Confirm Web Recovery and Active TFTP are marked as not supported/unknown for this candidate.
  6. Confirm no final profile publication is approved at this Stage 1 milestone.
- fields to modify before any draft:
  - Set `observation_only: true` on all field groups (button_recovery, network_recovery, tftp_details, firmware_details, post_upload_behavior, observed_outcomes).
  - Frame `network_recovery.required_lan_port` as guidance, not a strict requirement.
  - Add explicit note to `observed_outcomes.config_retention_observed` that this is a single-test outcome and not guaranteed.
  - Add all required risk warnings to the profile's `risk_warnings` array.
- fields that must remain unknown/null:
  - `button_recovery.press_duration_seconds` (exact hold time not recorded)
  - `tftp_details.filename_required` (no evidence of filename enforcement)
  - `firmware_version` (only specific versions tested, no general applicability)
- fields that must remain observation-only: All field groups listed above.
- maximum confidence: `medium`
- final-profile publication allowed: No. This candidate requires additional independent testing or cross-verification before final publication approval.

## 7. Schema / Tooling Feedback

- schema changes accepted: None. All observed fields fit within the existing schema v0.1 structure.
- schema changes requested: No changes required for this use case.
- validator changes requested: Add a validation rule that checks if all field groups marked `observation_only` have corresponding prominent warnings in the `risk_warnings` array.
- future export/app-profile implications: The `observation_only` flag must be prominently surfaced in the App UI to prevent users from treating this as a general-purpose profile for all RT-AX86U units. The App should also explicitly display the scope limits (hardware v1.0, Merlin firmware) before allowing the user to start a recovery workflow with this profile.

## 8. Recommendation To Owner

- whether to create an incoming/reviewed-candidate draft: Yes, proceed to create a reviewed-candidate draft profile after obtaining the required owner confirmations listed above.
- whether to keep this as runtime evidence only: No, the evidence is sufficiently strong and well-documented to support a reviewed-candidate draft with appropriate scope limits and warnings.
- whether any more router testing is needed now: No. The current test answers all critical Stage 1 reference device evidence questions. Additional testing (other LAN ports, stock firmware, different filenames) is not required unless product-blocking workflow gaps emerge.
- what Codex should do next: Codex should prepare the reviewed-candidate draft profile following the field decisions outlined in this review, then submit it to the owner for confirmation and review. No further device testing work is needed on RT-AX86U at this stage.

## Safety Confirmation

- no web browsing: Yes
- no new source collection: Yes
- no incoming writes: Yes (this is a review only, no file modifications performed)
- no reviewed writes: Yes
- no final writes: Yes
- no profile approval: Yes (this review only allows draft creation after confirmation, no final profile approval is granted)
