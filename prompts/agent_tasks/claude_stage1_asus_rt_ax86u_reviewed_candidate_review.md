# Claude Code Stage 1 ASUS RT-AX86U Reviewed-Candidate Evidence Review

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

Stage 1 reference-device evidence review.

This review is focused only on whether the ASUS RT-AX86U owner-lab evidence is strong enough to prepare a reviewed-candidate profile discussion.

This is not a final-profile approval task.

## Scope

Review only.

Do not collect new sources.
Do not browse the web.
Do not generate or edit profiles.
Do not write `incoming/`.
Do not write `reviewed/`.
Do not write `final/`.
Do not merge RT-AX86U evidence with RT-AC86U profile evidence.

## Files To Review

Use these absolute paths:

- `/Users/YiYuan/Projects/router-recovery-knowledge/lab_tests/live_sessions/asus_rt_ax86u_official_baseline_2026-05-17.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/runtime_attempts/asus_rt_ax86u_passive_tftp_put_2026-05-17.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/asus_rt_ax86u_reference_observation_summary_2026-05-17.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/asus_rt_ax86u_profile_candidate_guardrails_2026-05-17.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/reports/app_copy_upload_complete_vs_recovery_complete_2026-05-17.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/runtime_attempts/examples/asus_rt_ac86u_success_observed_2026-05-12.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/incoming/asus-rt-ac86u-unknown-unknown.jsonl`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/recovery_profile.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/app_runtime_attempt.schema.json`
- `/Users/YiYuan/Projects/router-recovery-knowledge/schema/enums.md`
- `/Users/YiYuan/Projects/router-recovery-knowledge/RULES.md`

RT-AC86U files are comparison context only. They do not prove RT-AX86U behavior.

## Facts To Review

The RT-AX86U evidence is based on Owner-supplied local lab testing, not public vendor documentation.

The evidence currently supports these observed facts:

- model: `ASUS RT-AX86U`
- hardware version: label `H/W Ver.: 1.0`
- firmware family during test: ASUSWRT-Merlin, official/unmodified per Owner
- firmware before TFTP write: `3004.388.11`
- firmware after TFTP write: `3004.388.10_2`
- later normal Web UI upgrade returned device to `3004.388.11`
- recovery entry method: hold Reset while powering on
- cable path: Mac wired Ethernet to LAN1
- recovery IP: `192.168.1.1`
- Mac static IP during recovery: `192.168.1.10/24`
- observed readiness signal: slow-flashing power LED plus `TTL=100`
- Web Recovery page: not observed during `TTL=100`
- passive capture before transfer: no router-initiated TFTP RRQ observed
- successful transfer direction: Mac/App acted as TFTP client; router acted as TFTP server
- TFTP method: WRQ/PUT to `192.168.1.1:69`
- ACK block 0 came from `192.168.1.1:69`
- no ephemeral TFTP server port was observed
- firmware image filename recorded during POC transfer: `388102.w`
- firmware image size: `86,900,756` bytes
- transfer completed in about 40 seconds
- after upload and more than 5 minutes waiting, DHCP did not return
- normal power cycle was performed after the wait
- after power cycle, DHCP/admin returned at `192.168.50.1`
- firmware version change verified the write
- configuration appeared retained in this single attempt

## Non-Claims / Boundaries

Do not treat these as proven:

- stock ASUSWRT behaves the same as ASUSWRT-Merlin
- all RT-AX86U hardware, region, or firmware variants behave the same
- LAN1 is strictly required
- ACK source port 69 behavior is universal
- no other Web Recovery state exists
- Active TFTP / router-pulls-firmware is supported
- configuration retention is guaranteed
- manual power cycle is universally required across RT-AX86U
- RT-AC86U and RT-AX86U can share one profile
- upload completion equals recovery completion
- `TTL=100` alone proves recovery readiness or success

## Review Questions

1. Is this evidence strong enough to prepare an RT-AX86U reviewed-candidate profile draft after Owner confirmation?
2. Should this remain only a runtime attempt and report, with no profile draft yet?
3. Is `personal_testing` acceptable as source type for this candidate evidence?
4. What is the maximum safe confidence level: `low`, `medium`, or another value?
5. Is `tftp_passive` justified for the tested RT-AX86U unit?
6. Should Active TFTP remain unsupported/false/unknown based on the passive capture?
7. How should Web Recovery be represented: unsupported, not observed, or unknown?
8. Should `required_lan_port: LAN1` be encoded, or should it remain observation-only guidance?
9. Should `server_uses_ephemeral_port=false` and `ack_source_port=69` be encoded, or downgraded to observation-only notes?
10. How should post-upload behavior be represented: wait several minutes, then manual power cycle may be required?
11. How should configuration state be represented given one RT-AX86U retained-configuration outcome and mixed RT-AC86U comparison outcomes?
12. Which fields require Owner confirmation before any reviewed-candidate profile draft is created?
13. Which fields must remain unknown/null if a draft is created?
14. What App copy warnings are mandatory before this evidence is used in a guided recovery flow?

## Expected Review Posture

Be strict about the difference between:

- runtime attempt evidence
- model-specific candidate evidence
- observed-only field values
- generally applicable device behavior
- App-facing user guidance
- reviewed/final profile status

Do not reject useful owner-lab evidence merely because it is not public documentation.

Do reject or downgrade any field that overgeneralizes from one tested unit, one firmware family, one LAN port, one filename, one TFTP client implementation, or one post-upload outcome.

Pay special attention to the post-upload phase. The App must not imply upload completion equals recovery success.

## Output Format

# Claude Code Stage 1 ASUS RT-AX86U Reviewed-Candidate Evidence Review

Task ID: stage1-asus-rt-ax86u-reviewed-candidate-review
Date:
Scope: review only, no collection, no profile generation

## 1. Executive Decision

Choose one:

- `CANDIDATE_EVIDENCE_ACCEPTED_PROFILE_DRAFT_ALLOWED_AFTER_OWNER_CONFIRMATION`
- `CANDIDATE_EVIDENCE_ACCEPTED_RUNTIME_ONLY`
- `REQUEST_EVIDENCE_CHANGES`
- `BLOCKED`

Then provide a short summary.

## 2. Evidence Assessment

- source type judgment:
- confidence judgment:
- hardware/firmware scope judgment:
- TFTP direction judgment:
- Web Recovery judgment:
- App-guidance readiness:

## 3. Candidate Field Review

For each group, mark `accept`, `downgrade`, `remove`, `needs owner confirmation`, or `keep observation-only`.

### profile identity / scope

- decision:
- notes:

### button_recovery

- decision:
- notes:

### network_recovery

- decision:
- notes:

### tftp_details

- decision:
- notes:

### firmware_details / firmware_source

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

## 4. RT-AC86U Comparison Boundary

State clearly:

- which RT-AC86U facts may be used only as cautionary comparison
- which RT-AC86U facts must not be imported into RT-AX86U fields
- whether mixed RT-AC86U configuration outcomes should affect RT-AX86U copy wording

## 5. Critical App Guidance

State clearly:

- Should the App show upload completion as only transfer completion?
- Should the App require a post-upload wait before any power action?
- Should the App show a manual power-cycle step, and if so with what wording strength?
- Should the App warn that DHCP/admin may not return until after power cycle?
- Should the App warn that configuration retention is not guaranteed?
- Which user-facing warnings are mandatory?

## 6. Reviewed-Candidate Gate

- can prepare reviewed-candidate draft after Owner confirmation:
- required Owner confirmations:
- fields to modify before any draft:
- fields that must remain unknown/null:
- fields that must remain observation-only:
- maximum confidence:
- final-profile publication allowed: no

## 7. Schema / Tooling Feedback

- schema changes accepted:
- schema changes requested:
- validator changes requested:
- future export/app-profile implications:

## 8. Recommendation To Owner

Give a concise owner-facing recommendation:

- whether to create an incoming/reviewed-candidate draft
- whether to keep this as runtime evidence only
- whether any more router testing is needed now
- what Codex should do next

## Safety Confirmation

Answer yes/no:

- no web browsing:
- no new source collection:
- no incoming writes:
- no reviewed writes:
- no final writes:
- no profile approval:
