import logging
import string
from collections import defaultdict, deque

from helpers import read_raw_entries, Point

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Packet:
    dirs = {
        'left': Point(-1, 0),
        'right': Point(1, 0),
        'up': Point(0, -1),
        'down': Point(0, 1)
    }
    chars = set(string.ascii_uppercase)

    def __init__(self, start, network_map):
        self.direction = Packet.dirs['down']
        self.position = start
        self.seen = deque()
        self.network_map = network_map
        self.steps = 1

    def step(self) -> bool:
        # These are my intersection cases
        if self.network_map[self.position.tup()] == '+' and self.network_map[
            (self.position + self.direction).tup()] == ' ':
            # Gotta turn
            # We're going UP
            if self.direction == Packet.dirs['up'] and self.network_map[
                (self.position + Packet.dirs['left']).tup()] in Packet.chars.union('-'):
                self.direction = Packet.dirs['left']
            elif self.direction == Packet.dirs['up'] and self.network_map[
                (self.position + Packet.dirs['right']).tup()] in Packet.chars.union('-'):
                self.direction = Packet.dirs['right']

            # We're going DOWN
            elif self.direction == Packet.dirs['down'] and self.network_map[
                (self.position + Packet.dirs['right']).tup()] in Packet.chars.union('-'):
                self.direction = Packet.dirs['right']
            elif self.direction == Packet.dirs['down'] and self.network_map[
                (self.position + Packet.dirs['left']).tup()] in Packet.chars.union('-'):
                self.direction = Packet.dirs['left']

            # We're going LEFT
            elif self.direction == Packet.dirs['left'] and self.network_map[
                (self.position + Packet.dirs['down']).tup()] in Packet.chars.union('|'):
                self.direction = Packet.dirs['down']
            elif self.direction == Packet.dirs['left'] and self.network_map[
                (self.position + Packet.dirs['up']).tup()] in Packet.chars.union('|'):
                self.direction = Packet.dirs['up']

            # We're going RIGHT
            elif self.direction == Packet.dirs['right'] and self.network_map[
                (self.position + Packet.dirs['up']).tup()] in Packet.chars.union('|'):
                self.direction = Packet.dirs['up']
            elif self.direction == Packet.dirs['right'] and self.network_map[
                (self.position + Packet.dirs['down']).tup()] in Packet.chars.union('|'):
                self.direction = Packet.dirs['down']
            else:
                return False

        elif self.network_map[(self.position + self.direction).tup()] == ' ':
            return False

        # We've either bailed out or changed our direction if we need to
        self.position += self.direction
        self.steps += 1
        log.debug('position: {}, value: {}'.format(self.position, self.network_map[self.position.tup()]))

        if self.network_map[self.position.tup()] in Packet.chars:
            self.seen.append(self.network_map[self.position.tup()])

        return True


def solve_19(entries):
    packet = inspect_and_walk_path(entries)
    return ''.join(packet.seen)


def solve_19b(entries):
    packet = inspect_and_walk_path(entries)
    return packet.steps


def inspect_and_walk_path(entries):
    network_map = build_network_map(entries)
    start = find_start_pos(network_map)
    packet = Packet(start, network_map)
    while packet.step():
        pass
    return packet


def find_start_pos(network_map):
    # Find starting position
    start = None
    x = 0
    while start is None:
        if network_map[(x, 0)] == '|':
            start = Point(x, 0)
        x += 1

    return start


def build_network_map(entries):
    _network_map = defaultdict(lambda: ' ')
    x, y = 0, 0
    for row in entries:
        for col in list(row):
            if col == '\n':
                col = ' '

            _network_map[(x, y)] = col
            x += 1
        y += 1
        x = 0

    return _network_map


if __name__ == '__main__':
    entries = read_raw_entries('input_d19.txt', strip=False)
    r = solve_19(entries)
    print('part 1, order of letters: {}'.format(r))

    r = solve_19b(entries)
    print('part 2, total steps: {}'.format(r))
