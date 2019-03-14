from collections import deque

from helpers import read_raw_entries


def solve_09(input_str, return_garbage_count=False):
    capture = deque(list(input_str))
    stack = deque()

    total = 0
    current_value = 0
    garbage_count = 0

    while len(capture) > 0:
        char = capture.popleft()

        if char == '{':
            stack.append(char)
            current_value += 1
        elif char == '}':
            stack.pop()
            total += current_value
            current_value -= 1
        elif char == '<':
            next_char = capture.popleft()
            while next_char != '>':
                if next_char == '!':
                    capture.popleft()
                else:
                    garbage_count += 1
                next_char = capture.popleft()

    if return_garbage_count:
        return garbage_count

    return total


if __name__ == '__main__':
    input_str = read_raw_entries('input_d9.txt')[0].strip()
    r = solve_09(input_str)
    print('part 1, total value: {}'.format(r))
    r = solve_09(input_str, True)
    print('part 2, garbage removed: {}'.format(r))
