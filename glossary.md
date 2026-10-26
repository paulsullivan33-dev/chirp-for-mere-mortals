# Glossary

**Bank** — a named group of channels
on radios that support them, so
scanning and browsing can be narrowed
to a set. Yaesu calls them memory
groups. The least portable part of a
plan (chapters 2 and 11).

**Cable (programming cable)** — the
lead between computer and radio, with
a USB-to-serial chip inside it. Sold
by radio family, not by plug shape
(chapter 4).

**Channel** — see **memory**.

**chirpc** — CHIRP's command-line
face: the same engine as the window,
driven by commands, suited to
scripts and verification (chapter 1).

**Clone** — to copy a radio's whole
memory at once, radio to file or file
to radio. The operation CHIRP is
built around.

**Clone model** — CHIRP's way of
working: download the whole memory
as an **image**, edit the image, upload
the whole image back (chapter 1).

**CPS** — customer programming
software: a maker's own programming
program for its radios (chapter 12).

**Cross mode** — the CSV column
saying how a memory's encode and
decode tones relate (`Tone->Tone` in
this guide's plan). Advanced plumbing
behind chapter 2's tone directions.

**CSV** — comma-separated values: the
plain-text spreadsheet format a
channel plan lives in — one row per
channel, one column per field
(chapter 6).

**CTCSS** — the continuous tone a
radio sends to wake a repeater, and
may require to open its own squelch.
In channel lists, simply "tone"
(chapter 2).

**DTCS** — a digital coded squelch: a
three-digit code, sent digitally,
doing CTCSS's job (chapter 2).

**Decode (tone squelch)** — requiring
an incoming signal to carry a tone
before the radio opens its speaker.
Useful deliberately, silent-making
by accident (chapters 2 and 14).

**Driver (CHIRP)** — the per-model
code inside CHIRP that knows one
radio's memory layout. 564 models in
the lab's count means 564 pieces of
reverse engineering (chapter 13).

**Driver (system)** — the operating
system's software for the cable's
chip, which creates the named serial
port CHIRP connects to (chapter 4).

**Duplex** — which way a repeater
channel's transmit frequency shifts:
plus, minus, split, or none —
**simplex** (chapter 2).

**Encode** — sending a tone so a
repeater wakes. The tone most
repeater channels need (chapter 2).

**Image** — a file holding one
radio's whole memory: channels,
settings, all of it. The unit of
backup, editing and upload in the
clone model (chapter 1).

**Legacy build** — the older,
per-system CHIRP releases, kept for
the few radios and computers that
need them (chapter 3).

**Live mode** — the minority of
radios CHIRP drives one memory at a
time instead of cloning; no whole
image, no whole-image backup
(chapter 13).

**Memory** — one slot in a radio,
holding everything needed to use one
frequency: frequency, offset, tone,
mode, name. Also called a channel
(chapter 2).

**Offset** — the size of a repeater
shift: conventionally 0.600 MHz on
2 metres, 5.000 MHz on 70 centimetres
(chapter 2).

**Repeater** — a station, usually on
high ground, that re-transmits what
it hears on one frequency out on
another, so small radios cover a
town (chapter 2).

**RepeaterBook** — the community
repeater directory CHIRP can import
from directly (chapter 7).

**RT Systems** — a company selling
per-family programming software and
cables, the polished commercial
neighbour (chapter 12).

**Serial port** — the named connection
the cable's driver presents:
`COM5`, `/dev/ttyUSB0` and friends
(chapter 4).

**Settings** — everything in the
image that is not a channel: squelch,
timeout, display, locks. They ride
along in every clone (chapter 9).

**Simplex** — transmit and receive on
the same frequency; no repeater
involved (chapter 2).

**Split** — a channel whose transmit
frequency is given outright rather
than computed from an offset
(chapter 2).

**Stock configuration** — a ready-made
channel set shipped inside CHIRP:
calling frequencies, weather,
licence-free services (chapter 8).

**Tuning step (TStep)** — the grid a
radio's frequencies must sit on;
imports off the grid get rounded
(chapter 2).
