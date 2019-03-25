aoc17() if 'aoc17' in dir() else None

import logging
from collections import defaultdict
from typing import Dict, Optional, Callable

from helpers import read_raw_entries

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Soundcard:
    def __init__(self):
        self.last_played: Optional[int] = None
        self.go = True
        self.instruction_pos = 0
        self.registers: Dict[str, int] = defaultdict(lambda: 0)
        self.operations: Dict[str, Callable] = {
            'snd': self.snd,
            'set': self.set,
            'add': self.add,
            'mul': self.mul,
            'mod': self.mod,
            'rcv': self.rcv,
            'jgz': self.jgz,
        }

    def process_instructions(self, instructions):
        self.go = True
        self.instruction_pos = 0
        while self.go and 0 <= self.instruction_pos < len(instructions):
            self.process_instruction(instructions[self.instruction_pos])
            self.instruction_pos += 1

        return self.last_played

    def process_instruction(self, instruction):
        values = instruction.split()
        log.debug('Registers: {}'.format(self.registers.items()))
        log.debug('Processing instruction: {}'.format(values))
        self.operations[values[0]](*values[1:])

    def read_value(self, register_or_value: str) -> int:
        log.debug('Looking up value for {}'.format(register_or_value))
        try:
            ret_val = int(register_or_value)
        except ValueError:
            ret_val = self.registers[register_or_value]
        log.debug(ret_val)
        return ret_val

    def snd(self, x):
        self.last_played = self.read_value(x)

    def set(self, x, y):
        self.registers[x] = self.read_value(y)

    def add(self, x, y):
        self.registers[x] += self.read_value(y)

    def mul(self, x, y):
        self.registers[x] *= self.read_value(y)

    def mod(self, x, y):
        self.registers[x] %= self.read_value(y)

    def rcv(self, x):
        _x = self.read_value(x)
        if _x != 0:
            self.go = False
            return _x
        else:
            log.debug('Skipping rcv. {} == 0'.format(_x))

    def jgz(self, x, y):
        _x = self.read_value(x)
        if _x > 0:
            self.instruction_pos += self.read_value(y)
            self.instruction_pos -= 1
        else:
            log.debug('Skipping jgz. {} <= 0'.format(_x))


def solve_18(entries):
    soundcard = Soundcard()
    return soundcard.process_instructions(entries)


if __name__ == '__main__':
    entries = read_raw_entries('input_d18.txt')
    r = solve_18(entries)
    print('part 1, last freq: {}'.format(r))
