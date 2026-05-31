# NETGEAR Recovery Guide

NETGEAR recovery behavior varies by model, firmware family, and bootloader state. Some recovery paths involve TFTP, some community workflows use NMRP-related tooling, and some devices are recoverable through normal management or app-based setup flows.

Do not treat "NETGEAR recovery" as one universal method.

## Common NETGEAR Recovery Paths

Possible paths include:

- vendor-documented TFTP recovery
- normal web UI firmware update
- Nighthawk app setup or firmware update
- community NMRP-based recovery workflows
- serial console recovery for advanced cases

Each path has different requirements and evidence strength.

## TFTP Recovery Checklist

For TFTP recovery, confirm:

- exact model
- hardware version
- firmware file format, such as `.chk` or `.img`
- computer static IP
- router recovery IP
- timing window
- whether the router is ready to receive TFTP traffic
- whether the transfer completed
- whether the router later booted successfully

Ping behavior alone is not enough.

## NMRP Boundary

NMRP-based workflows can be useful for some NETGEAR devices, but this project separates community tooling from official vendor recovery instructions.

When documenting NMRP-related recovery, label the evidence clearly:

- official vendor documentation
- upstream tool documentation
- community report
- lab observation
- failed or partial attempt

Do not present NMRP as an official NETGEAR method unless an official source for that device says so.

For detailed source boundaries, see [NETGEAR NMRP Evidence Boundary](netgear-nmrp-evidence-boundary.md).

## Firmware Selection Risks

NETGEAR firmware files are model-specific. A firmware image for a similar-looking model can fail or create a harder recovery problem.

Check:

- device label
- exact model string
- hardware revision
- official support page
- file extension and release notes
- OpenWrt device page, if relevant

## Evidence Boundary

This project preserves failed NETGEAR attempts when they reveal useful details, such as timing windows, `TTL=100` behavior, TFTP timeout patterns, or firmware acceptance uncertainty.

A failed attempt should not become a successful guide. It can still become a useful troubleshooting note.

## Related Tool

Router Recovery for macOS can help preserve recovery attempt details. NETGEAR-specific workflows still require careful model, firmware, and method verification before any claim is treated as guidance.
