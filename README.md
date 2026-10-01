# claude-skills-starter

A free pack of **reusable AI skills** (`SKILL.md` files) for Claude Code and other agent tools that support the skills format, plus a validator so your own skills stay well-formed.

A skill is a folder with a `SKILL.md`: YAML frontmatter (`name`, `description`) and instructions the agent loads when the task matches the description. Good descriptions are what make a skill trigger at the right time.

## Skills included

| Skill | Use it when |
|---|---|
| [`prompt-reviewer`](skills/prompt-reviewer/SKILL.md) | You want a prompt critiqued and rewritten for clarity and robustness |
| [`rag-debugger`](skills/rag-debugger/SKILL.md) | A RAG app gives wrong or ungrounded answers and you need a diagnosis order |
| [`eval-designer`](skills/eval-designer/SKILL.md) | You need an eval set and scoring plan for an LLM feature |
| [`agent-spec-writer`](skills/agent-spec-writer/SKILL.md) | You're scoping an agent: tools, guardrails, failure modes |

## Install

Copy a skill folder into your skills directory, for example for Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -r skills/prompt-reviewer ~/.claude/skills/
```

Or project-local: `.claude/skills/` in your repo.

## Validate

```bash
pip install pytest
python scripts/validate_skills.py   # exits non-zero on problems
pytest -q
```

Rules enforced: frontmatter has `name` matching the folder and a `description` of at least 40 characters that says *when* to use the skill.

## Write your own

1. `mkdir skills/my-skill && $EDITOR skills/my-skill/SKILL.md`
2. Put the trigger conditions in the description, the procedure in the body.
3. Keep it under ~150 lines; link out to reference files if it needs more.
4. Run the validator.

---

## Part of Learn AI Engineering

This repo is a free resource from [Learn AI Engineering](https://learnaiengineering.dev/?utm_source=github&utm_medium=repo&utm_campaign=claude-skills-starter) — *Build production AI systems.*

- Structured learning paths, labs and portfolio projects: [https://learnaiengineering.dev](https://learnaiengineering.dev/?utm_source=github&utm_medium=repo&utm_campaign=claude-skills-starter)
- Want the production-ready version (enterprise templates, deployment, evals, runbooks)? See the **FDE Toolkit** on the portal.
- More free repos: [github.com/learnaiengineering-dev](https://github.com/learnaiengineering-dev)

Licensed under MIT.
