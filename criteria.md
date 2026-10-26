# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's town is invented and its radios are files.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: radios no driver supports and radios locked
   against it, no live control or logging, live-mode radios
   with no whole-image safety net, and the all-or-nothing
   upload in which one mistake programs every channel at once.
8. **The safety rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *program only radios you
   own or may change, and transmit only where your licence
   allows* — before any procedure depends on it: a cloned
   image carries someone else's settings and identity, an
   imported list is a claim to be checked, and no channel is
   transmitted on until it has been checked by hand and by
   ear (chapters 5, 7 and 10).
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox.
CHIRP was installed into a fresh virtual environment
(Python 3.12.3) — from the project's own source checkout, for
the reason given below — and exercised against two **radio
test images** from the CHIRP project's test collection
(`tests/images/` in its repository): a Baofeng UV-5R image
(6,657 bytes) and a Kenwood TH-D72 clone-mode image
(65,536 bytes). Those files are real radio memories, written
by the project's own test process, and every operation the
lab performed on them is one CHIRP performs on an image
between a download and an upload. All transcripts live in
`chirp-lab/transcripts/`; the CSV exchange script the lab
wrote is `chirp-lab/scripts/exchange_csv.py`; the images and
CSVs are in `chirp-lab/images/` and `chirp-lab/csv/`.

Run for real, with transcripts as evidence:

- Install: the PyPI package attempted first and its failure
  recorded (its source release compiles a small Fortran
  extension whose build chain fails with current
  numpy/setuptools: `error: unknown file type '.pyf'`); the
  identical code then installed from the project's git
  source, whose setup needs no such build for chirpc (t00).
- chirpc's model list: 564 models, including both lab
  radios (t01).
- The UV-5R image opened and listed: 37 programmed
  memories, in the mixed state the project's fixture ships
  (t02) — and its settings listed, 91 lines in two driver
  groups (t03).
- CSV export of that image by CHIRP's own CSV code: all 37
  memories, exact against the listing after the lab fixed an
  off-by-one of its own (CHIRP's memory bounds are inclusive;
  the first export dropped channel 127) (t04).
- The fictional Millbrook channel plan (ten channels, all
  amateur-band, invented town and repeaters) authored as a
  CSV and imported into a working copy of the UV-5R image:
  10 memories in, verified line by line with chirpc
  (t05, t06). Two genuine failures on the way — a plan row
  one column short, then an empty Power column the CSV
  reader rejects — are recorded in `examples/lab-notes.txt`.
- The same plan imported into the Kenwood TH-D72 image and
  verified (t07), including the one real divergence: the
  Kenwood stores the plan's decode tone where the Baofeng
  keeps its own default; neither radio uses it to open its
  squelch.
- A channel copied and renamed with chirpc itself (t08),
  and the working image exported back to CSV to close the
  round trip: 47 memories, plan rows and the chirpc edit
  read back letter for letter (t10).
- The stock configurations shipped with CHIRP: 20 files,
  and US Calling Frequencies loaded with CHIRP's own CSV
  reader — 4 channels (t09).
- The lab's own trap, run for real: chirpc invoked with
  stdin not a terminal exits 0 and prints nothing, having
  redirected its output to `~/.chirp/debug.log`; the
  `CHIRP_TESTENV=1` remedy is the same transcript (t90).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Everything involving a physical radio or cable: the
  download that produces a first image, the upload that
  finishes the job, cable chips and their drivers, the
  clone-mode ceremonies of particular models, the on-air
  checks. The build machine had no radio attached, so
  chapters 4, 5 and 10 teach those moments from the
  project's cable and model documentation.
- The CHIRP window's interactive work — its menus are named
  and its dialogs described; the engine underneath is the
  one the lab verified through chirpc and the library, and
  the transcripts are of that engine.
- The RepeaterBook online import (chapter 7): the
  mechanics and the hand check are taught, but no live
  directory query was made from the sandbox.
- The comparison tools in chapter 12 are characterised,
  not benchmarked; the neighbours were not installed.

Fixtures are this guide's own and deliberately generic: a
fictional town, Millbrook, with ten invented channels on
amateur-band frequencies, names belonging to nobody, and two
test images from the CHIRP project's public test collection.
No example is modelled on any real person, club, repeater or
organisation, and no radio was programmed, or transmitted,
at any point in the making of this guide.
