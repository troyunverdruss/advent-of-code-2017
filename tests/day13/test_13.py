from unittest import TestCase

from days.day13.puzzle_13 import solve_13, solve_13b


class TestSolve13(TestCase):
    def test_part_1(self):
        input = [
            '0: 3', '1: 2', '4: 4', '6: 4'
        ]
        r = solve_13(input)
        self.assertEqual(24, r)

    def test_part_2(self):
        input = [
            '0: 3', '1: 2', '4: 4', '6: 4'
        ]
        delay = solve_13b(input)
        self.assertEqual(10, delay)
