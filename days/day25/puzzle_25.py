from collections import defaultdict
import re
import pysnooper

aoc17() if 'aoc17' in dir() else None
from helpers import read_raw_entries


class StateResult:
    def __init__(self, to_write, direction, next_state):
        self.to_write = to_write
        self.direction = direction
        self.next_state = next_state
        
    def __str__(self):
        return '{}, {}, {}'.format(self.to_write, self.direction, self.next_state)

    def __repr__(self):
        return repr(str(self))


class State:
    def __init__(self):
        self.results = {
            0: None,
            1: None
        }
    def __str__(self):
        return '{}'.format(self.results)
        
    def __repr__(self):
        return repr(str(self))


class StateMachine:
    def __init__(self, state):
        self.state = state
        self.tape = defaultdict(lambda: 0)
        self.cursor = 0
        self.states = {}

    #@pysnooper.snoop()
    def step(self):
        state = self.states[self.state]
        result = state.results[self.tape[self.cursor]]
        
        self.tape[self.cursor] = result.to_write
        
        if result.direction == 'right':
            self.cursor += 1
        else:
            self.cursor -= 1
        self.state = result.next_state

    def checksum(self):
        return sum(self.tape.values())

#@pysnooper.snoop()
def parse_input(entries):
    start_state = re.match(r'Begin in state (.*)\.', entries[0]).group(1)
    steps = re.match(r'Perform a diagnostic checksum after (.*) steps\.', entries[1]).group(1)
    steps = int(steps)
    
    _entries = list(entries[2:]+[''])
    state_machine = StateMachine(start_state)
    
    while len(_entries) > 0:
        e = _entries.pop(0)
        while e == '' and len(_entries) > 0:
            e = _entries.pop(0)
        
        if len(_entries) == 0:
            break
        
        state_id = re.match(r'In state (.*)\:', e).group(1)

        cur_val_0 = re.match(r'.*If the current value is (.*):', _entries.pop(0)).group(1)
        wr_0_val = re.match(r'.*Write the value (.*)\.', _entries.pop(0)).group(1)
        dir_0 = re.match(r'.*Move one slot to the (.*)\.', _entries.pop(0)).group(1)
        cont_0 = re.match(r'.*Continue with state (.*)\.', _entries.pop(0)).group(1)

        cur_val_1 = re.match(r'If the current value is (.*):', _entries.pop(0)).group(1)
        wr_1_val = re.match(r'.*Write the value (.*)\.', _entries.pop(0)).group(1)
        dir_1 = re.match(r'.*Move one slot to the (.*)\.', _entries.pop(0)).group(1)
        cont_1 = re.match(r'.*Continue with state (.*)\.', _entries.pop(0)).group(1)            
        
        state_0 = StateResult(int(wr_0_val), dir_0, cont_0)
        state_1 = StateResult(int(wr_1_val), dir_1, cont_1)
        state = State()
        state.results[0] = state_0
        state.results[1] = state_1
        state_machine.states[state_id] = state
        
    return steps, state_machine     

# Begin in state A.
# Perform a diagnostic checksum after 6 steps.
#
# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state B.


def solve_25(entries):
    steps, state_machine = parse_input(entries)

    for _ in range(steps):
        state_machine.step()

    return state_machine.checksum()


if __name__ == '__main__':
    entries = read_raw_entries('input_d25.txt')
    r = solve_25(entries)
    print('part 1, checksum: {}'.format(r))
