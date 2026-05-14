# Runtime Attempt Quick Note Template

Use this during live testing. After the test, convert the notes into `schema/app_runtime_attempt.schema.json` or an incident candidate.

## Identity

- Date:
- Tester:
- Device:
- Model:
- Hardware version:
- Firmware before:
- Firmware after:
- Profile ID, if any:
- Workflow tested:

## Firmware

- Official download/support URL:
- Filename, no local path:
- Extension:
- Size:
- Checksum available:
- Checksum checked:
- Model match confirmed:

## Mac / Network Preflight

- Power-off wait before entry:
- Direct Mac-to-router Ethernet:
- WAN/other LAN cables disconnected:
- Mac interface:
- Wi-Fi kept available:
- Wired service priority / route confirmed:
- Local Network permission:
- File picker authorized:
- Static IP set:
- Client IP/CIDR:
- Notes:

## Recovery Entry

- LAN port:
- LAN1/nearest-WAN default used:
- Button:
- Hold seconds:
- LED state:
- Ping replied:
- TTL:
- Recovery IP / page:
- Service probe result:

## Transfer

- Method:
- TFTP direction, if applicable:
- Mac/App role:
- Router role:
- Tool:
- Started:
- Completed:
- First WRQ/RRQ timing:
- Required filename:
- Duration:
- Bytes sent:
- Block count:
- ACK source port:
- Ephemeral port switch observed:
- Retry pattern:
- Retry helped / hurt / unknown:
- Error message:
- Error category:

## Post Upload

- Wait completed:
- Wait seconds:
- Waited 2-3 minutes before judging result:
- Power cycle performed:
- DHCP restored:
- Gateway:
- Admin UI opened:
- Notes:

## Outcome

- Success / failed / partial / unknown:
- Configuration retained / reset-like / changed / unknown:
- User-visible result:
- Incident candidate:
- Incident reason:

## Follow-Up

- Profile update candidate:
- Incident needed:
- App issue found:
- Schema gap found:
- Next action:
