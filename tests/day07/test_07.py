from unittest import TestCase

from days.day07.puzzle_07 import solve_07b
from helpers import read_raw_entries


class TestSolve07(TestCase):
    def test_balancing(self):
        entries = read_raw_entries('test_input_d7.txt')
        r = solve_07b(entries)
        self.assertEqual(60, r)
