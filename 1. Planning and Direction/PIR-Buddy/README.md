# PIR Buddy 🕵️‍♀️ — a CTI requirements assistant Skill

**PIR Buddy** is a cheerful Claude skill that helps a cyber threat intelligence
(CTI) analyst do the hard part of the Planning & Direction phase: **identify
stakeholders, develop their Intelligence Requirements, and fill out the
`IR-PIR-SIR-and-Intelligence-Collection-Plan` workbook** — correctly and
consistently.

When invoked, PIR Buddy greets you and offers four paths:

1. 🧭 **Identify potential intelligence stakeholders**
2. ➕ **Add a new PIR** (and its IR / SIRs)
3. ✏️ **Modify an existing PIR** (or IR / SIR)
4. 💬 **Ask questions** about your PIRs or CTI requirements best practices

It coaches you toward best practice (every requirement must drive a decision)
and reads/writes the workbook for you through a bundled Python helper, so you
never hand-edit cells or risk clobbering the template.

## What's in the bundle

```
PIR-Buddy/
├── SKILL.md                       # the PIR Buddy persona + the four-branch workflow
├── README.md                      # this file
├── references/
│   ├── stakeholder-taxonomy.md    # 8 stakeholder groups, tiering, discovery questions
│   ├── ir-pir-sir-framework.md    # IR→PIR→SIR→Products→ICP, numbering, worked examples
│   ├── requirements-methodology.md# Assets / Adversaries / Intelligence-Consumers model
│   ├── best-practices.md          # the "so what?" test, good-vs-weak PIRs, cadence, estimative language
│   ├── source-library.md          # deeper folder docs + external references
│   └── workbook-schema.md         # exact sheets, columns, ID formats, integrity rules
└── scripts/
    └── pir_workbook.py            # openpyxl CLI to read/add/modify/validate the workbook
```

## Requirements

- **Claude Code** (or any Claude harness that supports skills).
- **Python 3.9+** with **openpyxl** for the workbook helper:

  ```bash
  pip install openpyxl
  ```

If Python isn't available in your environment, PIR Buddy can still coach you
conversationally and hand you the exact rows to paste into the workbook by hand —
you just lose the automated read/write.

## Install (Claude Code)

Copy the `PIR-Buddy/` folder into your skills directory so Claude can discover
it:

- **Project scope:** `.claude/skills/pir-buddy/`  (copy the *contents* of
  `PIR-Buddy/` so `SKILL.md` sits at `.claude/skills/pir-buddy/SKILL.md`)
- **User scope:** `~/.claude/skills/pir-buddy/`

Then start (or restart) Claude Code and just ask — e.g. *"Hey PIR Buddy, help me
add a PIR"* or *"help me identify my CTI stakeholders."* The skill triggers on
those requests. You can also keep the folder right here in `1. Planning and
Direction/` as documentation and point Claude at it.

## Using the workbook helper directly

You don't have to — PIR Buddy drives it for you — but it's a normal CLI.
Everything writes to a **working copy**; it refuses to write to a file whose name
contains `TEMPLATE`.

```bash
cd "1. Planning and Direction/PIR-Buddy/scripts"

# 1) make a working copy of the template (once)
python pir_workbook.py copy \
  -w "../../IR-PIR-SIR-and-Intelligence-Collection-Plan-TEMPLATE-and-Starting-Examples.xlsx" \
  --out "../../IR-PIR-SIR-Working-Copy.xlsx"

WB="../../IR-PIR-SIR-Working-Copy.xlsx"

# 2) explore
python pir_workbook.py list-stakeholders -w "$WB"
python pir_workbook.py list-irs -w "$WB" --stakeholder "Strategic - Executives"
python pir_workbook.py list-pirs -w "$WB" --ir IR-13
python pir_workbook.py show -w "$WB" PIR.13.1

# 3) build (IDs are auto-assigned)
python pir_workbook.py add-ir -w "$WB" \
  --stakeholder "Operational - Threat Hunting" \
  --text "Are active hunts warranted by current [industry] campaigns?" \
  --decision "Launch a targeted hunt and brief the SOC" --cadence Weekly

python pir_workbook.py add-pir -w "$WB" \
  --ir IR-13 --question "What ransomware groups target [industry] this quarter?" \
  --source "Mandiant, H-ISAC" --frequency Quarterly \
  --report-type Template --report-method "Quarterly Leadership Report"

python pir_workbook.py add-sir -w "$WB" \
  --pir PIR.13.1 --text "Akira — indication of increased threat to us?" \
  --source "Mandiant, Intel471" --frequency Weekly

python pir_workbook.py add-product-row -w "$WB" --pir PIR.13.1 \
  --set "Monthly CTI Report=Yes" \
  --set "Quarterly Strategic Cybersecurity Leadership Reporting=Yes"

python pir_workbook.py add-icp-row -w "$WB" \
  --source Mandiant --pir PIR.13.1 --frequency Quarterly --time "45 min" --per-week 0.08

# 4) edit + check
python pir_workbook.py modify -w "$WB" --id PIR.13.4 --set "frequency=Monthly"
python pir_workbook.py validate -w "$WB"
```

### Command reference

| Command | Purpose |
|---------|---------|
| `copy -w SRC --out DST` | Make a working copy of the template. |
| `list-stakeholders` | Every stakeholder + how many IR rows they own. |
| `list-irs [--stakeholder S] [--ir IR-n]` | List IRs with their decisions. |
| `list-pirs [--ir IR-n]` | List PIRs and their sources/cadence/reporting. |
| `list-sirs [--pir PIR.n.m]` | List SIRs. |
| `list-products` | Show the reporting-product columns. |
| `show <id>` | Show one IR / PIR / SIR. |
| `next-id --type ir\|pir\|sir [--parent id]` | Preview the next free ID. |
| `add-ir --stakeholder --text --decision [--cadence] [--ir]` | Add an IR. |
| `add-pir --ir --question [--source --frequency --report-type --report-method] [--pir]` | Add a PIR under an IR. |
| `add-sir --pir --text [--source --frequency --report-type --report-method] [--sir]` | Add a SIR under a PIR. |
| `add-product-row --pir --set "Product=Yes"` | Map a PIR to reporting products. |
| `add-icp-row --source --pir [--frequency --desc --time --per-week]` | Add a collection line. |
| `modify --id --set field=value [--stakeholder]` | Edit a row in place. |
| `validate` | Check referential integrity (IR→PIR→SIR) and ID formats. |

**Editable `modify` fields** — PIR: `question, source, frequency, report-type,
report-method` · SIR: `text, source, frequency, report-type, report-method` ·
IR: `stakeholder, text, cadence, decision` (add `--stakeholder` when an IR is
reused across audiences).

## Safety & scope notes

- The helper **never overwrites** the shipped `...TEMPLATE...xlsx` (name guard;
  override only with `--force`). Work on a copy.
- It preserves the workbook's formatting and only appends/edits rows.
- Reference docs **paraphrase and attribute** the CrowdStrike *Definitive Guide
  to Cyber Threat Intelligence* (`cti-guide.pdf`) and the ENISA model; the PDFs
  stay in this folder and are cited, not duplicated.

---

Part of **[CTI in a Box](https://github.com/cybershujin/CTIinaBox)** ·
Planning & Direction phase.
