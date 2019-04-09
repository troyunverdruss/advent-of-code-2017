aoc17() if 'aoc17' in dir() else None

from collections import defaultdict

from helpers import Point, read_raw_entries

dirs = {
    'up': Point(0, -1),
    'lt': Point(-1, 0),
    'rt': Point(1, 0),
    'dn': Point(0, 1)
}

turn_lt = {'up': 'lt', 'lt': 'dn', 'rt': 'up', 'dn': 'rt'}

turn_rt = {'up': 'rt', 'lt': 'up', 'rt': 'dn', 'dn': 'lt'}

reverse = {'up': 'dn', 'lt': 'rt', 'rt': 'lt', 'dn': 'up'}


class Virus:
    def __init__(self, _loc, _grid):
        self.loc: Point = _loc
        self.grid = _grid
        self.direction = 'up'
        self.infection_count = 0

    def burst(self):
        if self.grid[self.loc] == '#':
            # turn right
            self.direction = turn_rt[self.direction]
            # clean node
            self.grid[self.loc] = '.'

        else:
            # turn left
            self.direction = turn_lt[self.direction]
            # infect node
            self.grid[self.loc] = '#'
            self.infection_count += 1

        # move forward 1 place
        self.loc += dirs[self.direction]


class Virus2:
    def __init__(self, _loc, _grid):
        self.loc: Point = _loc
        self.grid = _grid
        self.direction = 'up'
        self.infection_count = 0

    def burst(self):
        if self.grid[self.loc] == '#':
            # turn right
            self.direction = turn_rt[self.direction]
            # clean node
            self.grid[self.loc] = 'F'

        elif self.grid[self.loc] == '.':
            # turn left
            self.direction = turn_lt[self.direction]
            # infect node
            self.grid[self.loc] = 'W'


        elif self.grid[self.loc] == 'W':
            self.grid[self.loc] = '#'
            self.infection_count += 1

        else:  # Flagged
            self.direction = reverse[self.direction]
            self.grid[self.loc] = '.'

        # move forward 1 place
        self.loc += dirs[self.direction]


def setup_grid_and_start(entries):
    grid = defaultdict(lambda: '.')
    for y in range(len(entries)):
        for x in range(len(entries[y])):
            grid[Point(x, y)] = entries[y][x]

    start = Point(len(entries[0]) / 2, len(entries) / 2)

    return grid, start


def solve_22(entries):
    grid, start = setup_grid_and_start(entries)

    virus = Virus(start, grid)

    for _ in range(10_000):
        virus.burst()

    return virus.infection_count


def solve_22b(entries):
    grid, start = setup_grid_and_start(entries)

    virus = Virus2(start, grid)

    for _ in range(10_000_000):
        virus.burst()

    return virus.infection_count


if __name__ == '__main__':
    entries = read_raw_entries('input_d22.txt')
    r = solve_22(entries)
    print('part 1, number of infections: {}'.format(r))

    r = solve_22b(entries)
    print('part 2, number of infections: {}'.format(r))
