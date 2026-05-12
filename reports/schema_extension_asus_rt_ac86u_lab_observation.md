# Schema Extension From ASUS RT-AC86U Lab Observation

Date: 2026-05-12
Prepared by: Codex

## Decision

The ASUS RT-AC86U lab observation revealed profile variables that are important for App guidance and were not represented cleanly in the v0.1 schema.

Rather than adding many top-level fields, the schema was extended with grouped fields:

- `network_recovery.client_static_ip`
- `network_recovery.client_static_cidr`
- `network_recovery.required_lan_port`
- `network_recovery.rescue_ping_ttl`
- `button_recovery.press_duration_seconds_min`
- `button_recovery.press_duration_seconds_max`
- `tftp_details`
- `firmware_details`
- `post_upload_behavior`
- `observed_outcomes`

## Why This Matters

The most important new product variable is `post_upload_behavior.power_cycle_required`.

The RT-AC86U observation shows that upload completion is not the end of the user journey. The App must be able to tell the user to wait, manually power cycle, switch the Mac back to DHCP, and use the DHCP gateway IP as the admin URL.

Without these fields, the profile would imply an incomplete or misleading recovery flow.

## Incoming Draft Added

- `incoming/asus-rt-ac86u-unknown-unknown.jsonl`

This is an incoming draft only.

It uses `source_type: personal_testing`, `confidence_level: medium`, and keeps hardware and broad firmware scope as `unknown`.

## Safety Boundaries

- No `reviewed/` data was written.
- No `final/` data was written.
- The draft must not be promoted without human review.
- The power-cycle requirement is recorded as observed behavior, not vendor-official universal truth.
