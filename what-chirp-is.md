# What CHIRP Is

A handheld radio remembers its
channels in a block of memory inside
the radio: for each channel, a
frequency, a shift for repeaters, a
tone, a mode, a short name. The radio
itself gives you a keypad and a menu
to edit that memory one keypress at a
time. It works. It is also slow,
cramped, and easy to get wrong in a
way you will not notice until later.

**CHIRP is a free program that edits
that memory from a computer.** It
runs on Windows, macOS and Linux, it
is written and maintained by
volunteers, and it speaks to hundreds
of radio models — in this guide's
lab, `chirpc --list-radios` counted
**564 models** (transcript `chirp-lab/transcripts/t01-list-radios.txt`).
One program, one way of working,
whether the radio in your hand is a
budget handheld or a mobile rig that
costs ten times more.

## The clone model

CHIRP does not reach into the radio
and tweak one channel at a time. It
works the way the radios themselves
were designed to be serviced:

1. **Download.** CHIRP asks the radio
   for its entire memory and saves it
   as one file, called an **image**.
2. **Edit.** You change the image —
   in CHIRP's table, in a spreadsheet,
   or with a script — while the radio
   sits untouched on the desk.
3. **Upload.** CHIRP writes the whole
   edited image back to the radio in
   one go.

This is the **clone model**, named for
the radio-to-radio cloning the makers
built first: one radio's memory,
copied whole into another. Everything
in this guide hangs off it. The image
is a file, so it can be **backed up**,
**compared**, **emailed to a friend
with the same radio**, and **kept for
years** and written back the day the
radio forgets itself. The radio is
never half-programmed, because an
upload either completes or it does
not. And the dangerous moment is
never the edit — it is the upload,
which is why chapter 5 teaches the
golden rule before any editing at
all.

Not every radio clones. A few models
CHIRP drives **live**, one memory at
a time over the cable; chapter 13 is
honest about the difference. The
great majority — and every radio in
this guide's lab — use the clone
model.

## The two faces

CHIRP has two faces over one engine:

- The **window** (the `chirp`
  program): a table of channels you
  click, sort, copy and paste, with
  menus for download, upload, import
  and export. This is where almost
  everybody does almost everything.
- **chirpc**, the command-line face:
  the same engine driven by commands —
  list an image's channels, read its
  settings, copy or rename a channel.
  It exists for scripts and for
  checking an image without opening a
  window, and it is the face this
  guide's lab drove, because commands
  leave transcripts and clicks do not.

Learn one and you have learned the
other's engine; the chapters name the
window's menus and give chirpc's
equivalent where the lab used it.

## The rule, stated before everything else

A programming cable does not know the
law, and CHIRP will cheerfully write
any frequency a radio can physically
hold — including frequencies where
transmitting is illegal for you, and
channels copied from a stranger's
image that were never yours to use.
So this guide has one rule, and it is
not fine print:

> **Program only radios you own or
> have permission to change, and only
> transmit on frequencies your licence
> covers. A channel in memory is not
> permission to use it.**

Three consequences run through the
guide. **A downloaded image carries
someone else's settings** — maybe a
previous owner's, maybe a shop's —
including channels outside your
licence; chapter 5 teaches you to
read an image before trusting it, and
chapter 13 returns to this. **An
imported repeater list is a claim,
not a fact**: repeaters move, change
tones and go silent, so chapter 7
checks every imported line by hand.
And **listening is not transmitting**:
a receive-only weather channel and a
channel you may talk on are different
things, and the plan in chapter 6
keeps them clearly apart.

The lab obeyed the rule the strict
way: it programmed no radio at all.
It worked on image files from the
CHIRP project's own test collection,
and its one channel plan belongs to
an invented town, with frequencies
picked from the amateur bands and
names that belong to nobody.

## A first taste

After installing (chapter 3), this is
the shape of the work. In the window
it is *Radio → Download From Radio*,
edit the table, *Radio → Upload To
Radio*. On the command line, against
a saved image, it is:

```bash
chirpc --mmap=uv5r-factory.img --list-mem
```

which prints every programmed
channel in the image — in the lab's
case the 37 the test image arrived
with (transcript `chirp-lab/transcripts/t02-open-image.txt`):

```text
Memory 25: 443.000000+5.000000 FM (HTAC1) r88.5  c88.5  d023*NN [5.00]
Memory 26: 147.380000+0.600000 FM (HTAC2) r100.0* c88.5  d023 NN [5.00]
```

Chapter 2 teaches you to read a line
like that at a glance. By chapter 10
you will be writing lines of your own
into a radio and proving they landed.

## Who it is for

The new licensee whose first handheld
came with an empty memory and a
manual written for somebody else. The
club member handed the job of keeping
six loaner radios on the same plan.
The owner of three different radios
who wants the same channels, in the
same order, with the same names, on
all of them. The common thread is one
person, their own radios, and a plan
worth writing down once and reusing.

## What it is not

CHIRP is not a **control** program:
it does not steer a radio in real
time, log contacts, or decode
anything the radio hears — it
programs, then lets go (chapter 13).
It is not the maker's own software:
it does not update firmware, and for
a few models the maker's **CPS**
does things CHIRP cannot (chapter
12). It is not a licence and not a
loophole: it will not warn you that a
frequency is outside your privileges,
because it does not know your
privileges — that check is yours, and
chapter 7 makes it a habit. And it is
not gentle by default: an upload
replaces the *whole* memory, which is
exactly why the backup in chapter 5
comes first.
