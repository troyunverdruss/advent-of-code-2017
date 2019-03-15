from collections import deque
from unittest import TestCase

from days.day10.puzzle_10 import solve_10, compute_lengths, solve_10b


class TestSolve10(TestCase):
    def test_sample(self):
        r = solve_10(deque(range(0, 5)), [3, 4, 1, 5])
        self.assertEqual(12, r)

    def test_compute_lengths(self):
        lengths = compute_lengths('1,2,3')
        self.assertEqual(
            lengths,
            [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
        )

    def test_empty(self):
        r = solve_10b(deque(range(0, 256)), '')
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', r)

    def test_aoc2017(self):
        r = solve_10b(deque(range(0, 256)), 'AoC 2017')
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', r)

    def test_123(self):
        r = solve_10b(deque(range(0, 256)), '1,2,3')
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', r)

    def test_124(self):
        r = solve_10b(deque(range(0, 256)), '1,2,4')
        self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', r)
