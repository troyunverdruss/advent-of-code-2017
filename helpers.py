from pathlib import Path


def path(caller_file, path):
    return Path(caller_file).parent.joinpath(path)


def read_raw_entries(input, strip=True):
    entries = []
    with open(input, 'r', encoding='utf8') as f:
        for line in f:
            if strip:
                entries.append(line.strip())
            else:
                entries.append(line)

    return entries


class Point:
    def __init__(self, x=None, y=None, id=''):
        self.id = id
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) != Point:
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return repr('{}({},{})'.format(self.id, self.x, self.y))

    def __hash__(self):
        return hash('{}({},{})'.format(self.id, self.x, self.y))

    def __str__(self):
        return '{}({},{})'.format(self.id, self.x, self.y)

    def tup(self):
        return self.x, self.y


class Point3d(Point):
    def __init__(self, x=None, y=None, z=None, id=''):
        super().__init__(x, y, id)
        self.z = int(z)

    def __add__(self, other):
        # Changing this will probably break some of the older puzzles, but
        # I think it's better this way ...
        return Point3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        if type(other) != Point3d:
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return repr('{}({},{},{})'.format(self.id, self.x, self.y, self.z))

    def __hash__(self):
        return hash('{}({},{},{})'.format(self.id, self.x, self.y, self.z))

    def __str__(self):
        return '{}({},{},{})'.format(self.id, self.x, self.y, self.z)


def manhattan_distance(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def manhattan_distance_3d(a: Point3d, b: Point3d) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)
