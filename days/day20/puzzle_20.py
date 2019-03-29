aoc17() if 'aoc17' in dir() else None
import logging
from collections import Counter

from helpers import read_raw_entries, Point3d, manhattan_distance_3d

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)


class Particle:
    def __init__(self, loc, vel, acc, id):
        self.loc = loc
        self.vel = vel
        self.acc = acc
        self.id = id

    def __eq__(self, other):
        if type(other) != Particle:
            return False
        return self.loc == other.loc and self.vel == other.vel and self.acc == other.acc

    def __repr__(self):
        return repr('{} {} {} {}'.format(self.id, self.loc, self.vel, self.acc))

    def __hash__(self):
        return hash('{} {} {} {}'.format(self.id, self.loc, self.vel, self.acc))

    def step(self):
        self.vel.x = self.vel.x + self.acc.x
        self.vel.y = self.vel.y + self.acc.y
        self.vel.z = self.vel.z + self.acc.z

        self.loc.x = self.loc.x + self.vel.x
        self.loc.y = self.loc.y + self.vel.y
        self.loc.z = self.loc.z + self.vel.z


def parse_details(string):
    data = string.split('<', 1)[1]
    data = data.split('>', 1)[0]
    return list(map(int, data.split(',')))


def solve_20(entries):
    particles = parse_particles(entries)

    origin = Point3d(0, 0, 0)

    least_accel = manhattan_distance_3d(origin, min(particles, key=lambda p: manhattan_distance_3d(origin, p.acc)).acc)

    final_closest = None
    while final_closest is None:
        for p in particles:
            p.step()

        closest = min(particles, key=lambda p: manhattan_distance_3d(origin, p.loc))
        slowest = min(particles, key=lambda p: manhattan_distance_3d(origin, p.vel))

        # Bail out when the closest particle to the origin is
        # also the slowest and has an acceleration equal to the
        # slowest that was in the original set
        if closest == slowest and manhattan_distance_3d(origin, closest.acc) == least_accel:
            final_closest = closest

    return final_closest.id


def solve_20b(entries):
    particles = parse_particles(entries)
    origin = Point3d(0, 0, 0)

    go = True
    while go:
        counter = Counter(map(lambda p: p.loc, particles))

        to_remove = []
        for p in particles:
            if counter[p.loc] >= 2:
                log.debug('loc: {}, particle: {}'.format(p.loc, p))
                to_remove.append(p)

        for p in to_remove:
            particles.remove(p)

        for p in particles:
            p.step()

        log.debug(len(particles))
        # Bail out when you can sort the particles by distance from the origin
        # and each subsequent particle further from the origin has the same or
        # faster velocity and also has the same or faster acceleration
        _vel = 0
        _acc = 0
        done = True
        for p in sorted(particles, key=lambda _p: manhattan_distance_3d(origin, _p.loc)):
            p_vel = manhattan_distance_3d(origin, p.vel)
            if p_vel < _vel:
                done = False
                break
            _vel = p_vel

            p_acc = manhattan_distance_3d(origin, p.acc)
            if p_acc < _acc:
                done = False
                break
            _acc = p_acc

        if done:
            go = False

    return len(particles)


def parse_particles(entries):
    particles = []
    for i in range(0, len(entries)):
        vals = entries[i].split('>, ', 3)
        particles.append(
            Particle(Point3d(*parse_details(vals[0])),
                     Point3d(*parse_details(vals[1])),
                     Point3d(*parse_details(vals[2])),
                     i)
        )
    return particles


if __name__ == '__main__':
    entries = read_raw_entries('input_d20.txt')
    r = solve_20(entries)
    print('part 1, final closest id: {}'.format(r))

    r = solve_20b(entries)
    print('part 2, total final particle count: {}'.format(r))
