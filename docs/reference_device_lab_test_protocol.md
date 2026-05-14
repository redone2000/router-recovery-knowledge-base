# Reference Device Lab Test Protocol

Date: 2026-05-14
Status: Stage 1 lab preparation draft

## Purpose

This protocol defines how to test the three reference devices before App upgrade integration.

The goal is not to "get the router recovered once." The near-term test focus is TFTP active/passive completion behavior and the small operational details that improve user recovery success rate.

The goal is to produce structured evidence that can safely feed:

- App runtime behavior
- runtime attempt records
- incident candidates
- profile updates after review
- workflow/schema improvements

## TFTP Success-Rate Focus

For this testing round, prioritize details that ordinary vendor instructions often omit:

- whether the device acts as TFTP server or TFTP client
- whether the App should run a TFTP client or TFTP server
- exact timing relationship between power-on, LED state, ping, and first WRQ/RRQ
- whether ping/TTL appears before the TFTP service is actually ready
- whether the server ACKs from port 69 or switches to an ephemeral port
- whether the router requires a fixed filename
- whether the accepted filename differs from the downloaded firmware filename
- whether retrying WRQ/RRQ improves success rate or causes failure
- which LAN port is most reliable
- whether wired service priority or route ownership remains correct while Wi-Fi is available
- whether macOS Local Network permission appears as a network error
- whether upload completion leads to automatic reboot or requires manual action

These details should become App workflow improvements before they become broad profile claims.

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

## Hygiene Defaults Under Test

The App may recommend recovery hygiene defaults unless contradicted by profile evidence. During reference-device testing, explicitly note whether these defaults helped, had no visible effect, or were contradicted:

- power off for about 10 seconds before recovery entry
- direct Mac-to-router Ethernet
- disconnect WAN and other LAN clients
- prefer LAN1 / LAN port nearest WAN when no model-specific port is known
- keep Wi-Fi available when needed, while confirming wired service priority or route ownership
- confirm wired interface owns the static IP
- use official firmware source and extract archive before selecting firmware
- wait 2-3 minutes after upload before judging the result
- return Mac to DHCP after recovery

See `docs/recovery_hygiene_defaults.md`.

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
- whether Wi-Fi remains available and wired route is confirmed
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

## TFTP Direction Classification

Use these labels consistently:

| Label | Router role | Mac/App role | Typical packet clue |
| --- | --- | --- | --- |
| Passive TFTP PUT | router is TFTP server | Mac/App sends WRQ and uploads firmware | Mac sends WRQ to router, router ACKs |
| Active TFTP Server | router is TFTP client | Mac/App runs TFTP server | router sends RRQ to Mac-side server |

Do not infer direction from brand or model. Direction must come from packet behavior, official documentation, or successful tool behavior.

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
- timing tuning becomes arbitrary without new observations
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

For a one-page checklist to use during live testing, see `lab_tests/recovery_preflight_checklist.md`.
