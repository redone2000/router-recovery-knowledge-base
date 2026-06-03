# ASUS Rescue Mode vs Firmware Restoration

ASUS recovery discussions often mix three different things:

- Rescue Mode: the router state entered during recovery.
- Firmware Restoration: the ASUS utility/workflow used to upload firmware in some official guides.
- TFTP transfer behavior: what may actually happen on the network for some models and states.

They are related, but they are not the same thing. Treating them as interchangeable can lead to wrong IP settings, wrong firmware assumptions, or premature "recovery complete" claims.

## Quick Difference

| Term | What it means | What it does not prove |
| --- | --- | --- |
| Rescue Mode | A recovery state entered by button timing during boot | TFTP direction, firmware acceptance, or completed recovery |
| Firmware Restoration | ASUS recovery utility/workflow used by official guides | macOS TFTP behavior or model-specific support |
| Passive TFTP | Router acts as TFTP server; computer uploads firmware | Universal ASUS behavior |
| Upload completed | Firmware file transferred over the network or utility workflow | Flash write, reboot, DHCP return, or usable admin UI |
| Recovery completed | Router booted and became usable again | Configuration retention or broad model applicability |

## Rescue Mode

ASUS official pages describe Rescue Mode entry patterns such as reset-held power-on, static client IP setup, and LED behavior.

Useful Rescue Mode evidence can include:

- button used and timing
- LED pattern
- router IP
- computer static IP
- whether ping appears
- whether a recovery utility or TFTP transfer can start

Rescue Mode is a state signal. It should not be used alone to claim that a router accepts a given firmware file or that recovery completed.

## Firmware Restoration

ASUS Firmware Restoration is the official recovery utility/workflow referenced in ASUS support pages. It is useful evidence for the existence of ASUS recovery workflows and post-upload wait guidance.

However, official Firmware Restoration pages are often Windows-utility oriented and may be brand-level or series-level. They should not automatically generate model-specific macOS app instructions.

Before converting Firmware Restoration evidence into app guidance, verify:

- exact model and hardware version
- firmware family and file type
- recovery IP and Mac static IP
- whether the transfer is utility-driven, passive TFTP, web upload, or another mechanism
- post-upload behavior
- final boot result

## Passive TFTP

Some ASUS lab observations in this project support passive TFTP behavior: the router acted as a TFTP server, and the Mac/App acted as a client uploading firmware.

This is model- and state-specific evidence, not universal ASUS guidance.

For the app, passive TFTP should be treated as App-guidable only when model-specific evidence exists. Otherwise, the app can help users record attempt details and preserve logs, but it should not imply the method is known.

## Post-Upload Phase

ASUS recovery should always separate transfer from final recovery.

After upload, the router may still need time to:

- validate the firmware
- write flash
- reboot
- return DHCP
- expose the admin UI again

Local lab observations for ASUS reference devices show why this matters: upload completion can happen before DHCP or the admin UI returns, and a normal power cycle may be part of the observed recovery path for a tested unit.

Do not call recovery complete until the router boots and becomes usable again.

## App Boundary

Router Recovery for macOS can safely support ASUS-oriented recovery work in different levels:

| Capability | App status | Boundary |
| --- | --- | --- |
| Record model, firmware, IP settings, and attempt result | App-guidable | Safe for all ASUS attempts as recordkeeping |
| Warn that upload completion is not recovery completion | App-guidable | Supported by public workflow evidence and lab observations |
| Guide passive TFTP PUT | Model-specific App-guidable | Only when model/state evidence supports passive TFTP |
| Recommend exact firmware file | Model-specific only | Requires model, hardware version, region, and firmware-family checks |
| Promise configuration retention | Not allowed | Single observations must not become promises |
| Claim all ASUS routers share one method | Not allowed | Evidence varies by model, series, and firmware state |

## Current Evidence Boundary

Public official ASUS evidence supports Rescue Mode / Firmware Restoration as ASUS recovery workflow context.

Current project evidence boundaries:

- ASUS FAQ 1000814: brand-level Rescue Mode / Firmware Restoration context.
- ASUS FAQ 1030642: brand-level context with RT-AC68U example; not an RT-AC68U profile.
- ASUS FAQ 1033090: Lyra series-level Rescue Mode context; not universal ASUS router proof.
- ASUS RT-AC86U lab observation: owner-lab evidence only; not final profile guidance.
- ASUS RT-AX86U H/W Ver. 1.0 reviewed candidate: scoped to tested unit and ASUSWRT-Merlin evidence; not stock ASUSWRT or all RT-AX86U variants.

## Recommended Next ASUS Work

Near-term ASUS work should focus on capability boundaries, not model count:

1. Compare RT-AX86U and RT-AC86U Rescue Mode entry and passive TFTP behavior.
2. Preserve post-upload wait, DHCP return, admin UI return, and power-cycle observations.
3. Search for model-specific official ASUS recovery pages only when they can close a known gap.
4. Keep stock ASUSWRT and ASUSWRT-Merlin evidence separate.
5. Do not create final ASUS profiles until the reviewed-candidate process and owner approval gates are complete.

## Related Pages

- [ASUS Recovery Guide](asus-recovery-guide.md)
- [ASUS Firmware Restoration Evidence Links](asus-firmware-restoration-evidence-links.md)
- [Brand Capability Boundary Matrix](brand-capability-boundary-matrix.md)
- [TTL=100 Does Not Mean TFTP Is Ready](ttl-100-does-not-mean-tftp-ready.md)

## Source Notes

- ASUS FAQ 1000814: https://www.asus.com/ca-en/support/faq/1000814/
- ASUS FAQ 1030642: https://www.asus.com/me-en/support/faq/1030642/
- ASUS FAQ 1033090: https://www.asus.com/support/faq/1033090/
