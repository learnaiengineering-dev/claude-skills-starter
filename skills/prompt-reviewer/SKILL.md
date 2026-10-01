---
name: prompt-reviewer
description: Review and rewrite an LLM prompt for clarity, structure and robustness. Use when the user shares a prompt, system prompt or template and asks to improve it, debug inconsistent outputs, or harden it.
---

# Prompt Reviewer

## Procedure

1. **Restate the goal** in one sentence. If you cannot, ask one clarifying question before proceeding.
2. **Audit** the prompt against this checklist and note only real problems:
   - Task is stated up front and unambiguous
   - Output format is specified (schema, length, tone) with one example if non-trivial
   - Inputs are clearly delimited (XML tags or fenced blocks), instructions separated from data
   - Constraints say what to do, not only what to avoid
   - Edge cases: empty input, missing info, conflicting instructions, "I don't know"
   - Untrusted input cannot override instructions (injection exposure)
3. **Rewrite** the prompt, keeping the author's intent and voice. Do not add features they did not ask for.
4. **Explain** the three highest-impact changes in plain language.
5. **Propose 3 test inputs** (typical, edge, adversarial) with the expected behavior.

## Output format

- Goal (1 line)
- Issues found (bullets, most severe first)
- Revised prompt (code block)
- Why these changes (max 3 bullets)
- Test inputs (table: input, expected)

## Rules

- Never claim a change "will" improve quality without a test to show it; say "should" and give the test.
- Prefer removing words over adding them.

