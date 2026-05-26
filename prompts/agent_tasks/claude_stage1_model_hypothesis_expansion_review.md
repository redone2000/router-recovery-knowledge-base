# Claude Task: Stage 1 Model Hypothesis Expansion Review

## Agent Identity Gate

This task is intended only for: Claude Code.

If you are not this agent, stop immediately and reply only:

WRONG_AGENT_TASK
Expected agent: Claude Code
Your role: [your actual role if known]
No action performed.

Do not reinterpret, adapt, or partially execute this task if your agent identity does not match.

## Repository

Work in:

```text
/Users/YiYuan/Projects/router-recovery-knowledge
```

## Goal

Expand the model hypothesis queue without creating recovery profiles.

This is evidence triage, not support-list generation. Your output should help decide which models deserve later owner review or lab tests.

## Required Reading

Read these files first:

- `AGENTS.md`
- `HANDOFF.md`
- `PROJECT_STATUS.md`
- `docs/evidence_lifecycle.md`
- `docs/recovery_priority_strategy.md`
- `schema/model_hypothesis.schema.json`
- `model_hypotheses/README.md`
- `model_hypotheses/asus-expansion-seeds.jsonl`

## Hard Boundaries

Do not write or modify:

- `incoming/`
- `reviewed/`
- `final/`
- App project files

Do not claim:

- official support
- final profile readiness
- recovery success
- configuration retention
- TFTP direction unless the source or lab evidence explicitly proves it
- ping/TTL as proof of recovery

Do not use long copyrighted excerpts. Summarize sources briefly and include URLs.

## Research Targets

Start with these candidate groups unless the Owner gives a narrower target:

- ASUS RT-AX88U
- ASUS RT-AX86U Pro
- ASUS RT-AC68U
- ASUS RT-AC86U
- TP-Link Archer AX73
- TP-Link Archer AX6000
- TP-Link Archer C7
- NETGEAR R7000
- NETGEAR R7800
- NETGEAR RAX50

## Output

Produce one report under `reports/` named:

```text
reports/claude_stage1_model_hypothesis_expansion_review_YYYY-MM-DD.md
```

The report must include:

1. Recommended candidates to add to `model_hypotheses/`.
2. Candidates to block or defer.
3. Evidence gaps per candidate.
4. Whether each candidate has official evidence, community evidence, lab evidence, or only weak hints.
5. Suspected workflow only when explicitly supported; otherwise use `unknown`.
6. Exact JSONL records ready for human review before they are added.

If you modify the repository, only add or edit files under:

- `model_hypotheses/`
- `reports/`

Run:

```text
python3 tools/validate_model_hypotheses.py model_hypotheses
git diff --check
```

## Acceptance Standard

Prefer saying "not enough evidence" over overfitting a model into a known workflow.

No candidate should move beyond `ready_for_incoming_review` without explicit Owner approval.
