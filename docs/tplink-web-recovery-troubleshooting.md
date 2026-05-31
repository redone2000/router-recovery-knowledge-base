# TP-Link Web Recovery Troubleshooting

TP-Link Web Recovery can look simple: set a static IP, open a local recovery page, select firmware, and upload. The risky part is that several different TP-Link states can look similar in a browser.

This page focuses on troubleshooting and evidence boundaries. It is not a model-specific success guarantee.

## Recovery Page vs Setup Page

A TP-Link page asking you to create an administrator password is usually normal setup or factory-reset behavior. It is not proof that the router is in firmware recovery mode.

More recovery-like signals include:

- a firmware file picker
- an upgrade or upload button
- warning text about choosing the correct firmware
- warning text not to power off during upgrade
- a progress bar for local firmware upload

Even then, the page only proves recovery page entry. It does not prove firmware acceptance or completed recovery.

## Page Entry Does Not Prove Firmware Recovery

Keep these states separate:

- recovery page entry
- firmware file selected
- upload started
- upload completed
- firmware accepted
- flash/write completed
- router rebooted
- admin UI or normal network returned

Only the final usable state should be called completed recovery.

## Wrong Subnet

Many TP-Link recovery workflows use a `192.168.0.x` network, but exact values differ by product line and source.

Examples seen in source notes and observations:

- Archer AX series source note: static client IP and browser-based recovery page at a fixed local IP.
- Omada Gateway emergency mode source note: PC static IP `192.168.0.20/24` and recovery page at `192.168.0.10`.
- AX55(CA) v1.0 lab observation: Mac static IP `192.168.0.10/24` and recovery page at `http://192.168.0.1`.

Do not copy one subnet rule across all TP-Link devices.

## Wrong Hardware Version Or Region

Firmware must match the exact model, hardware version, and region. A web recovery page may appear even when the selected firmware is wrong.

Before upload, check:

- router label
- model shown in the normal web UI, if available
- hardware version
- region suffix or regional support site
- official firmware download page
- file name and release notes

If any of these disagree, stop and resolve the mismatch.

## Upload Accepted vs Recovery Complete

For TP-Link recovery, a browser may show upload progress or upgrade progress before the router is usable again. This is not enough to declare success.

Record:

- file name
- file size
- source URL
- hardware version
- region
- upload result
- wait time
- whether the router rebooted
- whether admin UI returned
- whether DHCP returned
- firmware version after recovery

## Browser Cache Or Stale Page

If the page behavior does not match the expected state, consider:

- browser cache
- old tab still open
- router returned to normal setup page
- computer still using the wrong static IP
- router not actually in recovery mode

Use a fresh browser tab and verify the current router IP before assuming the recovery state changed.

## Button Sequence Confusion

TP-Link button sequences vary by model and source. Some sources mention WPS/Reset-style entry behavior, but model-specific observation matters.

For example, one AX55(CA) v1.0 lab observation found:

- WPS-held power-on did not enter recovery in the observed attempt.
- Reset-held power-on did enter a browser-based recovery page.
- No firmware was uploaded during that observation.

This confirms recovery page entry for that observed unit only. It does not prove firmware acceptance, completed recovery, or applicability to other AX55 variants.

## Evidence You Should Capture

For a useful TP-Link Web Recovery report, include:

- exact model
- hardware version and region
- firmware version before recovery
- firmware file source URL
- filename and file size
- computer static IP
- router recovery page IP
- button sequence
- LED behavior
- screenshot of the recovery page, with private details removed
- upload result
- reboot and post-upload behavior
- final admin UI or network state

## Evidence Boundaries

This project treats official series-level sources as workflow evidence, not model-specific proof. A source can be useful for understanding TP-Link Web Recovery without being enough to create a device profile.

Current public-source boundaries:

- TP-Link FAQ 1482 is useful Archer AX series Web Recovery context, but not AX55 model-specific proof by itself.
- TP-Link FAQ 2571 is useful post-upload caution context, but not recovery-mode proof.
- TP-Link FAQ 3062 is useful Omada Gateway Emergency Mode context, but not a universal TP-Link rule.

## Related Tool

Router Recovery for macOS can help preserve recovery attempt details such as IP settings, firmware choice, and result boundaries. TP-Link firmware selection and recovery claims still need evidence from the exact device workflow.
