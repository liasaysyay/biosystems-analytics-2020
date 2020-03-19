#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-03-15
Purpose: translate DNA/RNA to amino acids
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Be the ribosome"""

    args = get_args()

    translation = {line.split()[0]: line.split()[1] for line in args.codons}

    k = 3
    for codon in [args.sequence[i:i + k] for i in range(0, len(args.sequence) - k + 1, 3)]:
        print(translation.get(codon.upper(), '-'), file=args.outfile, end="")

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
