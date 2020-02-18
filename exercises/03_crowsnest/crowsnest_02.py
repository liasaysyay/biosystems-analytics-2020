#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-01-27
Purpose: Accepts a single positional argument
         Prints a statement and chooses 'a' or 'an' according to the argument
Version: 2 - uses if expression instead of if statement
             uses str.format instead of concatenation
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

    article = 'an' if char == True else 'a'


    # print('positional = "{}"'.format(word))

    print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()