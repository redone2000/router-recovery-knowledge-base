# Public Launch Checklist

Use this checklist before making the repository public or submitting the OpenAI Codex for Open Source application.

## Repository Basics

- [ ] Repository name is public-facing, preferably `router-recovery-knowledge-base`.
- [ ] README states that this is not the Router Recovery app source code.
- [ ] README explains the public benefit in the first screen.
- [ ] Documentation license is present.
- [ ] Code, schema, and tooling license is present.
- [ ] Contribution policy is present.
- [ ] Security policy is present.
- [ ] Issue and pull request templates are present.

## v0.1 Documentation

- [ ] TFTP Recovery Guide is present.
- [ ] OpenWrt Recovery Guide is present.
- [ ] Firmware Selection Guide is present.
- [ ] Common Recovery Failures is present.
- [ ] ASUS Recovery Guide is present.
- [ ] TP-Link Recovery Guide is present.
- [ ] NETGEAR Recovery Guide is present.
- [ ] Each guide avoids unsupported device-wide claims.
- [ ] Each commercial app mention is optional and secondary.

## Evidence Hygiene

- [ ] No serial numbers, MAC addresses, credentials, or private screenshots.
- [ ] No copied vendor documentation beyond short references or links.
- [ ] TFTP direction is evidenced or marked unknown.
- [ ] Upload completion is not described as completed recovery.
- [ ] `TTL=100` is described as a clue, not proof.
- [ ] AI-generated model hypotheses are not presented as verified guidance.

## Validation

- [ ] `git diff --check`
- [ ] `python3 tools/validate_model_hypotheses.py model_hypotheses`
- [ ] `python3 tools/validate_profiles.py incoming reviewed`
- [ ] `python3 tools/validate_incidents.py`
- [ ] `python3 tools/validate_runtime_attempts.py runtime_attempts`
- [ ] `python3 tools/validate_workflows.py`
- [ ] `python3 tools/validate_system_links.py --allow-reviewed`

## OpenAI Application

- [ ] Public GitHub repository URL is ready.
- [ ] GitHub profile visibility is public.
- [ ] OpenAI Organization ID is available.
- [ ] Application text in `docs/openai-codex-for-oss-application.md` has been reviewed.
- [ ] No star, download, or user-count claims are invented.

## Website And App Funnel

- [ ] Router Recovery website links to the public knowledge base.
- [ ] Wiki links to the public knowledge base.
- [ ] Knowledge base links back to the app only as an optional related tool.
- [ ] App CTA wording is educational, not aggressive.
