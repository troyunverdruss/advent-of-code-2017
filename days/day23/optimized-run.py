aoc17() if 'aoc17' in dir() else None
import math

b_init = 106700
c = 123700
# hits
h = 0


def prime(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


for b in range(b_init, c + 1, 17):
    if not prime(b):
        h += 1

print('{}'.format(h))
