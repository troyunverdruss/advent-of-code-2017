from unittest import TestCase

from days.day15.puzzle_15 import Generator


class TestSolve15(TestCase):
    def test_gen_a(self):
        gen = Generator(65, 16807)
        self.assertEqual(1092455, gen.next())
        self.assertEqual(1181022009, gen.next())
        self.assertEqual(245556042, gen.next())
        self.assertEqual(1744312007, gen.next())
        self.assertEqual(1352636452, gen.next())

    def test_gen_b(self):
        gen = Generator(8921, 48271)
        self.assertEqual(430625591, gen.next())
        self.assertEqual(1233683848, gen.next())
        self.assertEqual(1431495498, gen.next())
        self.assertEqual(137874439, gen.next())
        self.assertEqual(285222916, gen.next())

    def test_gen_a_part_2(self):
        gen = Generator(65, 16807, 4)
        self.assertEqual(1352636452, gen.next())
        self.assertEqual(1992081072, gen.next())
        self.assertEqual(530830436, gen.next())
        self.assertEqual(1980017072, gen.next())
        self.assertEqual(740335192, gen.next())

    def test_gen_b_part_2(self):
        gen = Generator(8921, 48271, 8)
        self.assertEqual(1233683848, gen.next())
        self.assertEqual(862516352, gen.next())
        self.assertEqual(1159784568, gen.next())
        self.assertEqual(1616057672, gen.next())
        self.assertEqual(412269392, gen.next())
