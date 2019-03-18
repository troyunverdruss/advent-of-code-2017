from helpers import read_raw_entries


class SimpleLayer:
    def __init__(self, depth, _range):
        self.depth = depth
        self.range = _range
        self.severity = depth * _range
        self.positions = _range * 2 - 2

    def compute_collision(self, delay):
        loc_at_time = (self.depth + delay) % self.positions
        if loc_at_time == 0:
            return True, self.severity
        return False, 0


def solve_13(entries, delay=0, end_on_catch=False):
    layers = {}

    for entry in entries:
        vals = list(map(int, entry.split(':')))
        layers[vals[0]] = SimpleLayer(vals[0], vals[1])

    total_severity = 0
    for layer in layers.values():
        collision, severity = layer.compute_collision(delay)
        if end_on_catch and collision:
            return -1
        total_severity += severity

    return total_severity


def solve_13b(entries):
    delay = 0
    computed_severity = solve_13(entries, delay, True)

    while computed_severity != 0:
        delay += 1
        computed_severity = solve_13(entries, delay, True)

    return delay


if __name__ == '__main__':
    entries = read_raw_entries('input_13.txt')
    r = solve_13(entries)
    print('part 1, total severity: {}'.format(r))

    delay = solve_13b(entries)
    print('part 2, required delay: {}'.format(delay))
