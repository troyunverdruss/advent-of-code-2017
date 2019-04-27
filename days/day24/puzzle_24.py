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
        self.strongest_sum = 0
        self.longest_length = 0
        self.longest_strength = 0


def list_sub(_list, _remove):
    l = list(_list)
    try:
        for r in _remove:
            l.remove(r)
        return l
    except:
        l.remove(_remove)
        return l


def add_components(must_match, parents, available_components, solution):
    options = list(filter(lambda c: must_match in c, available_components))

    if len(options) == 0:
        _sum = sum(itertools.chain.from_iterable(parents))
        _len = len(parents)
        if _sum > solution.strongest_sum:
            solution.strongest_sum = _sum

        if _len > solution.longest_length or (_len >= solution.longest_length and _sum > solution.longest_strength):
            solution.longest_strength = _sum
            solution.longest_length = _len

    else:
        for option in options:
            _next_match = list_sub(option, must_match)[0]
            _avail = list_sub(available_components, option)

            _parents = list(parents)
            _parents.append(option)
            add_components(_next_match, _parents, _avail, solution)


def solve_24(entries):
    components = []
    for e in entries:
        components.append(tuple(map(int, e.split('/'))))
    solution = Solution()
    add_components(0, [], components, solution)
    return solution.strongest_sum, solution.longest_strength


if __name__ == '__main__':
    entries = read_raw_entries('input_d24.txt')
    strongest, longest_strongest = solve_24(entries)
    print('part 1, strongest bridge: {}'.format(strongest))
    print('part 2, longest strongest {}'.format(longest_strongest))
