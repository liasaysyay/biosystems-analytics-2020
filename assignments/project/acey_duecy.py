#!/usr/bin/env python3
"""
Author : Lia Crocker and K. Humberto Lopez Felix
Date   : 2020-04-20
Purpose: Final Project - plays the card game Acey Duecy
"""

import argparse
import os
import sys


class players:
    player = ''


money = ''


def description(self):
    print("The player's name is: ", self.name)
    return


class cards:
    face = ''


suit = ''


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Play a game of Acey Duecy',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('players',
                        nargs='+',
                        help='Player names text or file',
                        metavar='str',
                        type=str)

    parser.add_argument('-b',
                        '--bank',
                        help='Start value of bank',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--money',
                        help='Start value for players',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.players):
        args.players = open(args.players).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    com_line_player = args.players
    player1 = players()
    player1.name = com_line_player[0]

    print(player1.description())
    print(args.players)


# --------------------------------------------------
if __name__ == '__main__':
    main()
