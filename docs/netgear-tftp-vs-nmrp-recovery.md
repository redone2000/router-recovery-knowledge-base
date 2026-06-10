# NETGEAR TFTP vs NMRP Recovery

NETGEAR recovery discussions often mix official TFTP instructions, third-party NMRP tooling, and model-specific timing incidents.

These are different evidence types. Keep them separate before turning any NETGEAR behavior into app guidance or public recovery instructions.

## Quick Difference

| Question | Official TFTP | NMRP / nmrpflash |
| --- | --- | --- |
| Source type | NETGEAR support documentation | Third-party tooling and lab/community evidence |
| Typical user action | Use a TFTP client to upload firmware | Run a protocol-aware tool that handles NMRP orchestration |
| Direction | Usually computer-side TFTP client uploads to router | Tool-specific request/response sequence |
| Timing risk | Can be sensitive to boot window and WRQ timing | Tool may automate timing and keep-alive behavior |
| Model guidance | Requires model, hardware, firmware, and successful result evidence | Requires model-level proof and clear non-official labeling |
| App status | App-assisted unless reproducible model evidence exists | Research/documentation-only unless separately validated |

## Official TFTP

Official NETGEAR TFTP sources in this repository describe computer-side TFTP client upload workflows and list R7000 in the applies-to scope.

Useful official TFTP evidence includes:

- exact model listed by NETGEAR
- firmware file type and source URL
- computer static IP
- router recovery IP
- TFTP client workflow
- transfer completion
- final boot and admin UI return

Official TFTP evidence is important, but it is not enough by itself for strong app guidance when local reproduction is unresolved.

## NMRP / nmrpflash

NMRP-based recovery is documented here as NETGEAR-related recovery context, especially through third-party tooling such as `nmrpflash`.

Useful NMRP evidence includes:

- exact model and hardware version
- firmware file source
- operating system and tool version
- interface used
- command used
- request/response or tool log output
- upload result
- post-upload wait behavior
- final admin or network state

NMRP should not be presented as official NETGEAR guidance unless an official NETGEAR source says so for that device.

## R7000 Timing Boundary

R7000 is the current cautionary example in this project:

- official NETGEAR TFTP sources exist
- R7000 is listed in applies-to evidence
- `TTL=100` and ping were observable in lab
- manual macOS TFTP PUT timed out or did not receive ACK in the observed timing window
- nmrpflash completed recovery easily in that test context

This does not prove official TFTP is wrong. It also does not prove NMRP should be used for all R7000 units.

The safe conclusion is:

```text
R7000 remains blocked from reviewed guidance until TFTP recovery is reproduced with stronger timing evidence or NMRP recovery is separately modeled and reviewed.
```

## App Boundary

Router Recovery for macOS can support NETGEAR recovery work at different levels:

| Capability | App status | Boundary |
| --- | --- | --- |
| Record model, firmware source, static IP, timing, and result | App-guidable | Safe as recovery recordkeeping |
| Warn that `TTL=100` is not TFTP readiness | App-guidable | Supported by incident evidence and general recovery boundary |
| Preserve failed TFTP timing attempts | App-guidable | Useful for troubleshooting and future workflow design |
| Guide official TFTP upload | Model-specific App-assisted | Requires reproducible model evidence before strong guidance |
| Guide NMRP / nmrpflash | Documentation-only or research-only | Do not present as official or universal |
| Promote R7000 as stable TFTP guidance | Blocked | Current incident is unresolved |

## Practical Decision Flow

1. Confirm exact NETGEAR model and hardware version.
2. Check whether official NETGEAR TFTP documentation applies to that model.
3. Verify firmware file source, file type, and firmware version scope.
4. If attempting TFTP, record timing, static IP, router IP, and ACK/RRQ/WRQ behavior.
5. Do not treat ping or `TTL=100` as proof that TFTP is ready.
6. If using NMRP tooling, label it as third-party/tool-based evidence unless official documentation supports it.
7. Keep failed timing attempts as useful incidents rather than turning them into success guidance.
8. Call recovery complete only after firmware upload, write/reboot, and usable admin/network state are confirmed.

## Recommended Next NETGEAR Work

Near-term NETGEAR work should focus on resolving workflow uncertainty:

1. Keep R7000 as an incident/legacy timing case, not a reviewed profile.
2. Design a program-assisted TFTP timing test before retesting R7000.
3. Compare R7000 timing against packet traces from nmrpflash only as research evidence.
4. Use RAX40/RAX40v2 as a modern reference target only after source and lab planning are clear.
5. Do not expand NETGEAR model count until TFTP/NMRP boundary handling is stable.

## Related Pages

- [NETGEAR Recovery Guide](netgear-recovery-guide.md)
- [NETGEAR NMRP Evidence Boundary](netgear-nmrp-evidence-boundary.md)
- [TTL=100 Does Not Mean TFTP Is Ready](ttl-100-does-not-mean-tftp-ready.md)
- [TFTP Recovery Guide](tftp-recovery-guide.md)
- [Brand Capability Boundary Matrix](brand-capability-boundary-matrix.md)

## Source Notes

- NETGEAR KB 000059633: https://kb.netgear.com/000059633/How-to-upload-firmware-to-a-NETGEAR-router-using-TFTP-client
- NETGEAR KB 000064624: https://kb.netgear.com/000064624/How-do-I-upload-firmware-to-my-NETGEAR-router-using-TFTP-on-Apple-macOS
- nmrpflash: https://github.com/jclehner/nmrpflash
