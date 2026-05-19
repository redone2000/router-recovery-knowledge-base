# ASUS RT-AX86U Profile Candidate Guardrails

Date: 2026-05-17
Prepared by: Codex
Status: guardrails only, no profile promotion

## Candidate Basis

Primary evidence:

- `lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`
- `runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md`

Scope:

- ASUS RT-AX86U, label hardware version `1.0`
- ASUSWRT-Merlin official/unmodified firmware in this test
- Firmware before recovery attempt: `3004.388.11`
- Firmware written by TFTP downgrade attempt: `3004.388.10_2`
- Normal Web UI upgrade returned device to `3004.388.11`

## Promotion Boundary

This evidence is strong enough for a reviewed-candidate discussion.

It is not strong enough for final profile publication.

Do not write a final profile from this session.

Do not merge RT-AX86U and RT-AC86U into one conclusion.

## Fields That May Become Reviewed-Candidate Values

Candidate values, if owner approves:

- `recovery_methods`: include passive TFTP / TFTP PUT.
- `network_recovery.default_ip`: `192.168.1.1`.
- `network_recovery.client_static_ip`: `192.168.1.10/24`.
- `network_recovery.required_lan_port`: LAN1, observation-only.
- `button_recovery.entry_method`: hold Reset while powering on.
- `button_recovery.led_indicator`: slow-flashing power LED, observation-only.
- `readiness_signals`: TTL=100 on `192.168.1.1`, supporting signal only.
- `tftp_details.mode`: `octet`.
- `tftp_details.ack_source_port`: `69`.
- `tftp_details.server_uses_ephemeral_port`: `false`, observation-only.
- `post_upload_behavior.wait_seconds`: at least several minutes before next action.
- `post_upload_behavior.power_cycle_required`: likely required after TFTP upload for this observed unit.
- `post_upload_behavior.dhcp_after_power_cycle`: yes.
- `post_upload_behavior.gateway_ip_as_admin_url`: yes, observed as `192.168.50.1`.

## Required Warnings

Any reviewed candidate must include prominent warnings:

- Upload completion is not recovery completion.
- Do not power-cycle immediately at transfer completion; wait several minutes first.
- DHCP may not return until after manual power cycle.
- Web Recovery was not observed during TTL=100.
- Active TFTP / router-pulls-firmware was not observed.
- Ping/TTL is not enough by itself; use it with LED and transfer readiness context.
- Configuration retention is not guaranteed.
- Firmware image must match the exact model and firmware family.
- Use the extracted firmware image, not the `.zip` archive.

## Configuration Retention Boundary

This RT-AX86U attempt retained configuration.

That must remain this-run evidence only.

Owner reports prior RT-AC86U repeated tests behaved inconsistently: about 3-4 attempts included at least one configuration-clear outcome.

Therefore profile or App language must not say:

- configuration will be retained
- configuration will be reset
- retention is controllable by the user

Safer wording:

- Back up configuration before recovery.
- Recovery may retain configuration or may reset/alter it.
- After recovery, verify firmware version, LAN/DHCP, Wi-Fi, WAN, and any installed add-ons.

## Observation-Only Groups

Mark these as observation-only if encoded into a candidate:

- LAN1 requirement
- hold duration
- slow-flashing power LED behavior
- TTL=100 duration
- ACK source port 69 behavior
- lack of Web Recovery page
- lack of active RRQ in passive capture
- post-upload LAN1-only LED state
- manual power-cycle requirement
- configuration retention

## Owner Confirmation Required

Before reviewed-candidate migration, owner should confirm:

1. The recorded RT-AX86U observations are accurate.
2. The candidate scope is limited to the tested unit and tested firmware family.
3. `confidence_level: medium` or equivalent is acceptable.
4. Configuration retention is treated as non-guaranteed.
5. Web Recovery remains unconfirmed/unsupported by this evidence.
6. Active TFTP remains unsupported by this evidence.
7. Passive TFTP PUT is supported by this evidence.
8. Final profile publication is not approved by this checklist.

## Stop Line

No more device tests are required for this candidate right now.

Future tests should only be run if they answer a product-blocking question that cannot be resolved by documentation or existing evidence.
