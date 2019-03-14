from unittest import TestCase

from days.day09.puzzle_09 import solve_09


class TestSolve09(TestCase):
    def test_1(self):
        r = solve_09('{}')
        self.assertEqual(r, 1)

    def test_2(self):
        r = solve_09('{{{}}}')
        self.assertEqual(r, 6)

    def test_3(self):
        r = solve_09('{{},{}}')
        self.assertEqual(r, 5)

    def test_4(self):
        r = solve_09('{{{},{},{{}}}}')
        self.assertEqual(r, 16)

    def test_5(self):
        r = solve_09('{<a>,<a>,<a>,<a>}')
        self.assertEqual(r, 1)

    def test_6(self):
        r = solve_09('{{<ab>},{<ab>},{<ab>},{<ab>}}')
        self.assertEqual(r, 9)

    def test_7(self):
        r = solve_09('{{<!!>},{<!!>},{<!!>},{<!!>}}')
        self.assertEqual(r, 9)

    def test_8(self):
        r = solve_09('{{<a!>},{<a!>},{<a!>},{<ab>}}')
        self.assertEqual(r, 3)
