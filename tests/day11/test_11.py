from unittest import TestCase

from days.day11.puzzle_11 import solve_11


class TestSolve11(TestCase):
    def test_1(self):
        r = solve_11(['ne', 'ne', 'ne'])
        self.assertEqual(3, r)

    def test_2(self):
        r = solve_11(['ne', 'ne', 'sw', 'sw'])
        self.assertEqual(0, r)

    def test_3(self):
        r = solve_11(['ne', 'ne', 's', 's'])
        self.assertEqual(2, r)

    def test_4(self):
        r = solve_11(['se', 'sw', 'se', 'sw', 'sw'])
        self.assertEqual(3, r)
