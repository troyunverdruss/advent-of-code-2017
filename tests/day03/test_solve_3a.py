from unittest import TestCase

from days.day03.puzzle_3 import solve_3


class TestSolve3(TestCase):
    def test_2(self):
        r = solve_3(12)
        self.assertEqual(3, r)

    def test_3(self):
        r = solve_3(23)
        self.assertEqual(2, r)

    def test_4(self):
        r = solve_3(1024)
        self.assertEqual(31, r)
