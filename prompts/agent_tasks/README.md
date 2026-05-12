# Agent Task Prompts

This directory stores long task prompts for handoff to external agents.

## Path Rule

OpenClaw does not reliably share the Router Recovery Knowledge working directory context. Always give OpenClaw the absolute task-file path.

Example:

```text
Please read and strictly follow this task file:

/Users/YiYuan/Projects/router-recovery-knowledge/prompts/agent_tasks/openclaw_stage1_source_list_proposal.md

Only output text. Do not operate on the repository, browse the web, search, collect real source material, or generate incoming profiles.
```

Do not give OpenClaw relative paths such as `prompts/agent_tasks/...`.

Claude Code may use relative paths only when it is already operating in this repository. If uncertain, use absolute paths for Claude Code as well.
