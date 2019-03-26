from unittest import TestCase

from days.day18.puzzle_18 import Soundcard, SoundcardPair


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
        soundcard = Soundcard(instructions)
        value = soundcard.process_instructions()
        self.assertEqual(value, 4)

    def test_part_2(self):
        instructions = [
            'snd 1',
            'snd 2',
            'snd p',
            'rcv a',
            'rcv b',
            'rcv c',
            'rcv d',
        ]

        soundcard_pair = SoundcardPair(instructions)
        soundcard_pair.run()

        self.assertEqual(3, soundcard_pair.card_1.snd_count)
