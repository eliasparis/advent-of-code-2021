# Part 1: First fold.
# How many dots are visible after completing just the first fold instruction on your transparent paper?
# Part 2: Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.
# What code do you use to activate the infrared thermal imaging camera system?

lines = open('./input.txt').read().splitlines()
separationi = lines.index('')
points = [(int(x.split(',')[0]), int(x.split(',')[1]))
          for x in lines[:separationi]]

instructions = [(list(x.split('=')[0])[-1], int(x.split('=')[1]))
                for x in lines[separationi + 1:]]


def cut(points, axis):
    edge = 0 if axis[0] == 'x' else 1
    delimiter = axis[1]
    sidea = []
    sideb = []
    for point in points:
        if point[edge] > delimiter:
            sideb.append(point)
        elif point[edge] < delimiter:
            sidea.append(point)
    return (sidea, sideb)


def reverse(side, axis):
    edge = 0 if axis[0] == 'x' else 1
    noedge = 1 if axis[0] == 'x' else 0
    reversered = []
    for point in side:
        np = list(range(2))
        np[edge] = (2*axis[1]) - point[edge]
        np[noedge] = point[noedge]
        reversered.append((np[0], np[1]))
    return reversered


def merge(sidea, sideb):
    both = sidea + sideb
    return list(set(both))


for instruction in instructions:
    sides = cut(points, instruction)
    reversedside = reverse(sides[1], instruction)
    merged = merge(sides[0], reversedside)
    points = merged

# create display grid
xlength = max([p[0] for p in points]) + 1
ylength = max([p[1] for p in points]) + 1
l = [[' '] * xlength for _ in range(ylength)]

for point in points:
    x, y = point
    l[y][x] = '#'

print('                                                        ')
print('                                                        ')
for line in l:
    print(''.join(line))
print('                                                        ')
print('                                                        ')
