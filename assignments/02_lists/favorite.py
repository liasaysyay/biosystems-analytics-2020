#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-02-10
Purpose: Homework 2
Version: 2 - remove the else for sep
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('things',
                        metavar='str',
                        nargs='+',
                        help='Some things')

    parser.add_argument('-s',
                        '--sep',
                        help='A separator',
                        metavar='str',
                        type=str,
                        default=', ')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """List my favorite things separated by a , or any given separator. """

    args = get_args()
    things = args.things
    num = len(things)

    if args.sep:
        print(args.sep.join(things))

    if num == 1:
        print('This is one of my favorite things.')
    else:
        print('These are a few of my favorite things.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
