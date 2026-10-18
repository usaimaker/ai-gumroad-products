# The Agent Harness Tuning Checklist

Stop paying for model upgrades to fix harness problems. This free checklist turns Google Research's Harness2 findings (open-sourced October 9, 2026) into a weekly routine you can run on any agent, on any model, at $0.

## The core idea

Harness2 showed that optimizing the eight components *around* a fixed model produced gains of up to 11.8 percentage points on professional benchmarks — with model weights never touched. Your prompt, tools, memory and guardrails are the harness. That is the part you control, and it is usually what is actually broken.

## The eight components to audit (one per week)

| # | Component | What to check | One change to try |
|---|-----------|---------------|-------------------|
| 1 | System prompt | Execution priorities stated? | Add a ranked priority list (correctness > speed > cost) |
| 2 | Guardrails | What is the agent allowed to touch? | List forbidden actions explicitly; add a confirm-before-irreversible rule |
| 3 | Memory | Does it remember last week's lessons? | Add a persistent notes file the agent reads at start and appends to at end |
| 4 | Tool guidance | Wrong tool calls happening? | Add one line per tool: *when to use, when NOT to use* |
| 5 | Subagents | Is one agent doing everything? | Split read-only research from write actions; run research in parallel |
| 6 | Skills | Repeated procedures re-derived each run? | Save the procedure as a reusable skill file with inputs and steps |
| 7 | Scripts | Same shell/python run every session? | Promote it to a checked-in script the agent calls with arguments |
| 8 | Plugins | Manual data fetching each time? | Wire one connector (search, calendar, sheets) and cache its output |

## The weekly Propose-Probe-Compose loop

1. **Propose** — pick ONE component from the table. Write the exact change you will make (one sentence).
2. **Probe** — run your weekly benchmark task twice: once with the current harness, once with the change. Save both outputs side by side.
3. **Compose** — keep the change only if the new output is better on criteria you wrote down *before* running. If it is a tie or worse, revert and note why.

No ground-truth answer required. Contrasting two real runs is enough evidence for most workflow decisions.

## Copy-paste starter prompts

**Harness audit prompt:**
```
List every instruction, tool, memory source and restriction in your current
setup. For each, state: (a) what it is for, (b) whether it fired in the last
run, (c) whether removing it would change anything. Flag anything that never
fires.
```

**Guardrail prompt:**
```
Before any action that deletes, sends, publishes, spends money, or modifies
files outside this project folder: stop, state the action and its blast
radius, and wait for my explicit approval.
```

**Memory prompt:**
```
At the start of each session, read LESSONS.md. At the end, append one line:
what failed, what fixed it. Never repeat a logged failure.
```

## Scoring rubric (write this before you probe)

- Correctness: factual errors? invented steps? (count them)
- Completeness: all requested parts delivered?
- Cost: tokens or tool calls used vs. last run
- Time: wall-clock from prompt to usable output

Keep a one-line log per week: component changed, probe result, kept/reverted. After eight weeks you have a harness tuned to *your* work — for free, with no vendor lock-in.

## CTA

Free forever. If you want this turned into a scheduled routine for your own stack, email felovery@gmail.com — we build done-for-you automation at $0.
