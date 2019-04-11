aoc17() if 'aoc17' in dir() else None
from days.day23.puzzle_23 import Coprocessor

proc = Coprocessor([], 1)

proc.registers['b'] = 106700
proc.registers['c'] = 123700
# proc.registers['b'] = 1067
# proc.registers['c'] = 1084

while 1 != 0:
    proc.registers['f'] = 1
    proc.registers['d'] = 2
    proc.print_state('')

    while 'g' not in proc.registers or proc.registers['g'] != 0:
        proc.registers['e'] = 2
        proc.print_state('')
        while 'g' not in proc.registers or proc.registers['g'] != 0:
            proc.registers['g'] = proc.registers['d']
            proc.print_state('')

            proc.registers['g'] *= proc.registers['e']
            proc.print_state('')

            proc.registers['g'] -= proc.registers['b']
            proc.print_state('')

            if 'g' in proc.registers and proc.registers['g'] == 0:
                proc.registers['f'] = 0
                proc.print_state('')

            proc.registers['e'] -= -1
            proc.print_state('')

            proc.registers['g'] = proc.registers['e']
            proc.print_state('')

            proc.registers['g'] -= proc.registers['b']
            proc.print_state('')

        proc.registers['d'] -= -1
        proc.print_state('')

        proc.registers['g'] = proc.registers['c']
        proc.print_state('')

        proc.registers['g'] -= proc.registers['b']
        proc.print_state('')

    if 'f' in proc.registers and proc.registers['f'] == 0:
        proc.registers['h'] -= -1
        proc.print_state('')

    proc.registers['g'] = proc.registers['b']
    proc.print_state('')

    proc.registers['g'] -= proc.registers['c']
    proc.print_state('')

    if 'g' in proc.registers and proc.registers['g'] == 0:
        if 1 != 0:
            exit()
    proc.registers['b'] -= -17
    proc.print_state('')
