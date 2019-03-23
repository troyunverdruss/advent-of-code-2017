# For pypy
# import sys
# sys.path.append('/Users/troy/Documents/code/advent-of-code-2017')
from helpers import read_raw_entries


class Generator:
    def __init__(self, seed, factor, match_multiple=1):
        self.value = seed
        self.factor = factor
        self.match_multiple = match_multiple

    def next(self):
        # Part 1
        if self.match_multiple == 1:
            _next = self.value * self.factor % 2147483647
            self.value = _next
            return _next

        # Part 2
        _next = self.value * self.factor % 2147483647
        while _next % self.match_multiple != 0:
            self.value = _next
            _next = self.value * self.factor % 2147483647
        self.value = _next
        return _next


def lower_16(i):
    return bin(i)[2:].zfill(16)[-16:]


def solve_15(seed_a, seed_b):
    # generator_a = Generator(65, 16807)
    # generator_b = Generator(8921, 48271)
    generator_a = Generator(seed_a, 16807)
    generator_b = Generator(seed_b, 48271)

    matches = 0
    for i in range(40_000_000):
        if lower_16(generator_a.next()) == lower_16(generator_b.next()):
            matches += 1

    return matches


def solve_15b(seed_a, seed_b):
    generator_a = Generator(seed_a, 16807, 4)
    generator_b = Generator(seed_b, 48271, 8)

    matches = 0
    for i in range(5_000_000):
        if lower_16(generator_a.next()) == lower_16(generator_b.next()):
            matches += 1

    return matches


if __name__ == '__main__':
    entries = read_raw_entries('input_15.txt')
    seed_a = int(entries[0].split()[-1])
    seed_b = int(entries[1].split()[-1])
    r = solve_15(seed_a, seed_b)
    print('part 1, 40M cycles, matched: {}'.format(r))
    # 592

    r = solve_15b(seed_a, seed_b)
    print('part 2, 5M cycles, matched: {}'.format(r))
    # 320
