# Router Recovery Knowledge Base

A community-curated knowledge base of router and network device recovery methods.

## Schema Version
Current schema version: v0.1

## Directory Structure

```
router-recovery-knowledge/
├── incoming/       # Newly submitted profiles awaiting review
├── reviewed/       # Profiles that have passed initial review, pending final approval
├── final/          # Finalized, verified profiles ready for use
├── schema/         # JSON schema and enumeration definitions
├── prompts/        # AI prompt templates for review and processing
├── sources/        # Source documents (manuals, forum posts, etc.) referenced by profiles
├── data/           # Additional supporting data files
├── reports/        # Generated reports and statistics
└── tools/          # Utility scripts for validation and processing
```

## Data Flow & Review Workflow

```
[Submission] → [incoming/] → [AI Review] → [Human Review] → [reviewed/] → [Final Approval] → [final/]
                                                                  ↓
                                                          [Changes Requested] → [Update] → [Re-review]
```

### Workflow Stages

1. **Submission**: New profiles are submitted to the `incoming/` directory
   - Must be JSONL records following the JSON schema in `schema/recovery_profile.schema.json`
   - Must include source information
   - Must include `source_evidence` for each claimed recovery method
   - Initial confidence level set by submitter

2. **AI Review**: Automated review using Claude with the prompt in `prompts/claude_profile_review_prompt.md`
   - Validates schema compliance
   - Checks enum values
   - Verifies confidence level is appropriate
   - Flags missing information or inconsistencies
   - Generates review report

3. **Human Review**: Human reviewer evaluates the AI report and profile
   - Approves, requests changes, or rejects
   - Adjusts confidence level if needed
   - Validates source credibility
   - Moves approved profiles to `reviewed/` directory

4. **Final Approval**: Senior reviewer does final check
   - Verifies accuracy and completeness
   - Moves fully verified profiles to `final/` directory
   - Profiles in `final/` are considered production-ready

## Core Rules

### Required Fields
All profiles must include:
- `id`: Unique identifier (vendor-model-firmware-version format)
- `vendor`: Device manufacturer
- `model`: Device model
- `recovery_methods`: List of supported recovery methods
- `source_type`: Type of source information
- `confidence_level`: Confidence in the accuracy of the information
- `submitted_date`: Date of submission

### Confidence Downgrade Rules
Confidence level must be lowered if:
- Source is AI-generated, unknown, or from social media (max `low`)
- Source is an unverified community post (max `medium`)
- Required fields are missing (max `low`)
- There are conflicting reports about recovery methods (max `low`)
- TFTP type is specified without supporting evidence (max `medium`)

### TFTP Method Classification
- **Passive TFTP (`passive_tftp_from_router`)**: Router acts as TFTP server. User connects to router's IP to perform recovery.
- **Active TFTP (`active_tftp_to_router`)**: Router acts as TFTP client. User must run a TFTP server for the router to connect to.

## Usage
TODO: Add usage instructions for tools and querying the knowledge base.

## Contributing
TODO: Add contribution guidelines.
