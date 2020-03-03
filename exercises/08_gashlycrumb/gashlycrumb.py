#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-03-01
Purpose: Look up a line of text from an input file based on a letter provided by the user
Version: 1
"""

import argparse
import os
import sys
from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='See how kids died',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        nargs='+',
                        type= str,
                        help='Letter')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    death_dict = {line[0].upper(): line.rstrip() for line in args.file}

    for letter in args.letter:
        if letter.upper() in death_dict:
            print(death_dict[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
