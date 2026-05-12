# Profile Rules v0.1

## 0. Project Maintenance Rules
- Stage-level project work MUST be committed to git and pushed to the configured private remote repository after validation.
- If no better repository name is specified, the private remote repository SHOULD match the local directory name: `router-recovery-knowledge`.
- Do not include secrets, credentials, generated caches, or destructive outputs in commits.
- Do not perform destructive operations, public releases, or externally visible submissions without explicit confirmation.
- OpenClaw does not reliably share this project's working directory context. Any task file given to OpenClaw MUST be referenced by absolute path, for example `/Users/YiYuan/Projects/router-recovery-knowledge/prompts/agent_tasks/openclaw_stage1_source_list_proposal.md`.
- Store long agent handoff prompts under `prompts/agent_tasks/`; chat messages to agents should reference the absolute file path plus the current safety limits.

## 1. Required Fields
All recovery profiles MUST include the following fields. Missing any of these fields will automatically trigger a confidence downgrade and require changes before review can proceed.

| Field | Description |
|-------|-------------|
| `id` | Unique identifier in format: `{vendor}-{model}-{hardware-version}-{firmware-version}` (all lowercase, hyphen-separated) |
| `vendor` | Device manufacturer name (e.g., "tp-link", "cisco", "mikrotik") |
| `model` | Exact device model number/name |
| `hardware_version` | Hardware revision, or `unknown` if sources do not identify it |
| `recovery_methods` | Array of at least one valid recovery method from the `recovery_method` enum |
| `source_type` | Type of source the information comes from, from the `source_type` enum |
| `source_evidence` | Structured evidence supporting each claimed recovery method |
| `confidence_level` | Initial confidence level set by submitter, from the `confidence_levels` enum |
| `submitted_date` | Date of submission in ISO format (YYYY-MM-DD) |

## 2. Confidence Level Downgrade Rules
Confidence level MUST be lowered (at least one level) if any of the following conditions are met:

### 2.1 Source-Related Downgrades
| Condition | Maximum Allowed Confidence |
|-----------|-----------------------------|
| Source type is `ai_generated` | `low` |
| Source type is `unknown` | `low` |
| Source type is `social_media` | `low` |
| Source type is `community_forum_post` with < 5 upvotes/positive confirmations | `low` |
| Source type is `community_forum_post` with ≥ 5 upvotes/positive confirmations | `medium` |
| Source is a single uncorroborated report | `medium` |
| Source URL is not provided for web sources | Lower by one level |

### 2.2 Field-Related Downgrades
| Condition | Maximum Allowed Confidence |
|-----------|-----------------------------|
| Any required field is missing | `low` |
| `source_evidence` is missing or empty | `low` |
| Claimed recovery method has no supporting evidence entry | Lower by one level |
| `recovery_methods` is empty array | `low` |
| TFTP recovery is listed but `passive_tftp_from_router` and `active_tftp_to_router` are both null | `medium` |
| TFTP direction is inferred from vendor/family/model without direct evidence | `low` |
| `default_credentials` is present but missing username or password | Lower by one level |
| Recovery steps are missing for listed recovery methods | Lower by one level |
| `firmware_version` is null but profile claims to apply only to specific versions | Lower by one level |

### 2.3 Consistency-Related Downgrades
| Condition | Maximum Allowed Confidence |
|-----------|-----------------------------|
| Conflicting information in recovery steps | `low` |
| Contradiction between different sources | `low` |
| Recovery method claims contradict known device capabilities | `low` |
| TFTP type classification is inconsistent with device family behavior | Lower by one level |

## 3. TFTP Direction Evidence Rules
TFTP direction MUST be supported by direct evidence. Vendor, chipset, bootloader family, or common model behavior is not enough.

### 3.1 Passive TFTP (`passive_tftp_from_router`)
Set `network_recovery.passive_tftp_from_router` to true only when evidence states that the router/device runs a TFTP server or that the user connects to the router with a TFTP client and uploads/downloads firmware.

Sufficient evidence examples:
- The source says the router runs a TFTP server in recovery mode.
- The source instructs the user to connect to the router IP with a TFTP client.
- The source instructs the user to use a TFTP `put` command to send firmware to the device.

### 3.2 Active TFTP (`active_tftp_to_router`)
Set `network_recovery.active_tftp_to_router` to true only when evidence states that the router/device acts as a TFTP client or that the user must run a TFTP server for the device to fetch a named file.

Sufficient evidence examples:
- The source instructs the user to run a TFTP server on the computer.
- The source says the router looks for a TFTP server at a specified computer IP.
- UART or bootloader logs show the device requesting a file from a TFTP server.

### 3.3 Ambiguous TFTP
If the source only says "TFTP recovery" without server/client direction, set both TFTP direction fields to null, record an evidence gap, and cap confidence at `medium`.

Conflicting TFTP direction evidence caps confidence at `low` until reviewed.

## 4. Confidence Level Upgrade Rules
Confidence level may be raised after review if:
- Multiple independent sources confirm the same information
- Hands-on testing confirms the recovery method works
- Official documentation supports the claims
- Additional validation is performed during review

### Requirements for `verified` level
To achieve the highest `verified` confidence level, the profile must meet at least one of these criteria:
1. Two independent, reliable sources confirming the same recovery method
2. Documented hands-on testing with proof (screenshots, logs, etc.)
3. Official vendor documentation explicitly describing the recovery process
4. Firmware or bootloader analysis confirming the recovery mechanism

## 5. Field Usage Guidelines
### 5.1 Optional Fields That Strongly Impact Confidence
While not required, providing these fields significantly improves confidence:
- `source_url` or `source_document`: Proof of source material
- `source_evidence`: Direct evidence for each claimed recovery method
- `recovery_details`: Step-by-step instructions for each recovery method
- `default_credentials`: Known default credentials for the device
- Any device-specific details (UART settings, IP addresses, filenames, etc.)

### 5.2 Unknown and Null Policy
Use `unknown` for scalar values that may exist but are not identified by current evidence, such as hardware version or firmware version. Use null when the value does not apply, or when a boolean direction field explicitly uses null for unknown/not evidenced state.

Example: If `tftp_active` is listed as a recovery method but `network_recovery.default_ip` is null, confidence cannot be higher than `medium`.
