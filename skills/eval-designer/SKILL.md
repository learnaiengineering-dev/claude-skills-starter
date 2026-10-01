---
name: eval-designer
description: Design an evaluation plan and test set for an LLM feature or agent. Use when the user needs to measure quality, choose scorers, build a golden dataset, or set a CI regression gate for prompts or models.
---

# Eval Designer

## Procedure

1. **Define success** per feature in observable terms (e.g. "cites a source", "valid JSON matching schema", "resolves the ticket category correctly").
2. **Build the dataset** from real traffic or logs first; add synthetic cases only for gaps. Target 20-50 cases to start, covering typical, edge and adversarial inputs. Tag each with a category.
3. **Choose scorers** in this order of preference: exact or schema check, regex or contains, programmatic check (code, SQL result), then LLM-judge with a written rubric. Spot-check judge verdicts against human labels on 10-20 cases.
4. **Set thresholds**: baseline the current system, then require no regression overall and no regression per category.
5. **Wire into CI**: run on every prompt or model change; fail the build under the threshold; store results over time.

## Output format

- Success criteria (bullets)
- Dataset plan (sources, size, categories)
- Scorer table (criterion | scorer | notes)
- CI gate (threshold, when it runs)
- First 5 concrete test cases as JSONL

