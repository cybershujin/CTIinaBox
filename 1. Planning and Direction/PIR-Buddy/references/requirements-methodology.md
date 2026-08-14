# Requirements Methodology — the three-pillar model

> Source & attribution: this file **paraphrases** the requirements-development approach in *Definitive Guide to Cyber Threat Intelligence* (`cti-guide.pdf` in this folder), Chapter 2, and blends it with the folder's `Company Baseball Card.md` and `cti-stakeholder-needs-guide.md`. Quote the guide sparingly and with attribution; the PDF stays in the repo — don't copy long passages into products.

Good intelligence requirements are built by answering three questions in order: **what must we protect, who might come after it, and who needs the resulting intelligence (and in what form)?** The guide frames these as Assets, Adversaries, and Intelligence Consumers.

## Pillar 1 — Assets to prioritize

You can't monitor everything, so decide what matters most and quantify the business loss if it's hit. Asset categories the guide highlights:

- **Financial / payment data** — card numbers, bank accounts, credentials to them; high breach-notification, fine, and fraud costs.
- **Personal information (PII/PHI)** — regulated (HIPAA and privacy laws); fuels phishing and fraud.
- **Intellectual property** — designs, source code, technical docs; loss = lost competitive advantage or contract/licensing violations.
- **Confidential business information** — plans, bids, M&A and financial inside information; leaks move markets and invite investigations.
- **Credentials & IT-systems information** — the master key; can open the door to every other asset (watch third-party access especially).
- **Operational systems / availability** — not "data," but DDoS or destructive malware against revenue-generating systems still hurts.

**Tie-in:** these map directly onto the Company Baseball Card's *crown-jewel data / applications / products* and *value-chain* rows. Each prioritized asset should generate at least one IR ("Are we being targeted for X?") with a real decision attached.

## Pillar 2 — Adversaries

Decide **which threat actors to monitor** and, just as importantly, which ones to *deprioritize* ("shrinking the problem"). Broad actor types from the guide:

- **Cybercriminals** — financially motivated; target monetizable data (cards, PII, access). Wide range of skill and industry focus (retail, healthcare, finance, POS, etc.).
- **Competitors & cyber-espionage agents** — steal IP and confidential info for commercial, economic, political, or military advantage. Involve line-of-business managers to value what's worth stealing.
- **Hacktivists** — disruptive action for ideological reasons; watch for **"trigger actions"** (layoffs, expansions, controversies, who you do business with) that can suddenly make you a target.

Also fold in the actor questions from `Company Baseball Card.md`: who has attacked *us* and our *industry* before, when, how often, with what success, and against which crown-jewel assets. Adversary analysis feeds workbook IRs like `IR-13` (actors of interest) and `IR-17` (threat profiles — the template notes STEMPLES+).

Treat relevant-adversary identification as **ongoing** — new actor types and tools keep emerging.

## Pillar 3 — Intelligence Consumers

Requirements must match **who uses the intelligence and in what format**. The guide's three consumer levels line up exactly with the workbook's stakeholder tiers:

- **Tactical users** (SOC, NOC, infrastructure/patching) — need accurate, timely indicators and alert context to act now and avoid false positives.
- **Operational users** (IR, forensics, fraud) — need deep context around alerts and events: malware analysis, campaign breakdowns, adversary TTPs, attribution.
- **Strategic users** (CISOs, IT and risk leaders) — need trend and forecast reporting to steer budgets, process, technology, and staffing.

**This is why the workbook labels stakeholders `Strategic / Operational / Tactical - <Function>`.** Content *and* format are part of the requirement — capture both (the PIR's "Type of reporting method" and "Method of reporting" columns).

## Putting it together into requirements

A well-formed requirement sits at the intersection of the three pillars:

> **A [consumer/tier] needs to know [question about an asset or adversary] so they can [decision].**

Example: *A tactical SOC analyst needs to know whether an alert matches a known adversary campaign so they can adjudicate the alert correctly.* That becomes an IR with a decision, then PIRs against named sources.

## Estimative & analytic language

For forecast-style IRs (the workbook's "What is the likelihood…?" requirements), use consistent **Words of Estimative Probability** (see `source-library.md`) rather than vague terms — e.g. "likely / highly likely / roughly even chance / unlikely" with a shared meaning — so leadership reads probability the same way every time. For structuring adversary/threat-environment profiles, the template references **STEMPLES Plus** (Social, Technical, Economic, Military, Political, Legal, Educational, Security — plus religion, demographics, geography).
