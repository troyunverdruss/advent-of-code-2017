from collections import defaultdict

from helpers import read_raw_entries


class Instruction:
    def __init__(self, instruction_str):
        parts = instruction_str.split()
        self.target_register = parts[0]
        self.operation = parts[1]
        self.mod_value = int(parts[2])
        self.test_register = parts[4]
        self.condition = parts[5]
        self.condition_value = int(parts[6])

    def __repr__(self):
        return repr('{} {} {} if {} {} {}'.format(
            self.target_register,
            self.operation,
            self.mod_value,
            self.test_register,
            self.condition,
            self.condition_value,
        ))


# a dec -511 if x >= -4
# pq inc -45 if cfa == 7
# vby dec 69 if tl < 1
# yg dec 844 if v > -6
# tl inc -756 if u != 9
# l inc -267 if f == 0

def test(a, t, b):
    if t == '<':
        return a < b
    if t == '<=':
        return a <= b
    if t == '==':
        return a == b
    if t == '>':
        return a > b
    if t == '>=':
        return a >= b
    if t == '!=':
        return a != b


def solve_08(entries, return_highest_ever=False):
    registers = defaultdict(lambda: 0)

    instructions = list(map(lambda s: Instruction(s), entries))
    highest_ever = 0
    for i in instructions:
        if test(registers[i.test_register], i.condition, i.condition_value):
            if i.operation == 'inc':
                registers[i.target_register] += i.mod_value
            else:
                registers[i.target_register] -= i.mod_value
            if return_highest_ever:
                highest_ever = max(max(registers.values()), highest_ever)

    if return_highest_ever:
        return highest_ever

    return max(registers.values())


if __name__ == '__main__':
    entries = read_raw_entries('input_d8.txt')
    r = solve_08(entries)
    print('part 1, highest value register: {}'.format(r))
    r = solve_08(entries, True)
    print('part 2, highest value register ever: {}'.format(r))
