from collections import deque
from unittest import TestCase

from days.day16.puzzle_16 import solve_16, spin, exchange, partner, solve_16b


class TestSolve16(TestCase):
    def test_spin(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        spin(seq, 's1')
        self.assertEqual(''.join(seq), 'eabcd')

    def test_exchange_1(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        exchange(seq, 'x3/4')
        self.assertEqual(''.join(seq), 'abced')

    def test_exchange_2(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        exchange(seq, 'x0/4')
        self.assertEqual(''.join(seq), 'ebcda')

    def test_partner(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        partner(seq, 'pe/b')
        self.assertEqual(''.join(seq), 'aecdb')

    def test_part_1(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        instructions = ['s1', 'x3/4', 'pe/b']
        result = solve_16(seq, instructions)
        self.assertEqual(result, 'baedc')

    def test_part_2_example(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        instructions = ['s1', 'x3/4', 'pe/b']
        result = solve_16b(seq, instructions, 2)
        self.assertEqual(result, 'ceadb')

    def test_part_2_offset_math(self):
        seq = deque([chr(i) for i in range(ord('a'), ord('e') + 1)])
        instructions = ['s1', 'x3/4', 'pe/b']
        result = solve_16b(seq, instructions, 100)
        self.assertEqual(result, 'abcde')
