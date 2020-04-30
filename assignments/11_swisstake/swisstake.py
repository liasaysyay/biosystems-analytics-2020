#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-04-29
Purpose: Homework 11
"""

import argparse
import os
import sys
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        nargs='+',
                        default=None,
                        required=True)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='taxa',
                        type=str,
                        nargs='*')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    skipped = 0
    took = 0
    skip = set(map(str.lower, args.skiptaxa))
    kw = set(map(str.lower, args.keyword))

    for rec in SeqIO.parse(args.file, 'swiss'):
        taxonomy = rec.annotations.get('taxonomy')
        keywords = rec.annotations.get('keywords')

        if taxonomy:
            taxa = set(map(str.lower, taxonomy))
            if skip.intersection(taxa):
                skipped += 1

        if keywords:
            keywords = set(map(str.lower, keywords))
            if kw.intersection(keywords):
                SeqIO.write(rec, args.outfile, 'fasta')
                took += 1

    print(f'Done, skipped {skipped} and took {took}. See output in {args.outfile.name}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
