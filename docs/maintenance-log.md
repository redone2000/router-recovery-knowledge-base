# Maintenance Log

This log records public maintenance work for Router Recovery Knowledge Base. It is meant to show ongoing upkeep, not marketing activity.

## 2026-06-10

### Added

- NETGEAR TFTP vs NMRP recovery boundary guide.

### Maintainer Notes

- GitHub release status checked: `v0.2.1` remains latest.
- No open GitHub issues were present during maintenance.
- NETGEAR official TFTP KB links and `nmrpflash` source link were reachable during the check.

### Evidence Boundaries

- NETGEAR official TFTP documentation, third-party NMRP tooling, and R7000 incident evidence are documented as separate source categories.
- R7000 remains blocked from reviewed guidance until TFTP timing is reproduced or NMRP recovery is separately modeled and reviewed.
- NETGEAR work remains focused on workflow uncertainty, not model-count expansion.

## 2026-06-06

### Added

- Submitting router recovery reports guide.
- OpenWrt failsafe vs TFTP recovery comparison guide.
- Brand capability boundary matrix.
- ASUS Rescue Mode vs Firmware Restoration boundary guide.
- TP-Link Web Recovery vs TFTP Recovery boundary guide.
- v0.2.1 release notes.

### Maintainer Notes

- Public support routing now separates GitHub issues from private recovery support requests.
- Recovery report issue routing now uses the existing `device-report` triage label.
- The next maintenance focus is source freshness, incoming issue triage, and one NETGEAR boundary follow-up before any broader device expansion.

### Evidence Boundaries

- Public issue reporting now links to official support for private or app-specific requests.
- Brand and device expansion is defined as capability-boundary work, not model-count growth.
- OpenWrt failsafe and vendor bootloader/TFTP recovery are documented as separate paths.
- ASUS Rescue Mode, Firmware Restoration, passive TFTP, and post-upload recovery are documented as separate concepts.
- TP-Link Web Recovery, Emergency Mode, Active TFTP, Passive TFTP, and firmware filename boundaries are documented as separate concepts.

## 2026-05-31

### Added

- ImmortalWrt recovery notes.
- ASUS Firmware Restoration evidence links.
- NETGEAR NMRP evidence boundary page.
- Public source index.
- OpenWrt failsafe recovery guide.
- TTL=100 troubleshooting guide.
- Public maintenance log.
- Router recovery glossary.
- TP-Link Web Recovery troubleshooting guide.

### Repository Metadata

- GitHub repository description, homepage, and topics now identify the project as a public router recovery knowledge base.
- Recovery report issue template now uses the existing `device-report` triage label.

### Maintainer Notes

- The repository is now public as `router-recovery-knowledge-base`.
- `v0.1.0` has been released.
- The OpenAI Codex for Open Source application has been submitted.
- The next maintenance focus is issue triage, evidence-needed tracking, and lightweight SEO expansion.

### Evidence Boundaries

- ImmortalWrt is documented as OpenWrt-related, but firmware images and device support are not treated as interchangeable.
- ASUS official FAQ evidence is documented as workflow-level support unless model-specific proof exists.
- NETGEAR NMRP documentation is separated from official NETGEAR TFTP guidance and from model-specific success claims.
- Public source index separates official workflow evidence, model-scope notes, third-party context, and lab observations.
- OpenWrt failsafe is documented as distinct from vendor bootloader recovery.
- TTL=100 is documented as a signal, not proof of TFTP readiness or completed recovery.
- Glossary terms separate transfer, firmware acceptance, and completed recovery.
- TP-Link Web Recovery documentation separates page entry, firmware upload, firmware acceptance, and completed recovery.
- Commercial app mentions remain optional and secondary.
