#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-02-25
Purpose: Homework 4 - give the first 10 (or otherwise specified) lines of a file
Version: 2
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate the Unix head command',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in range(args.num):
        print(args.file.readline().strip('\n'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
