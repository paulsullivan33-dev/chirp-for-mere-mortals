# Memories and Banks

Outcome: by the end of this chapter
you can read any line of a radio's
channel list and say exactly what the
radio will do on that channel — and
check: the worked line below should
hold no surprises by the last
section.

A **memory** (also called a
**channel**) is one slot in the
radio's memory, holding everything
the radio needs to use one frequency
without further instructions. Radios
hold from a hundred to a thousand of
them, numbered from 0 or 1. A slot
can be **empty** — most are, in a new
radio — and an empty slot costs
nothing. Everything else in this
chapter is the parts of a filled one,
in the order CHIRP's table shows
them.

## Frequency

The **frequency** is where the radio
listens, in megahertz: `146.520` is
the middle of the 2-metre amateur
band's calling channel. CHIRP stores
frequencies to the hertz —
`146.520000` — but you will type and
read them in megahertz. A radio can
only hold frequencies it was built
for: a dual-band handheld accepts
2-metre and 70-centimetre channels
and will reject a 6-metre one, a fact
chapter 11 puts to work.

## Duplex and offset: the repeater shift

A **repeater** listens on one
frequency and re-transmits what it
hears on another, so a hilltop box
can serve a whole valley. Your radio
must therefore *transmit* and
*receive* on different frequencies
for a repeater channel. The
**duplex** setting says which way the
shift goes, and the **offset** says
how big it is:

- **Simplex** (duplex shown blank or
  `off`): transmit and receive on the
  same frequency. Radio to radio,
  direct.
- **Minus (`-`)**: transmit *below*
  the listening frequency by the
  offset. The 2-metre habit:
  `146.940 - 0.600` means listen on
  146.940, transmit on 146.340.
- **Plus (`+`)**: transmit *above* by
  the offset — the 2-metre habit above
  147 MHz, and the 70-centimetre habit
  at 5.000 MHz: `444.775 + 5.000`
  transmits on 449.775.
- **Split**: transmit on a frequency
  given outright, not computed from
  an offset. Rare, real, and the
  reason one line of the lab's first
  listing reads `146.000000split446.000000`.

The offsets are conventions, not
laws, but they are *strong*
conventions: 0.600 MHz on 2 metres,
5.000 MHz on 70 centimetres. A
repeater channel with the wrong sign
is the classic beginner's silence —
you hear the repeater perfectly and
it never hears you.

## Tone: CTCSS and DTCS

Many repeaters sleep until woken.
They open their transmitter only when
the incoming signal carries an
inaudible low **tone**, so random
noise and distant stations do not key
them up. Two systems exist:

- **CTCSS** (the **tone** in most
  channel lists): a continuous tone
  between 67.0 and 254.1 Hz, sent
  while you transmit. A channel line
  like `r88.5*` in chirpc's output
  means the radio *sends* 88.5 Hz.
- **DTCS**: a digital code instead of
  a tone — a three-digit number such
  as `023`, with a **polarity** (the
  `NN` in the listings).

Tones work in two directions, and
confusing them causes the second
classic silence:

- **Tone (encode)** — the radio *sends*
  the tone so the repeater wakes. This
  is what most repeater channels need.
  In CHIRP's CSV this is the `Tone`
  column set to `Tone`, with the value
  in `rToneFreq`.
- **Tone squelch (decode)** — the
  radio also *refuses to open its own
  speaker* unless the incoming signal
  carries the tone (`cToneFreq`).
  Useful against interference; a trap
  when set by accident, because the
  repeater may not send any tone back,
  and then you hear nothing at all.

The lab's round trip showed the two
directions are stored separately in
every row of a plan — and, in
chapter 11, that two radios do not
always treat a plan's decode tone the
same way. Rule of thumb for a first
plan: **encode the tone the repeater
asks for, leave decode off** unless
you have a reason.

## Mode and step

The **mode** is how the voice rides
the signal: **FM** for nearly
everything in this guide, **NFM**
(narrow FM) on radios and bands that
use tighter channels, **AM** for
airband listening on radios that
offer it. A digital radio adds its
own modes, which CHIRP shows but this
guide does not teach. The **tuning
step** (`TStep`, 5.00 kHz in the
listings) is the grid the frequency
must sit on; a frequency that is not
on the radio's grid gets rounded —
one more reason chapter 7 checks
imported data by eye.

## Name

The **name** is the short label the
radio's display shows instead of the
frequency: `MB R94`, `CALL 52`. Names
are where models differ rudely. One
radio allows 16 letters, the next 7,
a third none at all — and a name that
does not fit is truncated or the
channel refused. The plan in chapter
6 keeps every name to seven
characters or fewer, not because the
first radio needs it, but because
chapter 11's second radio does.
Write names for the *smallest* radio
you own: short, distinct at a glance,
and ordered so the channels you reach
for in the rain sit early.

## Skip, power, and the small print

Three columns ride along in most
plans. **Skip** (`S` in the display)
tells the radio's *scan* to pass this
channel by — right for a noisy
channel you still want by hand.
**Power** is the transmit level the
channel uses; note that a CSV plan
must state one — the lab's first
import failed on an empty power
column, and the failure is kept in
`examples/lab-notes.txt`.
And a **comment** column exists purely
for humans: CHIRP carries it in the
CSV and ignores it for the radio, so
it is the safe place to write *why* a
channel exists.

## Banks: groups of channels

Bigger radios organise memories into
**banks** (Kenwood and Icom say
banks; Yaesu says **memory groups**;
the idea is one): named sets a channel
can belong to, so scanning and
browsing can be narrowed — *repeaters*
in one bank, *simplex* in another,
*the channels for the trip* in a
third. A channel may sit in one bank,
several, or none, depending on the
model. CHIRP shows bank membership
where the radio supports it, and the
CSV format carries it where the
model's driver does. Two warnings.
Bank support is the least portable
part of a plan: chapter 11's trip
between two models kept every
frequency, tone and name, and bank
membership is the first thing to
check afterwards. And a channel in no
bank can vanish from a banked radio's
scan list while sitting plainly in
its memory — a "missing" channel that
is not missing at all (chapter 14).

## Reading one line whole

From the lab's verified working
image (transcript `chirp-lab/transcripts/t06-verify-working.txt`):

```text
Memory 2: 147.330000+0.600000 FM (MB D33) r103.5* c88.5  d023 NN [5.00]
```

Channel 2. Listens on 147.330 MHz,
transmits 0.600 above it (147.930) —
a repeater channel. FM, name
`MB D33`, sends the 103.5 Hz tone
(the `*` marks the active one), does
not require a tone to open its own
squelch (`c88.5` is stored but not
starred), DTCS code 023 polarity NN
is on file but unused, tuning step
5.00 kHz. If you can read that line,
you can read any radio CHIRP knows —
the rest of this guide is workflow.
