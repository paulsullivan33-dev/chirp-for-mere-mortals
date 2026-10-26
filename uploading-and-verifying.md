# Uploading and Verifying

Outcome: the edited image written
back to the radio, and a verify pass
— a fresh download compared against
the plan — that proves the radio
holds what you think it holds.
Check: the comparison at the end
shows the plan's rows and nothing
moved that should not have.

The upload itself, like the download
in chapter 5, is taught from the
project's documentation; the verify
half of this chapter is the lab's
real work, done on images.

## Before the cable: the calm checklist

An upload **replaces the radio's
whole memory** with the image. There
is no merge, no undo, and no "only
the channels I changed". So:

1. **The factory image exists and is
   safe** (chapter 5's golden rule).
   If this sentence is not true,
   stop; nothing else in the chapter
   matters until it is.
2. **The working image is the one you
   meant.** File names with dates,
   opened and looked at once more:
   this exact table, this radio's
   model chosen in the dialog — an
   image for the wrong model is
   refused by CHIRP when it knows,
   and written blindly by nobody you
   want to imitate.
3. **The battery is charged**, or the
   radio is on a mains supply. An
   upload starved halfway is the one
   accident in this book that can
   leave a radio needing its maker's
   help.
4. **The channel plan passed its
   hand check** (chapter 7) — because
   an upload is faithful: it writes
   errors with the same care as
   truths.

## The upload

In the window: open the working
image, *Radio → Upload To Radio*,
confirm the port and model, OK.
chirpc's equivalent:

```bash
chirpc -r Baofeng_UV-5R --serial=COM5 \
       --mmap=uv5r-millbrook.img --upload-mmap
```

The progress bar crosses the other
way; the radio may restart into its
new personality. Do not unplug mid-
bar. When it finishes, look at the
radio before touching the computer:
scroll two or three channels on its
own display. The plan should be
sitting there, named as the plan
named it.

## Verify: trust, then download again

"Upload succeeded" is a claim by a
progress bar. The verify pass turns
it into evidence, and it costs two
minutes: **download the radio again,
into a new file** (`uv5r-verify.img`),
and compare that image against the
plan. In the window that means
opening the verify image beside the
plan; in the lab it meant exporting
the verify image to CSV and reading
the rows back — the full round trip,
run for real (transcript
`chirp-lab/transcripts/t10-round-trip.txt`):

```bash
python3 exchange_csv.py export \
    images/uv5r-millbrook.img csv/uv5r-millbrook-export.csv
# exported 47 memories
```

The count itself is a check: 37
channels the radio arrived with, plus
the plan's 10, is 47 — nothing lost,
nothing doubled. And the rows read
back letter for letter, down to the
channel chirpc itself had copied and
renamed along the way:

```text
1,MB R94,146.940000,-,0.600000,Tone,88.5,88.5,...
11,CALL B,146.520000,,0.000000,,88.5,88.5,...
```

That editing demo is worth having on
the record, because you will do it in
the window: chirpc copied channel 5
to 11 and renamed it (transcript
`chirp-lab/transcripts/t08-chirpc-edit.txt`),
and the export proves the edit stuck
in the image, not just on a screen.

Finally, the **on-air check**, for
the channels that matter: listen to
each repeater channel once (do you
hear it?), key one repeater briefly
with your call sign (does it answer,
and does its tone open?), and try one
simplex channel against a second
radio or a friend. A plan that has
passed the file check and the ear
check is done. Label the verify
image with its date and keep it: it
is the new known-good, and the radio
can be restored to *this* state any
day you need it.
