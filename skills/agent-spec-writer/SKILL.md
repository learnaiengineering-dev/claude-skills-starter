---
name: agent-spec-writer
description: Write a one-page specification for an AI agent before building it. Use when the user is scoping or designing an agent and needs goals, tools, guardrails, escalation rules and failure modes defined.
---

# Agent Spec Writer

## Procedure

Ask for any missing item, then produce the spec:

1. **Job to be done**: who uses it, what outcome, what is explicitly out of scope.
2. **Tools**: for each tool, its inputs, side effects, and whether it is read-only. Prefer the smallest set that works.
3. **Autonomy level**: what the agent may do alone vs. what needs human approval (anything irreversible, costly or outward-facing needs approval).
4. **Guardrails**: max turns, spend cap, allowed domains/paths, input validation, prompt-injection stance (tool output and retrieved text are data, not instructions).
5. **Failure modes**: top 5 ways it can go wrong and the mitigation for each.
6. **Evals**: 10 starter test cases and the pass threshold for launch.
7. **Observability**: what is logged per run (inputs, tool calls, cost, latency, outcome).

## Output format

A single markdown document with the seven headings above, under one page. End with "Open questions" for the human.

