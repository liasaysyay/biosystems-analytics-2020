#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-02-17
Purpose: 	Accept input text from the command line or a file
            Change strings to uppercase
            Print output to command line or a file to be created
            Make plain text behave like a file handle
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    print(args.text.upper(), file=out_fh)
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
