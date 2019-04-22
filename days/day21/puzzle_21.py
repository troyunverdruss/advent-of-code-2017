import itertools
import logging
# m = [[(i*3) + j for j in range(3)] for i in range(3)]
import math
from collections import deque, Counter, defaultdict
from copy import copy
from typing import Tuple, Dict

aoc17() if 'aoc17' in dir() else None
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

        self.output = output.replace('/', '')

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


def solve_21(entries):
    rules = process_entries_to_rules(entries)
    rules_lookup = make_rules_lookup(rules)

    image = run_magnifications('.#...####', 5, rules_lookup)

    # We're done disassembling and reassembling ...
    # time to count up # marks
    return Counter(list(to_str(image.values())))['#']


def solve_21b(entries):
    rules = process_entries_to_rules(entries)
    rules_lookup = make_rules_lookup(rules)
    magnification_lookup = defaultdict(lambda: [])

    for key in [''.join(i) for i in itertools.product(['.', '#'], repeat=9)]:
        image = run_magnifications(key, 3, rules_lookup)
        carved_up = carve_into_segments(image)
        for segment in carved_up:
            magnification_lookup[key].append(to_str(segment))

    queue = deque(['.#...####'])
    for a in range(6):  # Note, using 6 because each lookup group is "3" iterations, so 3*6=18

        for b in range(len(queue)):
            key = queue.popleft()
            for r in magnification_lookup[key]:
                queue.append(r)
        log.debug('{}: {}'.format((a + 1) * 3, Counter(list(to_str(queue)))['#']))

    return Counter(list(to_str(queue)))['#']


def run_magnifications(init_square, iterations, rules_lookup):
    image = create_image_grid(init_square)

    for it in range(iterations):
        log.debug('Starting iteration: {}'.format(it))

        results = deque()
        for segment in carve_into_segments(image):
            processed_segment = process_segment(rules_lookup, segment)
            # print('{} => {}'.format(segment, processed_segment))

            results.append(processed_segment)

        image = reassemble_into_full_image(results)

        # Printing out the grids for debugging
        # image_size = int(math.sqrt(len(image)))
        # for y in range(image_size):
        #     row = ''
        #     for x in range(image_size):
        #         row += image[(x, y)]
        #     print(row)
        log.debug('{}: {}'.format((it + 1), Counter(list(image.values()))['#']))
        # print('{}: {}'.format((it + 1), Counter(list(image.values()))['#']))
        # print()

    return image


def create_image_grid(init_square):
    image = {
        (0, 0): init_square[0], (1, 0): init_square[1], (2, 0): init_square[2],
        (0, 1): init_square[3], (1, 1): init_square[4], (2, 1): init_square[5],
        (0, 2): init_square[6], (1, 2): init_square[7], (2, 2): init_square[8],
    }
    return image


def reassemble_into_full_image(results):
    wrap_size = int(math.sqrt(len(results)))
    segment_size = int(math.sqrt(len(results[0])))

    image = {}
    result_pos = 0
    for y in range(0, wrap_size * segment_size, segment_size):
        for x in range(0, wrap_size * segment_size, segment_size):
            segment = results[result_pos]
            segment_pos = 0
            for coord in sorted(itertools.product(range(segment_size), repeat=2), key=lambda t: (t[1], t[0])):
                # print((coord[0] + x, coord[1] + y))
                image[(coord[0] + x, coord[1] + y)] = segment[segment_pos]
                segment_pos += 1
            result_pos += 1

    return image


def carve_into_segments(image: Dict[Tuple, str]):
    results = deque()
    image_size = int(math.sqrt(len(image)))

    if image_size % 2 == 0:
        for y in range(0, image_size, 2):
            for x in range(0, image_size, 2):
                m = [
                    image[(x, y)], image[(x + 1, y)],
                    image[(x, y + 1)], image[(x + 1, y + 1)]
                ]
                results.append(''.join(m))
    else:
        for y in range(0, image_size, 3):
            for x in range(0, image_size, 3):
                m = [
                    image[(x, y)], image[(x + 1, y)], image[(x + 2, y)],
                    image[(x, y + 1)], image[(x + 1, y + 1)], image[(x + 2, y + 1)],
                    image[(x, y + 2)], image[(x + 1, y + 2)], image[(x + 2, y + 2)],
                ]
                results.append(''.join(m))
    return results


def process_entries_to_rules(entries):
    rules = []
    for e in entries:
        rules.append(Rule(e))
    return rules


if __name__ == '__main__':
    entries = read_raw_entries('input_d21.txt')
    r = solve_21(entries)
    print('part 1, number of #: {}'.format(r))

    r = solve_21b(entries)
    print('part 2, number of #: {}'.format(r))
