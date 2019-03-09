from helpers import read_raw_entries


def solve_05(entries):
    jumps = list(map(int, entries))
    max_index = len(jumps) - 1

    curr_index = 0
    step_count = 0
    while 0 <= curr_index <= max_index:
        step_count += 1

        last_index = curr_index
        curr_index += jumps[curr_index]
        jumps[last_index] += 1

    return step_count


def solve_05b(entries):
    jumps = list(map(int, entries))
    max_index = len(jumps) - 1

    curr_index = 0
    step_count = 0
    while 0 <= curr_index <= max_index:
        step_count += 1

        last_index = curr_index
        curr_index += jumps[curr_index]

        if jumps[last_index] >= 3:
            jumps[last_index] -= 1
        else:
            jumps[last_index] += 1

    return step_count


if __name__ == '__main__':
    entries = read_raw_entries('input_d5.txt')
    r = solve_05(entries)
    print('part 1, steps til escape: {}'.format(r))
    r = solve_05b(entries)
    print('part 2, steps til escape: {}'.format(r))
