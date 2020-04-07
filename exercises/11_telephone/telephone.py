#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-04-06
Purpose: Play telephone
"""

import argparse
import os
import random
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='float',
                        type=float,
                        default='0.1')

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    len_text = len(text)
    num_mutations = round(len_text * args.mutations)
    alpha = string.ascii_letters + string.punctuation
    new_text = list(text)

    for i in random.sample(range(len_text), num_mutations):
        char = new_text[i]
        new_char = random.choice(alpha.replace(char, ''))
        new_text[i] = new_char

    new_text = ''.join(new_text)
    print(f'You said: "{text}"')
    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
