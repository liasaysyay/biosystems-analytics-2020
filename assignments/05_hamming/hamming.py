#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-03-02
Purpose: Homework 5 - find the edit distance between two strings
"""

import argparse
import os
import sys
from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find the hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-m',
                        '--min',
                        help='A minimum integer',
                        metavar='int',
                        type=int,
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """find the hamming distance and set an optional minimum"""

    args = get_args()

    for line in args.file:
        num_words = len(line.split())
        num_pairs = int(num_words / 2)
        for i in range(num_words - num_pairs):
            word1, word2 = line.split()
            ham = [c1 == c2 for c1, c2 in zip(word1, word2)]
            hamming = len(word2) - (sum(ham[:]))

            if hamming >= args.min:
                print(f'{hamming:8}:{word1:20}{word2:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
