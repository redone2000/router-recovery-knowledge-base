# Claude Code Stage 1 ASUS RT-AC86U Incoming Draft Review

You are the Knowledge Architect / Schema Reviewer for the Router Recovery Knowledge project.

## Agent Identity Gate

This task is intended only for: Claude Code.

If you are not this agent, stop immediately and reply only:

WRONG_AGENT_TASK
Expected agent: Claude Code
Your role: [your actual role if known]
No action performed.

Do not reinterpret, adapt, or partially execute this task if your agent identity does not match.

## Current Stage

Stage 1 incoming draft evidence-quality review.

This review is focused only on the ASUS RT-AC86U lab-observation incoming draft and the related schema additions.

## Scope

Review only.

Do not collect new sources.
Do not browse the web.
Do not generate or edit profiles.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/incoming/asus-rt-ac86u-unknown-unknown.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/sources/stage1/lab/asus_rt_ac86u_rescue_tftp_observation.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/schema_extension_asus_rt_ac86u_lab_observation.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/stage1_schema_migration_2026-05-12.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/coverage-stage1-incoming-drafts-after-migration-2026-05-12.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_profile.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/enums.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`

## Facts To Review

The incoming draft is based on Owner-supplied local lab testing, not public vendor documentation.

The draft currently claims:

- model: `ASUS RT-AC86U`
- recovery method: `tftp_passive`
- recovery family: `asus`
- client action: Mac-side TFTP WRQ upload to router
- entry method: `reset_hold_power_on`
- required LAN port: LAN1 nearest the WAN port
- rescue IP: `192.168.1.1`
- client static IP: `192.168.1.10/24`
- observed ping TTL: `100`
- firmware format: official ASUS `.w`
- TFTP mode: `octet`
- filename required: `false` based on observed `test.w` acceptance
- server transfer-port behavior: fixed port 69 observed, no ephemeral transfer port observed
- post-upload behavior: wait about 180 seconds, then manual power cycle required
- after power cycle: switch Mac back to DHCP, use DHCP gateway IP as admin URL
- configuration outcome: mixed; both retained and factory-reset-like outcomes observed
- firmware downgrade/overwrite: observed
- confidence: `medium`

## Review Questions

1. Is `personal_testing` acceptable as the source type for this incoming draft?
2. Is `confidence_level: medium` appropriate, too high, or too low?
3. Does unknown hardware/firmware scope require confidence to be lower than medium?
4. Is `tftp_passive` justified by the local observation?
5. Are the new schema groups appropriate: `tftp_details`, `firmware_details`, `post_upload_behavior`, `observed_outcomes`?
6. Should `post_upload_behavior.power_cycle_required=true` be treated as a critical App guidance field?
7. Is `tftp_details.server_uses_ephemeral_port=false` safe to store as observed behavior, or should it be downgraded to unknown until more evidence exists?
8. Is `tftp_details.filename_required=false` safe to store from a single accepted filename observation, or should it be represented more cautiously?
9. Is `observed_outcomes.config_retention_observed="mixed"` appropriate given the reported retained and factory-reset-like outcomes?
10. Which fields require Owner confirmation before moving to `reviewed/`?
11. Is this incoming draft eligible to move to a `reviewed/` candidate after Owner confirmation, or should it remain in `incoming/` until additional evidence is added?
12. Should any fields be removed, downgraded to `unknown`/`null`, or rewritten before reviewed-candidate migration?

## Expected Review Posture

Be strict about the difference between:

- lab observation
- generally applicable device behavior
- app-facing recovery guidance
- reviewed/final data

Do not reject useful lab evidence merely because it is not public documentation, but clearly identify which claims are observed-only and must not be generalized.

Pay special attention to the unusual post-upload power-cycle requirement. The App must not imply upload completion equals immediate success if the evidence supports a post-upload manual step.

## Output Format

# Claude Code Stage 1 ASUS RT-AC86U Incoming Draft Review

Task ID: stage1-asus-rt-ac86u-incoming-review
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `INCOMING_ACCEPTED_REVIEWED_CANDIDATE_ALLOWED_AFTER_OWNER_CONFIRMATION`
- `INCOMING_ACCEPTED_REMAIN_IN_INCOMING`
- `REQUEST_INCOMING_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Evidence Assessment

- source type judgment:
- confidence judgment:
- hardware/firmware scope judgment:
- TFTP direction judgment:
- app-guidance readiness:

## 3. Field-by-Field Review

For each group, mark `accept`, `downgrade`, `remove`, or `needs owner confirmation`.

### button_recovery

- decision:
- notes:

### network_recovery

- decision:
- notes:

### tftp_details

- decision:
- notes:

### firmware_details

- decision:
- notes:

### post_upload_behavior

- decision:
- notes:

### observed_outcomes

- decision:
- notes:

### risk_warnings / known_issues

- decision:
- notes:

## 4. Critical App Guidance

State clearly:

- Should the App show the post-upload wait and manual power-cycle instruction?
- Should the App warn that ping and previous LAN IP are not reliable failure signals?
- Should the App warn that configuration may be retained or reset?
- Which user-facing warnings are mandatory?

## 5. Reviewed-Candidate Gate

- can move to reviewed candidate after Owner confirmation:
- required Owner confirmations:
- fields to modify before migration:
- fields that must remain unknown:
- maximum confidence:

## 6. Schema / Tooling Feedback

- schema changes accepted:
- schema changes requested:
- validator changes requested:
- future export/app-profile implications:

## 7. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to keep this incoming draft
- whether to revise any fields
- whether to allow reviewed-candidate migration after confirmation
- what Codex should do next

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming writes:
- no reviewed writes:
- no final writes:
- no profile approval:
