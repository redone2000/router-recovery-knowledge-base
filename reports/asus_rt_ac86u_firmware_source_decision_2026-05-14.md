# ASUS RT-AC86U Firmware Source Decision

Date: 2026-05-14
Scope: schema/profile guidance refinement only

## Decision

Official firmware source should be part of an App-ready recovery profile, but it must be represented separately from recovery behavior and firmware-version applicability.

## Rationale

The user needs a safe way to obtain the firmware file before attempting recovery. Without an official firmware source field, the profile can describe the transfer mechanics but still leave a critical App workflow gap: where the user should obtain the correct `.w` firmware and how to verify that it matches the device.

However, an official download page does not prove:

- Rescue Mode behavior
- TFTP direction
- LAN port requirements
- post-upload power-cycle behavior
- broad hardware-version applicability
- broad firmware-version applicability

Therefore the repository now uses a separate `firmware_source` object rather than changing `firmware_version`.

## Implemented Boundary

- `firmware_version` remains `unknown`.
- `applies_to_all_firmware_versions` remains `null`.
- `firmware_source` stores the official ASUS RT-AC86U support/download page metadata.
- `firmware_source.binary_stored` must be `false`.
- Direct firmware binary URLs are not stored as stable profile data.
- The official source is listed in `source_evidence` only for firmware-source guidance.

## App Guidance Implication

The App can now say:

- use the official ASUS RT-AC86U support/download page
- select firmware that explicitly matches RT-AC86U
- verify checksum when ASUS provides one
- do not use firmware for a different model, region, or unsupported hardware scope

The App must not say:

- this profile applies to all RT-AC86U firmware versions
- every RT-AC86U hardware/region variant behaves identically
- the official download page proves the observed post-upload power-cycle behavior
