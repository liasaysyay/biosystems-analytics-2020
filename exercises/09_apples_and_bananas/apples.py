#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-03-21
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        default='a',
                        choices='aeiou')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    new = ''
    for char in text:
        if char in 'aeiou':
            new += vowel
        elif char in 'AEIOU':
            new += vowel.upper()
        else:
            new += char
    print(new)


# --------------------------------------------------
if __name__ == '__main__':
    main()
