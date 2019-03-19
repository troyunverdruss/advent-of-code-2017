from collections import Counter

from days.day10.puzzle_10 import knot_hash


def knot_hash_bin(_str):
    binary_str = ''
    h = knot_hash(_str)
    for c in list(h):
        binary_str += bin(int(c, 16))[2:].zfill(4)

    return binary_str


def solve_14(seed_str):
    disk = [list(knot_hash_bin(seed_str + '-{}'.format(i))) for i in range(0, 128)]

    counter = Counter([entry for row in disk for entry in row])

    return counter['1']


def search_adjacent_squares(disk, visited, x, y):
    if (x, y) in visited:
        return

    if y >= len(disk) or y < 0 or x >= len(disk[y]) or x < 0:
        return

    visited[(x, y)] = True
    if disk[y][x] == '0':
        return

    search_adjacent_squares(disk, visited, x, y - 1)
    search_adjacent_squares(disk, visited, x, y + 1)
    search_adjacent_squares(disk, visited, x - 1, y)
    search_adjacent_squares(disk, visited, x + 1, y)


def solve_14b(seed_str):
    disk = [list(knot_hash_bin(seed_str + '-{}'.format(i))) for i in range(0, 128)]

    visited = {}
    groups = 0

    for y in range(len(disk)):
        for x in range(len(disk[y])):
            if (x, y) in visited:
                continue

            # visited[(x, y)] = True
            if disk[y][x] == '1':
                groups += 1
            search_adjacent_squares(disk, visited, x, y)

    return groups


if __name__ == '__main__':
    seed = 'ffayrhll'
    r = solve_14(seed)
    print('part 1, count of filled entries: {}'.format(r))
    r = solve_14b(seed)
    print('part 2, distinct groups: {}'.format(r))
