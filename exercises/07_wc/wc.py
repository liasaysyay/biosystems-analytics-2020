#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-02-20
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_lines, num_words, num_chars = 0, 0, 0
    total_lines, total_words, total_chars = 0, 0, 0

    for fh in args.file:
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

        print(f'{num_lines:8}{num_words:8}{num_chars:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_chars:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
