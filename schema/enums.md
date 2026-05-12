# Enumeration Definitions v0.1

## 1. recovery_method

Recovery methods supported by network devices.

| Value | Description |
|-------|-------------|
| `tftp_passive` | Passive TFTP recovery: router acts as TFTP server |
| `tftp_active` | Active TFTP recovery: router acts as TFTP client |
| `uart_serial` | UART/serial port recovery |
| `web_ui` | Web UI-based firmware upload recovery |
| `button_reset` | Hardware button reset to factory defaults |
| `usb_storage` | Recovery from USB storage device |
| `sd_card` | Recovery from SD card |
| `ssh_cli` | SSH CLI-based recovery |
| `telnet_cli` | Telnet CLI-based recovery |
| `jtag` | JTAG interface recovery |
| `nand_programmer` | NAND flash programmer recovery |
| `auto_recovery` | Automatic recovery without user intervention |
| `other` | Other recovery method not listed |

## 2. recovery_family

Family of recovery mechanisms used by the device.

| Value | Description |
|-------|-------------|
| `broadcom_cfe` | Broadcom Common Firmware Environment |
| `uboot` | U-Boot bootloader |
| `openwrt` | OpenWrt recovery system |
| `ddwrt` | DD-WRT recovery system |
| `tomato` | Tomato firmware recovery |
| `mikrotik_routeros` | MikroTik RouterOS recovery |
| `cisco_ios` | Cisco IOS recovery |
| `juniper_junos` | Juniper JunOS recovery |
| `tp_link` | TP-Link proprietary recovery |
| `d_link` | D-Link proprietary recovery |
| `asus` | ASUS proprietary recovery |
| `netgear` | NETGEAR proprietary recovery |
| `linksys` | Linksys proprietary recovery |
| `huawei` | Huawei proprietary recovery |
| `zte` | ZTE proprietary recovery |
| `ubiquiti` | Ubiquiti proprietary recovery |
| `generic` | Generic/unknown recovery family |

## 3. source_type

Type of source where the recovery information was obtained.

| Value | Description | Confidence Impact |
|-------|-------------|-------------------|
| `official_documentation` | Official vendor documentation | High confidence baseline |
| `vendor_support_forum` | Official vendor support forum | High confidence baseline |
| `verified_community_guide` | Verified community guide (high reputation source) | Medium-High confidence baseline |
| `community_forum_post` | General community forum post | Medium confidence baseline |
| `personal_testing` | First-hand testing and verification | Highest confidence when documented |
| `security_research_paper` | Security research paper or publication | Medium-High confidence baseline |
| `firmware_analysis` | Extracted from firmware analysis | High confidence baseline |
| `bootloader_dump` | Extracted from bootloader dump analysis | High confidence baseline |
| `third_party_repository` | Third-party firmware/recovery repository | Medium confidence baseline |
| `social_media` | Social media post (Twitter, Reddit, etc.) | Low confidence baseline |
| `ai_generated` | AI-generated content (requires extra validation) | Lowest confidence baseline |
| `unknown` | Source unknown | Lowest confidence baseline |

## 4. confidence_levels

Confidence level indicating the accuracy and reliability of the profile.

| Level | Description | Minimum Requirements |
|-------|-------------|----------------------|
| `verified` | Highest confidence: Information has been independently verified through multiple sources or hands-on testing | ≥2 independent sources matching, or verified hands-on testing |
| `high` | High confidence: Information comes from a reliable source and has no conflicting reports | Official documentation or verified research |
| `medium` | Medium confidence: Information comes from a reasonably reliable source but lacks independent verification | Community guide with good reputation, no conflicting reports |
| `low` | Low confidence: Information comes from an unreliable source or has conflicting reports | Single unconfirmed report, social media, AI-generated content |
| `unverified` | No confidence: Newly submitted profile awaiting review | Any unvetted source |

## 5. Field Semantics

Use explicit strings for unknown values in scalar fields when the source does not identify a value.

| Value | Meaning |
|-------|---------|
| `unknown` | The value may exist, but current evidence does not identify it |
| `null` | The value does not apply, or the schema explicitly defines null for an unknown boolean state |
| omitted field | The collector has not evaluated this optional field yet |

For TFTP direction booleans, `null` means direction is unknown or not evidenced. Do not infer `passive_tftp_from_router` or `active_tftp_to_router` from vendor, family, or model patterns.

## 6. deprecation_status

| Value | Description |
|-------|-------------|
| `active` | Current profile candidate |
| `deprecated` | Profile is outdated and should not be used for new guidance |
| `superseded` | Profile has been replaced by another profile |

## 7. tftp_port_behavior

TFTP transfer-port behavior observed or documented during recovery.

| Value | Description |
|-------|-------------|
| `standard_ephemeral` | Server switches from port 69 to a separate transfer port after request negotiation |
| `fixed_server_port` | Server continues sending ACK/data from port 69 throughout transfer |
| `unknown` | Transfer-port behavior is not known or not evidenced |

## 8. config_retention_observed

Observed configuration state after recovery.

| Value | Description |
|-------|-------------|
| `retained` | Existing configuration was observed to remain after recovery |
| `factory_reset` | Device was observed to return to factory-default-like state |
| `mixed` | Both retained and factory-reset-like outcomes have been observed |
| `unknown` | Configuration retention outcome is not known or not evidenced |

## 9. client_ip_assignment

How the user's computer should obtain an IP address during the recovery upload phase.

| Value | Description |
|-------|-------------|
| `static` | User should manually configure a static IP address before recovery upload |
| `dhcp` | User should use DHCP during recovery upload |
| `unknown` | IP assignment mode is not known or not evidenced |

## 10. button_recovery.entry_method

Machine-readable recovery entry method values should be stable lowercase identifiers.

| Value | Description |
|-------|-------------|
| `reset_hold_power_on` | Hold reset while powering on the device |
| `wps_hold_power_on` | Hold WPS while powering on the device |
| `unknown` | Entry method is not known or not evidenced |
