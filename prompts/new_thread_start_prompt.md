# New Thread Start Prompt

Use this prompt when starting a new Codex thread for this project.

```text
You are working in /Users/YiYuan/Projects/router-recovery-knowledge.

Read AGENTS.md, PROJECT_STATUS.md, and HANDOFF.md first. Then inspect git status.

Goal: continue the router recovery knowledge project from Stage 1 reference-device evidence and App-upgrade preparation. Do not broaden into long-tail model collection.

Current priorities:
1. Protect evidence boundaries.
2. Review the RT-AX86U incoming candidate draft before any reviewed-candidate migration.
3. Keep AX55 at recovery-entry observed until firmware upload is explicitly approved.
4. Treat ASUS RT-AX86U draft as incoming only, not reviewed or final.
5. Keep R7000 blocked as incident-only.
6. Treat RAX40v2 as official management/update baseline only, not recovery proof.

Before editing, run or inspect:
- git status --short
- python3 tools/validate_runtime_attempts.py runtime_attempts
- python3 tools/validate_profiles.py incoming
- python3 tools/validate_incidents.py incidents
- python3 tools/validate_system_links.py

Important rules:
- Never write final/.
- Do not write reviewed/ unless Owner explicitly approves the specific promotion.
- Do not infer TFTP direction.
- Do not treat ping/TTL as proof.
- Do not label upload completion as recovery success.
- Do not commit secrets, local paths, serials, MACs, Wi-Fi passwords, admin passwords, firmware binaries, or router backups.
- Keep runtime attempts, incidents, workflow evidence, and model profiles separate.

Recommended first task:
Review `incoming/asus-rt-ax86u-1-0-merlin.jsonl` against `reports/asus_rt_ax86u_reviewed_candidate_migration_plan.md`. If acceptable, ask Owner whether to approve reviewed-candidate migration. Do not write reviewed/ or final/ without explicit Owner approval.
```
