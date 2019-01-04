import math
from collections import deque

from helpers import manhattan_distance, Point


def traverse_grid(origin, side_length, input, target_max=None):
    if target_max == 1:
        return origin

    grid = []
    for x in range(0, side_length):
        grid.append([])
        for y in range(0, side_length):
            grid[x].append(0)

    d = deque([
        Point(x=1, y=0),
        Point(x=0, y=-1),
        Point(x=-1, y=0),
        Point(x=0, y=1)
    ])

    cell = Point(x=origin.x, y=origin.y)
    grid[cell.x][cell.y] = 1

    cell += d[0]
    grid[cell.x][cell.y] = 1

    d.rotate(-1)

    i = 3
    temp_side_limit = 1
    inc_toggle = True

    while i <= input:

        for l in range(0, temp_side_limit):
            cell += d[0]

            if i == input:
                return cell

            value = compute_value(cell, grid)
            grid[cell.x][cell.y] = value

            if target_max is not None and value > target_max:
                print('Part 2: found larger than target value: {}'.format(value))
                exit()

            i += 1

        if inc_toggle:
            temp_side_limit += 1
            inc_toggle = False
        else:
            inc_toggle = True

        d.rotate(-1)


def compute_value(cell, grid):
    value = 0
    dirs = [
        Point(-1, -1),
        Point(0, -1),
        Point(1, -1),
        Point(-1, 0),
        Point(1, 0),
        Point(-1, 1),
        Point(0, 1),
        Point(1, 1)
    ]

    for dir in dirs:
        value += grid[cell.x + dir.x][cell.y + dir.y]

    return value


def solve_3(input, target_max=None):
    # Adding 5 to give us some buffer
    side_length = math.ceil(math.sqrt(input)) + 5

    center_index = math.floor(side_length / 2.0)
    origin = Point(x=center_index, y=center_index, id=1)

    target = traverse_grid(origin, side_length, input, target_max)

    return manhattan_distance(origin, target)


if __name__ == '__main__':
    r = solve_3(289326)
    print('Part 1: {}'.format(r))

    r = solve_3(289326, 289326)
    print('Part 2: {}'.format(r))
