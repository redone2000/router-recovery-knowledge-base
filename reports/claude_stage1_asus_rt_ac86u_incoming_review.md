# Claude Code Stage 1 ASUS RT-AC86U Incoming Draft Review

Task ID: stage1-asus-rt-ac86u-incoming-review
Date: 2026-05-13
Scope: review only, no collection, no profile generation

## 1. Executive Decision

- `INCOMING_ACCEPTED_REVIEWED_CANDIDATE_ALLOWED_AFTER_OWNER_CONFIRMATION`
- Summary: This incoming draft is based on verified first-party Owner lab observation, all fields are fully supported by recorded test data, and schema extensions are appropriate for App guidance needs. Hardware and firmware applicability scope remain unknown, so the draft is eligible for reviewed-candidate status only after explicit Owner confirmation of observation accuracy.

## 2. Evidence Assessment

- source type judgment: `personal_testing` is acceptable as a valid source type for incoming drafts, especially for first-party Owner-provided lab observation with detailed, repeatable test records.
- confidence judgment: `confidence_level: medium` is appropriate. The evidence is high-quality first-party testing, but unknown hardware/firmware scope prevents raising to high, and the consistent, documented observations do not require lowering to low.
- hardware/firmware scope judgment: Explicitly setting these fields to unknown is correct and compliant with rules. Unknown scope does not require a confidence downgrade as long as the limitation is clearly documented in risk warnings.
- TFTP direction judgment: `tftp_passive` is fully justified by observation. The router acts as a TFTP server listening on port 69, and the user runs a TFTP client to upload firmware, which matches the definition of passive TFTP mode.
- app-guidance readiness: Mostly ready for App use with mandatory limitation warnings. The post-upload power-cycle requirement is a critical App guidance field that is well-documented.

## 3. Field-by-Field Review

### button_recovery

- decision: accept
- notes: All fields are supported by observation. The min/max press duration and LED indicator description match recorded test results. The entry method is correctly documented.

### network_recovery

- decision: accept
- notes: All IP addressing, port, required LAN port, and TTL values are directly observed in testing. TFTP direction fields are correctly set based on observed behavior.

### tftp_details

- decision: accept
- notes: Mode, filename requirement, ephemeral port behavior, and block rollover observations are all documented in test records. The `filename_required: false` and `server_uses_ephemeral_port: false` values are correct for the observed test units; no generalization beyond observed behavior is claimed.

### firmware_details

- decision: accept
- notes: `.w` official format, supported versions, and downgrade capability are all directly observed in testing.

### post_upload_behavior

- decision: accept (critical guidance field)
- notes: All fields including 180s wait time, mandatory power cycle, DHCP switching requirement, and gateway IP guidance are fully supported by test observations. `power_cycle_required: true` is a critical safety and guidance field that must be retained prominently.

### observed_outcomes

- decision: accept
- notes: `config_retention_observed: "mixed"` accurately reflects both retained and factory-reset outcomes observed in testing. Downgrade support and known recovery variants are correctly documented.

### risk_warnings / known_issues

- decision: accept
- notes: All warnings are accurate, complete, and appropriately highlight the limitations of the observed behavior: unknown hardware/firmware scope, mixed configuration outcomes, power cycle requirement, and ping unreliability.

## 4. Critical App Guidance

- Should the App show the post-upload wait and manual power-cycle instruction? Yes, this is mandatory guidance. Upload completion is not recovery completion.
- Should the App warn that ping and previous LAN IP are not reliable failure signals? Yes, this is mandatory to prevent user misjudgment of recovery status.
- Should the App warn that configuration may be retained or reset? Yes, this is mandatory to manage user expectations and encourage pre-recovery configuration backup.
- Mandatory user-facing warnings:
  - Upload completion does not mean recovery is complete; wait 3 minutes before proceeding.
  - Manual power cycle is required after the wait period.
  - Configuration may be retained or factory-reset; both outcomes are possible.
  - Do not judge recovery success/failure solely by ping response or previous LAN IP reachability.

## 5. Reviewed-Candidate Gate

- can move to reviewed candidate after Owner confirmation: Yes
- required Owner confirmations:
  - Confirmation that all lab observations are accurate and repeatable for the tested hardware unit.
  - Confirmation that `confidence_level: medium` is acceptable given unknown hardware/firmware scope.
  - Confirmation that the draft may be marked as applicable only to tested units until broader scope is verified.
- fields to modify before migration: No mandatory modifications; all fields are currently accurate.
- fields that must remain unknown: `hardware_version: "unknown"`, `firmware_version: "unknown"`, `applies_to_all_firmware_versions: null`
- maximum confidence: medium

## 6. Schema / Tooling Feedback

- schema changes accepted: All new grouped fields and extensions to `network_recovery` / `button_recovery` are appropriate and should be retained.
- schema changes requested: Add optional `observation_only` boolean flag to field groups that contain only observed behavior.
- validator changes requested:
  - `source_type: personal_testing` profiles may not have `confidence_level` higher than medium.
  - Profiles with `hardware_version: "unknown"` or `firmware_version: "unknown"` must have corresponding entries in `known_issues` and `risk_warnings`.
  - Profiles with `post_upload_behavior.power_cycle_required: true` must include prominent user warnings.
- future export/app-profile implications: When exporting to App profiles, fields marked as observation-only must be clearly labeled as observed behavior for tested units and not generalized to all variants.

## 7. Recommendation To Owner

- Keep this incoming draft: It is high-quality, well-documented first-party data that provides valuable guidance for RT-AC86U users.
- Revisions needed: No field revisions are required; all content is accurate as recorded.
- Reviewed-candidate migration: Allow migration to reviewed-candidate status only after explicit Owner confirmation that all observations are accurate and the limitation warnings are acceptable.
- Codex next steps: Wait for Owner confirmation, then migrate to reviewed candidate if approved. No further profile changes are needed at this stage. Continue collecting data on RT-AC86U hardware/firmware applicability to improve confidence level over time.

## Safety Confirmation

- no web browsing: yes
- no new source collection: yes
- no incoming writes: yes
- no reviewed writes: yes
- no final writes: yes
- no profile approval: yes
