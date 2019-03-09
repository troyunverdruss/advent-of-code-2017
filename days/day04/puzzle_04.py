from typing import List

from helpers import read_raw_entries


def sort_chars_in_passphrases(_passphrases: List[str]):
    sorted_passphrases = []

    for p in _passphrases:
        sorted_passphrases.append(''.join(sorted(list(p))))

    return sorted_passphrases


def solve_04(entries):
    valid = 0

    for e in entries:
        passphrases = e.split()

        if len(passphrases) == len(set(passphrases)):
            valid += 1

    return valid


def solve_04b(entries):
    valid = 0

    for e in entries:
        passphrases = e.split()

        if len(passphrases) == len(set(passphrases)):
            sorted_passphrases = sort_chars_in_passphrases(passphrases)
            if len(sorted_passphrases) == len(set(sorted_passphrases)):
                valid += 1

    return valid


if __name__ == '__main__':
    entries = read_raw_entries('input_d4.txt')
    r = solve_04(entries)
    print('part 1, valid passphrases: {}'.format(r))
    r = solve_04b(entries)
    print('part 2, valid passphrases: {}'.format(r))
