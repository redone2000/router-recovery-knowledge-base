# v0.2.1 Release Notes

Date: 2026-06-06

This maintenance release focuses on contribution flow, support routing, and recovery boundary documentation after the public knowledge base launch.

## Added

- [Submitting Router Recovery Reports](submitting-recovery-reports.md)
- [OpenWrt Failsafe vs TFTP Recovery](openwrt-failsafe-vs-tftp-recovery.md)
- [Brand Capability Boundary Matrix](brand-capability-boundary-matrix.md)
- [ASUS Rescue Mode vs Firmware Restoration](asus-rescue-mode-vs-firmware-restoration.md)
- [TP-Link Web Recovery vs TFTP Recovery](tplink-web-recovery-vs-tftp-recovery.md)

## Improved

- README now links to the official support page for private recovery requests.
- GitHub issue templates now include a private support contact link.
- Recovery reports now use the existing `device-report` triage label.
- Public source index links to the new ASUS and TP-Link boundary guides.
- TP-Link and ASUS guide pages now point to their boundary decision pages.

## Evidence Boundaries

- OpenWrt failsafe is separated from vendor bootloader and TFTP recovery.
- ASUS Rescue Mode, Firmware Restoration, passive TFTP, upload completion, and completed recovery are documented as separate concepts.
- TP-Link Web Recovery, Emergency Mode, Active TFTP, Passive TFTP, and firmware filename requirements are documented as separate concepts.
- Brand and device expansion remains capability-boundary work, not model-count growth.

## Validation

The following local checks passed before release preparation:

- `git diff --check`
- `python3 tools/validate_model_hypotheses.py model_hypotheses`
- `python3 tools/validate_profiles.py incoming reviewed`
- `python3 tools/validate_incidents.py`
- `python3 tools/validate_runtime_attempts.py runtime_attempts`
- `python3 tools/validate_workflows.py`
- `python3 tools/validate_system_links.py --allow-reviewed`
