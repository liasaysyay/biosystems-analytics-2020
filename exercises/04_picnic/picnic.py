#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-02-05
Purpose: 	Store one or more positional arguments in a list
            Count the number of arguments
            Accept a --sorted argument
            Print a statement that lists the arguments with appropriate grammar
Version: 1
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print the picnic statement with commas and 'and' before the last item"""

    args = get_args()
    items = args.items

    if args.sorted:
        items = sorted(items)
    bringing = ''

    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
