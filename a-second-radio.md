# The Same Plan on a Second Radio

Outcome: one CSV plan written into a
different model of radio, and a
clear account of what survives the
trip, what changes dialect, and what
has to be done again. Check: the
second radio's listing below shows
the same ten channels — read them
against chapter 6's table and spot
the one difference before the text
names it.

This is the job CHIRP exists for at
household scale: the club loaner, the
car radio, the spouse's handheld,
all agreeing. The lab ran it for
real: the Millbrook plan, authored
once, imported into a Baofeng UV-5R
image in chapter 6 and into a
**Kenwood TH-D72** image here
(transcript `chirp-lab/transcripts/t07-second-radio.txt`):

```bash
cp images/thd72-factory.img images/thd72-millbrook.img
python3 exchange_csv.py import \
    csv/millbrook-plan.csv images/thd72-millbrook.img
# imported 10 memories
```

and the read-back, locations 1–10:

```text
Memory 1: 146.940000-0.600000 FM (MB R94) r88.5* c88.5 ...
Memory 2: 147.330000+0.600000 FM (MB D33) r103.5* c103.5 ...
Memory 3: 444.775000+5.000000 FM (MB U775) r131.8* c131.8 ...
```

## What survives

Everything the plan is *about*:
frequency, offset and its sign, tone
and its direction, mode, name,
location. Ten rows in, ten rows out,
in the Kenwood's 1,000-channel memory
as happily as in the Baofeng's 128.
The CSV is the contract; both radios
signed it. (The Kenwood driver chats
while it works — its "dirty blocks"
lines are it repainting its own
memory map, per writing, and the
transcript keeps a sample: harmless,
but a fine reminder that each model
under CHIRP is its own small
program with its own manners.)

## What changes dialect

Look again at channel 2. In the
Baofeng's listing, the stored decode
tone (`c`) reads 88.5 — the plan's
row carried `cToneFreq` 103.5, and
the Baofeng's format keeps its own
default on file. In the Kenwood's
listing the same channel reads
`c103.5`: the Kenwood stored the
plan's decode value. **Neither radio
uses that tone to open its squelch**
(neither `c` is starred), so both
radios behave identically — but the
*images differ*, in a column a
careless plan-diff would flag as an
error. The lesson generalises past
tones: **verify a second radio by
behaviour — the checklist in chapter
10 — not by demanding byte-identical
rows.** Each model rounds, defaults
and files away the details in its
own accent, and a power level is the
classic case: the plan's flat 4.0W
becomes whatever the second radio's
nearest level is.

Names tell the same story from the
other side: the plan's names were
written short for the smallest
radio (chapter 6), so both radios
show them whole. Write names for a
16-character radio and the 7-character
one will truncate them into riddles.

And some things simply do not cross:
a row the second radio cannot hold
is refused or skipped at import —
the plan's question 1 from chapter 7
again, now asked by hardware. A
6-metre row into a dual-band radio,
an airband row into a radio with no
AM: the import report is where you
watch for the count. "Imported 10
memories" against a 10-row plan is
a sentence worth reading slowly,
every time.

## What is done again

Chapter 9's settings do not travel:
the second radio's squelch, timeout,
display and locks live in *its*
image, set by hand there. Bank
membership, where the plan used it,
is re-checked channel by channel
(chapter 2's warning). So the second
radio's ceremony is: its own factory
download (golden rule, again), the
plan import, its own settings pass,
its own verify download, its own
on-air check. Ten minutes a radio,
once — and from then on, a plan
change is one CSV edit and the same
ceremony everywhere, which is the
whole point of keeping the plan as a
file and the radios as its readers.
