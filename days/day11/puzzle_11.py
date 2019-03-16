from collections import Counter

from helpers import read_raw_entries, Point

dir_offsets = {
    'n': Point(0, 2),
    's': Point(0, -2),
    'sw': Point(-1, -1),
    'ne': Point(1, 1),
    'se': Point(1, -1),
    'nw': Point(-1, 1)
}


def solve_11(input):
    final_dest = compute_destination(input)
    return compute_shortest_distance(Point(final_dest.x, final_dest.y))


def compute_destination(input):
    counter = Counter(input)

    # We're using a normal grid, but every orthogonal move is +2 and diagonal moves are +1, +1
    loc = Point(0, 0)
    for direction, count in counter.items():
        loc.x = loc.x + (dir_offsets[direction].x * count)
        loc.y = loc.y + (dir_offsets[direction].y * count)
    return loc


def solve_11b(input):
    farthest_point, dist = compute_farthest_point(input)
    print('farthest point reaches: {}'.format(farthest_point))
    return dist


def compute_farthest_point(input):
    # We're using a normal grid, but every orthogonal move is +2 and diagonal moves are +1, +1
    positions = set()

    loc = Point(0, 0)
    for direction in input:
        loc.x = loc.x + dir_offsets[direction].x
        loc.y = loc.y + dir_offsets[direction].y
        positions.add(Point(loc.x, loc.y))

    return max(
        map(lambda p: (p, compute_shortest_distance(p)), positions),
        key=lambda p: p[1]
    )


def compute_shortest_distance(loc):
    # Since all we care about is distance, let's make it easy on ourselves
    # and make everything positive
    _loc = Point(abs(loc.x), abs(loc.y))

    # Now let's walk back to the start
    # Easy cases, we're already on an axis
    if _loc.x == 0:
        return _loc.y / 2
    if _loc.y == 0:
        return _loc.x / 2
    # Now we're not on an axis, so:
    # - get to an axis on a diagonal
    # - and then walk on axis back to origin
    dist = 0
    if _loc.x < _loc.y:
        dist += _loc.x
        dist += (_loc.y - _loc.x) / 2
    elif _loc.y < _loc.x:
        dist += _loc.y
        dist += (_loc.x - _loc.y) / 2
    else:
        dist = _loc.x
    # answer: 834
    return int(dist)


if __name__ == '__main__':
    input = read_raw_entries('input_d11.txt')[0].split(',')
    r = solve_11(input)
    print('part 1, fewest steps: {}'.format(r))
    r = solve_11b(input)
    print('part 2, farthest distance: {}'.format(r))
