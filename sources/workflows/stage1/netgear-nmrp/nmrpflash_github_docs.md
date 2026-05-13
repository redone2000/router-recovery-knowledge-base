# nmrpflash GitHub Documentation Source Note

URL: https://github.com/jclehner/nmrpflash
Title: GitHub - jclehner/nmrpflash: Netgear Unbrick Utility
Workflow target: NMRP
Applicability scope: brand_level / compatible NETGEAR devices
Source type: third_party_repository

## Evidence Topics

- NMRP as a NETGEAR recovery protocol used by `nmrpflash`
- computer-side recovery tool and selected network interface
- orchestrated sequence: start tool, power on router, receive configuration request, upload firmware
- NMRP workflow differs from simple passive TFTP PUT
- post-upload waiting and keep-alive behavior
- macOS is listed as a supported platform for the tool

## Evidence Gaps

- Not official NETGEAR documentation
- Brand-level / compatibility-list evidence, not a reviewed model profile
- Does not provide enough model-specific parameters for profile generation
- R7000 remains incident/research until local recovery is reproducible

## Profile Boundary

This source can support NMRP workflow abstraction and NETGEAR recovery orchestration research. It must not generate model-specific profile guidance without model-level evidence and reviewer approval.
