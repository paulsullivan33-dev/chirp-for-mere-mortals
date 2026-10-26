# CHIRP for Mere Mortals

A modern handheld radio holds a
hundred or a thousand channels, and
its front panel offers you two small
buttons and a menu tree to program
them with. Typing a hundred
frequencies, offsets and tones that
way is an afternoon of beeps, and one
wrong digit hides until the day you
need the channel. **CHIRP** is a free
program that moves the job to a
computer: it copies the radio's whole
memory into a single **image file**,
lets you edit that memory as a table
you can read, check and keep, and
writes it back down the same cable.
One program speaks to hundreds of
radio models from almost every maker,
so the plan you build for one radio
can travel to the next.

This guide explains how that works:
the **clone model** underneath it, the
parts of a **memory** (frequency,
offset, tone, mode, name), the cable
and its driver, and the working
habits that keep a radio safe — above
all the golden rule, *save the
untouched first image before you
change anything*. It builds one small
channel plan for an invented town,
checks every line by hand, writes it
into two different radios, and states
the limits plainly, including the
legal one: a program can type any
frequency, but **you may only transmit
where your licence allows**, and a
downloaded image can contain channels
nobody should transmit on.

The lab behind this guide ran the
real thing. CHIRP's command-line face,
**chirpc**, was installed on a small
Linux machine and driven against
**radio test images** from the CHIRP
project's own test collection — real
memory files for a Baofeng UV-5R and a
Kenwood TH-D72, standing in for the
radios themselves. Against them the
lab listed an image's 37 programmed
memories and its settings, exported
the memories to a **CSV** spreadsheet,
built a ten-channel plan for the
fictional town of Millbrook, imported
that plan into working copies of both
images, edited a channel with chirpc
itself, exported the result back to
CSV, and read every step back to
prove it landed.

What the lab could not do, it did not
fake. No physical radio was attached
to the build machine, so the two
moments a real cable carries an image
— the download that starts everything
and the upload that finishes it — are
taught carefully from the project's
documentation and labelled as such
wherever they appear. Everything that
happens *between* those two moments,
which is most of the work and all of
the thinking, was run for real, and
`criteria.md` keeps the full ledger
of what was run and what was only
read.

## What this guide covers

- [**What CHIRP is**](what-chirp-is.md) —
  the clone model: a radio's memory
  as a file you can copy, edit and
  keep, and the licensing rule that
  comes before everything else
- [**Memories and banks**](memories-and-banks.md) —
  the parts of one channel: frequency,
  duplex and offset, tone, mode, name,
  and the banks that group channels on
  radios that have them
- [**Installing CHIRP**](installing-chirp.md) —
  the unified build for Windows, Mac
  and Linux, the legacy builds and
  when they are the right answer, and
  the two faces of the program
- [**Cables and drivers**](cables-and-drivers.md) —
  the programming cable, the chip
  inside it, the driver your operating
  system needs, and the counterfeit
  chip problem, in plain terms
- [**Downloading from a radio**](downloading-from-a-radio.md) —
  the first clone, the golden rule of
  the untouched first image, and
  reading what you actually got
- [**Building a channel plan**](building-a-channel-plan.md) —
  the plan as a spreadsheet: one row
  per channel, the columns CHIRP
  expects, and habits that keep a big
  plan honest
- [**Importing repeater data**](importing-repeater-data.md) —
  repeater lists from files and online
  sources, and the hand check every
  imported line needs before it is
  trusted
- [**Stock configurations**](stock-configurations.md) —
  the ready-made channel sets CHIRP
  ships with: calling frequencies,
  weather channels, licence-free
  services, and when to take a row
  and when to leave it
- [**Settings beyond memories**](settings-beyond-memories.md) —
  the radio's other settings — squelch,
  timeout, display, lockouts — and why
  they ride along in the same image
- [**Uploading and verifying**](uploading-and-verifying.md) —
  writing the edited image back, and
  the verify pass that proves the
  radio holds what the plan says
- [**The same plan on a second radio**](a-second-radio.md) —
  one CSV, two radios: what survives
  the trip between models, what each
  radio's dialect changes, and what
  to check by hand
- [**The neighbours**](the-neighbours.md) —
  the makers' own CPS software,
  programming from the front panel,
  and RT Systems: what each does that
  CHIRP doesn't, and vice versa
- [**Limits**](limits.md) — unsupported
  radios, no live control, the mistake
  that programs every channel at once,
  and the licensing edge, stated
  plainly
- [**Troubleshooting**](troubleshooting.md) —
  the radio that will not clone, the
  cable the system cannot see, the
  silent chirpc, and the traps this
  guide's lab fell into so you don't
  have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Programming radios you do not own or
have no right to change — an image is
the whole personality of a radio, and
writing one is not a prank. Defeating
a radio's band limits, opening up
transmit on services your licence
does not cover, and cloning one
radio's identity into another are
likewise out; chapter 13 explains the
line. Commercial and public-safety
fleet programming — hundreds of
radios, managed keys, audit trails —
belongs to the makers' own software
and your organisation's rules; this
guide stays with one person and their
own radios, where the tool does its
honest work.

## How to use this guide

Read chapter 1 for the model and the
rule, and chapter 2 before touching a
radio — knowing the parts of a memory
turns later confusion into a named
problem. Chapter 5 is the one to
practise until it is boring: download,
save the untouched image, and only
then edit. Chapters 6 and 7 are where
plans are made and checked, and the
check is not the optional step —
imported data is wrong often enough
that this guide checks every line by
hand and teaches you to do the same.
The lab's files live in
`chirp-lab/images/` and
`chirp-lab/csv/`; its transcripts are
`chirp-lab/transcripts/`; its exchange
script is `chirp-lab/scripts/`; its
notes are `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Ham Radio for Mere Mortals](https://paulsullivan33-dev.github.io/ham-radio-for-mere-mortals/)
- [RTL-SDR for Mere Mortals](https://paulsullivan33-dev.github.io/rtl-sdr-for-mere-mortals/)
- [WSJT-X for Mere Mortals](https://paulsullivan33-dev.github.io/wsjtx-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/chirp-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/chirp-for-mere-mortals/blob/main/LICENSE-CODE).
