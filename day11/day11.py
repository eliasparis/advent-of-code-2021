# Part 1: Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps.
# How many total flashes are there after 100 steps?

file = open('./input.txt').read().splitlines()
lines = [list(x) for x in file]
lines = [list(map(int, x)) for x in file]

flashes = 0


def iterate_octos(octos):
    if not(len(octos)):
        return 0

    flashess = 0
    flashed_octos = []

    for y, x in octos:
        adjacents = list(filter(
            lambda octo: octo[0] > -1 and octo[1] > -
            1 and octo[0] < len(lines) and octo[1] < len(lines[0]),
            [(y - i, x - j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]))

        for adjacent in adjacents:
            yy, xx = adjacent
            lines[yy][xx] += 1
            if lines[yy][xx] == 10:
                flashess += 1
                flashed_octos.append((yy, xx))

    flashess += iterate_octos(flashed_octos)
    return flashess


for _ in range(100):

    flashed_octos = []

    for y in range(len(lines)):

        for x in range(len(lines[y])):
            lines[y][x] += 1
            if lines[y][x] > 9:
                flashed_octos.append((y, x))

    flashes += iterate_octos(flashed_octos)
    flashes += len(flashed_octos)

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] > 9:
                lines[y][x] = 0


print(flashes)

# Part 2: If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern.
# What is the first step during which all octopuses flash?

file = open('./input.txt').read().splitlines()
lines = [list(x) for x in file]
lines = [list(map(int, x)) for x in file]

totallength = len(lines) * len(lines[0])
step = 0


def iterate_octos(octos):
    if not(len(octos)):
        return 0

    flashed_octos = []

    for y, x in octos:
        adjacents = list(filter(
            lambda octo: octo[0] > -1 and octo[1] > -
            1 and octo[0] < len(lines) and octo[1] < len(lines[0]),
            [(y - i, x - j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]))

        for adjacent in adjacents:
            yy, xx = adjacent
            lines[yy][xx] += 1
            if lines[yy][xx] == 10:
                flashed_octos.append((yy, xx))

    iterate_octos(flashed_octos)


while True:

    step += 1
    flashed_octos = []
    zeroscount = 0

    for y in range(len(lines)):

        for x in range(len(lines[y])):
            lines[y][x] += 1
            if lines[y][x] > 9:
                flashed_octos.append((y, x))

    iterate_octos(flashed_octos)

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] > 9:
                lines[y][x] = 0
            if lines[y][x] == 0:
                zeroscount += 1

                # All flashed

    if zeroscount == totallength:
        break


print(step)
