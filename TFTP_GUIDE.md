# TFTP Recovery Mode Classification Guide v0.1

## Core Definitions
There are two distinct TFTP recovery modes used by network devices. Correct classification is critical for end users to successfully perform recovery.

### Passive TFTP (passive_tftp_from_router = true)
**Router acts as TFTP server** - The device listens for incoming TFTP connections from the user.

### Active TFTP (active_tftp_to_router = true)
**Router acts as TFTP client** - The device actively requests firmware from a TFTP server run by the user.

---

## Judgment Criteria

### Passive TFTP Identification (Router as Server)
Look for these indicators in documentation or device behavior:

#### Key Indicators
1. **User connects to router's IP** - Documentation instructs user to set their computer to a specific IP (e.g., 192.168.0.10) and connect to the router's IP (e.g., 192.168.0.1)
2. **User initiates TFTP transfer** - User runs TFTP client command to push firmware to router or pull configuration from router
3. **No requirement for user to run TFTP server** - Documentation never mentions setting up a TFTP server on the user's computer
4. **Router listens on fixed IP** - Device uses a pre-configured IP address during recovery mode (common: 192.168.1.1, 192.168.0.1, 192.168.10.1)
5. **HTTP recovery often coexists** - Many devices with passive TFTP also have a web UI recovery mode on the same IP

#### Typical Recovery Flow
```
1. User holds reset button while powering on router
2. Router boots into recovery mode with fixed IP (e.g., 192.168.1.1)
3. User sets computer to static IP in same subnet (e.g., 192.168.1.10)
4. User runs TFTP client to send firmware to router:
   tftp 192.168.1.1 -m binary -c put firmware.bin
5. Router receives firmware and flashes itself
```

#### Common Vendor Examples
- Many TP-Link devices
- Older D-Link devices
- Some ASUS consumer routers

---

### Active TFTP Identification (Router as Client)
Look for these indicators in documentation or device behavior:

#### Key Indicators
1. **User must run TFTP server** - Documentation explicitly tells user to install and run a TFTP server on their computer
2. **User sets specific fixed IP** - User must set their computer to a specific IP (usually 192.168.0.2, 192.168.1.10, or 192.168.31.100) - this is hardcoded in the router's bootloader
3. **Router broadcasts/requests firmware** - Router sends TFTP read requests looking for a specific filename on the user's TFTP server
4. **Specific filename requirement** - Firmware must be named exactly as expected (e.g., `firmware.bin`, `cfe.bin`, `tp_recovery.bin`)
5. **UART boot logs show TFTP attempts** - Bootloader output includes lines like:
   - "Trying TFTP boot..."
   - "Looking for server at 192.168.1.10"
   - "Requesting file firmware.bin"

#### Typical Recovery Flow
```
1. User downloads and runs TFTP server software on their computer
2. User places firmware file with exact required name in TFTP server root
3. User sets computer's IP to the required fixed address (e.g., 192.168.1.10)
4. User powers on router (sometimes holding reset button)
5. Router automatically sends TFTP request to user's IP
6. TFTP server sends firmware file to router
7. Router receives firmware and flashes itself
```

#### Common Vendor Examples
- Ubiquiti devices (often uses 192.168.1.20 as server IP)
- MikroTik RouterBOARD devices
- Many enterprise-grade devices
- Devices using U-Boot bootloader with default TFTP configuration

---

## Dual Mode Support
Some devices support both modes. Set both fields to true if:
- Documentation explicitly describes both TFTP methods
- Multiple sources confirm different TFTP approaches work
- Device automatically falls back between modes

## Common Mistakes to Avoid
1. **IP address confusion**: Just because a device uses 192.168.1.1 doesn't mean it's passive TFTP - always check who initiates the connection
2. **Filename requirement**: Active TFTP almost always requires a specific filename, passive TFTP rarely does
3. **TFTP client vs server**: If user needs to run server software = active TFTP; if user only needs client = passive TFTP
4. **U-Boot assumptions**: Most U-Boot devices use active TFTP, but some custom builds use passive

## Decision Tree
```
Is TFTP recovery mentioned?
├─ No → Both fields = null
└─ Yes
   ├─ Does documentation tell user to RUN a TFTP server?
   │  ├─ Yes → active_tftp_to_router = true
   │  └─ No → active_tftp_to_router = false
   └─ Does documentation tell user to CONNECT TO router via TFTP client?
      ├─ Yes → passive_tftp_from_router = true
      └─ No → passive_tftp_from_router = false
```

## Example Verifications
### Example 1: Active TFTP
> "Set your computer to 192.168.1.10, run TFTP server, place firmware.bin in TFTP root, power on router while holding reset."
→ **active_tftp_to_router = true, passive_tftp_from_router = false**

### Example 2: Passive TFTP
> "Set your computer to 192.168.0.10, connect to router at 192.168.0.1, use TFTP client to send firmware.bin to router."
→ **active_tftp_to_router = false, passive_tftp_from_router = true**

### Example 3: Dual Mode
> "You can either run a TFTP server at 192.168.1.10 or connect to 192.168.1.1 to upload firmware via TFTP."
→ **active_tftp_to_router = true, passive_tftp_from_router = true**
