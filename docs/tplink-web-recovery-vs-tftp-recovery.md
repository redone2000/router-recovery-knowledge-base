# TP-Link Web Recovery vs TFTP Recovery

TP-Link recovery documentation can mention browser-based recovery pages, Emergency Mode, and TFTP recovery. These are different workflows.

Do not assume a TP-Link device supports TFTP just because another TP-Link product line does. Do not assume a browser recovery page proves firmware recovery completed.

## Quick Difference

| Question | Web Recovery / Emergency Mode | TFTP Recovery |
| --- | --- | --- |
| User interface | Browser page at a local recovery IP | TFTP client/server transfer |
| Main user action | Select firmware in a web page and upload | Run a TFTP client or server, depending on direction |
| Direction question | Usually HTTP upload to router recovery page | Must identify whether router or computer is the TFTP client |
| Filename requirement | Often selected through browser file picker | May require an exact filename such as `recovery.bin` |
| Evidence needed | page IP, static computer IP, upload result, reboot result | static IP, router IP, filename, client/server direction, transfer logs |
| Success condition | Router boots and becomes usable after upload/write/reboot | Router accepts firmware, writes it, reboots, and becomes usable |

## Web Recovery / Emergency Mode

TP-Link Web Recovery usually means the router exposes a local browser page while in a recovery state. Some TP-Link documentation calls this Emergency Mode or Recovery Mode.

Useful evidence includes:

- exact recovery page URL
- computer static IP and subnet
- button sequence
- LED behavior
- whether the page is HTTP-only
- firmware file picker and upload behavior
- progress or reboot behavior
- final admin UI or network return

Page entry is useful evidence, but it is not completed recovery.

For page-entry troubleshooting, see [TP-Link Web Recovery Troubleshooting](tplink-web-recovery-troubleshooting.md).

## Active TFTP

Some TP-Link product lines document active TFTP behavior: the computer runs a TFTP server and the TP-Link device requests a firmware file.

Evidence to capture:

- computer static IP
- TFTP server root directory
- exact firmware filename required by the device
- router request packet or TFTP server log
- transfer result
- post-transfer reboot behavior

Examples in current source notes:

- TP-Link EAP recovery documentation includes a TFTP path where the PC acts as TFTP server and the EAP acts as TFTP client.
- TP-Link Pharos recovery documentation requires a computer-side TFTP server and a firmware file named `recovery.bin`.

These are series-level workflow examples. They do not prove that an Archer router or Omada gateway uses the same method.

## Passive TFTP

Passive TFTP means the router runs a TFTP server and the computer uploads firmware as a TFTP client.

Do not infer passive TFTP for TP-Link unless a model-specific source, packet capture, or successful lab attempt proves it. Current TP-Link evidence in this repository is stronger for Web Recovery and selected active TFTP examples than for a universal passive TFTP rule.

## Firmware File Boundary

TP-Link firmware selection is high risk because model, hardware version, and region matter.

Before any upload or TFTP transfer, verify:

- exact model name
- hardware version on the label
- region suffix or regional support site
- firmware source URL
- firmware filename and file size
- whether the recovery method expects a normal firmware `.bin` or a renamed file

A Web Recovery page, TFTP request, or upload progress bar does not prove the firmware file is correct.

## Current Evidence Boundary

Current public-source boundaries in this repository:

- TP-Link FAQ 1482: Archer AX series Web Recovery context; not AX55-specific proof by itself.
- TP-Link FAQ 3062: Omada Gateway Emergency Mode context; not universal TP-Link behavior.
- TP-Link FAQ 3186: EAP Recovery Mode with Web Recovery and selected Active TFTP behavior; partial series/listed-model applicability.
- TP-Link FAQ 2954: Pharos Active TFTP workflow with `recovery.bin`; series-level only.
- Archer AX55(CA) v1.0 lab observation: recovery page entry observed; no firmware upload, firmware acceptance, or completed recovery proof.

## App Boundary

Router Recovery for macOS can support TP-Link recovery work at different levels:

| Capability | App status | Boundary |
| --- | --- | --- |
| Record model, hardware version, region, IP settings, and attempt result | App-guidable | Safe as recovery recordkeeping |
| Warn that page entry or upload progress is not completed recovery | App-guidable | Supported by public workflow evidence and lab observations |
| Help preserve firmware source, filename, and result boundaries | App-guidable | Useful before any profile is final |
| Guide a Web Recovery upload | Model-specific only | Requires model/hardware/region evidence and recovery page behavior |
| Run an Active TFTP server with exact filename | Model- or series-specific only | Requires exact filename and request evidence |
| Claim all TP-Link devices share one recovery method | Not allowed | Evidence differs by product line |

## Practical Decision Flow

1. Confirm model, hardware version, and region from the label or official UI.
2. Check whether the official source describes Web Recovery, Emergency Mode, TFTP, or only normal firmware upgrade.
3. If a browser recovery page is documented, use the exact static IP and recovery URL from that source.
4. If TFTP is documented, identify whether the computer is client or server.
5. If an exact filename is required, record it before starting.
6. Keep page entry, upload, firmware acceptance, reboot, and final usable state separate.
7. Do not promote the result beyond the tested model and firmware context.

## Recommended Next TP-Link Work

Near-term TP-Link work should focus on closing evidence gaps, not expanding model count:

1. For Archer AX55, only run a firmware upload/acceptance test with explicit approval and a matching official firmware file.
2. Record whether the recovery page accepts the file, writes firmware, reboots, and returns normal admin access.
3. Keep AX55(CA) v1.0 separate from other AX55 hardware versions and regions.
4. Do not turn Archer AX series evidence into all-Archer guidance.
5. Keep EAP and Pharos Active TFTP examples separate from consumer router Web Recovery behavior.

## Related Pages

- [TP-Link Recovery Guide](tplink-recovery-guide.md)
- [TP-Link Web Recovery Troubleshooting](tplink-web-recovery-troubleshooting.md)
- [TFTP Recovery Guide](tftp-recovery-guide.md)
- [Firmware Selection Guide](firmware-selection-guide.md)
- [Brand Capability Boundary Matrix](brand-capability-boundary-matrix.md)

## Source Notes

- TP-Link FAQ 1482: https://www.tp-link.com/us/support/faq/1482/
- TP-Link FAQ 3062: https://www.tp-link.com/us/support/faq/3062/
- TP-Link FAQ 3186: https://www.tp-link.com/us/support/faq/3186/
- TP-Link FAQ 2954: https://www.tp-link.com/us/support/faq/2954/
