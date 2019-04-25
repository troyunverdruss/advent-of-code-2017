aoc17() if 'aoc17' in dir() else None
import itertools

from helpers import read_raw_entries


class Component:
    def __init__(self, _representation: str):
        self.ports = list(sorted(_representation.split('/')))
        self.avail = self.ports

    def __repr__(self):
        return repr('{}/{}'.format(self.ports[0], self.ports[1]))

    def __str__(self):
        return str('{}/{}'.format(self.ports[0], self.ports[1]))

    def use_port(self, port):
        if port not in self.avail:
            raise Exception('Tried to use a port, but already used')

        self.avail.remove(port)

    def reset(self):
        self.avail = self.ports


class Solution:
    def __init__(self):
        self.solution = None
        self.sum = 0
        self.length = 0


def list_sub(_list, _remove):
    l = list(_list)
    try:
        for r in _remove:
            l.remove(r)
        return l
    except:
        l.remove(_remove)
        return l


def add_components(must_match, parents, available_components, bridges):
    options = list(filter(lambda c: must_match in c, available_components))

    if len(options) == 0:
        _sum = sum(itertools.chain.from_iterable(parents))
        # _len = len(parents)
        if _sum > bridges.sum:
            bridges.solutions = parents
            bridges.sum = _sum

    else:
        for option in options:
            _next_match = list_sub(option, must_match)[0]
            _avail = list_sub(available_components, option)

            _parents = list(parents)
            _parents.append(option)
            add_components(_next_match, _parents, _avail, bridges)


def solve_24(entries):
    components = []
    for e in entries:
        components.append(tuple(map(int, e.split('/'))))
    bridges = Solution()
    add_components(0, [], components, bridges)
    return bridges.sum


if __name__ == '__main__':
    entries = read_raw_entries('input_d24.txt')
    r = solve_24(entries)
    print('part 1, strongest bridge: {}'.format(r))
