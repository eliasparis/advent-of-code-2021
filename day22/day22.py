from itertools import product, chain
# Part 1: Execute the reboot steps.
# Afterward, considering only cubes in the region x=-50..50,y=-50..50,z=-50..50, how many cubes are on?

file = open('./input.txt').read().splitlines()


def parse(range):
    a, b = range.split('=')[1].split('..')
    return (int(a), int(b))


lines = [(x, y.split(',')) for x, y in [line.split(' ') for line in file]]
lines = [(x, list(map(parse, y))) for x, y in lines]

cuboid = set()


def switch(step):
    i, ranges = step
    cubes = {*product(*map(lambda x: range(x[0], x[1] + 1), ranges))}
    if i == 'on':
        cuboid.update(cubes)
    else:
        cuboid.difference_update(cubes)


for step in lines:
    switch(step)

print(len(cuboid))

# Part 2: Starting again with all cubes off, execute all reboot steps.
# Afterward, considering all cubes, how many cubes are on?
# Not working :((((((((((((


def volume(x1, x2, y1, y2, z1, z2):
    return (x2-x1) * (y2-y1) * (z2-z1)


def intersect(cube0, cube1):
    x, y, z = cube0
    X, Y, Z = cube1

    a = x[0] if x[0] > X[0] else X[0]
    A = x[1] if x[1] < X[1] else X[1]
    b = y[0] if y[0] > Y[0] else Y[0]
    B = y[1] if y[1] < Y[1] else Y[1]
    c = z[0] if z[0] > Z[0] else Z[0]
    C = z[1] if z[1] < Z[1] else Z[1]

    if a <= A and b <= B and c <= C:
        return [(a, A), (b, B), (c, C)]
    else:
        return [(0, 0), (0, 0), (0, 0)]


def is_contained(cube0, cube1):
    x, y, z = cube0
    X, Y, Z = cube1
    if x[0] >= X[0] and x[1] <= X[1] and y[0] >= Y[0] and y[1] <= Y[1] and z[0] >= Z[0] and z[1] <= Z[1]:
        return True
    else:
        return False


def counter(cubes):
    maintotal = 0
    parsed = list()
    intersections = list()
    pintersections = list()
    reintersections = dict()

    for cube in cubes:
        if cube[0] == 'on':
            maintotal += volume(*chain(*cube[1]))
            for cparsed in parsed:
                cintersection = intersect(cparsed, cube[1])
                intersections.append(cintersection)
            parsed.append(cube[1])

    for i, intersection in enumerate(intersections):
        maintotal -= volume(*chain(*intersection))
        for ii, rintersection in enumerate(intersections):
            if i == ii:
                continue
            if is_contained(intersection, rintersection):
                continue
            reintersection = intersect(intersection, rintersection)
            reintersections[tuple(chain(*reintersection))
                            ] = volume(*chain(*reintersection))

    for reintersection in reintersections.values():
        maintotal += reintersection

    return maintotal
