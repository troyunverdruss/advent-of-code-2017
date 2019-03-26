aoc17() if 'aoc17' in dir() else None

import logging
from collections import defaultdict, deque
from typing import Dict, Optional, Callable

from helpers import read_raw_entries

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class SoundcardPair:
    def __init__(self, instructions):
        self.card_0 = Soundcard2(instructions, 0)
        self.card_1 = Soundcard2(instructions, 1)

        # Set up our 2-way comms
        self.card_0.rcv_q = self.card_1.snd_q
        self.card_1.rcv_q = self.card_0.snd_q

    def run(self):
        go = True

        while go:
            if self.card_0.go:
                self.card_0.step()
            else:
                go = False

            if self.card_1.go:
                self.card_1.step()
            else:
                go = False

            if self.card_0.rcv_wait and self.card_1.rcv_wait:
                log.debug('Reached deadlock')
                go = False


class Soundcard:
    def __init__(self, instructions, id=0):
        self.instructions = instructions
        self.last_played: Optional[int] = None
        self.go = True
        self.rcv_wait = False
        self.instruction_pos = 0
        self.snd_q = deque([])
        self.snd_count = 0
        self.rcv_q = None
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

        self.registers['p'] = id

    def process_instructions(self):
        self.go = True
        self.instruction_pos = 0
        while self.go and 0 <= self.instruction_pos < len(self.instructions):
            self.process_instruction(self.instructions[self.instruction_pos])
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


class Soundcard2(Soundcard):

    # def process_instructions(self):
    #     self.go = True
    #     self.instruction_pos = 0
    #     while self.go and 0 <= self.instruction_pos < len(self.instructions):
    #         self.process_instruction(self.instructions[self.instruction_pos])
    #         self.instruction_pos += 1
    #
    #     return self.last_played
    #
    # def process_instruction(self, instruction):
    #     values = instruction.split()
    #     log.debug('Registers: {}'.format(self.registers.items()))
    #     log.debug('Processing instruction: {}'.format(values))
    #     self.operations[values[0]](*values[1:])

    def step(self):
        if self.go is False:
            return

        # Make sure whatever instruction we're dealing with is in our range, otherwise mark as done
        if 0 <= self.instruction_pos < len(self.instructions):
            self.process_instruction(self.instructions[self.instruction_pos])
        else:
            self.go = False

        # Only advance the instruction if we're not paused waiting to receive
        if self.rcv_wait is False:
            self.instruction_pos += 1

    def snd(self, x):
        _x = self.read_value(x)
        self.last_played = _x
        self.snd_q.append(_x)
        self.snd_count += 1

    def rcv(self, x):
        self.rcv_wait = True
        if len(self.rcv_q) > 0:
            self.registers[x] = self.rcv_q.popleft()
            self.rcv_wait = False


def solve_18(entries):
    soundcard = Soundcard(entries)
    return soundcard.process_instructions()


def solve_18b(entries):
    soundcard_pair = SoundcardPair(entries)
    soundcard_pair.run()
    return soundcard_pair.card_1.snd_count


if __name__ == '__main__':
    entries = read_raw_entries('input_d18.txt')
    r = solve_18(entries)
    print('part 1, last freq: {}'.format(r))

    r = solve_18b(entries)
    print('part 2, card 1 send count: {}'.format(r))
