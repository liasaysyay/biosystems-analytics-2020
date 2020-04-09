#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-04-08
Purpose: Homework 9
"""

from Bio import SeqIO
import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not 0 < args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out_dir = args.outdir
    count = 0

    for i, fh in enumerate(args.file, start=1):
        basename = os.path.basename(fh.name)
        out_file = os.path.join(out_dir, basename)
        print(f'{i:3}: {basename}')

        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                count += 1

        out_fh.close()

    sequence = 'sequence' if count == 1 else 'sequences'
    file = 'file' if len(args.file) == 1 else 'files'
    print(f'Wrote {count:,} {sequence} from {len(args.file)} {file} to directory "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
