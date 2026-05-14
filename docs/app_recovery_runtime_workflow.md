# App Recovery Runtime Workflow

Date: 2026-05-14
Status: Stage 1 design draft

## Purpose

This document maps recovery knowledge profiles to the steps a macOS App must guide during a real router recovery attempt.

The App runtime workflow is not the same as a recovery profile:

- profile data stores evidence-backed model parameters
- source evidence stores where those parameters came from
- runtime state stores what the user and App observe during one live attempt

Do not put runtime-only data, such as a user's selected local firmware path or current network interface state, into model profiles.

## Runtime Step Map

| Step | App user action or state | Profile / knowledge fields | Runtime-only state | Current RT-AC86U coverage |
| --- | --- | --- | --- | --- |
| 1 | Select device | `vendor`, `model`, `hardware_version`, `firmware_version`, `device_type` | selected profile ID | Covered, but hardware/firmware scope remains `unknown` |
| 2 | Read scope and risk warnings | `confidence_level`, `known_issues`, `risk_warnings`, `observation_only_groups` | user acknowledgement | Covered |
| 3 | Get firmware from official source | `firmware_source`, `firmware_details.file_type`, `firmware_details.official_format` | browser/open action, selected local file | Covered after firmware-source update |
| 4 | Validate selected firmware file | `firmware_details.file_type`, `firmware_source.checksum_available`, `firmware_source.checksum_algorithms` | selected file name, extension, size, checksum result | Partially covered; runtime validation model still needed |
| 5 | Prepare Mac networking | `network_recovery.client_ip_assignment`, `client_static_ip`, `client_static_cidr`, `default_subnet` | selected Ethernet interface, current Wi-Fi state, current IP config | Profile covered; runtime preflight still needed |
| 6 | Prepare app permissions | `known_issues`, source notes | Local Network permission, file picker access, sandbox entitlement state | Partially covered in notes only |
| 7 | Connect cable / choose port | `network_recovery.required_lan_port` | link-up state, interface carrier state | Covered for RT-AC86U observed unit |
| 8 | Enter recovery mode | `button_recovery.entry_method`, hold-time fields, LED indicator | user timer, observed LED state | Covered |
| 9 | Detect recovery readiness | `network_recovery.default_ip`, `rescue_ping_ttl`, `button_recovery.led_indicator`, warnings | ping result, TTL result, service probe result | Partially covered; signal reliability model needs refinement |
| 10 | Execute transfer | `recovery_methods`, `network_recovery.passive_tftp_from_router`, `tftp_details` | transfer progress, block number, ACK source port, errors | Covered for passive TFTP PUT |
| 11 | Interpret transfer errors | `known_issues`, `risk_warnings`, incident patterns | timeout, TFTP ERROR, `No route to host`, permission failure | Partially covered; error taxonomy needed |
| 12 | Post-upload wait | `post_upload_behavior.wait_seconds`, `user_warning_after_upload` | countdown state | Covered |
| 13 | Post-upload power action | `post_upload_behavior.power_cycle_required` | user-confirmed power cycle | Covered and critical for RT-AC86U |
| 14 | Restore Mac networking | `post_upload_behavior.dhcp_after_power_cycle` | DHCP state, assigned IP, gateway | Covered |
| 15 | Open admin UI | `post_upload_behavior.gateway_ip_as_admin_url` | detected gateway URL, browser open result | Covered |
| 16 | Outcome classification | `observed_outcomes`, `risk_warnings` | success/failure, retained config, factory-reset-like state | Covered conceptually; runtime outcome schema needed |
| 17 | Incident capture if failed | incident schema, linked workflows | packet trace, timing, symptoms, user notes | Supported by incident layer, not yet App-integrated |

## Current RT-AC86U App Coverage

The RT-AC86U incoming profile is strong enough to model the main guided flow:

- official firmware source guidance
- `.w` firmware file type
- LAN1 physical connection
- static Mac IP
- reset-hold-power-on Rescue Mode entry
- slow flashing power LED cue
- passive TFTP PUT
- octet mode
- fixed ACK source port behavior observed on port 69
- upload-complete-is-not-recovery-complete warning
- 180 second wait
- manual power cycle
- DHCP return
- gateway IP as admin URL
- mixed configuration retention warning

It is not strong enough to claim:

- all RT-AC86U hardware revisions behave identically
- all firmware versions are covered
- all regions use the same firmware package
- ping alone proves recovery readiness
- configuration will be preserved
- configuration will be reset

## Missing Runtime Structures

These should be designed before App export or App integration.

### 1. Firmware Runtime Validation

Knowledge profile should continue storing only source metadata.

The App runtime should separately track:

- selected local filename
- selected local file extension
- selected file size
- whether the file appears compressed and needs extraction
- checksum value calculated by the App
- checksum match result if the user supplies or selects a vendor checksum
- user confirmation that the model matches

Do not store the user's local path in profiles.

### 2. macOS Preflight

Needed runtime checks:

- selected wired Ethernet interface
- Wi-Fi disabled or warning shown
- current interface IP before modification
- ability to set static IP or instructions for manual setup
- Local Network permission state
- sandbox file access through file picker
- network client/server entitlement availability for App builds

Knowledge profile should only define expected network target and warnings.

### 3. Recovery Readiness Signal Model

Current fields store TTL and LED cues, but the App needs signal reliability:

- primary readiness signal
- secondary readiness signal
- weak signals that must not be used alone
- signals that are workflow-specific
- whether service probing is allowed

For RT-AC86U, LED state and recovery IP/TTL are useful, but ping alone is weak.

### 4. Transfer Error Taxonomy

The App needs structured error mapping:

| Runtime symptom | Likely category | Example user guidance |
| --- | --- | --- |
| `No route to host` | local network permission, wrong interface, wrong IP config | Recheck Local Network permission and wired IP setup |
| timeout before ACK | not in recovery mode, wrong timing, wrong IP, cable/interface issue | Re-enter Rescue Mode and confirm LED/IP setup |
| TFTP ERROR packet | firmware rejected, wrong filename, wrong file type | Recheck firmware model and file format |
| ACK stops mid-transfer | link interruption or device transition | Preserve logs and classify as incident if repeatable |

This belongs to App runtime logic plus incident capture, not directly inside a model profile.

### 5. Outcome And Incident Capture

The App should record failed or ambiguous attempts as incident candidates:

- profile ID
- workflow ID
- firmware version/file metadata, excluding private local path
- observed LED state
- ping/TTL timing
- transfer start time and error
- post-upload wait/power-cycle result
- DHCP/gateway result
- user-visible outcome

Incident capture must default to private/local until the user explicitly exports or submits it.

## Schema Implications

Do not immediately expand `recovery_profile.schema.json` for every runtime state.

Recommended separation:

- `recovery_profile.schema.json`: model parameters and evidence-backed guidance
- future `app_runtime_attempt.schema.json`: one live recovery attempt
- existing `recovery_incident.schema.json`: structured success/failure observations worth preserving
- workflow docs: common state transitions and error categories

## Minimum Next Step

Before App export, draft `app_runtime_attempt.schema.json` with only runtime fields that the App must track locally.

Do not block RT-AC86U reviewed-candidate migration on the runtime schema unless the App export is starting immediately.
