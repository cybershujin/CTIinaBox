# IR → PIR → SIR → Products → ICP: the framework

This is the mental model PIR Buddy teaches and enforces. Each level is *more specific* and *more collectible* than the one above it.

## The four object types

- **IR — Intelligence Requirement.** A decision-driving question owned by a stakeholder. Broad by design. Always paired with a **Decision** (the action it triggers). *"Is [organization name] being targeted for an attack?"* → Decision: *activate counter-threat playbooks, warn SOC and IR.*
- **PIR — Priority Intelligence Requirement.** A *prioritized, collectible* decomposition of an IR into a question you can actually go answer against named sources. *"Are there any dark-web mentions of attacking us?"* → source: Recorded Future, Intel471, Flashpoint.
- **SIR — Specific Intelligence Requirement.** A named *instance* of a PIR you are tracking right now — a specific threat actor, vendor, CVE, or campaign. *"Black Basta — is there indication of increased threat from this group?"*
- **Products** and **ICP** are the *operationalization*: which reports carry each PIR, and which sources/time it costs to collect.

## Why "priority" matters

You cannot collect against every question. Fredrick the Great's maxim — paraphrased in `cti-guide.pdf` — is that defending everything defends nothing. PIRs are the IRs you have decided are worth spending collection time and money on. Marking a requirement "priority" is a resourcing decision, and the `ICP by Source` sheet is where that decision gets a price tag (minutes × frequency = analyst load).

## Numbering (the script generates these for you)

| Object | Pattern | Example |
|--------|---------|---------|
| IR | `IR-<n>` | `IR-13` |
| PIR | `PIR.<IR#>.<n>` | `PIR.13.2` (2nd PIR under IR-13) |
| SIR | `PIR.<x>.<y>.SIR.<n>` | `PIR.13.1.SIR.3` (3rd SIR under PIR.13.1) |

The number carries the lineage: from `PIR.13.1.SIR.3` you can read the whole ancestry without a lookup. `pir_workbook.py next-id` computes the next free number so you never collide.

## Worked example (straight from the template's starter data)

**Stakeholder:** `Strategic - Cybersecurity Leadership`
**IR-13** — *"What known threat actors are of interest to [organization name]?"*
**Decision:** ensure training, testing, and detections are aligned / prioritized. **Cadence:** Quarterly.

Decompose into PIRs:
- **PIR.13.1** — *"What threat actors have attacked [organization name] in the past 3 years?"* · Source: IR forensic artifact review · Quarterly · Template · Quarterly Strategic Cybersecurity Leadership Report.
- **PIR.13.2** — *"What are the top 5 threat actors targeting [industry] organizations?"* · Source: Mandiant, Flashpoint, H-ISAC.
- **PIR.13.3** — *"What are the top 5 threat actors that have impacted third-party vendors critical to us?"*

Instantiate PIR.13.1 into SIRs (the actors you're actually watching):
- **PIR.13.1.SIR.1** — *"Royal/Zeon — increased threat from this group?"* · Weekly.
- **PIR.13.1.SIR.2** — *"Conti — increased threat from this group?"* · Weekly.
- **PIR.13.1.SIR.3** — *"Black Basta — increased threat from this group?"* · Daily.

Then wire it up:
- **Products:** mark which reports carry each PIR (e.g. PIR.13.1 → Quarterly Strategic Cybersecurity Leadership Reporting = Yes).
- **ICP by Source:** each source×PIR line gets an average collection time and a frequency-per-week, so leadership can see what this requirement costs in analyst hours.

## When to create which object

- New audience or new decision surfaced in a stakeholder interview → **new IR** (+ its decision).
- An existing IR is too broad to collect against → break it into **PIRs**, each tied to specific sources.
- A PIR names "which actors / which vendors / which CVEs" and you now have specific ones to watch → add a **SIR** per named entity.
- A PIR is settled → record it in **Products** (what carries it) and **ICP by Source** (what it costs).

## Reuse over proliferation

The template deliberately reuses IR numbers across stakeholders (e.g. `IR-1`, `IR-2`, `IR-3` appear for Executives, IR, SOC, and Detection Engineering). Before minting a new IR, check whether an existing one already asks the question for a different audience — if so, reuse the IR# and text and just add the new stakeholder row with its own **Decision** and **Cadence**. `pir_workbook.py list-irs` shows what already exists.
