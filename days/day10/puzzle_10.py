import itertools
from collections import deque

from helpers import read_raw_entries


def solve_10(string, lengths):
    skip_size = 0
    rotate_count = 0

    rotate_count, skip_size = round(lengths, rotate_count, skip_size, string)

    # Reverse rotate to put our index in the correct position
    string.rotate(rotate_count % len(string))
    return string[0] * string[1]


def compute_dense_hash(string):
    dense_hash = []
    for g in range(0, 256, 16):
        value = None
        for v in itertools.islice(string, g, g + 16):
            if value is None:
                value = v
            else:
                value ^= v
        dense_hash.append(value)
    return dense_hash


def solve_10b(string, input_string):
    compute_sparse_hash(string, input_string)
    dense_hash = compute_dense_hash(string)
    hex_string = ''
    for v in dense_hash:
        hex_string += hex(v)[2:].zfill(2)

    return hex_string


def compute_sparse_hash(string, input_string):
    lengths = compute_lengths(input_string)
    skip_size = 0
    rotate_count = 0
    for i in range(0, 64):
        rotate_count, skip_size = round(lengths, rotate_count, skip_size, string)
    # Reverse rotate to put our index in the correct position
    string.rotate(rotate_count % len(string))


def compute_lengths(input_string):
    lengths = []
    for c in list(input_string):
        lengths.append(ord(c))

    return lengths + [17, 31, 73, 47, 23]


def round(lengths, rotate_count, skip_size, string):
    for l in lengths:

        if l > 1:
            group = list(itertools.islice(string, 0, l))
            group.reverse()

            i = 0
            for v in group:
                string[i] = v
                i += 1

        string.rotate(-(l + skip_size))
        rotate_count += l + skip_size

        skip_size += 1

    return rotate_count, skip_size


def knot_hash(input_str):
    return solve_10b(deque(range(0, 256)), input_str)


if __name__ == '__main__':
    entries = map(int, read_raw_entries('input_d10.txt')[0].split(','))
    r = solve_10(deque(range(0, 256)), entries)
    print('part 1 checksum: {}'.format(r))
    r = solve_10b(deque(range(0, 256)), read_raw_entries('input_d10.txt')[0])
    print('part 2 hash: {}'.format(r))
