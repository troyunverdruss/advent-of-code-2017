# For pypy
import itertools
import sys

sys.path.append('/Users/troy/Documents/code/advent-of-code-2017')

from helpers import read_raw_entries
from collections import deque


def parse_instruction(instruction):
    return instruction[1:].split('/')


def spin(sequence, instruction):
    sequence.rotate(int(instruction[1:]))


def exchange(sequence, instruction):
    idx_a, idx_b = list(map(int, parse_instruction(instruction)))

    # Nothing to do if they're the same
    if idx_a == idx_b:
        return

    lower_idx = min(idx_a, idx_b)
    upper_idx = max(idx_a, idx_b)

    sequence.rotate(-1 * lower_idx)
    swap_value_a = sequence.popleft()
    sequence.rotate(-1 * (upper_idx - lower_idx - 1))
    swap_value_b = sequence.popleft()
    sequence.appendleft(swap_value_a)
    sequence.rotate(upper_idx - lower_idx - 1)
    sequence.appendleft(swap_value_b)
    sequence.rotate(lower_idx)


def partner(sequence, instruction):
    char_a, char_b = parse_instruction(instruction)
    new_instruction = 'x{}/{}'.format(sequence.index(char_a), sequence.index(char_b))
    exchange(sequence, new_instruction)


def solve_16(sequence, instructions):
    # Set up map of instruction methods
    operations = {
        's': spin,
        'x': exchange,
        'p': partner
    }

    # Run instructions
    for instruction in instructions:
        operations[instruction[0]](sequence, instruction)

    return ''.join(sequence)


def solve_16b(sequence, instructions, rounds):
    # Seen will hold our string formation with the index when we last saw it
    # Seen_order will hold the last 500 elements in order so we can get a representative
    # slice based on the order in which things are happening (searching the dict would kinda suck)
    seen = {}
    seen_order = deque([], maxlen=500)

    for i in range(rounds):
        solve_16(sequence, instructions)
        sequence_str = ''.join(sequence)

        # If we hit a repeat here, then we're gonna compute the final value
        if sequence_str in seen:
            # How long between repeats?
            repeat_period = i - seen[sequence_str]
            print('{} seen in loop {}, just repeated in loop {}. [{}]'.format(sequence_str, i, seen[sequence_str],
                                                                              repeat_period))

            # Compute the offset in the group based on the requested number of rounds
            offset_in_period = (rounds - i) % repeat_period - 1

            # Compute and extract the element at the correct index
            return list(itertools.islice(
                seen_order,
                len(seen_order) - repeat_period,
                len(seen_order)))[offset_in_period]

        # No repeat yet, append the new data to our tracking lists
        seen_order.append(sequence_str)
        seen[sequence_str] = i

    # Never found a repeating pattern, return the computed value
    # (this will only happen for small values probably)
    return ''.join(sequence)


if __name__ == '__main__':
    # Set up list
    letters = [chr(i) for i in range(ord('a'), ord('p') + 1)]
    sequence = deque(letters)

    instructions = read_raw_entries('input_d16.txt')[0].split(',')
    r = solve_16(sequence, instructions)
    print('part 1, order: {}'.format(r))

    # Reset for part 2
    letters = [chr(i) for i in range(ord('a'), ord('p') + 1)]
    sequence = deque(letters)

    instructions = read_raw_entries('input_d16.txt')[0].split(',')
    r = solve_16b(sequence, instructions, 1_000_000_000)
    print('part 2, order: {}'.format(r))
