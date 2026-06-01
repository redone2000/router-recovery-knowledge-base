# Router Recovery Knowledge Base

An open, evidence-based knowledge base for router firmware recovery, TFTP recovery, OpenWrt recovery, and device-specific troubleshooting.

This repository is not the source code for the Router Recovery macOS app. It contains public documentation, evidence notes, troubleshooting guides, schemas, and validation tooling for safer router recovery work. Commercial app development remains separate.

## Start Here

- [TFTP Recovery Guide](docs/tftp-recovery-guide.md)
- [OpenWrt Recovery Guide](docs/openwrt-recovery-guide.md)
- [ImmortalWrt Recovery Notes](docs/immortalwrt-recovery-notes.md)
- [Firmware Selection Guide](docs/firmware-selection-guide.md)
- [Common Recovery Failures](docs/common-recovery-failures.md)
- [Submitting Router Recovery Reports](docs/submitting-recovery-reports.md)
- [Router Recovery Glossary](docs/router-recovery-glossary.md)
- [OpenWrt Failsafe Guide](docs/openwrt-failsafe-guide.md)
- [OpenWrt Failsafe vs TFTP Recovery](docs/openwrt-failsafe-vs-tftp-recovery.md)
- [TTL=100 Does Not Mean TFTP Is Ready](docs/ttl-100-does-not-mean-tftp-ready.md)
- [ASUS Recovery Guide](docs/asus-recovery-guide.md)
- [ASUS Firmware Restoration Evidence Links](docs/asus-firmware-restoration-evidence-links.md)
- [TP-Link Recovery Guide](docs/tplink-recovery-guide.md)
- [TP-Link Web Recovery Troubleshooting](docs/tplink-web-recovery-troubleshooting.md)
- [NETGEAR Recovery Guide](docs/netgear-recovery-guide.md)
- [NETGEAR NMRP Evidence Boundary](docs/netgear-nmrp-evidence-boundary.md)
- [Public Source Index](docs/public-source-index.md)

## What This Project Covers

- TFTP recovery workflows
- OpenWrt and ImmortalWrt recovery notes
- ASUS Rescue Mode recovery notes
- TP-Link Web Recovery notes
- NETGEAR TFTP and NMRP-related notes
- Firmware selection and region or hardware-version checks
- Common recovery failures and troubleshooting
- Evidence-backed device recovery profiles

## What This Project Does Not Do

- It does not publish the Router Recovery app source code.
- It does not promise that a firmware upload equals a complete recovery.
- It does not generalize one hardware revision to every device variant.
- It does not treat AI-generated model lists as verified recovery instructions.
- It does not copy vendor documentation into this repository.

## Core Principles

- Recovery claims need evidence.
- TFTP direction must be proven or clearly marked unknown.
- Upload completion is not the same as recovery completion.
- Failed attempts are useful when they reveal timing, network, firmware, or device-state behavior.
- Device-specific pages must separate confirmed facts from assumptions.

## Evidence Levels

- `official`: documented by the vendor or upstream project.
- `lab-observed`: reproduced in hands-on testing.
- `community-reported`: reported by users but not independently verified here.
- `hypothesis`: plausible, but not enough for user-facing recovery instructions.

## Repository Layout

```text
router-recovery-knowledge-base/
├── docs/             # Public guides and recovery explanations
├── incoming/         # Draft recovery profiles awaiting review
├── reviewed/         # Reviewed profile candidates, not final user promises
├── incidents/        # Failure cases and lab incidents with useful recovery signals
├── model_hypotheses/ # AI-assisted expansion seeds, not recovery guidance
├── schema/           # JSON schemas and enumerations
├── sources/          # Source notes and evidence excerpts
├── data/             # Source indexes and workflow indexes
├── reports/          # Review reports and project decisions
└── tools/            # Validation and export scripts
```

## Using Router Recovery for macOS

The public guides in this repository are written so users can understand recovery concepts and manual steps. If you want a guided macOS tool for TFTP-oriented recovery workflows and local recovery attempt records, see Router Recovery for macOS.

The app is optional. This knowledge base should remain useful even if you never use the app.

## Contributing

Contributions are welcome, especially:

- verified recovery steps
- device-specific observations
- corrections to firmware version or hardware revision notes
- failure cases with logs or screenshots
- links to official documentation

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting recovery claims.
For user-facing report guidance, see [Submitting Router Recovery Reports](docs/submitting-recovery-reports.md).

## Support

Use GitHub issues for public recovery reports, documentation corrections, source additions, and evidence gaps.

For private support requests or recovery details that should not be published publicly, use the official support page:

https://www.router-recovery.com/en/support

## Maintainer Notes

- [OpenAI Codex for Open Source Application Notes](docs/openai-codex-for-oss-application.md)
- [Public Launch Checklist](docs/public-launch-checklist.md)
- [Maintenance Log](docs/maintenance-log.md)

## License

Documentation is licensed under [CC BY 4.0](LICENSE). Code, schemas, and tooling are licensed under [MIT](LICENSE-CODE).
