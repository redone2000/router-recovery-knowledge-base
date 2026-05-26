# ASUS RT-AX86U Pro Source Probe

Date: 2026-05-26
Status: source probe, not profile evidence

## Decision

Move `asus-rt-ax86u-pro-unknown-unknown` from pure `research_seed` to `evidence_indexed`, with `evidence_strength=official_but_incomplete`.

Do not create an `incoming/` profile.

Do not assert TFTP direction.

## Sources Checked

### ASUS RT-AX86U Pro Driver & Tools

URL:

```text
https://www.asus.com/us/networking-iot-servers/wifi-routers/asus-gaming-routers/rt-ax86u-pro/helpdesk_download/?model2Name=RT-AX86U-Pro
```

Finding:

- Official ASUS model-specific support page for RT-AX86U Pro.
- The page lists `ASUS Firmware Restoration` under the model support download area.
- The page describes Firmware Restoration as a utility for an ASUS wireless router that failed during firmware upgrade.

Boundary:

- This proves model-specific utility availability.
- It does not prove TFTP direction, recovery IP, port behavior, post-upload behavior, or success semantics.

### ASUS Rescue Mode FAQ

URL:

```text
https://www.asus.com/support/faq/1000814/
```

Finding:

- Official ASUS brand-level Rescue Mode / Firmware Restoration FAQ.
- It describes Firmware Restoration as a rescue-mode upload path for failed normal firmware upgrades.
- It gives static client IP `192.168.1.10` and subnet `255.255.255.0`.
- It describes reset-held power-on and a slowly flashing power LED as Rescue Mode signal.
- It instructs restoring TCP/IPv4 settings after the rescue-mode process.

Boundary:

- The FAQ uses RT-AC68U as the example router.
- It is brand-level guidance, not RT-AX86U Pro-specific workflow evidence.
- It does not establish TFTP direction for RT-AX86U Pro.

## Hypothesis Update

Updated:

```text
model_hypotheses/asus-expansion-seeds.jsonl
```

Record:

```text
asus-rt-ax86u-pro-unknown-unknown
```

New state:

- `hypothesis_status=evidence_indexed`
- `evidence_strength=official_but_incomplete`
- `suspected_workflows=["unknown"]`
- `workflow_confidence=none`
- `promotion_gate=do_not_promote`
- `app_copy_allowed=false`

## Missing Proof

Before this can become an `incoming/` profile candidate, it still needs:

- RT-AX86U Pro model-specific recovery entry confirmation beyond support-page linkage.
- TFTP direction and port behavior.
- Recovery IP and client IP requirements confirmed for RT-AX86U Pro specifically.
- Accepted firmware file type and filename requirements.
- Post-upload wait, reboot, DHCP/admin return behavior.
- Hardware revision and firmware version scope.
- Lab attempt or high-quality model-specific successful recovery report.

## Next Step

Search for RT-AX86U Pro-specific manual sections or lab/community recovery attempts. If no model-specific evidence appears, keep this candidate as `evidence_indexed` only.
