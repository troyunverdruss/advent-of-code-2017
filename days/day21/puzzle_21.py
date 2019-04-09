import itertools
import logging
# m = [[(i*3) + j for j in range(3)] for i in range(3)]
import math
from collections import deque, Counter
from copy import copy

from helpers import read_raw_entries

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Rule:
    def __init__(self, rule_str):
        self.matches = set()

        matrix = []
        input, output = rule_str.split(' => ')
        for row in input.split('/'):
            matrix.append(list(row))

        self.output = []
        for row in output.split('/'):
            self.output.append(list(row))

        matrixes = []
        matrixes.append(matrix)
        matrixes.append(rotate(matrix))
        matrixes.append(rotate(matrix, 2))
        matrixes.append(rotate(matrix, 3))

        matrixes.append(flip_over_x(matrix))
        matrixes.append(flip_over_x(rotate(matrix)))
        matrixes.append(flip_over_x(rotate(matrix, 2)))
        matrixes.append(flip_over_x(rotate(matrix, 3)))

        matrixes.append(flip_over_y(matrix))
        matrixes.append(flip_over_y(rotate(matrix)))
        matrixes.append(flip_over_y(rotate(matrix, 2)))
        matrixes.append(flip_over_y(rotate(matrix, 3)))

        for m in matrixes:
            self.matches.add(to_str(m))


def to_str(matrix):
    return ''.join(map(str, itertools.chain.from_iterable(matrix)))


def rotate(matrix, count=1):
    _matrix = copy(matrix)
    for _ in range(count):
        _matrix = list(zip(*_matrix[::-1]))
    return _matrix


def flip_over_x(matrix):
    return matrix[::-1]


def flip_over_y(matrix):
    return [row[::-1] for row in matrix]


def process_segment(rules_lookup, segment):
    return rules_lookup[to_str(segment)].output


def make_rules_lookup(rules):
    lookup = {}
    for r in rules:
        for m in r.matches:
            if m in lookup:
                log.error('Conflicting rule found for {}'.format(m))
            lookup[m] = r

    return lookup


def solve_21(entries, iterations=5):
    rules = process_entries_to_rules(entries)
    rules_lookup = make_rules_lookup(rules)

    image = deque([
        deque(['.', '#', '.']),
        deque(['.', '.', '#']),
        deque(['#', '#', '#']),
    ])

    for it in range(iterations):
        log.info('Starting iteration: {}'.format(it))

        results = deque()
        if len(image) % 2 == 0:
            for i in range(0, len(image), 2):
                for j in range(0, len(image), 2):
                    m = []
                    m.append(list(itertools.islice(image[j], i, i + 2)))
                    m.append(list(itertools.islice(image[j + 1], i, i + 2)))
                    results.append(process_segment(rules_lookup, m))
        else:
            for i in range(0, len(image), 3):
                for j in range(0, len(image), 3):
                    m = []
                    m.append(list(itertools.islice(image[j], i, i + 3)))
                    m.append(list(itertools.islice(image[j + 1], i, i + 3)))
                    m.append(list(itertools.islice(image[j + 2], i, i + 3)))
                    results.append(process_segment(rules_lookup, m))

        wrap = math.sqrt(len(results))
        row_cursor = 0
        image = deque()
        for i in range(len(results)):
            if i % wrap == 0 and i != 0:
                row_cursor += len(results[0])

            for r in range(len(results[i])):
                if r + row_cursor not in image:
                    image.append(deque())
                for e in results[i][r]:
                    image[r + row_cursor].append(e)

        for i in range(len(image) - 1, -1, -1):
            if len(image[i]) == 0:
                del image[i]

    # We're done disassembling and reassembling ...
    # time to count up # marks
    return Counter(list(to_str(image)))['#']


def process_entries_to_rules(entries):
    rules = []
    for e in entries:
        rules.append(Rule(e))
    return rules


if __name__ == '__main__':
    entries = read_raw_entries('input_d21.txt')
    r = solve_21(entries)
    print('part 1, number of #: {}'.format(r))

    r = solve_21(entries, 18)
    print('part 2, number of #: {}'.format(r))

    # too low: 2364534
    # too high: 2418435
