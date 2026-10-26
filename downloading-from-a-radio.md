# Downloading from a Radio

Outcome: one image file, downloaded
from your radio, named well, copied
somewhere safe, and *read* — so you
know what your radio actually holds
before you change a single line.
Check: the last section's listing of
your own image should match what the
radio's display scrolls through.

The cable moments in this chapter are
taught from the project's
documentation (the lab had no radio
attached); everything done to the
image afterwards is the lab's real
work, on a real image.

## The download itself

Connect the cable, radio on, volume
and squelch as the model's note in
the dialog advises. In the window:
*Radio → Download From Radio*, choose
the port from chapter 4, the maker,
the model, and OK. A progress bar
crosses; some radios beep or show
`CLONE` on their display; then the
table fills with the radio's
channels. On the command line the
equivalent is:

```bash
chirpc -r Baofeng_UV-5R --serial=COM5 \
       --mmap=my-radio.img --download-mmap
```

either way the result is the same
prize: **the image**, one file
holding the radio's whole memory.
Sizes are modest — the lab's UV-5R
image is 6,657 bytes, its Kenwood
image 65,536 — and that smallness is
a gift: images are cheap to keep,
all of them, forever.

## The golden rule

Now the rule this whole guide bends
around, stated once and repeated
wherever it matters:

> **The first image you download is
> sacred. Save it untouched, under a
> name that says so, and keep a copy
> somewhere the radio's desk cannot
> reach. Never edit the only copy of
> anything.**

Name it like evidence:
`uv5r-factory-2026-10-25.img` — model,
the word *factory*, the date. Copy
it to your ordinary backups. Then
make a *working copy* for editing
(`uv5r-millbrook.img`, say) and leave
the original alone. Why so stern?
Because the factory image is the only
certain way back: whatever you do
later — a bad plan, a wrong model
chosen in a dialog, an upload to the
wrong radio — uploading the factory
image restores the radio to exactly
the state it arrived in. Every other
paragraph of this guide assumes you
have it. The lab obeyed mechanically:
its `uv5r-factory.img` is the
project's test image, byte for byte,
and every experiment happened on
copies (the transcripts' first lines
are the `cp` commands).

## Read what you got

Before editing anything, *read* the
image. In the window the table is in
front of you; on the command line:

```bash
chirpc --mmap=uv5r-factory.img --list-mem
```

The lab's image listed **37
programmed memories** among its 128
(transcript `chirp-lab/transcripts/t02-open-image.txt`) —
and reading it was the education.
Alongside ordinary amateur repeaters
and simplex channels it held weather
channels, a block of channels in the
150 MHz range that are not amateur
frequencies at all, and one *split*
channel transmitting on a different
band from where it listens. That is
a project's test fixture, deliberately
varied — but it makes the real point
better than a tidy example could:

**A real first download is a
biography, not a blank page.** A new
radio may hold the shop's demo
channels; a used radio holds the
previous owner's whole world,
including channels outside your
licence and tones for repeaters in a
town you will never visit. Some of
it you will keep, most of it you
will replace, and all of it you read
first — because whatever you leave
in place, you now own. A channel
that should not be transmitted on is
a chapter 13 problem with a chapter
6 solution (delete it, or mark it
so the radio cannot transmit there,
where the model allows).

While reading, count. A radio whose
listing shows channels you cannot
find on its display may be showing
you **bank** behaviour (chapter 2),
not corruption. And a listing that
stops early or shows nonsense rows
is a download to do again, not data
to build on (chapter 14).

## The image is now the radio, on paper

From here to chapter 10, the radio
can go back in its charger. Every
edit, import and check in the next
five chapters happens to files: the
working image, and the spreadsheet
the next chapter builds. That is the
clone model's whole comfort — the
thinking happens at a desk, with
backups, and the radio is disturbed
exactly twice: once to give up its
memory, and once, at the end, to
receive the finished plan.
