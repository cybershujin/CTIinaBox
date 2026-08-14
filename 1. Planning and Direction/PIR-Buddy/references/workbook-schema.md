# Workbook Schema — IR-PIR-SIR-and-Intelligence-Collection-Plan

This is the exact structure of `IR-PIR-SIR-and-Intelligence-Collection-Plan-TEMPLATE-and-Starting-Examples.xlsx`.
`pir_workbook.py` reads and writes against these sheets and enforces the integrity rules below.

Every sheet is a **flat table with a header in row 1**. There are **no merged cells and no data-validation dropdowns**, so rows can be appended or edited without disturbing formatting. Data starts on row 2.

---

## Sheet 1 — `IRs` (Intelligence Requirements)

| Col | Header | Meaning |
|-----|--------|---------|
| A | Stakeholder | `<Tier> - <Function>`, e.g. `Strategic - Executives`, `Operational - Incident Response`, `Tactical - Security Operations Center`. Tier ∈ {Strategic, Operational, Tactical}. |
| B | IR# | `IR-<n>` (e.g. `IR-13`). **The same IR# is intentionally reused across multiple stakeholder rows** — one requirement can serve several audiences. Reuse the existing IR# and text when the question is the same; only mint a new number for a genuinely new question. |
| C | Intelligence Requirement | The decision-driving question, ideally with `[organization name]` / `[industry]` placeholders so it stays reusable. |
| D | Reporting Cadence | Ad-hoc, Daily, Weekly, Monthly, Quarterly, Annual, or a combination. |
| E | Decision | The **"so what"** — the action or decision this IR drives. An IR with no decision is not a real requirement. |

A shorthand row like `IR1-12 | see above | see above | see above` is used when a whole block of IRs applies to another stakeholder. The script treats such rows as references, not as new IRs.

## Sheet 2 — `PIRs` (Priority Intelligence Requirements)

| Col | Header | Meaning |
|-----|--------|---------|
| A | IR# | Parent IR (`IR-<n>`). **Must already exist on the IRs sheet.** |
| B | (IR text) | Copy of the parent IR's text, for readability. |
| C | PIR | `PIR.<IR#>.<n>` — e.g. `PIR.13.2` is the 2nd PIR under `IR-13`. |
| D | PIR question | A **specifically collectible** sub-question. |
| E | Collection Source | Named source(s): Feedly, Recorded Future, Flashpoint, Intel471, Mandiant, H-ISAC, SIEM review, IR forensic review, etc. |
| F | Collection Frequency | How often it is collected (Daily, Weekly, Quarterly, Ad-hoc Alerting…). |
| G | Type of reporting method | Format of the answer: Yes/No + free text, Template, Heatmap, Sum total + free text… |
| H | Method of reporting or sharing with stakeholder | Channel/product: "Ad-hoc via CTI channel in Teams", "Monthly CTI Report", etc. |

## Sheet 3 — `SIRs` (Specific Intelligence Requirements)

A SIR is a **specific instance** of a PIR — usually a named entity (threat actor, vendor, CVE) the PIR is watching right now.

| Col | Header | Meaning |
|-----|--------|---------|
| A | IR# | Grandparent IR. |
| B | IR | IR text. |
| C | PIR | Parent PIR id (`PIR.x.y`). **Must already exist on the PIRs sheet.** |
| D | PIR text | Parent PIR question. |
| E | SIR # | `PIR.<x>.<y>.SIR.<n>` — e.g. `PIR.13.1.SIR.3`. |
| F | SIR | The specific question, e.g. "Black Basta — is there indication of increased threat from this group?" |
| G | Collection Source | Named source(s). |
| H | Collection Frequency | How often collected. |
| I | Type of reporting method | Format (often "Template - SIR update"). |
| J | Method of reporting or sharing with team | Channel/product. |

## Sheet 4 — `Products` (PIR → reporting-product matrix)

| Col | Header | Meaning |
|-----|--------|---------|
| A | IR | Parent IR#. |
| B | (IR text) | IR text. |
| C | PIR | PIR id. |
| D | (PIR text) | PIR question. |
| E…I | One column **per reporting product** | Header is the product name (e.g. "Ad-hoc via CTI channel in Teams", "Monthly CTI Report", "Quarterly Strategic Executive Reporting"). Cell value is `Yes`/`No` — does this PIR feed that product? |

Product columns are defined by the header row; new products are added as new columns. The script matches a product by its header text.

## Sheet 5 — `ICP by Source` (Intelligence Collection Plan, quantified)

The collection plan viewed **by source**, with the time cost that feeds FTE / resource planning (see `CTI-Resource-Planning-and-FTE-utilization.xlsx`).

| Col | Header | Meaning |
|-----|--------|---------|
| A | Source | The collection source. |
| B | Frequency | Cadence for this source+PIR pairing. |
| C | PIR | Which PIR this collection line answers. **Should exist on the PIRs sheet.** |
| D | Description of PIR | PIR question text. |
| E | Average Time Collection Takes | e.g. `3 min`, `90 min`. |
| F | Frequency per week | Numeric multiplier used to estimate weekly analyst load. |

---

## Integrity rules (`pir_workbook.py validate`)

1. **Every PIR's `IR#` exists** on the IRs sheet (not counting `see above` reference rows).
2. **Every SIR's parent `PIR`** exists on the PIRs sheet.
3. **ID formats are well-formed:** `IR-<int>`, `PIR.<int>.<int>`, `PIR.<int>.<int>.SIR.<int>`.
4. **A PIR's number prefix matches its parent IR** — `PIR.13.x` must sit under `IR-13`.
5. **No duplicate PIR or SIR ids.**
6. **Warn** (not fail) when: an IR has a blank Decision; a PIR has no Collection Source; an `ICP by Source` PIR is not found on the PIRs sheet.

## The chain, end to end

```
Stakeholder ─▶ IR (+ Decision/"so what")
                 └─▶ PIR (+ Collection Source, Frequency, Reporting)
                        ├─▶ SIR   (specific instance: a named actor/vendor/CVE)
                        ├─▶ Products  (which reports carry this PIR — Yes/No matrix)
                        └─▶ ICP by Source  (source + time cost → analyst workload)
```
