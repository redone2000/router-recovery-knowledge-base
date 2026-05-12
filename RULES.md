# Profile Rules v0.1

## 1. Required Fields
All recovery profiles MUST include the following fields. Missing any of these fields will automatically trigger a confidence downgrade and require changes before review can proceed.

| Field | Description |
|-------|-------------|
| `id` | Unique identifier in format: `{vendor}-{model}-{firmware-version}` (all lowercase, hyphen-separated) |
| `vendor` | Device manufacturer name (e.g., "tp-link", "cisco", "mikrotik") |
| `model` | Exact device model number/name |
| `recovery_methods` | Array of at least one valid recovery method from the `recovery_method` enum |
| `source_type` | Type of source the information comes from, from the `source_type` enum |
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
| `recovery_methods` is empty array | `low` |
| TFTP recovery is listed but `passive_tftp_from_router` and `active_tftp_to_router` are both null | `medium` |
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

## 3. Confidence Level Upgrade Rules
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

## 4. Field Usage Guidelines
### 4.1 Optional Fields That Strongly Impact Confidence
While not required, providing these fields significantly improves confidence:
- `source_url` or `source_document`: Proof of source material
- `recovery_details`: Step-by-step instructions for each recovery method
- `default_credentials`: Known default credentials for the device
- Any device-specific details (UART settings, IP addresses, filenames, etc.)

### 4.2 Null Field Policy
Fields may be set to null if the information is unknown, but this should be noted in the review process. Fields that are unknown but required for specific recovery methods will trigger a confidence downgrade.

Example: If `tftp_active` is listed as a recovery method but `network_recovery.default_ip` is null, confidence cannot be higher than `medium`.
