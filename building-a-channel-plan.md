# Building a Channel Plan

Outcome: a channel plan as a
spreadsheet — one row per channel,
every column filled on purpose —
that CHIRP can read without a single
complaint. Check: the lab's plan at
the end loads clean, and you can say
why each of its ten rows is the way
it is.

## Why a spreadsheet at all

You can edit channels in CHIRP's own
table, and for three channels you
should. A *plan* is different: tens
of channels, meant to be read whole,
argued with, shared, and written
into more than one radio. For that,
the plan wants to live as a **CSV
file** — plain text, one row per
channel, one column per part of a
memory — that any spreadsheet program
(LibreOffice Calc, Excel, a text
editor at a push) can open. CHIRP
reads and writes exactly this format:
the window exports and imports it
from the File menu, and the lab's
`chirp-lab/scripts/exchange_csv.py`
does the same two jobs from the
command line, using CHIRP's own code
both ways.

Get the shape first. Exporting the
lab's factory image produced
`chirp-lab/csv/uv5r-export.csv`,
whose header is the whole contract
(transcript `chirp-lab/transcripts/t04-export-csv.txt`):

```text
Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,RxDtcsCode,CrossMode,Mode,TStep,Skip,Power,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE
```

Twenty-one columns looks like a lot
until you notice most rows leave
most of them at their defaults. The
ones a plan actually steers are the
first seventeen; the last four serve
one digital voice system (D-STAR) and
stay empty in this guide.

## The Millbrook plan

The lab's plan is for **Millbrook**,
a town that does not exist, with a
ridge, a downtown, and ten channels
worth of needs. It lives at
`chirp-lab/csv/millbrook-plan.csv`:

| Loc | Name | Freq | Shift | Tone |
|----:|------|-------:|-------|-----:|
| 1 | MB R94 | 146.940 | −0.600 | 88.5 |
| 2 | MB D33 | 147.330 | +0.600 | 103.5 |
| 3 | MB U775 | 444.775 | +5.000 | 131.8 |
| 4 | MB U360 | 443.600 | +5.000 | 100.0 |
| 5 | CALL 52 | 146.520 | — | — |
| 6 | MB TAC1 | 146.460 | — | — |
| 7 | MB TAC2 | 147.540 | — | — |
| 8 | MB EVNT | 146.580 | — | 141.3 |
| 9 | UHF CAL | 446.000 | — | — |
| 10 | MB R23 | 145.230 | −0.600 | 67.0 |

Every choice in it is deliberate,
and the deliberation is the lesson:

- **Locations are addresses, not
  ranks.** The plan starts at 1 and
  leaves gaps later when it grows;
  into the lab's working image it
  landed at 1–10 while the image's
  pre-existing channels elsewhere
  sat untouched.
- **Names fit the smallest radio** —
  seven characters, per chapter 2.
  `MB R94` is Millbrook's ridge
  repeater on 146.94; the pattern
  survives squinting at a small
  screen in the rain.
- **Repeaters carry the standard
  offsets** (chapter 2): 0.600 on
  2 metres, 5.000 on 70 centimetres,
  sign by band habit — and each
  carries its wake-up tone in
  `rToneFreq` with `Tone` set to
  `Tone` (encode only; decode left
  off on purpose).
- **Simplex rows say so by silence**:
  Duplex empty, Offset 0, Tone
  empty. The calling frequencies
  (146.520, 446.000) come first among
  equals because chapter 8's stock
  list puts them there and every
  plan in the world agrees.
- **Power is stated, never blank.**
  4.0W on every row. An empty power
  column is not a neutral choice —
  CHIRP's CSV reader rejects the row
  outright ("Invalid power
  specification"), and the lab's
  first import died of exactly that
  before the column was filled in
  (the failure is kept in
  `examples/lab-notes.txt`).
- **Comments say why, in words a
  stranger can check**: "Ridge
  repeater (fictional)". On a real
  plan this is where "tone changed
  2026, verified by listening" lives.

And one row teaches by its shape:
channel 8, the events channel, is
*simplex with a tone* — a deliberate
oddity: the tone rides along so the
event team's radios can switch on
tone squelch and hear only each
other. It is legal, it is
occasionally useful, and it is the
row a hand check (next chapter)
should stop at and ask about.

## Habits that keep a plan honest

**Sort by geography, then band, then
use** — or any order you can defend;
a plan is read under pressure, by
someone who may not be you. **One
plan per place or purpose**, several
small CSVs over one giant one, since
importing is cheap and selective.
**Date the file in its name**, like
the images: `millbrook-plan-2026.csv`.
And **never edit the only copy of a
plan either** — the golden rule from
chapter 5 is about files, and a plan
is a file.

## The import, once

The plan becomes a radio's memory by
import. In the window: open the
working image, *File → Import*, choose
the CSV, and CHIRP shows a mapping
dialog — which CSV rows land at which
locations — before changing anything.
Read that dialog; it is the last
free check. The lab's command-line
equivalent (transcript
`chirp-lab/transcripts/t05-import-plan.txt`):

```bash
python3 exchange_csv.py import \
    csv/millbrook-plan.csv images/uv5r-millbrook.img
# imported 10 memories
```

and the read-back (transcript
`chirp-lab/transcripts/t06-verify-working.txt`)
is chapter 10's verification habit in
miniature: locations 1–10 hold the
plan, letter for letter, and location
0 and the old channels from 25 onward
are exactly as they were. A plan you
can diff is a plan you can trust.
