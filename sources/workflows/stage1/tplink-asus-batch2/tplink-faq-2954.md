# TP-Link FAQ 2954 Pharos Firmware Recovery Source Note

URL: https://www.tp-link.com/us/support/faq/2954/
Title: How to use firmware recovery on the Pharos products
Workflow target: Active TFTP Server
Applicability scope: series_level (Pharos Outdoor Products)
Source type: official_documentation

## Evidence Topics

- computer-side TFTP server software
- firmware file renamed exactly to `recovery.bin`
- static client IP `192.168.0.100/24`
- reset-hold timing until transfer appears
- wired connection requirement
- automatic reboot after transfer

## Evidence Gaps

- Series-level evidence, not a reviewed model profile
- Model-specific applicability remains unknown
- Hardware-version scope remains unknown

## Profile Boundary

This source can support Active TFTP workflow abstraction for TP-Link Pharos recovery. It must not generate model-specific profile guidance without model-level evidence and reviewer approval.
