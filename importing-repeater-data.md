# Importing Repeater Data

Outcome: repeater data brought into
a plan from an outside source, and a
hand check you can do in ten minutes
that catches the errors imports
routinely carry. Check: every row of
your imported list should survive the
five questions at the end of this
chapter, or it should not be in your
radio.

You will not type a hundred
repeaters by hand. Somebody already
has: repeater directories, club
lists, and CHIRP's own import
sources. The question is not where
the data comes from — it is what you
believe of it before you transmit on
it.

## Where repeater data lives

- **CHIRP's RepeaterBook import.**
  In the window, *Radio → Import From
  Data Source* offers RepeaterBook,
  the community repeater directory:
  pick a region and a band, and
  CHIRP pulls the directory's list
  into your table. It is the fastest
  honest source for a new plan.
- **Club and directory CSVs.** A club
  hands out its own list, or you save
  one from a directory's website.
  Import it as a CSV (chapter 6's
  format), and CHIRP will try to make
  sense of its columns — which is
  where the hand check earns its keep,
  because column names are not
  standardised across sources.
- **The stock configurations of
  chapter 8.** Fixed lists of
  frequencies that do not move —
  calling frequencies, weather
  channels — where the data's age
  does not matter.

In every case the import is a
*proposal*. CHIRP's import dialogs
ask which rows to take and where to
put them; they do not ask whether
the rows are true. That question is
yours.

## The five-question hand check

Take the list a row at a time, and
for each row answer:

1. **Is the frequency in a band I may
   use?** An import knows no licence.
   A repeater listed on 145 MHz
   belongs to your privileges; a row
   at 155 MHz does not belong in your
   radio's plan at all, however neatly
   the import formatted it.
2. **Is the offset right, and is the
   sign right?** Band habit says 0.600
   and 5.000 (chapter 2), but some
   repeaters are odd. A wrong sign is
   a silent failure: you hear it fine,
   it never hears you.
3. **Is the tone the one the repeater
   wants today?** Tones change. A
   list two years old has the old
   one, and a repeater that changed
   its tone will ignore you
   politely.
4. **Is the row a duplicate?** Imports
   overlap: the same repeater arrives
   twice, once at location 12 and once
   at 87, under slightly different
   names. Duplicates are not dangerous
   — they are confusing at the worst
   moment.
5. **Is this repeater actually there?**
   Repeaters go silent, move sites,
   change ownership. The only proof
   that costs nothing is listening:
   park on the frequency, wait for
   the repeater's identification or a
   conversation, and confirm the
   tone by keying once, briefly, and
   hearing the repeater answer. If
   you cannot confirm it, leave it
   out — a plan with nine verified
   repeaters beats one with forty
   rumours.

## Fixing before importing, not after

Do the surgery in the CSV, not in
the radio. If a source's column for
the tone is called `CTCSS` and CHIRP
expects `rToneFreq`, rename the
column in the spreadsheet (or
CHIRP's import mapping, which shows
you the guess it made). If a row
fails question 1, delete it. If a
frequency is off the tuning grid,
round it in the file where you can
see the rounding. The import dialog
is a filter, not a hospital; what
arrives clean arrives usable, and the
lab's Millbrook plan was authored in
a spreadsheet precisely so its
ten rows could be argued with before
any radio saw them.

## One more honesty note

Repeater directories are kept by
volunteers, and their listings are
*claims* gathered from owners,
listeners and old lists. Treat a
directory the way you would treat a
friend's directions: excellent, and
verified by driving the road once.
The hand check above is that drive,
and on a real plan it takes minutes
for a county's worth of repeaters —
the cheapest insurance in this whole
guide.
