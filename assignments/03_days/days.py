#!/usr/bin/env python3
"""
Author : lia
Date   : 2020-02-17
Purpose: Homework 3
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='What to do on each day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('day',
                        metavar='str',
                        nargs='+',
                        help='Days of the week')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """A dictionary of weekly activities"""

    args = get_args()

    week = {'Monday': 'On Mondays I never go to work',
            'Tuesday': 'On Tuesdays I stay at home',
            'Wednesday': 'On Wednesdays I never feel inclined',
            'Thursday': "On Thursdays, it's a holiday",
            'Friday': 'And Fridays I detest',
            'Saturday': "Oh, it's much too late on a Saturday",
            'Sunday': "And Sunday is the day of rest"}

    for day in args.day:
        print(week.get(day, f'Can\'t find "{day}"'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
