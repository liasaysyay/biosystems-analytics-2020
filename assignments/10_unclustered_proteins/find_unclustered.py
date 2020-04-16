#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-04-15
Purpose: Homework 10
"""

from Bio import SeqIO
import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    cluster_ids = set()
    protein_ids = set()
    count = 0

    for line in args.cdhit:
        if not line.startswith('>'):
            match = re.search(r'>(\d+)', line)
            id = match.group(1)
            cluster_ids.add(id)

    for rec in SeqIO.parse(args.proteins, 'fasta'):
        new_id = re.sub(r'\|.*', '', rec.id)
        protein_ids.add(new_id)
        if protein_ids not in cluster_ids:
            SeqIO.write(rec, args.outfile, 'fasta')
            count += 1

    print(f'Wrote {count} of {len(cluster_ids)} unclustered proteins to "{args.outfile}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
