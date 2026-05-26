# Stage 1 Model Hypothesis Expansion Review
## Date: 2026-05-26
## Agent: Claude Code
## Repository: router-recovery-knowledge

---

## Executive Summary
This review expands the AI-assisted model hypothesis queue with 9 new router models across ASUS, TP-Link, and NETGEAR families, aligned with the Stage 1 reference device strategy. All hypotheses strictly follow evidence boundaries and do not create recovery profiles or App support claims.

Important execution note: Claude CLI WebSearch was denied during this run. Therefore, the expansion output is treated as local-context triage and research-seed generation, not fresh internet source verification. Any candidate without existing repository evidence remains `research_seed` with `suspected_workflows=["unknown"]`.

### Key Statistics
- Total hypothesis records now: 10 (1 existing + 9 new)
- ASUS models: 4 (RT-AX88U, RT-AX86U Pro, RT-AC68U, RT-AC86U)
- TP-Link models: 3 (Archer AX73, Archer AX6000, Archer C7)
- NETGEAR models: 3 (R7000, R7800, RAX50)
- Status breakdown:
  - 8 research_seed (new candidates for future research)
  - 1 evidence_indexed (RT-AC86U, already has incoming profile)
  - 1 blocked (R7000, per lab incident)
- All records: app_copy_allowed = false, no App support claims

---

## Detailed Review by Vendor

### ASUS Family
#### 1. ASUS RT-AX86U Pro
- **Status**: research_seed
- **Suspected Workflow**: unknown (no model-specific evidence yet)
- **Evidence**: None (research seed only, based on AX86U family reference)
- **Missing Proof**: Official documentation, TFTP direction confirmation, recovery behavior details
- **Next Step**: Research official ASUS sources to confirm model-specific recovery behavior
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

#### 2. ASUS RT-AC68U
- **Status**: research_seed
- **Suspected Workflow**: unknown (official FAQ example is not enough to assert model-specific TFTP direction)
- **Evidence**: Official ASUS FAQ uses RT-AC68U as an example for Rescue Mode guidance (brand-level, not model-specific)
- **Missing Proof**: Model-specific official documentation, TFTP direction confirmation, hardware revision scope
- **Next Step**: Find model-specific official or high-quality community evidence
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

#### 3. ASUS RT-AC86U
- **Status**: evidence_indexed
- **Suspected Workflow**: asus_rescue_passive_tftp_put (medium confidence, lab observed)
- **Evidence**: Owner lab observation confirms passive TFTP PUT behavior, official firmware source exists
- **Missing Proof**: Hardware version scope, firmware version applicability, community validation
- **Next Step**: Keep the existing incoming profile as the active artifact; use this hypothesis only to track missing scope evidence before any reviewed migration.
- **Risk Level**: Medium
- **Promotion Gate**: needs_model_specific_evidence

---

### TP-Link Family
#### 1. TP-Link Archer AX73
- **Status**: research_seed
- **Suspected Workflow**: unknown (AX55 family similarity is not model-specific evidence)
- **Evidence**: None (research seed only)
- **Missing Proof**: Official documentation, recovery IP confirmation, web recovery behavior details
- **Next Step**: Research official TP-Link sources aligned with Archer AX family reference workflow
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

#### 2. TP-Link Archer AX6000
- **Status**: research_seed
- **Suspected Workflow**: unknown (AX55 family similarity is not model-specific evidence)
- **Evidence**: None (research seed only)
- **Missing Proof**: Official documentation, recovery IP confirmation, web recovery behavior details
- **Next Step**: Research official TP-Link sources aligned with Archer AX family reference workflow
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

#### 3. TP-Link Archer C7
- **Status**: research_seed
- **Suspected Workflow**: unknown (multiple possible workflows; no model-specific evidence yet)
- **Evidence**: None (research seed only, based on older TP-Link device patterns)
- **Missing Proof**: Official documentation, which recovery method is supported, hardware revision differences
- **Next Step**: Research official TP-Link sources, paying special attention to hardware revision behavior differences
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

---

### NETGEAR Family
#### 1. NETGEAR R7000 (Nighthawk AC1900)
- **Status**: blocked
- **Suspected Workflow**: netgear_official_tftp (official TFTP evidence exists, but lab reproduction is blocked)
- **Evidence**: Official TFTP documentation exists, but lab testing shows manual recovery is highly timing-sensitive and unreliable; nmrpflash succeeds easily as tool context but no official NMRP documentation was found
- **Missing Proof**: Consistent reproducible TFTP procedure, official NMRP confirmation, timing guidance
- **Next Step**: Blocked per lab incident; do not proceed to profile creation until consistent reproduction or official NMRP documentation
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

#### 2. NETGEAR R7800 (Nighthawk X4S AC2600)
- **Status**: research_seed
- **Suspected Workflow**: unknown (R7000 family similarity is not model-specific evidence)
- **Evidence**: None (research seed only)
- **Missing Proof**: Official documentation, which recovery method is supported, timing sensitivity
- **Next Step**: Research official NETGEAR sources, paying attention to potential timing sensitivity similar to R7000
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

#### 3. NETGEAR RAX50 (Nighthawk AX6)
- **Status**: research_seed
- **Suspected Workflow**: unknown (no confidence, similar to RAX40 reference which has no recovery evidence)
- **Evidence**: None (research seed only)
- **Missing Proof**: Official documentation, which recovery method is supported, recovery behavior details
- **Next Step**: Research official NETGEAR sources, aligned with RAX40 reference device once recovery evidence is available
- **Risk Level**: High
- **Promotion Gate**: do_not_promote

---

## Compliance Check
All records strictly adhere to the Stage 1 governance rules:
✅ No incoming/reviewed/final profile creation
✅ No App support claims (app_copy_allowed = false for all records)
✅ No inferred TFTP direction without evidence
✅ No ping/TTL as proof of recovery readiness
✅ All evidence boundaries clearly documented
✅ All missing proof explicitly listed
✅ No copyright material included
✅ R7000 remains blocked per incident guidance
✅ RT-AC86U aligned with existing incoming profile

---

## Validation
Claude initially generated the records, then Codex corrected over-specific research seeds so family similarity is not represented as a suspected workflow. Automated validation was then run locally.
- All required fields present
- All enum values valid
- All date formats correct
- All ID patterns valid
- All business rules satisfied after correction
- No validation issues found after running the validator

Validation command:

```text
python3 tools/validate_model_hypotheses.py model_hypotheses
```

---

## Recommendations
1. Prioritize research for models that fill reference workflow gaps:
   - ASUS RT-AX86U Pro (to confirm AX family Rescue Mode consistency)
   - TP-Link Archer AX73 (to confirm AX family Web Recovery consistency)
   - NETGEAR RAX50 (to align with RAX40 reference device research)
2. Do not promote any research_seed records to incoming profile without explicit Owner approval
3. Keep R7000 blocked until consistent TFTP recovery is reproduced in lab testing
4. Keep RT-AC86U in the existing incoming/review path; do not treat the hypothesis record as a separate promotion request.
