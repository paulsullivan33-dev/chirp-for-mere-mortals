# Cables and Drivers

Outcome: a cable your computer can
see, a port name you can point CHIRP
at, and the knowledge to tell a
driver problem from a radio problem.
Check: by the last section you can
plug the cable in — radio still
detached — and watch the port appear.

This chapter is documented from the
project's guidance rather than the
lab's bench: the lab had no physical
radio or cable (see `criteria.md`),
and everything here is the part of
CHIRP that only exists between a real
radio and a real computer. It is
taught carefully because it is where
nearly every first attempt stalls.

## What the cable is

A **programming cable** is not a
charger and not an audio lead,
although it may end in the same plug.
Inside it sits a small chip that
translates between the computer's USB
and the radio's serial signals. One
end is USB; the other is whatever the
radio wears — a two-pin plug for most
handhelds (the speaker/mic socket
doubles as the programming port), a
mini-USB or a round multi-pin plug on
mobiles. The cable belongs to the
*radio family*, not to CHIRP: the same
cable serves the maker's software too.

Two consequences. Buy the cable by
the radio's name, not by the plug's
shape — two plugs can match physically
and be wired differently. And seat
the plug *fully*: the commonest cable
fault in the world is a handheld's
two-pin plug stopped one click short,
which presents exactly like a dead
radio.

## The chip, and the counterfeit problem

The translation chip is usually one
of three: **FTDI**, **Prolific**, or a
**CH340**/WCH part. The chip decides
which **driver** — the small piece of
system software that turns USB into a
named serial port — your computer
needs:

- **Windows** often finds a driver by
  itself. When it does not, install
  the chip maker's current driver, not
  the one on the disc in the cable's
  bag.
- **macOS** carries drivers for the
  common chips in recent versions.
- **Linux** carries all three in the
  kernel; your work there is the
  group membership from chapter 3,
  not a download.

Now the honest paragraph. The market
is flooded with cables built around
**counterfeit Prolific chips** —
copies that identify as the real
thing. Prolific's current drivers
detect them and refuse to work, which
is why a brand-new cable plus a
brand-new driver can equal a port
that appears and instantly errors.
The project's cable guide names the
symptoms and the older driver that
tolerates the copies, and reading it
is worth ten forum threads. The
durable fixes, in order: buy the
cable from the radio's maker or a
radio dealer rather than the cheapest
listing; prefer an FTDI-chip cable
when one is offered for your radio;
and treat a cable that has never
worked anywhere as a cable problem
until proven otherwise.

## The port gets a name

When the driver is happy, plugging
the cable in creates a **serial port**
with a name, and the name is what
CHIRP asks for:

- Windows: `COM3`, `COM5` — find it in
  Device Manager under *Ports*, and
  watch which number appears when you
  plug in. The number can change
  between USB sockets.
- macOS: a file like
  `/dev/cu.usbserial-…`.
- Linux: `/dev/ttyUSB0` (or `ttyACM0`
  for some chips).

You can verify all of this with the
radio *detached*: plug in the bare
cable and the port should appear;
unplug and it should vanish. That
two-step test separates the whole
cable-and-driver stack from the radio
itself, and chapter 14 sends you back
to it constantly. In CHIRP's window
the port is chosen in the download
dialog; chirpc takes it as
`--serial=COM5`. The special value
`--serial=mmap` tells chirpc to work
on an image file alone — the mode
this guide's lab lived in.

## The radio's side of the bargain

Some radios clone whenever the cable
is connected. Others want a small
ceremony first — a menu entry, a
button held while switching on, a
"clone" mode chosen on the radio
itself. The download dialog in CHIRP
shows the instruction for the model
you picked, when there is one; read
it *before* clicking OK, because a
radio waiting for its ceremony looks,
to the computer, exactly like a radio
that is switched off. Use a charged
battery or a mains supply for
programming, never a nearly-flat one:
an upload interrupted by a dying
battery is the one genuinely bad day
in this hobby (chapter 13), and it
is entirely preventable here.
