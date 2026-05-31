# ASUS Firmware Restoration Evidence Links

This page collects public evidence links and local evidence boundaries for ASUS Firmware Restoration, Rescue Mode, and ASUS-oriented recovery workflows.

It is not a universal ASUS recovery recipe. ASUS behavior can vary by model, hardware revision, firmware family, recovery utility, and observed device state.

## How To Use This Page

Use this page to understand what each source can and cannot support:

- official ASUS FAQ pages can support general Rescue Mode and Firmware Restoration workflow concepts
- series-level ASUS pages should not be promoted to all ASUS routers
- lab observations can support the tested unit only
- TFTP direction must be proven by documentation, packet behavior, or tool behavior
- upload completion must be separated from completed recovery

## Official ASUS Sources

### ASUS FAQ 1000814: Rescue Mode / Firmware Restoration

- URL: `https://www.asus.com/ca-en/support/faq/1000814/`
- Local source note: `sources/workflows/stage1/batch1/asus_faq_1000814_rescue_mode.md`
- Scope: brand-level ASUS router workflow context

Evidence topics:

- Firmware Restoration / Rescue Mode workflow
- static client IP `192.168.1.10/24`
- reset-held power-on entry
- slow flashing power LED as Rescue Mode signal
- upload and wait behavior
- restore TCP/IPv4 automatic settings after recovery

Boundary:

- This is not model-specific proof.
- It is Windows-utility oriented.
- It does not prove macOS TFTP behavior by itself.
- It should not generate model profile parameters without model-level evidence.

### ASUS FAQ 1030642: Power LED Flashing / Rescue Mode

- URL: `https://www.asus.com/me-en/support/faq/1030642/`
- Local source note: `sources/workflows/stage1/gap-search/asus-faq-1030642.md`
- Scope: brand-level ASUS router workflow context, with RT-AC68U used as an example

Evidence topics:

- abnormal flashing power LED and Rescue Mode
- static client IP `192.168.1.10/24`
- reset-held power-on entry method
- Firmware Restoration upload flow
- post-upload wait and reboot guidance
- return TCP/IP settings to automatic addressing

Boundary:

- The worked example does not become a reviewed RT-AC68U profile.
- Hardware-version and firmware-version scope remain unknown.
- It does not prove non-Windows behavior.

### ASUS FAQ 1033090: Lyra Rescue Mode

- URL: `https://www.asus.com/support/faq/1033090/`
- Local source note: `sources/workflows/stage1/tplink-asus-batch2/asus-faq-1033090.md`
- Scope: series-level Lyra Mesh WiFi workflow context

Evidence topics:

- Reset-held power-on Rescue Mode entry
- solid purple light as Rescue Mode indication
- static client IP `192.168.1.10/24`
- Firmware Restoration upload flow
- LED changes during upload and reboot
- completion signal for Lyra context

Boundary:

- This is Lyra series evidence, not evidence for all ASUS routers.
- It should support workflow abstraction only unless model-level evidence is added.

## Local Lab Evidence

### ASUS RT-AC86U Rescue Mode TFTP Observation

- Local source note: `sources/stage1/lab/asus_rt_ac86u_rescue_tftp_observation.md`
- Scope: owner lab observation for ASUS RT-AC86U

Observed topics:

- Reset-held power-on Rescue Mode entry
- LAN1 wired recovery path
- rescue IP `192.168.1.1`
- Mac static IP `192.168.1.10/24`
- observed `TTL=100`
- passive TFTP WRQ upload behavior
- ACKs observed from router port `69`
- upload completion separate from completed recovery
- manual power cycle after post-upload wait in observed runs
- mixed configuration retention outcomes

Boundary:

- This is not final profile guidance.
- It must not be generalized to all ASUS routers.
- Configuration retention must not be promised.
- Upload completion must not be called completed recovery.

### ASUS RT-AX86U Reviewed Candidate

- Reviewed candidate: `reviewed/asus-rt-ax86u-1-0-merlin.jsonl`
- Key report: `reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md`
- Scope: ASUS RT-AX86U H/W Ver. 1.0 with ASUSWRT-Merlin evidence

Observed topics:

- Reset-held power-on recovery-like state
- slow-flashing power LED
- `TTL=100` at `192.168.1.1`
- passive TFTP PUT from Mac/App to router `192.168.1.1:69`
- fixed ACK source port `69` in the observed run
- firmware changed after upload, wait, and normal power cycle
- DHCP/admin did not return until normal power cycle after waiting more than 5 minutes
- configuration appeared retained in that single attempt

Boundary:

- Reviewed candidate only, not final.
- Limited to the tested RT-AX86U H/W Ver. 1.0 and ASUSWRT-Merlin context.
- Does not prove stock ASUSWRT behavior.
- Does not prove other hardware revisions, regions, or firmware versions.
- Does not prove configuration retention.
- Does not prove web recovery behavior.

## TFTP Direction Boundary

Some ASUS lab observations support passive TFTP: the router acted as the TFTP server, and the Mac/App acted as the TFTP client uploading firmware.

This does not mean every ASUS router uses passive TFTP. Each model needs evidence from:

- official documentation
- packet capture
- tool behavior
- successful transfer and final usable state

## Post-Upload Boundary

ASUS recovery copy should always separate:

- transfer started
- transfer completed
- firmware write in progress
- reboot or power-cycle stage
- DHCP/admin return
- completed recovery

This is especially important because ASUS lab observations show that transfer completion can happen before the router is usable again.

## Safe Public Wording

Prefer:

```text
ASUS official documentation and lab observations support Rescue Mode / Firmware Restoration as an ASUS recovery workflow, but exact behavior must be verified per model and firmware family.
```

Avoid:

```text
All ASUS routers can be recovered the same way.
```

## Related Tool

Router Recovery for macOS can help preserve ASUS recovery attempt details, including IP settings, firmware file selection, TFTP transfer behavior, and post-upload state. Evidence boundaries still need to be checked against the exact device and firmware.
