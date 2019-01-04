from collections import deque

from helpers import read_raw_entries, path


def solve_1(input, offset=1):
    d = deque(list(input))

    total = 0

    for i in range(0, len(d)):
        if d[0] == d[offset]:
            total += int(d[0])
        d.rotate(-1)
    return total


if __name__ == '__main__':
    input = read_raw_entries(path(__file__, 'input-d1.txt'))[0].strip()
    r = solve_1(input)
    print('Part 1: {}'.format(r))

    r = solve_1(input, int(len(list(input)) / 2))
    print('Part 2: {}'.format(r))
