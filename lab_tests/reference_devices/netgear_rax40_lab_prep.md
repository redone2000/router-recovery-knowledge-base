# NETGEAR RAX40 Lab Prep

Date: 2026-05-14
Status: pre-test plan
Reference role: NETGEAR TFTP/NMRP orchestration / timing-sensitive recovery research

## Goal

Use RAX40 as a modern NETGEAR reference target, not as an immediate profile.

This test should determine:

- which recovery path appears most relevant: Web, TFTP, NMRP, or other
- whether timing/orchestration is the primary blocker
- whether TFTP, if present, is active or passive
- what App runtime signals are needed before guidance can be safe
- whether R7000 lessons apply only as incident context or broader NETGEAR pattern

## Current Gate

No profile generation.

Known state:

- R7000 remains incident-only.
- NETGEAR official TFTP evidence exists for some models, but R7000 testing was unreliable.
- NMRP evidence is research-only and not official-workflow-ready.
- RAX40 should begin with source/lab exploration and incident capture.

## Pre-Test Checklist

- Confirm exact device label: `RAX40`
- Record hardware version if visible.
- Record current firmware version if reachable.
- Confirm official NETGEAR support/download page for RAX40.
- Record firmware file extension and checksum availability.
- Prepare Mac wired adapter and note interface name.
- Prepare packet capture if available.
- Decide which recovery path is being tested first.

## Source And Firmware Preparation

Record:

- official support/download page URL
- official recovery article URL, if found
- selected firmware filename, without local path
- extension
- size
- checksum status if available
- whether instructions are model-specific or generic

Do not treat generic NETGEAR recovery documentation as model-specific RAX40 guidance without verification.

## Recovery Entry Exploration

Record:

- power-off duration
- button used
- hold duration
- LED sequence
- LAN port used
- Mac link state
- ping response and TTL
- whether any web page appears
- whether any TFTP/NMRP-like traffic appears

Do not assume ping/TTL means the recovery service is ready.

## TFTP Exploration

Only if a TFTP path is explicitly selected for test:

- record Mac static IP/cidr
- target IP
- client tool
- first WRQ time relative to power-on
- whether any router RRQ appears when a Mac-side server is running
- whether the tested direction is passive PUT or active server
- required filename, if any
- whether ACK/error comes from port 69 or another port
- ACK/error/timeout behavior
- number of repeated controlled attempts
- whether timing appears manual or automatable
- whether continuous retry improves success or masks the real recovery window

If repeated timing attempts fail, stop and record an incident rather than tuning indefinitely.

## NMRP / Orchestration Exploration

Only if explicitly selected for test:

- record tool used
- network interface selected
- command/options
- timing relative to power-on
- discovery response
- firmware transfer result
- router reboot/result

NMRP findings should remain research/incident data unless official or lab-repeatable evidence becomes strong enough for workflow/profile review.

## App Questions To Answer

- Does NETGEAR need a distinct orchestration workflow instead of simple TFTP guidance?
- Can the App detect the correct recovery window, or does a helper tool need to drive timing?
- Which runtime signals are misleading?
- Which error category best describes failed attempts?
- Is RAX40 a better reference than R7000 for modern NETGEAR behavior?
- Should the App present NETGEAR TFTP as timing-sensitive/research-only until lab success is reproduced?

## Stop Conditions

Stop and record an incident if:

- timing attempts become guesswork
- ping responds but transfer service does not
- TFTP direction cannot be confirmed from packet behavior
- official instructions conflict with observed behavior
- NMRP/TFTP behavior is unclear after controlled attempts
- firmware source/model applicability is uncertain

## Expected Outputs

- source list or source index for RAX40 official evidence
- runtime attempt records for meaningful tests
- incident candidates for failures and timing issues
- no incoming profile until recovery method is reproduced or strongly evidenced
