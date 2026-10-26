# Settings Beyond Memories

Outcome: the rest of what lives in
an image — the radio's own settings
— and judgement about which of them
to touch. Check: the lab listed a
real image's settings below; your
check is finding them in the window
and changing exactly none of them
until this chapter is done.

## An image is more than channels

Chapter 5 called the image "the
radio's whole memory", and the whole
is bigger than the channel list.
Alongside its memories, a radio keeps
its **settings**: squelch level, the
transmitter **timeout timer**, what
the display shows, whether the keypad
beeps, whether the menu is locked
down. They are in the image because
they are in the same memory the clone
moves. CHIRP's window shows them
under *Settings* once an image is
open; chirpc lists them:

```bash
chirpc --mmap=uv5r-factory.img --list-settings
```

The lab's listing ran to 91 lines
(transcript `chirp-lab/transcripts/t03-settings.txt`),
in groups the driver names *basic*
and *advanced*:

```text
group 'basic': {
	squelch:1
	timeout:30 sec
	beep:False
	mdfa:Frequency
	...
}
group 'advanced': {
	bcl:True
	vox:OFF
	...
}
```

Squelch 1, a 30-second timeout,
no beep, the A display showing
frequencies, busy-channel lockout
on — a previous owner's taste,
written in the same file as their
channels, and restorable from the
same file.

## Why settings deserve respect

Three reasons to go slowly here.

**A setting cloned is a setting
copied everywhere.** Put a short
timeout or a locked menu into your
plan's working image and every radio
you upload it to inherits the
surprise. Settings are where an
image stops being a channel list
and becomes a whole personality,
and chapter 1's warning about a
stranger's image applies double:
their squelch, their lockouts,
their disabled menu (the lab's
image carried `menu:True` — the
setting that, flipped, locks the
owner out of the radio's own menus)
all arrive unannounced.

**Some settings guard the radio or
the law.** The timeout timer caps a
stuck transmission. The channel
range setting can widen a radio
beyond its certified bands, which
is chapter 8's certification rule
and chapter 13's edge — CHIRP shows
it because it is in the memory, not
because using it is licensed.

**Settings are the least portable
part of an image.** The next chapter
but one moves a plan between two
radios; memories cross because
CHIRP translates them, but settings
have no translation — each radio's
settings are its own, in its own
image. Building the same plan on a
second radio means doing the
settings again, by hand, in that
radio's image. That is not a flaw;
it is the boundary of what a plan
is.

## The working rule

Set settings in the image of the
radio they belong to, one radio at
a time, after its channels are
right — and keep a note in the plan
of what you chose and why (the CSV
comment habit, applied to a list).
The settings you should meet first,
on any radio: squelch, timeout,
display mode, the scan behaviour,
and the lock settings. Everything
with *lock*, *limit* or *range* in
its name gets read twice and a trip
to chapter 13 before it gets
changed.
