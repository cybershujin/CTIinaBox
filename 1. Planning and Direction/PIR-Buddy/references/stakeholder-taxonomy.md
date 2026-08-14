# Stakeholder Taxonomy & Discovery

PIR Buddy uses this when the analyst chooses **"Identify potential intelligence stakeholders."** It combines the folder's `cti-stakeholder-needs-guide.md` with the three-tier intelligence-consumer model from `cti-guide.pdf` (Chapter 2).

## Two lenses that combine into one label

The workbook's `Stakeholder` column uses `<Tier> - <Function>`. That's two ideas fused:

- **Tier = how they consume intelligence** (the altitude of the decision):
  - **Strategic** — CISOs, executives, risk leaders. Want trends and forecasts to steer budget, staffing, and program decisions.
  - **Operational** — IR, threat hunting, purple team, detection engineering, TPRM. Want context on campaigns, adversaries, and TTPs to run investigations and prioritize work.
  - **Tactical** — SOC, detection engineering, vuln management, NOC. Want timely, accurate indicators and alert context they can act on now.
- **Function = the team/role** doing the work.

The *same* person can appear at more than one tier (a detection engineer consumes tactical indicators *and* operational TTP analysis). That's expected — mirror the workbook, where `Detection Engineering` shows up under both Operational and Tactical.

## The eight starter stakeholder groups

From `cti-stakeholder-needs-guide.md` — use as a checklist, not a limit:

| # | Stakeholder | Typical tier | What intelligence supports their decisions |
|---|-------------|--------------|--------------------------------------------|
| 1 | Incident Response | Operational | Timely, actionable intel to investigate, contain, remediate; attacker attribution and TTPs during a case. |
| 2 | Security Operations Center (SOC) | Tactical | Current indicators and TTPs, plus context to adjudicate alerts. |
| 3 | Vulnerability Management | Tactical | Emerging vulns, exploitation-in-the-wild, patch prioritization. |
| 4 | Risk Management & Compliance | Strategic | Threat-actor motivations and business impact for risk assessments and regulatory posture. |
| 5 | Executive Leadership (CISO, board) | Strategic | High-level landscape and forecasts for decisions and board communication. |
| 6 | Application & Infrastructure teams | Operational/Tactical | Threat-informed secure design and control prioritization. |
| 7 | Legal & HR | Operational | Support for insider-threat, forensics, and legal matters. |
| 8 | Business Units (finance, IP-heavy lines) | Strategic/Operational | Unit-specific intelligence tied to their crown-jewel assets and risk profile. |

Others worth probing: Threat Hunting, Purple/Red Team, Third-Party Risk Management (TPRM), Fraud, Detection Engineering, Physical/Executive Protection, M&A/Corporate Development.

## How to discover stakeholders (six moves)

From the stakeholder-needs guide's assessment method:

1. **Engage** — meet each candidate team; ask open questions about their objectives, decisions, and pain points.
2. **Map needs to goals** — connect what intelligence can do to *their* mission (SOC → detect/investigate; execs → risk-based resource decisions).
3. **Identify gaps** — where do they lack the information to decide well today?
4. **Prioritize** — rank requirements by risk reduction, operational impact, and strategic alignment.
5. **Plan collection** — sources, methods, cadence (this becomes the PIRs and the ICP).
6. **Close the loop** — set up feedback so relevance and timeliness keep improving.

## Discovery questions that surface real requirements

Ask these; the *answers* become IRs, and each IR's **decision** is the action the answer triggers.

- "What decision do you make repeatedly that better threat information would improve?"
- "What would you do *differently* tomorrow if you knew you were being specifically targeted?"
- "What keeps you up at night about the threats to *your* part of the business?"
- "When you get a security surprise, where does it usually come from?"
- "What report, if it landed in your inbox every Monday, would actually change what you do that week?"
- "Who do you have to brief, and what do they ask you that you can't currently answer?"

## Feed discovery from the Company Baseball Card

`Company Baseball Card.md` in this folder profiles the org (lines of business, geolocations, crown-jewel data/apps/products, value chain, OSINT exposure, business rhythms, third-party dependencies, incident history + MITRE ATT&CK TTPs). Every entry there points at a stakeholder and a candidate requirement:

- Crown-jewel data/apps → the business unit that owns them, plus IR/compliance.
- Value-chain money-movement → finance/fraud + TPRM.
- Third-party dependencies → TPRM (see workbook `IR-20`, `IR-21`).
- Prior incidents + attributed actors → IR + detection engineering + purple team (workbook `IR-13`, `IR-18`, `IR-19`).
- Business rhythms (busy seasons) → SOC + awareness (social-engineering windows).

## Output PIR Buddy should produce for this branch

A short table of **candidate stakeholders** as `Tier - Function`, each with 1–3 **starter IRs** and a **decision** for each, ready to review and then write to the `IRs` sheet. Where the workbook already has a matching starter IR (e.g. "Is [organization name] being attacked?"), reuse that IR# rather than inventing a new one.
