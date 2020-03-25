#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-03-24
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir
    count = 0

    for fh in args.file:
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        for line in fh:
            count += 1
            DNA = line.split()[0]
            RNA = DNA.replace('T', 'U')
            print(RNA, file=out_fh)

    sequence = 'sequence' if count == 1 else 'sequences'
    file = 'file' if len(args.file) == 1 else 'files'
    print(f'Done, wrote {count} {sequence} in {len(args.file)} {file} to directory "{out_dir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
