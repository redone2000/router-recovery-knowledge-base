# Public Source Index

This index links to public recovery sources, local source notes, and evidence boundaries used by Router Recovery Knowledge Base.

It is not a list of verified device profiles. A source can be useful without being strong enough to generate model-specific recovery guidance.

## Evidence Use Rules

- Official source does not automatically mean model-specific proof.
- Series-level source does not apply to every model in that series.
- Brand-level source supports workflow abstraction only unless model evidence exists.
- Third-party tooling documentation can explain a workflow but should not be treated as vendor approval.
- Social media reports are context only unless independently verified.
- Lab observations apply only to the tested device and firmware context.

## Official Workflow Sources

| Vendor | Source | Scope | Workflow topics | Public boundary |
| --- | --- | --- | --- | --- |
| TP-Link | [FAQ 1482](https://www.tp-link.com/us/support/faq/1482/) | Archer AX series-level | Web Recovery, static IP, recovery page upload | Not AX55-specific by itself; no profile generation |
| TP-Link | [FAQ 2571](https://www.tp-link.com/us/support/faq/2571/) | brand-level context | post-upload waiting, firmware match, region/hardware version caution | Firmware-update context only; not recovery-mode proof |
| TP-Link | [FAQ 3062](https://www.tp-link.com/us/support/faq/3062/) | Omada Gateway series-level | Emergency Mode, web recovery, static IP, post-upload reboot | Not universal TP-Link guidance |
| TP-Link | [FAQ 3186](https://www.tp-link.com/us/support/faq/3186/) | EAP series-level | web recovery, HTTP-only page, active TFTP path | Partial model applicability; no profile generation |
| TP-Link | [FAQ 2954](https://www.tp-link.com/us/support/faq/2954/) | Pharos series-level | active TFTP server, required filename, static IP | Series-level only |
| ASUS | [FAQ 1000814](https://www.asus.com/ca-en/support/faq/1000814/) | ASUS brand-level | Rescue Mode, Firmware Restoration, static IP, post-upload wait | Windows utility oriented; not model-specific |
| ASUS | [FAQ 1030642](https://www.asus.com/me-en/support/faq/1030642/) | ASUS brand-level, RT-AC68U example | Rescue Mode, LED behavior, Firmware Restoration, post-upload wait | Example model does not become a profile |
| ASUS | [FAQ 1033090](https://www.asus.com/support/faq/1033090/) | Lyra series-level | Rescue Mode, LED states, Firmware Restoration, post-upload behavior | Lyra evidence only, not all ASUS routers |
| NETGEAR | [KB 000059633](https://kb.netgear.com/000059633/How-to-upload-firmware-to-a-NETGEAR-router-using-TFTP-client) | R7000 listed in applies-to | passive TFTP upload from computer-side client | Hardware/firmware scope unknown |
| NETGEAR | [KB 000064624](https://kb.netgear.com/000064624/How-do-I-upload-firmware-to-my-NETGEAR-router-using-TFTP-on-Apple-macOS) | R7000 listed in applies-to | macOS TFTP client upload workflow | Hardware/firmware scope unknown |
| Ubiquiti | [EdgeRouter TFTP Recovery](https://help.uisp.com/hc/en-us/articles/22591244564887-EdgeRouter-TFTP-Recovery) | EdgeRouter brand/series-level | passive TFTP PUT, router as TFTP server, workstation as TFTP client | Workflow pattern only without model-level evidence |

## Model-Scope Source Notes

| Vendor | Local note | Scope | What it supports | What it does not support |
| --- | --- | --- | --- | --- |
| TP-Link | `sources/stage1/batch1/tplink_archer_ax55_download.md` | Archer AX55 download page | model and hardware-version selection context | recovery procedure |
| NETGEAR | `sources/stage1/batch1/netgear_kb_000059633.md` | R7000 listed in applies-to | passive TFTP source indexing | reviewed/final profile without scope review |
| NETGEAR | `sources/stage1/batch2/netgear_kb_000064624_macos.md` | R7000 listed in applies-to | macOS TFTP source indexing | hardware/firmware applicability |
| ASUS | `sources/stage1/official/asus_rt_ac86u_firmware_download_page.md` | RT-AC86U firmware page | model-specific firmware source context | recovery behavior by itself |

## Third-Party And Community Context

| Vendor | Source | Scope | Use | Boundary |
| --- | --- | --- | --- | --- |
| NETGEAR | [nmrpflash](https://github.com/jclehner/nmrpflash) | NETGEAR-compatible devices, third-party repository | NMRP workflow mechanics and tooling context | not official NETGEAR documentation; no model profile by itself |
| NETGEAR | Reddit WNDR3400 NMRP report | WNDR3400 social-media report | context for one community attempt | not independently verified; no workflow or profile update by itself |

## Lab Observations

| Device | Local note | Evidence status | Boundary |
| --- | --- | --- | --- |
| ASUS RT-AC86U | `sources/stage1/lab/asus_rt_ac86u_rescue_tftp_observation.md` | owner lab observation | incoming/experimental evidence only; not final guidance |
| ASUS RT-AX86U H/W 1.0 | `reviewed/asus-rt-ax86u-1-0-merlin.jsonl` and `reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md` | reviewed candidate | scoped to tested unit and ASUSWRT-Merlin context; not final |
| TP-Link Archer AX55(CA) v1.0 | `reports/tplink_archer_ax55_recovery_entry_observation_summary_2026-05-17.md` | recovery page entry observed | no firmware upload or completed recovery proof |
| NETGEAR R7000 | `incidents/lab/netgear_r7000_ttl100_tftp_timeout_2026-05-13.json` | blocked incident | `TTL=100` did not prove successful TFTP recovery |

## Public Documentation Pages Using These Sources

- [ASUS Firmware Restoration Evidence Links](asus-firmware-restoration-evidence-links.md)
- [ASUS Rescue Mode vs Firmware Restoration](asus-rescue-mode-vs-firmware-restoration.md)
- [TP-Link Web Recovery vs TFTP Recovery](tplink-web-recovery-vs-tftp-recovery.md)
- [TP-Link Web Recovery Troubleshooting](tplink-web-recovery-troubleshooting.md)
- [NETGEAR Recovery Guide](netgear-recovery-guide.md)
- [NETGEAR TFTP vs NMRP Recovery](netgear-tftp-vs-nmrp-recovery.md)
- [NETGEAR NMRP Evidence Boundary](netgear-nmrp-evidence-boundary.md)
- [TFTP Recovery Guide](tftp-recovery-guide.md)
- [TTL=100 Does Not Mean TFTP Is Ready](ttl-100-does-not-mean-tftp-ready.md)

## Contribution Guidance

When adding a source, include:

- source URL
- source type
- vendor
- model or series scope
- recovery workflow topics
- evidence gaps
- whether profile generation is allowed
- why the source should or should not update user-facing guidance

Do not copy full vendor pages into this repository. Link to official documentation and summarize only the relevant recovery behavior and evidence boundary.
