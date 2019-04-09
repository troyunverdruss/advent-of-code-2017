aoc17() if 'aoc17' in dir() else None

import logging
from collections import defaultdict
from typing import Dict, Callable

from helpers import read_raw_entries

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Coprocessor:
    def __init__(self, instructions, reg_a=0):
        self.instructions = instructions

        self.registers = defaultdict(lambda: 0)
        self.mul_count = 0
        self.inst_pos = 0
        self.go = True
        self.inst_count = 0
        self.last_h = 0

        self.operations: Dict[str, Callable] = {
            'set': self.set,
            'sub': self.sub,
            'mul': self.mul,
            'jnz': self.jnz,
        }

        self.registers['a'] = reg_a

    def process_instructions(self):
        self.go = True
        self.inst_pos = 0
        while self.go and 0 <= self.inst_pos < len(self.instructions):
            self.process_instruction(self.instructions[self.inst_pos])
            self.inst_pos += 1
            self.inst_count += 1

    def process_instruction(self, instruction):
        values = instruction.split()

        # if self.last_h != self.registers['h']:
        log.debug('{} Registers: {}'.format(self.inst_count, sorted(self.registers.items())))
        log.debug('Processing instruction: {}'.format(values))
        self.last_h = self.registers['h']

        self.operations[values[0]](*values[1:])

    def read_value(self, register_or_value: str) -> int:
        # log.debug('Looking up value for {}'.format(register_or_value))
        try:
            ret_val = int(register_or_value)
        except ValueError:
            ret_val = self.registers[register_or_value]
        # log.debug(ret_val)
        return ret_val

    def set(self, x, y):
        self.registers[x] = self.read_value(y)

    def sub(self, x, y):
        self.registers[x] -= self.read_value(y)

    def mul(self, x, y):
        self.mul_count += 1
        self.registers[x] = self.read_value(x) * self.read_value(y)

    def jnz(self, x, y):
        _x = self.read_value(x)

        if _x != 0:
            self.inst_pos += self.read_value(y)
            self.inst_pos -= 1


def solve_23(entries):
    proc = Coprocessor(entries)
    proc.process_instructions()
    return proc.mul_count


def solve_23b(entries):
    proc = Coprocessor(entries, 1)
    proc.process_instructions()
    return proc.mul_count


if __name__ == '__main__':
    entries = read_raw_entries('input_d23.txt')
    # r = solve_23(entries)
    # print('part 1, total mul count: {}'.format(r))

    r = solve_23b(entries)
    print('part 2, final value of h: {}'.format(r))
