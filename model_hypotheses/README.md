# Model Hypotheses

This directory is the AI-assisted expansion queue.

Entries here are not recovery profiles, not App support claims, and not user-facing compatibility data. They exist to let AI agents collect and audit candidate model evidence without polluting `incoming/`, `reviewed/`, or `final/`.

Use this layer for:

- research seeds worth investigating
- suspected workflow classification
- source indexing and evidence gap tracking
- blocked candidates with useful negative evidence
- candidates ready for owner review before any `incoming/` draft

Do not use this layer for:

- final or reviewed support claims
- App copy that implies support
- inferred TFTP direction without source or lab proof
- broad model-family generalization
- firmware binaries, private local paths, serials, MAC addresses, passwords, or backups

Validation:

```text
python3 tools/validate_model_hypotheses.py model_hypotheses
```

Promotion rule:

Only `ready_for_incoming_review` with `promotion_gate=ready_for_owner_review` may be considered for an `incoming/` draft, and only after Owner approval.
