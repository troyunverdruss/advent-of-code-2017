aoc17() if 'aoc17' in dir() else None
from unittest import TestCase

from days.day20.puzzle_20 import parse_particles, Particle
from helpers import read_raw_entries, Point3d


class TestSolve20(TestCase):
    def test_parse_particles(self):
        entries = read_raw_entries('test_d20.txt')
        particles = parse_particles(entries)

        self.assertEqual(particles[0], Particle(Point3d(3, 0, 0), Point3d(2, 0, 0), Point3d(-1, 0, 0)))
        self.assertEqual(particles[1], Particle(Point3d(4, 0, 0), Point3d(0, 0, 0), Point3d(-2, 0, 0)))

    def test_sample_positions(self):
        entries = read_raw_entries('test_d20.txt')
        particles = parse_particles(entries)

        for _ in range(3):
            for p in particles:
                p.step()

        self.assertEqual(particles[0], Particle(Point3d(3, 0, 0), Point3d(-1, 0, 0), Point3d(-1, 0, 0)))
        self.assertEqual(particles[1], Particle(Point3d(-8, 0, 0), Point3d(-6, 0, 0), Point3d(-2, 0, 0)))

    def test_particles_in_set(self):
        zero = Point3d(0, 0, 0)
        a = Particle(zero, zero, zero, 1)
        aa = Particle(zero, zero, zero, 1)
        b = Particle(zero, zero, zero, 2)

        self.assertEqual(a, aa)

        set_a = {a, b}
        set_b = {a, b}
        set_c = {a}

        self.assertEqual(set(), set_a - set_b)
        self.assertEqual({b}, set_a - set_c)

        set_a -= set_c

        self.assertEqual({b}, set_a)
