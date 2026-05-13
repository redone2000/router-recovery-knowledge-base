# Review Workflow v0.1

## Overview
The review process ensures all recovery profiles meet quality standards before being made available for general use. Profiles move through three stages: `incoming/` → `reviewed/` → `final/`.

This profile workflow is now part of the broader Recovery Knowledge System. Evidence may also live as source indexes, incidents, workflows, and governance reports before it is eligible to become profile data.

See:

- `docs/recovery_knowledge_system_architecture.md`
- `docs/recovery_language.md`
- `docs/evidence_lifecycle.md`
- `docs/recovery_priority_strategy.md`

Unresolved incidents and draft workflows must not be treated as profile guidance.

## Production Priority

Recovery knowledge production must follow a deliberate priority order:

```text
Recovery Foundations
  -> Recovery Workflow Types
  -> Brand Recovery Worlds
  -> Reference Devices
  -> Family Expansion
  -> Long-tail Profiles
```

Do not expand by market-share lists or arbitrary model count.

Current brand priority:

1. TP-Link
2. ASUS
3. NETGEAR

OpenClaw tasks should be framed as workflow coverage gaps or reference-device evidence gaps, not as open-ended model collection.

## Repository Progress Sync
Stage-level project work should be committed to git and pushed to the configured private remote repository after validation. The default remote repository name should match this directory name (`router-recovery-knowledge`) unless there is a clear reason to use another name.

Do not push secrets, credentials, generated caches, destructive outputs, or unreviewed changes to `final/`. Destructive operations, public releases, and externally visible submissions still require explicit confirmation before execution.

## Roles
- **Submitter**: Person submitting a new recovery profile
- **AI Reviewer**: Automated review by Claude using the review prompt
- **Reviewer**: Human reviewer with domain knowledge
- **Maintainer**: Senior team member with final approval authority

---

## Stage 1: incoming/ (New Submissions)
### Purpose
Receive and triage new profile submissions.

### Entry Criteria
1. Submitter creates a JSONL profile file following the schema in `schema/recovery_profile.schema.json`
2. File is placed in `incoming/` directory with naming convention: `{batch-or-topic}.jsonl`
3. All required fields are present
4. Source information is provided (URL or document in `sources/` directory)
5. Each claimed recovery method has at least one `source_evidence` entry

### Processing Steps
1. **Automated Validation (Triage)**
   - Run JSON schema validation
   - Validate source evidence coverage for each claimed recovery method
   - Validate hardware version handling (`hardware_version` value or `unknown`)
   - If schema validation fails: Notify submitter of errors, profile remains in `incoming/` for fixes
   - If schema validation passes: Proceed to AI review

2. **AI Review**
   - Run Claude review using `prompts/claude_profile_review_prompt.md`
   - Generate review report with issues found and recommended confidence level
   - Attach report to the profile as `{id}.review.md`

### Exit Criteria
- Profile passes schema validation
- AI review report is generated

### Next Step
Move to human review queue.

---

## Stage 2: Human Review → reviewed/
### Purpose
Validate profile accuracy and completeness by a human reviewer.

### Entry Criteria
- Profile in `incoming/` with AI review report
- No critical schema errors

### Processing Steps
1. **Reviewer Assignment**
   - Reviewer claims profile from review queue
   - Reviews the AI report and profile content

2. **Validation Checks**
   - [ ] Verify source credibility and accuracy
   - [ ] Validate recovery methods are correct for the device
   - [ ] Confirm confidence level is appropriate
   - [ ] Check for missing information
   - [ ] Validate TFTP classification (passive/active) is correct
   - [ ] Confirm TFTP direction is directly evidenced, not inferred
   - [ ] Check whether hardware version differences are mentioned or unresolved
   - [ ] Cross-check with existing profiles for the same device if available

3. **Review Decision**
   - **Approve**: Profile is accurate and complete
     - Update `reviewed_by` and `reviewed_date` fields
     - Move profile to `reviewed/` directory
     - Move AI review report to `reports/` directory
   
   - **Request Changes**: Profile needs corrections or additional information
     - Add review notes to the report
     - Notify submitter of required changes
     - Profile remains in `incoming/` for updates
     - After updates, restart review process from AI review step
   
   - **Reject**: Profile has irreparable issues (wrong device, fake information, etc.)
     - Add rejection reason to the report
     - Move profile to archive (or delete as per policy)
     - Notify submitter of rejection

### Exit Criteria
- Profile has been reviewed and approved by a human reviewer
- All required fields are complete
- Confidence level is appropriate for the source quality

### Next Step
Move to final approval queue.

---

## Stage 3: Final Approval → final/
### Purpose
Final quality check before profile is made generally available.

### Entry Criteria
- Profile in `reviewed/` directory
- Has passed human review

### Processing Steps
1. **Maintainer Review**
   - Maintainer performs final spot check
   - Verifies consistency with other profiles from the same vendor
   - Confirms no known conflicting information exists
   - Validates that `verified` confidence level has sufficient evidence

2. **Final Decision**
   - **Approve**: Profile is ready for general use
     - Move profile to `final/` directory
     - Index profile in the knowledge base search system
   
   - **Request Changes**: Additional changes needed
     - Send back to reviewer with notes
     - Profile moves back to `reviewed/` for updates
   
   - **Reject**: Profile does not meet quality standards
     - Send back to `incoming/` for rework or archive

### Exit Criteria
- Profile is approved by a maintainer
- Profile is moved to `final/` directory

### Final State
Profiles in `final/` are considered:
- Accurate and reliable
- Ready for use in production tools
- Available for public querying

---

## Exception Handling
### Conflicting Profiles
If multiple profiles exist for the same device:
1. Compare sources and confidence levels
2. Prioritize profiles with higher confidence and more recent sources
3. Merge information where appropriate
4. Mark older/lower confidence profiles as deprecated

### Profile Updates
When updating an existing profile:
1. Submit updated version to `incoming/` as a new submission
2. Reference the existing profile ID in the submission notes
3. Go through full review process
4. Upon approval, replace the old profile in `final/` and archive the old version

### Removal Requests
If a profile is found to be incorrect:
1. Submit a removal request with evidence
2. Reviewer validates the issue
3. If confirmed: Mark profile as deprecated and remove from `final/`
4. Add note explaining why the profile was removed

---

## SLAs (Service Level Agreements)
- AI review: < 1 hour from submission
- Initial human review: < 3 business days
- Final approval: < 2 business days after human review
