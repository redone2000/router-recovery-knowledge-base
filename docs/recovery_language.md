# Recovery Language

Date: 2026-05-13
Status: Stage 1 vocabulary draft

## Purpose

Recovery knowledge needs a shared language.

The same terms should be used across:

- App UI
- profile schema
- support docs
- SEO pages
- AI assistant responses
- incident reports
- lab validation notes

This reduces fragmentation and prevents recovery guidance from drifting across surfaces.

## Core Terms

### Recovery Preparation

The phase before attempting recovery.

Includes:

- wired Ethernet setup
- disabling Wi-Fi if needed
- setting static IP or DHCP
- selecting the correct firmware file
- choosing the right LAN port
- confirming power/reset choreography

### Recovery Mode

A special device state where recovery services may become available.

Examples:

- ASUS Rescue Mode
- TP-Link recovery web UI
- NETGEAR recovery window
- bootloader TFTP mode

Recovery Mode is not the same as normal router operation.

### Recovery Window

The time interval where the device is ready to accept a recovery action.

Examples:

- TFTP WRQ may only be accepted during a short window.
- A web recovery page may appear only after a specific LED state.
- ICMP ping may respond before the recovery service is actually ready.

Important rule:

`ping responds` does not always mean `recovery service is ready`.

### Recovery Ready

A state where enough evidence suggests the next recovery action should be attempted.

This may be based on:

- LED state
- TTL value
- reachable recovery IP
- open service
- vendor instruction
- lab-observed timing

Recovery Ready must be tied to a workflow. It is not a universal signal.

### Passive TFTP / TFTP PUT

The router acts as the TFTP server.

The user or App acts as the TFTP client and uploads firmware to the router.

Profile mapping:

- `recovery_methods`: `tftp_passive`
- `network_recovery.passive_tftp_from_router`: `true`
- `network_recovery.active_tftp_to_router`: `false`

### Active TFTP / Router Pulls Firmware

The router acts as the TFTP client.

The user or App runs a TFTP server and the router requests a firmware file from it.

Profile mapping:

- `recovery_methods`: `tftp_active`
- `network_recovery.active_tftp_to_router`: `true`
- `network_recovery.passive_tftp_from_router`: `false`

### Rescue Mode

Vendor-specific recovery mode entered by a hardware action.

Example:

- hold reset while powering on
- wait for a slow flashing power LED

Rescue Mode should not be assumed to behave identically across models or firmware versions.

### Post-Upload Phase

The phase after firmware upload completes but before normal operation resumes.

This phase may require:

- waiting several minutes
- manual power cycle
- switching the Mac back to DHCP
- using the DHCP gateway IP as the admin URL

Important rule:

`upload complete` does not always mean `recovery complete`.

### Observed-Only

A field or behavior observed in testing but not yet proven as generally applicable.

Profile marker:

- `observation_only: true`

Use when:

- behavior was observed on a tested unit
- hardware/firmware scope is unknown
- vendor documentation does not confirm broad applicability

App/export implication:

Show as tested-unit behavior or reviewed observation, not universal truth.

### Incident

A structured success or failure case.

Examples:

- TTL=100 but TFTP WRQ times out
- manual `put` timing seems unreliable
- upload succeeds but router does not reboot until power cycle

Incidents are not profiles.

They are raw or semi-structured evidence that may later form a pattern.

### Pattern

A repeated incident-level behavior that may inform a workflow or profile.

Example:

```text
Multiple R7000 tests show ICMP TTL=100 before WRQ is accepted.
```

Patterns still require validation before becoming App guidance.

### Lab Validation

Controlled testing on a physical device.

Possible statuses:

- not tested
- reproduced success
- reproduced failure
- partial
- conflicting

Lab validation can increase confidence, but only within the tested hardware/firmware scope.

### Profile

A structured model-specific recovery candidate.

Profiles should only contain evidence-backed fields and must retain source evidence.

Profiles may be:

- incoming
- reviewed
- final
- paused
- deprecated

### Reviewed Candidate

A profile that passed evidence review and Owner confirmation but is not final.

Reviewed candidates can be used for further app/workflow design, but final publication still requires a separate decision.

### Final Profile

Approved production data.

Final profiles must never be written automatically by agents or tools.

## Terms To Avoid

Avoid:

- "guaranteed recovery"
- "works for all versions"
- "always keep configuration"
- "always factory resets"
- "ping means ready"
- "upload complete means done"

Use:

- "observed"
- "tested unit"
- "source says"
- "unknown scope"
- "may require"
- "do not judge by ping alone"

## Product Language Principles

1. Describe the current phase.
2. Tell the user what signal matters.
3. Warn when a signal is not sufficient.
4. Separate upload completion from recovery completion.
5. Separate observed behavior from universal behavior.
6. Preserve uncertainty instead of smoothing it away.
