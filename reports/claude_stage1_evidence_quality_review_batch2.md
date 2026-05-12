# Claude Code Stage 1 Evidence Quality Review Batch 2

Task ID: stage1-evidence-quality-review-batch2
Date: 2026-05-12
Scope: review only, no collection, no profile generation

## 1. Executive Decision

- `SOURCE_INDEX_ACCEPTED_PROFILE_DRAFT_ALLOWED_FOR_R7000`
- Summary: The batch 2 source index entry is correctly classified and fills the macOS workflow gap for NETGEAR R7000. Profile draft preparation is allowed for R7000 only, with strict guardrails requiring explicit marking of unknown hardware/firmware scope and medium maximum confidence. TP-Link Archer AX55 remains fully blocked.

## 2. Source Review

### src-stage1-batch2-001

- candidate: NETGEAR R7000
- applicability_scope: model_level (correct as indexed)
- applies_to_candidate_model: true (justified, R7000 is explicitly listed in the article's applies-to section)
- source_type: official_documentation
- tftp_direction_claimed: tftp_passive (justified under evidence rules)
- contains_macos_guidance: true (explicit macOS workflow provided)
- profile_generation_allowed: false (correct as indexed for production profile generation; draft preparation is separately allowed under guardrails)
- decision: ACCEPTED as valid model-level evidence
- issues: No classification issues; only standard evidence gaps for hardware/firmware scope remain
- required next evidence: R7000 hardware version applicability list, firmware version range compatibility for TFTP recovery

## 3. Combined NETGEAR R7000 Readiness

- current readiness: Ready for incoming draft preparation (human-review only, not for production)
- evidence supporting R7000 model applicability: Two official NETGEAR KB articles explicitly list R7000 in their applies-to sections for TFTP recovery procedures
- evidence supporting macOS workflow: Official KB 000064624 provides step-by-step macOS TFTP client guidance for R7000
- evidence supporting TFTP direction: Both KBs explicitly describe user-side TFTP client upload to the router, confirming passive TFTP mode
- remaining blockers: Hardware version scope unknown, firmware version scope unknown
- whether incoming draft is allowed: Yes, for human review only, with strict guardrails
- maximum confidence if draft is allowed: medium (official sources confirm model applicability, but unknown scope limits confidence from reaching high)

## 4. TFTP Direction Judgment

- Is this App-side active TFTP server mode? No
- Or is this Mac-side TFTP client upload mode? Yes
- Which profile field/recovery family should be used? `recovery_methods: ["tftp_passive"]`, `network_recovery.passive_tftp_from_router: true`, `network_recovery.active_tftp_to_router: false`
- What evidence supports that decision? Both official NETGEAR KBs explicitly describe the user running a TFTP client on their computer to upload firmware to the router at a fixed IP address, confirming the router acts as the TFTP server (passive mode). No inference was used; direction is explicitly stated in procedure text.

## 5. Draft Profile Guardrails

Mandatory guardrails for incoming draft preparation:

- `firmware_version`: Must be explicitly set to `unknown` (not null, not omitted)
- `applies_to_all_firmware_versions`: Must be set to null (unknown, cannot be assumed true)
- `recovery_method`: Only `tftp_passive` may be listed; no other recovery methods may be added without additional evidence
- TFTP direction: `passive_tftp_from_router: true`, `active_tftp_to_router: false` (both fields must be explicitly set based on evidence)
- confidence maximum: May not exceed `medium`; any attempt to set `high` or `verified` must be automatically rejected
- source_evidence requirements: Must include evidence entries for both `src-stage1-batch1-003` and `src-stage1-batch2-001`, with explicit reference to their support for R7000 applicability
- warning / limitation notes: Must include prominent note stating "Hardware version and firmware version applicability are unknown. This procedure may not work for all R7000 variants."
- fields that must remain unknown or omitted: `default_ip`, `default_subnet`, `tftp_filename`, `uart_details`, `web_recovery` fields, `default_credentials`; no optional fields may be populated without explicit supporting evidence

## 6. TP-Link AX55 Status

- current readiness: Fully blocked from profile preparation
- reason: No model-specific recovery instructions have been collected. Existing sources are either series-level (not AX55-specific) or contain no recovery procedure content.
- next required evidence: Official TP-Link support document or FAQ explicitly describing recovery procedures for the Archer AX55 model, not just the broader Archer AX series.

## 7. Required Corrections

No source index corrections are required. All fields in `src-stage1-batch2-001` are correctly classified, aligned with policies, and accurately reflect the source content.

## 8. Recommendation To Owner

- Keep the batch 2 source: The NETGEAR macOS KB is high-quality official model-level evidence and should be retained.
- R7000 advancement: Allow Codex to prepare an incoming draft profile for R7000 only, strictly adhering to the guardrails outlined above. The draft must be clearly marked as scope-unknown and for human review only.
- More sources needed: Continue collection of R7000 hardware/firmware applicability evidence to raise confidence level. No further AX55 work should be done until model-specific recovery evidence is found.
- AX55 should stay blocked: Keep AX55 fully blocked from any profile preparation work until model-specific recovery evidence is collected.
- Codex next steps: Prepare the R7000 incoming draft profile following the guardrails, then submit it for human review. Do not generate any other profiles. Continue source collection for R7000 hardware/firmware scope and AX55 model-specific recovery procedures.

## Safety Confirmation

- no web browsing: yes
- no new source collection: yes
- no incoming profile generation: yes
- no reviewed writes: yes
- no final writes: yes
- no profile approval: yes
