#!/usr/bin/env python3
"""Move memories between a CHIRP radio image and a CHIRP CSV file.

Usage:
    exchange_csv.py export IMAGE.img OUT.csv
    exchange_csv.py import PLAN.csv IMAGE.img

Export writes every non-empty memory of the image to a CSV file
in CHIRP's own spreadsheet format. Import reads a CSV file in
that format and writes each row into the image at the row's
Location, saving the image in place -- so work on a copy.

This is the same exchange the CHIRP window performs with its
File > Export and File > Import menu entries, scripted so the
lab can keep transcripts of it.
"""

import sys

sys.modules['builtins']._ = lambda x: x

from chirp import directory
from chirp.drivers import generic_csv

directory.import_drivers()


def load_image(path):
    radio = directory.get_radio_by_image(path)
    radio.load_mmap(path)
    return radio


def do_export(image_path, csv_path):
    radio = load_image(image_path)
    csvradio = generic_csv.CSVRadio(None)
    count = 0
    # CHIRP's memory_bounds are inclusive: (first, last)
    lo, hi = radio.get_features().memory_bounds
    for i in range(lo, hi + 1):
        mem = radio.get_memory(i)
        if mem.empty:
            continue
        csvradio.set_memory(mem)
        count += 1
    csvradio.save_mmap(csv_path)
    print('exported %i memories from %s to %s'
          % (count, image_path, csv_path))


def do_import(csv_path, image_path):
    csvradio = generic_csv.CSVRadio(None)
    csvradio.load_mmap(csv_path)
    radio = load_image(image_path)
    errors = radio.validate_memory
    count = 0
    lo, hi = csvradio.get_features().memory_bounds
    for i in range(lo, hi + 1):
        mem = csvradio.get_memory(i)
        if mem.empty:
            continue
        problems = errors(mem)
        if problems:
            print('SKIP location %i: %s' % (mem.number, problems))
            continue
        radio.set_memory(mem)
        count += 1
    radio.save_mmap(image_path)
    print('imported %i memories from %s into %s'
          % (count, csv_path, image_path))


if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[1] not in ('export', 'import'):
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == 'export':
        do_export(sys.argv[2], sys.argv[3])
    else:
        do_import(sys.argv[2], sys.argv[3])
