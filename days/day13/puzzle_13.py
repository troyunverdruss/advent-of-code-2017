import sys
from collections import deque

sys.path.append('/Users/troy/Documents/code/advent-of-code-2017')
from helpers import read_raw_entries


class SimpleLayer:
    def __init__(self, depth, _range):
        self.depth = depth
        self.range = _range
        self.severity = depth * _range


class Layer:
    def __init__(self, depth, _range):
        self.depth = depth
        self.range = _range

        valid_positions = list(range(0, _range)) + list(range(_range - 2, 0, -1))
        self.scanner_positions = deque(valid_positions)

    def tick(self):
        self.scanner_positions.rotate(1)

    def scanner_position(self):
        return self.scanner_positions[0]

    def severity(self):
        return self.depth * self.range


def solve_13(entries, delay=0, end_on_catch=False):
    layers = {}

    for entry in entries:
        vals = list(map(int, entry.split(':')))
        layers[vals[0]] = Layer(vals[0], vals[1])

    for _ in range(0, delay):
        for layer in layers.values():
            layer.tick()

    total_severity = 0
    my_depth = 0
    for depth in range(0, max(layers.keys()) + 1):
        if depth in layers and layers[my_depth].scanner_position() == 0:
            total_severity += layers[my_depth].severity()
            del layers[my_depth]

            # Bail out for part 2
            if end_on_catch:
                return -1

        for layer in layers.values():
            layer.tick()

        my_depth += 1

    return total_severity


def solve_13b(entries):
    delay = 0
    computed_severity = solve_13(entries, delay, True)

    while computed_severity != 0:
        delay += 1
        computed_severity = solve_13(entries, delay, True)
        # print('delay: {}, computed severity: {}'.format(delay, computed_severity))

    return delay


if __name__ == '__main__':
    entries = read_raw_entries('input_13.txt')
    r = solve_13(entries)
    print('part 1, total severity: {}'.format(r))

    delay = solve_13b(entries)
    print('part 2, required delay: {}'.format(delay))
