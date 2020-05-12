#!usr/bin/env python3
"""tests for acey_duecy.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

import acey_duecy

prg = './acey_duecy.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
# def test_players():
#     """fails on bad file"""
#
#     bad = random_string()
#     rv, out = getstatusoutput(f'{prg} {bad}')
#     assert rv != 0
#     assert re.search(f"No such file or directory: '{bad}'", out)
#

# --------------------------------------------------
def test_money():
    """fails on bad input"""


# --------------------------------------------------
def test_bets(capsys):
    """does not allow for players to place bets they cannot afford"""

    # rv, out = getstatusoutput(f'{prg} Lia Humberto -s 1')
    input_values = ['keep', 0, 'change', 10]

    def mock_input(s):
        return input_values.pop(0)
    acey_duecy.input = mock_input

    if __name__ == '__main__':
        acey_duecy

    out = capsys.readouterr()

    # assert out == "GAME OVER! Final Scores: {'Lia': 10, 'Humberto': 20}"
# assert rv == 0
    assert re.search("GAME OVER! Final Scores: {'Lia': 10, 'Humberto': 20}", out)


# --------------------------------------------------
def test_winning():
    """Money can be won"""


# --------------------------------------------------
def test_losing():
    """Money can be lost"""


# --------------------------------------------------
def test_ending():
    """Game ends"""
    rv, out = getstatusoutput(f'{prg} Lia Humberto -s 1')
    assert re.search("GAME OVER! Final Scores: {'Lia': 10, 'Humberto': 20}")


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
