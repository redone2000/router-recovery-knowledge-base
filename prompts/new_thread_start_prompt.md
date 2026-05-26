# New Thread Start Prompt

Use this prompt when starting a new Codex thread for this project.

```text
You are working in /Users/YiYuan/Projects/router-recovery-knowledge.

Read AGENTS.md, PROJECT_STATUS.md, and HANDOFF.md first. Then inspect git status.

Goal: continue the router recovery knowledge project from Stage 1 reference-device evidence and App-upgrade preparation. Do not broaden into long-tail model collection.

Current priorities:
1. Protect evidence boundaries.
2. Ask Owner to confirm the RT-AX86U 9-item checklist before candidate draft preparation.
3. Keep AX55 at recovery-entry observed until firmware upload is explicitly approved.
4. Treat ASUS RT-AX86U evidence as candidate/review material, not final.
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
Ask Owner whether they confirm the 9-item checklist in `reports/asus_rt_ax86u_reviewed_candidate_migration_plan.md`. If confirmed, prepare an RT-AX86U candidate draft in incoming/ only. Do not write reviewed/ or final/ without explicit Owner approval.
```
