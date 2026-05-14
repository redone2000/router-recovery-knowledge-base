# Reference Device Lab Test Protocol

Date: 2026-05-14
Status: Stage 1 lab preparation draft

## Purpose

This protocol defines how to test the three reference devices before App upgrade integration.

The goal is not to "get the router recovered once." The goal is to produce structured evidence that can safely feed:

- App runtime behavior
- runtime attempt records
- incident candidates
- profile updates after review
- workflow/schema improvements

## Core Rule

Every test result must land in one of these buckets:

| Result type | Where it belongs |
| --- | --- |
| reproducible success with clear evidence | runtime attempt first, then profile candidate after review |
| failed or ambiguous attempt | incident candidate |
| one-off observation | lab note / observed-only |
| source-only fact | source index |
| App implementation issue | App issue/task, not profile data |

Do not update model profiles directly from a single test without review.

## Before Testing

Prepare these before touching the router:

- device model and label photo or note
- hardware version if visible
- current firmware version if reachable
- official firmware support/download page
- firmware file extension
- checksum availability
- Ethernet adapter name
- current Mac network state
- whether Wi-Fi is on/off
- packet capture plan, if available
- expected recovery workflow
- stop conditions

## Recommended Capture Signals

Record these whenever possible:

- LED state and timing
- LAN port used
- button held and approximate duration
- Mac IP assignment before and during recovery
- recovery IP attempted
- ping response and TTL
- whether a web page, TFTP ACK, or other service responded
- transfer start time
- transfer completion/failure time
- exact error message
- post-upload wait time
- whether manual power cycle was needed
- DHCP result after recovery
- gateway/admin URL after recovery
- firmware version after recovery
- configuration retained/reset/unknown

## Packet Capture Guidance

Packet capture is optional but high value.

Capture filters by workflow:

- Passive TFTP PUT: UDP port 69 and server ACK source port behavior
- Active TFTP server: router request to the Mac-side TFTP server
- Web Recovery: HTTP requests to the recovery page
- NMRP/research: capture broad interface traffic during power-on, then narrow later

Do not send test packets to unrelated networks or scan broad ranges.

## Runtime Attempt Mapping

After each test, fill or generate an `app_runtime_attempt` record when enough data exists.

Use:

```text
schema/app_runtime_attempt.schema.json
```

Validate with:

```text
python3 tools/validate_runtime_attempts.py <attempt-file-or-directory>
```

## Incident Mapping

Create an incident candidate when:

- recovery fails after meaningful setup
- timing appears fragile
- official instructions do not match observed behavior
- ping/TTL is misleading
- transfer succeeds but post-upload behavior is unexpected
- App preflight misses a real blocker

Incident candidates should include:

- symptom
- context
- observed signals
- failed patterns
- successful patterns, if any
- hypothesis
- experiment
- result
- next action

## App Feedback Mapping

Create an App upgrade task when the test exposes:

- missing UI state
- confusing wording
- missing warning
- wrong preflight order
- missing permission handling
- poor error mapping
- runtime attempt field missing

Do not solve App product issues by stuffing extra text into profile notes.

## Stop Conditions

Stop a test and record an incident instead of continuing to guess when:

- the same failure repeats 3 times with the same setup
- firmware source or model match is uncertain
- the router enters an unknown LED/state loop
- the App cannot confirm interface/IP ownership
- packet behavior contradicts the assumed workflow
- post-upload behavior remains unknown after a reasonable wait

## Privacy

Do not export:

- local file paths
- router serial numbers
- Wi-Fi passwords
- admin passwords
- private LAN details beyond what is needed for the recovery record

Runtime records are local/private by default.
