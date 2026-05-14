# Recovery Hygiene Defaults

Date: 2026-05-14
Status: Stage 1 App guidance defaults

## Purpose

Recovery hygiene defaults are low-cost actions that usually improve the chance of router recovery and reduce avoidable failure.

They are not model-specific facts.

The App may recommend them by default unless a profile, official source, or lab observation provides a clear reason to do something different.

## Core Rule

Use this hierarchy:

```text
model profile evidence
  overrides brand/source evidence
  overrides workflow evidence
  overrides recovery hygiene defaults
```

Defaults should improve the user's recovery environment without pretending to be proven behavior for every router.

## Default Actions

| Default | App guidance | Why it helps | Override when |
| --- | --- | --- | --- |
| Power off before recovery entry | Unplug power and wait about 10 seconds before holding the recovery button and reconnecting power | Clears transient boot state and makes button timing repeatable | Official/profile instruction says not to power cycle or requires a different sequence |
| Direct wired connection | Connect Mac directly to the router LAN port; avoid switches, docks with routing, mesh nodes, or intermediate network devices | Removes path ambiguity, DHCP interference, and packet forwarding surprises | Official/profile requires a specific intermediate device or managed setup |
| Prefer LAN1 / LAN port near WAN | If the model does not specify a port, start with LAN1, commonly the LAN port closest to WAN | Many recovery bootloaders only enable one switch port or behave more reliably on a primary LAN port | Profile specifies another port, WAN port, or any-port behavior |
| Disconnect other router cables | During recovery, disconnect WAN and other LAN clients; keep only Mac-to-router Ethernet | Reduces DHCP, ARP, route, and broadcast noise | Workflow explicitly requires upstream network access |
| Confirm wired service priority | Keep Wi-Fi available when needed, but confirm the wired recovery interface is the first-priority service or owns the route to the recovery IP | Preserves App/network access while reducing wrong-interface routing risk | Profile/App can bind explicitly to the correct interface and tests show service priority is already correct |
| Confirm wired interface ownership | Ensure the selected wired interface owns the static IP before transfer | Avoids sending recovery packets from the wrong interface | DHCP-only workflow with no static IP requirement |
| Use official firmware source | Open official vendor support/download page; verify model, hardware/region, extension, and checksum when available | Prevents wrong firmware and avoids unsafe third-party binaries | A reviewed profile explicitly allows another source |
| Extract archives before selecting firmware | If the download is a zip/archive, select the actual firmware image inside, not the archive | Common user mistake; bootloaders usually reject archives | Profile explicitly says archive upload is accepted |
| Wait after upload | After transfer/upload completes, wait at least 2-3 minutes before judging the result | Flashing and reboot often continue after transfer completion | Profile gives a longer required wait or explicitly proves immediate completion |
| Do not judge by ping alone | Treat ping/TTL as a supporting signal, not proof that recovery service is ready or complete | ICMP can appear before TFTP/web service readiness and can persist during transitional states | Workflow has a stronger service-specific readiness signal |
| Return Mac to DHCP after recovery | After recovery/post-upload phase, switch wired interface back to DHCP and use detected gateway as admin URL | Many routers return to normal LAN subnet after recovery | Profile says static IP must remain or gives a fixed post-recovery IP |
| Record failures as incidents | Repeated timing failures or contradictory behavior become incident candidates, not profile edits | Preserves tacit knowledge without polluting model guidance | Behavior is reproduced and reviewed into profile data |

## App Presentation

The App should phrase defaults as preparation guidance:

- "Recommended before recovery"
- "Helps avoid common recovery failures"
- "Use unless your device-specific instructions say otherwise"

Avoid phrasing defaults as universal facts:

- "All routers require LAN1"
- "Always wait exactly 3 minutes"
- "Ping means recovery is ready"
- "This always preserves configuration"

## TFTP-Specific Defaults

For TFTP workflows, the App should additionally recommend:

- prefer direct Ethernet
- verify the Mac's active interface and IP
- confirm the wired interface has priority or owns the route to the recovery IP
- classify direction before transfer: passive PUT versus active server
- follow the server ACK source port for passive TFTP
- record whether the device uses fixed port 69 or an ephemeral port
- record WRQ/RRQ timing relative to power-on, LED state, and ping/TTL
- avoid arbitrary retry tuning once failures repeat without new evidence

## Profile Interaction

Profiles may override defaults with evidence-backed fields:

- `network_recovery.required_lan_port`
- `network_recovery.client_ip_assignment`
- `network_recovery.client_static_ip`
- `button_recovery.entry_method`
- `button_recovery.press_duration_seconds_min`
- `button_recovery.press_duration_seconds_max`
- `tftp_details.filename_required`
- `tftp_details.server_uses_ephemeral_port`
- `post_upload_behavior.wait_seconds`
- `post_upload_behavior.power_cycle_required`
- `post_upload_behavior.dhcp_after_power_cycle`
- `post_upload_behavior.gateway_ip_as_admin_url`

When the profile is unknown, the App may use hygiene defaults as recommendations, but the runtime attempt should record what actually happened.

## Reference Device Testing

During AX55, ASUS, and RAX40 testing, record whether each default:

- helped
- had no visible effect
- was required
- was harmful
- was contradicted by device-specific behavior

Contradictions should become incident candidates or profile override proposals after review.
