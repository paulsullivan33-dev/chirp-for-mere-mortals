# Installing CHIRP

Outcome: CHIRP on your machine, the
right build for it, and a first run
that proves the program can at least
*see* the radios it knows. Check: the
model list in this chapter's last
section should include your radio by
name or not at all — and "not at all"
is information, not failure.

## One build, three systems

CHIRP is one program shipped as a
**unified build** for Windows, macOS
and Linux. Download it from the
project's site (chirpmyradio.com) —
not from a download aggregator, whose
copies are old at best. What you get:

- **Windows:** an installer. Run it,
  accept the defaults, and CHIRP
  appears in the Start menu as two
  entries at most: the window, and
  nothing else to configure.
- **macOS:** a single app. macOS will
  warn that it is from an identified
  project rather than the App Store;
  the project's download page carries
  the current instructions for
  approving it, and they change
  oftener than this guide does.
- **Linux:** the project's downloads
  page offers the current packaging
  (a Flatpak and distribution
  packages, varying by release). On
  Linux there is one extra step that
  matters more than the install:
  your user must belong to the
  **serial group** (usually `dialout`)
  or the program runs perfectly and
  simply cannot see any cable.
  Chapter 14 starts there when a
  Linux radio "will not clone".

## The legacy builds, honestly

Older CHIRP releases — the ones a
thousand forum posts and videos still
describe — were separate builds per
system, frozen years ago. They remain
available because a handful of very
old radios and very old computers
need them. The rule is simple: **use
the unified build unless something
you own is on the legacy-only list**
on the download page. Files move
between old and new without trouble;
an image saved by one opens in the
other, which is the clone model doing
its job.

## The Python route, and what it teaches

CHIRP is also a Python package, and
developers install it with pip:

```bash
python3 -m venv chirp-venv
chirp-venv/bin/pip install chirp
```

This guide's lab tried exactly that,
and the lab notes keep the result
because it teaches something true
about this route: the package's
source release compiles a small
optional component, and on the lab's
machine its build chain failed
(`error: unknown file type '.pyf'` —
transcript `chirp-lab/transcripts/t00-install.txt`).
The lab installed the identical code
from the project's own source
checkout instead, which needs no such
build for the command line. Nothing
about the failure is a judgement on
CHIRP; it is the ordinary brittleness
of building from source, and it is
why the downloads above are the
supported route for everybody else.
If you do take the Python route, know
what you get: the `chirp` window
(which also wants the wxPython
toolkit) and **chirpc**, the command
line, which needs nothing graphical
at all.

## First run: does it see its radios?

Open the window. An empty table is
correct — CHIRP opens with no radio
loaded, waiting for a download or a
file. The check that matters is the
model list: *Radio → Download From
Radio* opens a dialog with maker and
model dropdowns, and your radio
should be findable there. On the
command line the same list is:

```bash
CHIRP_TESTENV=1 chirpc --list-radios
```

(The `CHIRP_TESTENV=1` matters only
when scripting chirpc from another
program; chapter 14 explains the
silence it prevents.) The lab's list
ran to **564 models** (transcript
`chirp-lab/transcripts/t01-list-radios.txt`) —
AOR to Zastone, including both of the
lab's stand-in radios: the Baofeng
UV-5R and the Kenwood TH-D72.

## If your radio is not in the list

Three honest possibilities, in order.
The model is there under a sibling's
name — radios are rebadged often, and
the project's supported-radios page
names the equivalents. The model is
supported only in the *other* build
(legacy versus unified), which the
same page states. Or the radio is
genuinely unsupported, in which case
chapter 12's neighbours — above all
the maker's own software — are the
answer, and chapter 13 explains why
no amount of wishing adds a model:
each one is a small reverse-engineering
project of its own.

Install done, list checked: the next
thing you need is the cable, and the
cable is a chapter of its own because
it causes a solid half of all CHIRP
trouble.
