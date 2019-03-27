aoc17() if 'aoc17' in dir() else None
from unittest import TestCase

from days.day19.puzzle_19 import solve_19, build_network_map, find_start_pos, solve_19b
from helpers import read_raw_entries, Point


class TestSolve19(TestCase):
    def test_sample(self):
        entries = read_raw_entries('test_input_d19.txt', strip=False)
        r = solve_19(entries)
        self.assertEqual(r, 'ABCDEF')

    def test_sample_part_2(self):
        entries = read_raw_entries('test_input_d19.txt', strip=False)
        r = solve_19b(entries)
        self.assertEqual(r, 38)

    def test_build_network_map(self):
        entries = read_raw_entries('test_input_d19.txt', strip=False)

        network_map = build_network_map(entries)

        self.assertEqual(network_map[(0, 0)], ' ')
        self.assertEqual(network_map[(5, 0)], '|')
        self.assertEqual(network_map[(5, 5)], '+')
        self.assertEqual(network_map[(6, 5)], 'B')
        self.assertEqual(network_map[(14, 5)], '+')

    def test_find_start(self):
        entries = read_raw_entries('test_input_d19.txt', strip=False)
        network_map = build_network_map(entries)
        start = find_start_pos(network_map)
        self.assertEqual(start, Point(5, 0))
