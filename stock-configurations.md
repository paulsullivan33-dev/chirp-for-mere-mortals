# Stock Configurations

Outcome: the ready-made channel sets
inside CHIRP, what each is for, and a
clear rule for when a stock row
belongs in your plan and when it
does not. Check: the lab loaded one
set and counted its channels below;
yours should open just as plainly.

## What ships in the box

CHIRP carries a folder of ready-made
plans called **stock configurations**:
CSV files, in the same format as
chapter 6, holding the standard
channels of various services and
countries. In the window they appear
under *File → Open Stock Config*. The
lab counted **twenty files** in its
install (transcript
`chirp-lab/transcripts/t09-stock-configs.txt`),
including:

- **US Calling Frequencies** — the
  channel each band calls home.
- **US NOAA Weather Alert** — the
  162 MHz weather channels, receive
  only.
- **US FRS and GMRS Channels**, **US
  MURS Channels** — licence-free
  neighbourhood radio services, for
  radios certified for them.
- **Marine VHF**, **Aviation**,
  **Railroad** lists — listening,
  mostly.
- Calling lists for other countries,
  and services such as PMR446 and
  Freenet overseas.

The sets are humble and useful:
they are the rows most plans repeat,
kept once, identically, by the
project — so a plan built anywhere
has the same 146.520 in it as
yours.

## Using them

Open the stock file, copy the rows
you want into your plan — in the
window, copy and paste between the
two tables; in CSV, paste the rows
into your plan file and renumber the
locations. The lab verified the
mechanics with CHIRP's own reader:
the US Calling Frequencies file
loads clean with **4 channels**
(52.525, 146.520, 223.500, 446.000).
Note two rows of it in your head:
the Millbrook plan took 146.520 and
446.000 from exactly this list, and
the 6-metre row did *not* come
along, because the lab's radios are
dual-band handhelds that cannot hold
it — stock data obeys the same
question 1 as chapter 7's imports:
*can this radio, and my licence,
use this row?*

One wrinkle worth knowing: the
shipped files use a slightly older,
shorter column layout (19 columns,
no power column among them) than a
fresh export writes. CHIRP reads
them anyway. If you build on a stock
file outside CHIRP, give every row a
Power value before importing, or
chapter 6's rejection will find you.

## The rule

Take from a stock set the rows that
are **facts by definition** (calling
frequencies, weather channels — a
frequency that a whole service
agrees on). Be warier of stock rows
that claim a *service exists at a
place*: airband and railroad lists
are listening material, FRS and
MURS channels are for radios
certified for those services (your
amateur handheld is not certified
for them, even though it can hold
the frequencies — the type-acceptance
rule, and it is the law, not a
suggestion), and marine channels
afloat are governed by their own
rules. The stock folder hands you
correct frequencies. What you may
do with each of them is still your
licence and your radio's
certification talking.
