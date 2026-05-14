# Recovery Preflight Checklist

Use this before each reference-device recovery attempt.

This checklist is intentionally practical. It captures default preparation steps that are easy to do and usually improve success rate, while leaving room for device-specific overrides.

After the test, copy and fill one of the runtime JSON templates in `runtime_attempts/templates/`.

## 1. Device And Firmware

- [ ] Exact model confirmed:
- [ ] Hardware version recorded or marked unknown:
- [ ] Current firmware version recorded or marked unknown:
- [ ] Official firmware/support page opened:
- [ ] Firmware selected from official source:
- [ ] Model match confirmed:
- [ ] Region/hardware applicability checked:
- [ ] Archive extracted if needed:
- [ ] Selected firmware filename recorded without local path:
- [ ] File extension recorded:
- [ ] File size recorded:
- [ ] Checksum available:
- [ ] Checksum checked or explicitly skipped:

## 2. Mac Network Setup

- [ ] Ethernet cable connects Mac directly to router:
- [ ] No switch/mesh node/intermediate device:
- [ ] WAN cable disconnected:
- [ ] Other LAN clients disconnected:
- [ ] Mac wired interface identified:
- [ ] Wi-Fi remains available if needed:
- [ ] Wired service priority or route to recovery IP confirmed:
- [ ] Static IP required:
- [ ] Static IP/CIDR set:
- [ ] Local Network permission available if using App:
- [ ] File picker authorization available if using App:

## 3. Recovery Entry

- [ ] Router powered off:
- [ ] Waited about 10 seconds before recovery entry:
- [ ] LAN port used:
- [ ] LAN1 / nearest-WAN default used if no model-specific port:
- [ ] Button used:
- [ ] Hold duration:
- [ ] Power connected while holding button:
- [ ] LED state observed:
- [ ] Mac link state observed:

## 4. Readiness Signals

- [ ] Recovery IP attempted:
- [ ] Ping replied:
- [ ] TTL:
- [ ] Web page reachable:
- [ ] TFTP packet observed:
- [ ] Readiness signal strength: strong / medium / weak / unknown
- [ ] Ping/TTL treated only as supporting evidence:

## 5. TFTP Direction

- [ ] TFTP involved:
- [ ] Passive TFTP PUT: Mac/App client uploads to router server
- [ ] Active TFTP Server: router client pulls from Mac/App server
- [ ] Direction proven by packet/tool behavior:
- [ ] Required filename:
- [ ] WRQ/RRQ timing relative to power-on/LED/ping:
- [ ] ACK source port:
- [ ] Ephemeral port switch observed:
- [ ] Retry pattern:
- [ ] Retry helped / hurt / unknown:

## 6. Transfer

- [ ] Tool used:
- [ ] Transfer started:
- [ ] Transfer completed:
- [ ] Duration:
- [ ] Bytes sent:
- [ ] Block count:
- [ ] Error message:
- [ ] Error category:

## 7. Post-Upload

- [ ] Upload completion treated as not-yet-recovery-complete:
- [ ] Waited 2-3 minutes or profile-specific duration:
- [ ] Reboot observed:
- [ ] Manual power cycle performed:
- [ ] Mac switched back to DHCP:
- [ ] Gateway detected:
- [ ] Admin UI opened:
- [ ] Firmware version after recovery:
- [ ] Configuration retained / reset-like / changed / unknown:

## 8. Output Decision

- [ ] Runtime attempt record needed:
- [ ] Incident candidate needed:
- [ ] Incident generated from runtime attempt:
- [ ] Profile update candidate:
- [ ] App issue found:
- [ ] Schema gap found:
- [ ] Next action:

## Stop Lines

Stop and record an incident instead of continuing to guess when:

- the same failure repeats 3 times with the same setup
- timing tuning becomes arbitrary
- TFTP direction cannot be proven
- model/firmware match is uncertain
- packet behavior contradicts the assumed workflow
- post-upload state remains unclear after a reasonable wait
