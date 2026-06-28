# HANDOFF

Use this file as the startup context for a new Codex thread working on this repository.

Repository: `/Users/YiYuan/Projects/router-recovery-knowledge`
Public GitHub repository: `https://github.com/redone2000/router-recovery-knowledge-base`
Last updated: 2026-06-28
Current branch: `main`
Current stage: public knowledge-base maintenance and evidence-boundary stewardship

## Current Goal

Router Recovery Knowledge Base is a public, evidence-based router recovery documentation and evidence repository.

It is not the source code for the Router Recovery macOS app.

The current goals are:

1. keep a credible public knowledge base for router recovery, TFTP recovery, OpenWrt recovery, and brand-specific recovery boundaries
2. support Router Recovery for macOS indirectly through evidence, terminology, workflow boundaries, and public trust
3. preserve commercial app separation while maintaining open public documentation
4. improve long-term SEO and support deflection without turning the repository into a marketing site
5. maintain evidence boundaries so device-specific claims do not overreach
6. keep the repository useful for OpenAI Codex for Open Source evaluation and future public maintenance

## Current Repository Status

As of this handoff update:

- branch: `main`
- latest known local commit before this handoff: `0014d44 Add weekly public maintenance review for 2026-06-28`
- latest public release: `v0.2.1 Recovery Boundary Maintenance`
- open GitHub issues at the last weekly review: none
- stars/forks/watchers at the last weekly review: 0 / 0 / 0
- public support page route: `https://www.router-recovery.com/en/support`
- public support page still links to GitHub knowledge base
- no known uncommitted user changes existed before this handoff edit
- no known dangerous or destructive changes are pending

## Current Development Phase

The project has moved beyond initial private evidence modeling into public maintenance.

Earlier Stage 1 reference-device evidence work still matters, but the active public lane is now:

```text
public KB foundation
  -> evidence-boundary guides
  -> support routing
  -> weekly/biweekly public maintenance reviews
  -> small corrections driven by traffic, support cases, or issues
```

Do not restart broad model expansion.

## Completed Public Work

Public launch and repository setup:

- public GitHub repository is `router-recovery-knowledge-base`
- repository is public
- GitHub About metadata is set
- homepage points to Router Recovery support page
- topics include `router-recovery`, `tftp-recovery`, `openwrt`, `immortalwrt`, `firmware-recovery`, `asus-router`, `tplink`, and `netgear`
- documentation license: CC BY 4.0
- code/schema/tooling license: MIT
- contribution, security, code of conduct, issue templates, and PR template exist
- GitHub issue template routes private support to official support page
- releases exist: `v0.1.0`, `v0.2.0`, `v0.2.1`

OpenAI Codex for Open Source:

- application was submitted on 2026-05-30
- repository submitted: `https://github.com/redone2000/router-recovery-knowledge-base`
- role submitted: primary maintainer
- confirmation screen indicated OpenAI received the submission
- do not claim selection or acceptance unless separately confirmed
- exact personal/account application fields are not recorded in this public repository; verify from the original form confirmation or private notes if needed

Website support routing:

- official website support pages were updated in the website repository, not this repo
- English support page verified live multiple times
- support page contains `Public Knowledge Base` section and links to GitHub
- do not modify website from this repository

## Completed Documentation Themes

Public user-facing guides now include:

- TFTP Recovery Guide
- OpenWrt Recovery Guide
- ImmortalWrt Recovery Notes
- Firmware Selection Guide
- Common Recovery Failures
- Router Recovery Glossary
- OpenWrt Failsafe Guide
- OpenWrt Failsafe vs TFTP Recovery
- TTL=100 Does Not Mean TFTP Is Ready
- ASUS Recovery Guide
- ASUS Rescue Mode vs Firmware Restoration
- ASUS Firmware Restoration Evidence Links
- TP-Link Recovery Guide
- TP-Link Web Recovery vs TFTP Recovery
- TP-Link Web Recovery Troubleshooting
- NETGEAR Recovery Guide
- NETGEAR TFTP vs NMRP Recovery
- NETGEAR NMRP Evidence Boundary
- Public Source Index
- Submitting Router Recovery Reports

Public maintenance records include:

- Maintenance Log
- v0.2.1 Release Notes
- Public Maintenance Review - 2026-06-14
- Public Maintenance Review - 2026-06-21
- Public Maintenance Review - 2026-06-28

## Key Design Decisions

Core evidence decisions:

- this repository is a Recovery Knowledge System, not an arbitrary tutorial dump
- public docs must separate concepts, evidence, and confidence boundaries
- TFTP direction must be proven or explicitly marked unknown
- `TTL=100` is a clue, not proof of TFTP readiness or recovery success
- upload completion is not recovery completion
- firmware acceptance, flash/write completion, reboot, DHCP return, and usable admin UI are separate states
- brand-level or series-level sources do not create model-specific profiles
- lab observations apply only to the tested device and firmware context
- failed attempts are useful evidence when they reveal timing, network, firmware, or device-state behavior
- AI-assisted expansion belongs in `model_hypotheses/`, not in `incoming/`, `reviewed/`, or `final/`
- `final/` must not be written without a separate explicit final approval process

Commercial boundary decisions:

- Router Recovery for macOS remains separate commercial software
- the app source is not open sourced here
- this repository can mention the app as optional related tooling, but public knowledge must remain useful without the app
- GitHub issues are for public recovery reports, corrections, source links, and evidence gaps
- private support and app-specific support should route to `https://www.router-recovery.com/en/support`

Public maintenance decisions:

- do not chase stars, forks, or artificial activity
- do not add large guides merely to appear active
- public maintenance should be evidence-backed and low noise
- after 2026-06-28, weekly reviews should likely move to biweekly unless real activity appears
- consider website-side SEO before adding more GitHub-only documentation

## Device And Brand Boundaries

### ASUS

Current public boundary:

- ASUS Rescue Mode, Firmware Restoration, passive TFTP, upload completion, and completed recovery are separate concepts
- official ASUS FAQs are useful as brand/series workflow evidence
- RT-AC86U lab data remains incoming/observed, not final
- RT-AX86U H/W Ver. 1.0 ASUSWRT-Merlin evidence is reviewed-candidate only, not final

Do not:

- generalize RT-AC86U or RT-AX86U behavior to all ASUS routers
- merge RT-AC86U and RT-AX86U facts
- claim stock ASUSWRT behavior from ASUSWRT-Merlin-only evidence
- promise configuration retention
- treat upload completion as recovery completion

### TP-Link

Current public boundary:

- Web Recovery, Emergency Mode, Active TFTP, Passive TFTP, and firmware filename requirements are separate concepts
- TP-Link FAQ 1482 is Archer AX series context, not AX55-specific proof by itself
- Archer AX55(CA) v1.0 has recovery-page entry observation only
- firmware upload/acceptance/recovery completion has not been proven for AX55

Do not:

- treat recovery page entry as completed recovery
- generalize AX55(CA) v1.0 to all AX55 regions/hardware revisions
- claim TFTP direction for AX55 without direct evidence
- turn EAP/Pharos Active TFTP examples into consumer Archer guidance

### NETGEAR

Current public boundary:

- official NETGEAR TFTP documentation, third-party NMRP/nmrpflash tooling, and R7000 incident evidence are separate source categories
- R7000 has official TFTP source evidence but local manual TFTP timing remains unresolved
- R7000 remains blocked from reviewed guidance
- nmrpflash succeeded in one R7000 incident context, but NMRP is not official NETGEAR guidance unless official source evidence proves it
- RAX40/RAX40v2 has official management/update baseline only, not recovery proof

Do not:

- promote R7000 to reviewed
- claim NMRP is official NETGEAR recovery
- claim NMRP is universally better than TFTP
- treat `TTL=100` as TFTP readiness
- treat RAX40 management/update behavior as recovery behavior

### OpenWrt / ImmortalWrt

Current public boundary:

- OpenWrt failsafe is OS-level recovery, not vendor bootloader recovery
- OpenWrt/ImmortalWrt firmware images and device support are related but not interchangeable
- device-specific OpenWrt pages or vendor pages still matter for recovery behavior

Do not:

- treat OpenWrt support as proof of vendor TFTP direction
- treat failsafe as a universal unbrick method
- recommend firmware without model, hardware version, region, and image-type checks

## Public Review Findings

### 2026-06-14

- GitHub views: 48
- unique viewers: 4
- DuckDuckGo referrer appeared: 40 views, 1 unique
- clones: 484 / 142 uniques, likely tool/bot-influenced
- no stars, forks, watchers, or issues
- `TFTP_GUIDE.md` appeared in popular paths and received a public reader note

### 2026-06-21

- views: 49
- unique viewers: 4
- DuckDuckGo remained but did not grow
- no Google or `router-recovery.com` referrer
- clones: 209 / 72 uniques, down
- no stars, forks, watchers, or issues
- decision: continue observation, do not add large docs

### 2026-06-28

- views: 4
- unique viewers: 3
- referrers: none reported
- clones: 134 / 59 uniques, down again
- popular paths: repository overview and `/pulls`
- `TFTP_GUIDE.md` no longer appeared in popular paths
- no stars, forks, watchers, or issues
- decision: move toward lower-frequency public review and consider website-side SEO before more GitHub-only docs

## Current Problems

- Public community participation has not started: no issues, stars, forks, or watchers.
- Search/referral traffic is very small and declined by 2026-06-28.
- GitHub traffic did not show `router-recovery.com` as a referrer, despite the support page link being live.
- GitHub-only documentation may not be enough for SEO; website-side SEO work may matter more.
- Older root-level docs such as `TFTP_GUIDE.md` still exist and may need occasional routing notes if they receive traffic.
- Some project status files are older than current public-maintenance state; `HANDOFF.md` should be treated as the freshest startup document after this update.

## Risks And Uncertainties

- It is uncertain whether Google has indexed the public knowledge base meaningfully.
- GitHub clone counts may be heavily automated and should not be interpreted as adoption.
- Low stars/forks may reduce open-source social proof, but this repo's primary value remains public trust, SEO, support routing, and evidence maintenance.
- Codex for Open Source application outcome is unknown.
- Device-profile evidence must not be overpromoted to app guidance.
- Website traffic/referral data may need website analytics access; GitHub traffic alone is incomplete.

## Remaining Tasks

Do next only when evidence or timing justifies it:

1. Continue public maintenance reviews, preferably biweekly unless real activity appears.
2. Watch for GitHub issues, public recovery reports, or support cases that can become anonymized docs.
3. Compare GitHub traffic against previous reviews.
4. Check whether `router-recovery.com`, Google, or DuckDuckGo appear as referrers.
5. If a guide page becomes popular, improve that page surgically.
6. Consider website-side SEO pages that summarize and link to GitHub knowledge base.
7. Keep source freshness checks for important vendor pages.
8. Do not create `v0.2.2` unless several real maintenance items accumulate.

## Avoid Repeating These Directions

- Do not continue weekly GitHub-only content additions without traffic, issue, or support signals.
- Do not expand by router model count.
- Do not use stars/forks chasing as a project goal.
- Do not market the commercial app aggressively inside public docs.
- Do not treat GitHub clone counts as human adoption.
- Do not promote `incoming/` or `reviewed/` candidates to `final/`.
- Do not create model-specific app guidance from brand-level or series-level sources.
- Do not perform public releases, form submissions, or account changes without explicit Owner confirmation.

## Important Files And Directories

Startup and governance:

- `README.md`
- `HANDOFF.md`
- `PROJECT_STATUS.md`
- `RULES.md`
- `WORKFLOW.md`
- `CHANGELOG.md`
- `docs/maintenance-log.md`
- `docs/brand-capability-boundary-matrix.md`
- `docs/recovery_priority_strategy.md`
- `docs/evidence_lifecycle.md`
- `docs/recovery_knowledge_system_architecture.md`

Public maintenance:

- `docs/public-maintenance-review-2026-06-14.md`
- `docs/public-maintenance-review-2026-06-21.md`
- `docs/public-maintenance-review-2026-06-28.md`
- `docs/release-notes-v0.2.1.md`

Public source and support routing:

- `docs/public-source-index.md`
- `docs/submitting-recovery-reports.md`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/recovery-report.md`
- `.github/ISSUE_TEMPLATE/documentation-correction.md`

Boundary guides:

- `docs/openwrt-failsafe-vs-tftp-recovery.md`
- `docs/asus-rescue-mode-vs-firmware-restoration.md`
- `docs/tplink-web-recovery-vs-tftp-recovery.md`
- `docs/netgear-tftp-vs-nmrp-recovery.md`
- `docs/ttl-100-does-not-mean-tftp-ready.md`
- `docs/common-recovery-failures.md`
- `docs/firmware-selection-guide.md`

Evidence and profiles:

- `incoming/`
- `reviewed/`
- `incidents/`
- `runtime_attempts/`
- `model_hypotheses/`
- `data/`
- `sources/`
- `reports/`

Schemas and validation:

- `schema/recovery_profile.schema.json`
- `schema/recovery_incident.schema.json`
- `schema/recovery_workflow.schema.json`
- `schema/app_runtime_attempt.schema.json`
- `schema/model_hypothesis.schema.json`
- `tools/validate_model_hypotheses.py`
- `tools/validate_profiles.py`
- `tools/validate_incidents.py`
- `tools/validate_runtime_attempts.py`
- `tools/validate_workflows.py`
- `tools/validate_system_links.py`

## Recommended Validation Commands

Run these before committing meaningful changes:

```text
git diff --check
python3 tools/validate_model_hypotheses.py model_hypotheses
python3 tools/validate_profiles.py incoming reviewed
python3 tools/validate_incidents.py
python3 tools/validate_runtime_attempts.py runtime_attempts
python3 tools/validate_workflows.py
python3 tools/validate_system_links.py --allow-reviewed
```

## New Session Recommended Reading Order

1. `AGENTS.md` if present in the environment
2. `README.md`
3. `HANDOFF.md`
4. `docs/maintenance-log.md`
5. latest public maintenance review, currently `docs/public-maintenance-review-2026-06-28.md`
6. `docs/brand-capability-boundary-matrix.md`
7. `docs/public-source-index.md`
8. `RULES.md`
9. `WORKFLOW.md`

Then inspect:

```text
git status --short
git branch --show-current
git log --oneline -8
```

## Suggested Next Step

Do not immediately write another large document.

Recommended next maintenance action:

```text
Schedule or perform the next public review no earlier than two weeks after 2026-06-28 unless a real GitHub issue, support case, or search/referral spike appears.
```

If the Owner asks what to do next, recommend:

1. biweekly public review instead of weekly
2. website-side SEO review before more GitHub-only docs
3. no release unless multiple real maintenance changes accumulate
4. no model expansion without user evidence or a documented capability gap

## New Session Prompt

Use this prompt to start a new Codex thread:

```text
You are working in /Users/YiYuan/Projects/router-recovery-knowledge.

Read AGENTS.md if present, then README.md, HANDOFF.md, docs/maintenance-log.md, and the latest public maintenance review. Then inspect git status and the current branch.

This repository is the public Router Recovery Knowledge Base, not the Router Recovery macOS app source. Preserve the commercial app boundary.

Current phase: public knowledge-base maintenance and evidence-boundary stewardship. The main public repository is https://github.com/redone2000/router-recovery-knowledge-base. Latest release is v0.2.1 unless GitHub says otherwise.

Do not start broad model expansion. Do not create large new guides unless there is real user feedback, a GitHub issue, support evidence, or a clear search-path gap.

Important rules:
- Never write final/.
- Do not promote incoming/ or reviewed/ without explicit Owner approval.
- Do not infer TFTP direction.
- Do not treat ping/TTL as proof.
- Do not label upload completion as recovery success.
- Do not treat brand-level or series-level sources as model-specific proof.
- Keep public app mentions optional and secondary.
- Do not perform public releases, form submissions, or account changes without explicit Owner confirmation.

Recommended first action:
Compare the latest public maintenance review against current GitHub traffic, issues, release status, and support-page routing. If there is no real activity or clear gap, record a short maintenance review only; do not force new content.
```
