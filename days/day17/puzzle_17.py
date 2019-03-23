from collections import deque


def solve_17(skip_size, max_value, target_value):
    spinlock = deque([0])

    for i in range(1, max_value + 1):
        spinlock.rotate(-skip_size)
        spinlock.rotate(-1)
        spinlock.appendleft(i)

    return spinlock[spinlock.index(target_value) + 1]


if __name__ == '__main__':
    puzzle_input = 301
    r = solve_17(301, 2017, 2017)
    print('part 1, target value: {}'.format(r))

    r = solve_17(puzzle_input, 50_000_000, 0)
    print('part 2, target value: {}'.format(r))
