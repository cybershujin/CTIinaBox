# Best Practices — writing IRs, PIRs & SIRs that earn their place

PIR Buddy uses this to coach quality and to sanity-check anything before it's written to the workbook.

## The one test that matters: "so what?"

Every IR must have a **Decision** — the action it drives. If you can't name what a stakeholder will *do differently* once the question is answered, it isn't a requirement; it's curiosity. This is the whole point of the requirements-driven approach: intelligence exists to support decisions, not to accumulate facts.

- ✅ *"Is [org] being targeted?"* → Decision: activate counter-threat playbooks, warn SOC/IR.
- ❌ *"What's happening in ransomware this month?"* → no owner, no decision. Reframe until a decision appears.

## Good vs. weak PIRs

A strong PIR is **specific, collectible, decision-linked, and time-bounded**.

| Weak | Why | Stronger |
|------|-----|----------|
| "Tell me about APTs." | Unbounded, no source, no decision. | "Which of our top-5 industry threat actors changed TTPs this quarter, and do our detections cover them?" |
| "Are we secure?" | Not answerable/collectible. | "Are there reports of widespread attacks using techniques known to evade our current defenses?" (workbook PIR.4.2) |
| "Monitor the dark web." | A task, not a question. | "Are there dark-web mentions of selling access that could reference us?" (workbook PIR.2.3) |

**PIR checklist** (PIR Buddy runs this before writing):
1. Does it decompose a real parent **IR**?
2. Is it phrased as a **question** you could hand to an analyst and a source?
3. Are one or more **named sources** attached (Collection Source)?
4. Is there a **cadence** (Collection Frequency)?
5. Is the **answer format** defined (Type of reporting method)?
6. Is the **delivery channel/product** defined (Method of reporting)?
7. Does it ultimately serve the parent IR's **decision**?

If a PIR names a category of entities ("which actors", "which vendors"), it usually wants **SIRs** — one per specific entity you're watching.

## Cadence guidance

Match cadence to the decision's tempo, not to convenience:

- **Ad-hoc / alerting** — "are we under attack / breached / targeted *right now*" (workbook IR-1/2/3). Push to a channel the moment it triggers.
- **Daily–Weekly** — tactical/operational monitoring (SOC escalations, dark-web mentions, industry attack reports).
- **Monthly** — control-sufficiency and detection-coverage questions feeding the monthly CTI report.
- **Quarterly** — threat-actor-of-interest reviews, forecasts, strategic leadership reporting.
- **Annual / ad-hoc** — full threat profiles (STEMPLES+).

## Estimative probability language

For "What is the likelihood…?" IRs, use a **shared probability vocabulary** so everyone reads the same word the same way, e.g.:

- Almost certain / highly likely — ~90%+
- Likely / probable — ~65–85%
- Roughly even chance — ~45–55%
- Unlikely / improbable — ~15–35%
- Highly unlikely / remote — ~<10%

Pick one scale, define it once, and cite it in the report so leadership isn't guessing what "possible" means. (References in `source-library.md`.)

## Requirements-driven, not source-driven

Start from the decision and work down to the source — never the reverse. A common failure mode is buying a feed and then reverse-engineering questions to justify it. The workbook enforces the right direction: **Stakeholder → IR → PIR → Source**, and the ICP prices the sources you actually need.

## Keep requirements reusable

- Use placeholders (`[organization name]`, `[industry]`) so an IR can serve many contexts and be reused across stakeholders.
- Reuse an existing IR# across stakeholders rather than duplicating the question.
- Review and prune every cycle — the CTI lifecycle is a loop; requirements that no longer drive a decision should be retired, and feedback should mint new ones.

## Prioritization

When everything feels important, rank by: **risk reduction** (how much does answering this lower real exposure?), **decision impact** (how consequential is the action it drives?), and **collection cost** (what does the ICP say it takes?). High-impact + low-cost requirements go first; high-cost + low-impact ones get deprioritized ("shrink the problem").
