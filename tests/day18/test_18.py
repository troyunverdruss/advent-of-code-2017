from unittest import TestCase

from days.day18.puzzle_18 import Soundcard


class TestSolve18(TestCase):
    def test_sample(self):
        instructions = [
            'set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2',
        ]
        soundcard = Soundcard()
        value = soundcard.process_instructions(instructions)
        self.assertEqual(value, 4)
