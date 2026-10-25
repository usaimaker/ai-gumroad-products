# Agent Safety Checklist: 24 Checks Before You Let an AI Agent Touch Production

You wrote the agent. It works on your machine. Now you are about to point it at a client database, a live inbox, or a billing system. This checklist is the difference between a tool you trust and an incident you explain.

Built for solo founders, consultants and small teams shipping AI automation without a platform team. Work through it in order. Every item is pass or fail.

---

## Part 1 - Permissions and blast radius (8 checks)

| # | Check | Why it matters |
|---|-------|----------------|
| 1 | The agent runs on a throwaway database or sandbox directory first | Most agent accidents are permission failures nobody exercised safely |
| 2 | It cannot reach anything with production credentials | A single leaked key turns a helper into an attack surface |
| 3 | Read-only is the default; write requires an explicit allowlist | Your starting position should be refusal, not access |
| 4 | Destructive operations are blocked below the prompt layer | Prompt guardrails are advisory; a proxy or parser is enforceable |
| 5 | Every write has a dry-run mode you tested this week | If you cannot preview it, you cannot trust it |
| 6 | There is a hard cap: max rows, max spend, max files touched | Limits convert a bad night into a bad afternoon |
| 7 | Credentials are scoped per agent, never shared across workflows | Shared keys make incidents impossible to attribute |
| 8 | You have asked it to do the worst plausible thing and watched what happened | Deliberate adversarial testing catches what happy paths hide |

**Four free tools that do most of Part 1 for you:** Vericto (SQL proxy that blocks destructive statements at the wire protocol), Kavela (isolated cloud computer per run), any container sandbox, and your database's own read-only role feature.

---

## Part 2 - Third-party trust (6 checks)

| # | Check | Why it matters |
|---|-------|----------------|
| 9 | Every plugin, skill or MCP server has a name you can trace to a maintainer | Anonymous dependencies are unreviewed code with your keys |
| 10 | Installation count, last commit date and issue history are all checked | Abandoned tools are how silent breakage enters your stack |
| 11 | Anything touching credentials was read, not just installed | Ten minutes of reading prevents months of cleanup |
| 12 | Dependencies are pinned to versions, not latest-forever | Unpinned means you get someone else's bad Tuesday automatically |
| 13 | A directory like PlugVet grades what you already run | Free A-F hygiene grades with the checks published behind them |
| 14 | You can list every add-on currently active in one command | If you cannot inventory it, you cannot secure it |

---

## Part 3 - Failure behaviour (10 checks)

| # | Check | Why it matters |
|---|-------|----------------|
| 15 | Every run writes a log you actually read | No log means no post-mortem, only guesses |
| 16 | Failures are loud: they alert you, not just error quietly | Silent failure is the number one reason agent projects get abandoned |
| 17 | Output is validated against a checklist before it counts as done | The reviewer pattern; this is what makes automation billable |
| 18 | There is a human approval gate on irreversible actions | Sending client-facing output and moving money are not retryable |
| 19 | Retry logic has a ceiling and a backoff | Unbounded retries turn a rate limit into a bill |
| 20 | Cheap reversible steps use a cheap model | Classification, triage and summaries do not need frontier pricing |
| 21 | Repeated context is cached rather than re-sent | Prompt caching usually halves an agent loop's token cost |
| 22 | You know what one failed run costs you in money and minutes | Unknown unit economics make every incident a surprise |
| 23 | Rollback takes one command and you have used it | Untested rollback is a plan, not a capability |
| 24 | Someone other than the author can restart it after it dies | Bus factor of one means your automation is a liability |

---

## Your 20-minute version

If you do nothing else today, do these five:

1. Point the agent at a sandbox and ask it to do something destructive on purpose.
2. Put every third-party add-on through a public hygiene directory.
3. Add one validation gate to your highest-consequence workflow.
4. Set a hard spend cap.
5. Turn on logging you will actually read tomorrow morning.

Score yourself out of 24. Under 14 means the agent is a demo, not a product. Bring it above 20 before a client sees it.

---

## Want this built for you?

We design and ship done-for-you AI automation - WhatsApp outreach, faceless video pipelines, content and SEO engines, custom agents - that runs 24/7 at zero ongoing cost.

Email felovery@gmail.com with the subject "AI Automation project" and describe the workflow you want automated. You will get a concrete build plan back.

More free kits: https://ai-gumroad-products.vercel.app/
