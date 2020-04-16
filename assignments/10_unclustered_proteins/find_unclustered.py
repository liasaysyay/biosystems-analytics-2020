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
    num_unclustered = 0
    num_proteins = 0

    for line in args.cdhit:
        if not line.startswith('>'):
            match = re.search(r'>(\d+)', line)
            prot_id = match.group(1)
            cluster_ids.add(prot_id)

    for rec in SeqIO.parse(args.proteins, 'fasta'):
        protein_ids = re.sub(r'\|.*', '', rec.id)
        num_proteins +=1
        if protein_ids not in cluster_ids:
            SeqIO.write(rec, args.outfile, 'fasta')
            num_unclustered += 1

    print(f'Wrote {num_unclustered:,} of {num_proteins:,} unclustered proteins to "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
