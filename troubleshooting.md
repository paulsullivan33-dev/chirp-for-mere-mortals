# Troubleshooting

Symptoms first, causes in the order
they actually occur. The two traps
from this guide's own lab close the
chapter; they are the ones nobody
warned the lab about either.

## The radio will not clone

The download fails, times out, or
says the radio did not respond.

1. **The cable again.** Bare-cable
   test from chapter 4: does the
   port appear when the cable alone
   is plugged in? If not, nothing
   downstream of this line matters.
2. **The plug is not seated.** The
   handheld two-pin plug, one click
   further. This is the answer
   embarrassingly often.
3. **The radio wants its ceremony.**
   Some models need a menu entry or a
   button held at power-on before
   they will clone (chapter 4). The
   download dialog names it; a radio
   waiting politely looks exactly
   like a radio switched off.
4. **Wrong model picked.** A sibling
   model's name in the dialog can
   open the port and speak the wrong
   dialect. Re-check against the
   radio's own label, not its family
   resemblance.
5. **The battery.** A radio that
   browns out mid-clone answers
   nothing. Charge, retry.

## The port is not in the list

The cable is plugged in; CHIRP's
dialog offers no port, or the system
shows none. On Linux, suspect
chapter 3's group membership first
(`dialout`), and log out and back in
after changing it — group changes do
not reach a running session. On
Windows, a port that appears with a
warning mark is chapter 4's driver
story, up to and including the
counterfeit-chip refusal; Device
Manager's wording is the diagnosis.
On any system, try the cable in a
different USB socket before suspecting
anything grander: sockets differ, and
hubs lie.

## The clone works but the radio is wrong afterwards

Channels missing, names garbled, a
radio behaving oddly in ways channels
do not explain. Ask, in order: was
the *working image* built from this
radio's own factory download, or
from a file that began life
elsewhere (chapter 13's identity
problem, settings and all)? Did the
verify pass of chapter 10 happen, or
only the progress bar? Is the
"missing" channel actually missing,
or out of the bank the radio is
scanning (chapter 2)? The cure for
all three is the same and it is the
reason chapter 5 exists: upload the
factory image, confirm the radio is
its old self, and rebuild from
evidence rather than from memory.

## A channel is silent, both ways or one way

- **Hears the repeater, never heard
  by it:** the offset's sign, or the
  encode tone (chapter 2's two
  classic silences). Check the row
  against the repeater's current
  listing, not the one you imported
  last year.
- **Hears nothing on a channel that
  should talk:** tone *squelch*
  (decode) set where none was
  intended — chapter 11 showed two
  radios filing the same plan's
  decode tone differently; confirm
  the squelch is open (`c` unstarred,
  in chirpc's listing) rather than
  trusting the CSV.
- **Off frequency by a hair:** a
  step-grid rounding from the import
  (chapter 2). The CSV is where to
  see it.

## chirpc runs and says nothing

The lab's own trap, kept as
transcript `chirp-lab/transcripts/t90-silent-chirpc.txt`:
run from a script — stdin not a
terminal — chirpc exits 0 and prints
nothing at all, because CHIRP
redirects its console output to a
debug log file for exactly that
situation. The answers are sitting
in `~/.chirp/debug.log` (566 lines
of them, in the lab's run). The
fixes: read the log, or set
`CHIRP_TESTENV=1` in the script's
environment, which keeps output on
the console where a script expects
it. Interactive users never meet
this; scripters meet it once,
memorably.

## The import that imports nothing

A CSV chosen, a dialog agreed with,
and no channels arrive. Read the
import's own complaints before
anything else: CHIRP's reader is
fussy in writing. The lab hit its
two favourites in its first hour —
a row one **column short** of the
header's 21 ("Line 2 has 20 columns,
expected 21"), and an **empty Power
column**, which the reader rejects
row by row until nothing is left and
it reports, accurately, "No
channels found". Both failures are
in `examples/lab-notes.txt`. The
general rule: compare the file
against a fresh *export* from CHIRP
itself, header first — the export is
the format's living definition.
