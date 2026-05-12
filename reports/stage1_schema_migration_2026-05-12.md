# Stage 1 Schema Migration

Date: 2026-05-12
Prepared by: Codex

## Reason

Owner review raised an App-consumption concern: profile data should support simple, direct runtime fields such as recovery IP, Mac IP mode, protocol action, firmware extension, recovery trigger, LAN port, LED cues, and ping TTL.

Most of those fields were already represented by the evidence-oriented schema after the ASUS RT-AC86U lab extension. Two small gaps remained:

- upload-phase client IP assignment mode
- machine-readable recovery entry method

## Schema Changes

Added:

- `network_recovery.client_ip_assignment`
  - allowed values: `static`, `dhcp`, `unknown`, `null`
- `button_recovery.entry_method`
  - machine-readable values such as `reset_hold_power_on`

These are source-data fields, not a replacement for future App export JSON.

## Incoming Draft Backfill

### ASUS RT-AC86U

Updated:

- `network_recovery.client_ip_assignment`: `static`
- `button_recovery.entry_method`: `reset_hold_power_on`

Reason: both values are supported by Owner lab observation.

### NETGEAR R7000

Updated:

- `network_recovery.client_ip_assignment`: `unknown`
- `button_recovery.entry_method`: `unknown`
- `tftp_details`: explicit unknown/null structure
- `post_upload_behavior`: explicit unknown/null structure
- `observed_outcomes`: explicit unknown/null structure

Reason: R7000 official sources support passive TFTP client upload but do not support these additional details in the current incoming draft.

## Non-Goals

- No new collection.
- No `reviewed/` writes.
- No `final/` writes.
- No guessed values.
- No separate `recovery_profiles/*.json` source of truth.

Future App-friendly JSON should be generated from reviewed/final profiles by an export tool, not maintained as a second manual data source.
