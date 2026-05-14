# ASUS RT-AC86U Reference Validation Owner Checklist

Date: 2026-05-14
Status: Owner confirmation checklist

## Candidate

```text
incoming/asus-rt-ac86u-unknown-unknown.jsonl
```

## Purpose

Confirm whether the ASUS RT-AC86U incoming profile may move to `reviewed/` as a reviewed candidate.

This does not approve `final/`.

## Minimum Owner Confirmations

Please confirm or reject each item:

1. The recorded lab observations are accurate for the tested RT-AC86U unit.
2. The profile should remain scoped to observed/tested behavior only.
3. `hardware_version` should remain `unknown`.
4. `firmware_version` should remain `unknown`.
5. `applies_to_all_firmware_versions` should remain `null`.
6. `confidence_level: medium` is acceptable for reviewed-candidate status.
7. The post-upload warning is correct: upload completion does not mean recovery is complete.
8. The observed post-upload process is correct: wait about 3 minutes, manually power cycle, switch Mac back to DHCP, then use the DHCP gateway IP.
9. Configuration outcome warning is correct: both retained and factory-reset-like outcomes were observed.
10. Ping / previous LAN IP should not be presented as reliable failure signals.
11. Moving to `reviewed/` is approved only as reviewed-candidate data, not App-final guidance.

## If Any Item Is Rejected

Do not move the profile to `reviewed/`.

Record the rejected item and update the incoming draft or supporting evidence first.

## If All Items Are Confirmed

Codex may prepare a reviewed-candidate migration plan:

- no write to `final/`
- preserve unknown scope
- preserve observation-only groups
- preserve risk warnings
- add lifecycle decision
- run validators before and after migration
