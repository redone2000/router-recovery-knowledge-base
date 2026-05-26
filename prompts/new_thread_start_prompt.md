# New Thread Start Prompt

Use this prompt when starting a new Codex thread for this project.

```text
You are working in /Users/YiYuan/Projects/router-recovery-knowledge.

Read AGENTS.md, PROJECT_STATUS.md, and HANDOFF.md first. Then inspect git status.

Goal: continue the router recovery knowledge project from Stage 1 reference-device evidence and App-upgrade preparation. Do not broaden into long-tail model collection.

Current priorities:
1. Protect evidence boundaries.
2. Review App/export readiness for the RT-AX86U reviewed candidate.
3. Keep AX55 at recovery-entry observed until firmware upload is explicitly approved.
4. Treat ASUS RT-AX86U as reviewed candidate only, not final.
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
Review App/export readiness for reviewed/asus-rt-ax86u-1-0-merlin.jsonl while preserving observation-only warnings. Do not write final/.
```
