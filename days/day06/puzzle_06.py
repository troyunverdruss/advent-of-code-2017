from helpers import read_raw_entries


def solve_06(entries):
    values = list(map(int, entries[0].split()))

    banks = {}
    for i in range(0, len(values)):
        banks[i] = values[i]

    seen = {}
    current_config = None

    count = 0
    while current_config not in seen:
        seen[current_config] = True

        count += 1
        max_bank = max(banks.items(), key=lambda i: i[1])
        index = max_bank[0]
        banks[index] = 0

        for i in range(0, max_bank[1]):
            index = (index + 1) % len(values)
            banks[index] += 1

        current_config = tuple(banks[key] for key in sorted(banks.keys()))

    return count


def solve_06b(entries):
    values = list(map(int, entries[0].split()))

    banks = {}
    for i in range(0, len(values)):
        banks[i] = values[i]

    seen = {}
    current_config = None

    while current_config not in seen:
        seen[current_config] = True

        rebalance_banks(banks, values)

        current_config = tuple(banks[key] for key in sorted(banks.keys()))

    # we've hit our first repeat
    count = 0
    target_config = current_config
    current_config = None
    while current_config != target_config:
        count += 1
        rebalance_banks(banks, values)
        current_config = tuple(banks[key] for key in sorted(banks.keys()))

    return count


def rebalance_banks(banks, values):
    max_bank = max(banks.items(), key=lambda i: i[1])
    index = max_bank[0]
    banks[index] = 0
    for i in range(0, max_bank[1]):
        index = (index + 1) % len(values)
        banks[index] += 1


if __name__ == '__main__':
    entries = read_raw_entries('input_d6.txt')
    r = solve_06(entries)
    print('part 1, repeat hit after {} iters'.format(r))
    r = solve_06b(entries)
    print('part 2, after first repeat, cycle length is {}'.format(r))
