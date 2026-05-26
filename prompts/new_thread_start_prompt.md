# New Thread Start Prompt

Use this prompt when starting a new Codex thread for this project.

```text
You are working in /Users/YiYuan/Projects/router-recovery-knowledge.

Read AGENTS.md, PROJECT_STATUS.md, and HANDOFF.md first. Then inspect git status.

Goal: continue the router recovery knowledge project from Stage 1 reference-device evidence and App-upgrade preparation. Do not broaden into long-tail model collection.

Current priorities:
1. Protect evidence boundaries.
2. Use the RT-AX86U App integration slice as internal App implementation input only.
3. Use `model_hypotheses/` for AI-assisted outward expansion without polluting profiles.
4. Keep AX55 at recovery-entry observed until firmware upload is explicitly approved.
5. Treat ASUS RT-AX86U as reviewed candidate only, not final.
6. Keep R7000 blocked as incident-only.
7. Treat RAX40v2 as official management/update baseline only, not recovery proof.

Before editing, run or inspect:
- git status --short
- python3 tools/validate_runtime_attempts.py runtime_attempts
- python3 tools/validate_profiles.py incoming
- python3 tools/validate_incidents.py incidents
- python3 tools/validate_model_hypotheses.py model_hypotheses
- python3 tools/validate_system_links.py

Important rules:
- Never write final/.
- Do not write reviewed/ unless Owner explicitly approves the specific promotion.
- Do not create incoming/ profiles directly from AI model expansion; use model_hypotheses/ first.
- Do not infer TFTP direction.
- Do not treat ping/TTL as proof.
- Do not label upload completion as recovery success.
- Do not commit secrets, local paths, serials, MACs, Wi-Fi passwords, admin passwords, firmware binaries, or router backups.
- Keep runtime attempts, incidents, workflow evidence, and model profiles separate.

Recommended first task:
If continuing App preparation, use reports/rt_ax86u_app_integration_slice_2026-05-26.md and app_exports/examples/asus_rt_ax86u_app_profile_draft.json as internal App implementation input, preserving observation-only warnings and upload-complete-vs-recovery-complete copy. Do not write final/.

If expanding outward with AI, use `prompts/agent_tasks/claude_stage1_model_hypothesis_expansion_review.md` and store candidates only in `model_hypotheses/` until Owner approves a specific incoming draft.
```
