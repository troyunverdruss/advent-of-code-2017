from unittest import TestCase

from days.day21.puzzle_21 import process_entries_to_rules, process_segment


class TestSolve21(TestCase):
    def test_rules_matching(self):
        entries = [
            "../.. => .#./.../###"
        ]

        rules = process_entries_to_rules(entries)

        self.assertEqual(1, len(rules))

        test = [
            ['.', '.'],
            ['.', '.'],
        ]

        output = process_segment(rules, test)
        self.assertEqual(3, len(output))
