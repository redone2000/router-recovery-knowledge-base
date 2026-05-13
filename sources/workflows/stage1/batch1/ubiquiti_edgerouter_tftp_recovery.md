# Ubiquiti EdgeRouter TFTP Recovery Source Note

URL: https://help.uisp.com/hc/en-us/articles/22591244564887-EdgeRouter-TFTP-Recovery
Title: EdgeRouter - TFTP Recovery
Workflow target: Passive TFTP PUT
Applicability scope: brand_level (Ubiquiti EdgeRouter)

## Evidence Topics

- reset button enables TFTP recovery mode
- EdgeRouter runs a TFTP server during recovery
- workstation runs TFTP client
- firmware image is uploaded to the router
- macOS TFTP client commands are documented
- static client IP may be required

## Evidence Gaps

- Brand/series-level, not a single model profile
- Timing requirements are not fully specified
- Does not apply to non-EdgeRouter devices without separate evidence

## Profile Boundary

This source directly supports Passive TFTP PUT workflow abstraction. It must not generate a model profile without model-specific parameters and applicability.
