# Public Maintenance Review - 2026-06-14

Date: 2026-06-14
Status: public maintenance review

This review checks whether the public knowledge base is discoverable, correctly routed from the Router Recovery support page, and showing early public activity signals.

## Repository Status

- Repository: `https://github.com/redone2000/router-recovery-knowledge-base`
- Visibility: public
- Latest release: `v0.2.1 Recovery Boundary Maintenance`
- Open GitHub issues: none at review time
- Stars: 0
- Forks: 0
- Watchers: 0
- Homepage: `https://www.router-recovery.com/en/support`
- Topics: `asus-router`, `firmware-recovery`, `immortalwrt`, `netgear`, `openwrt`, `tplink`, `router-recovery`, `tftp-recovery`

## Support Page Routing

The live Router Recovery English support page returned HTTP 200 and still includes the public knowledge base section.

Observed support-page signals:

- heading: `Public Knowledge Base`
- GitHub participation copy is present
- link target: `https://github.com/redone2000/router-recovery-knowledge-base`

This confirms the website-to-GitHub support path is still active.

## GitHub Traffic Snapshot

GitHub traffic API returned data during this review.

Views:

- total views: 48
- unique viewers: 4

Referrers:

- DuckDuckGo: 40 views, 1 unique
- github.com: 5 views, 3 uniques

Popular paths:

- repository overview
- ASUS Firmware Restoration evidence links
- ASUS Recovery Guide
- `schema/enums.md`
- `v0.2.1` release page
- `TFTP_GUIDE.md`
- ASUS Rescue Mode vs Firmware Restoration
- Brand Capability Boundary Matrix
- Common Recovery Failures
- Firmware Selection Guide

Clones:

- total clones: 484
- unique cloners: 142

Interpretation:

- The DuckDuckGo referral is an early search/discovery signal.
- Clone counts are likely inflated by tools, bots, or automated fetches and should not be treated as human adoption.
- No stars, forks, or issues means public community participation has not started yet.

## Maintenance Decision

Do not add a large new guide today.

The current public content already covers the main boundary pages:

- OpenWrt failsafe vs TFTP recovery
- ASUS Rescue Mode vs Firmware Restoration
- TP-Link Web Recovery vs TFTP Recovery
- NETGEAR TFTP vs NMRP Recovery

The useful action from this review is small cleanup:

- Add a compatibility note to `TFTP_GUIDE.md`, because it appeared in popular paths and uses older internal wording.

## Next Recommended Work

Next maintenance should focus on one of these:

1. check whether DuckDuckGo/Google discovery increases
2. inspect whether `TFTP_GUIDE.md` continues to receive traffic
3. decide whether legacy root-level docs should be redirected, refreshed, or left as internal references
4. triage any real user issues if they appear
5. avoid new model expansion unless it closes a documented capability gap
