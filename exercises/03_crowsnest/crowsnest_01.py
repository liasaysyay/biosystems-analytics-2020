#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-01-27
Purpose: Accepts a single positional argument
         Prints a statement and chooses 'a' or 'an' according to the argument
Version: 1
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print the Ahoy statement with the word argument and correct article"""

    args = get_args()
    word = args.word

    """choose article based on first letter of word"""
    char = word[0].lower() in 'aeiou'
    article = ''

    if char == True:
        article = 'an'

    else:
        article = 'a'


    # print('positional = "{}"'.format(word))

    print('Ahoy, Captain, ' + article + ' ' + word + ' off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
