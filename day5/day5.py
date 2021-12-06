# Part1 Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
# !!! super ineficient

file = open('./input.txt').read().splitlines()


def parse(element): return element.split(' -> ')


file = list(map(parse, file))


def spliter(val):
    x1, y1 = val[0].split(',')
    x2, y2 = val[1].split(',')
    return [[int(x1), int(y1)], [int(x2), int(y2)]]


def filter_x_y(val):
    return val[0][0] == val[1][0] or val[0][1] == val[1][1]


inputs = list(filter(filter_x_y, map(spliter, file)))

crossed_cordinates = dict()

for inp in inputs:
    for c in range(inp[0][0]+1, inp[1][0]):
        inp.append([c, inp[0][1]])
    for c in range(inp[1][0]+1, inp[0][0]):
        inp.append([c, inp[0][1]])
    for c in range(inp[0][1]+1, inp[1][1]):
        inp.append([inp[0][0], c])
    for c in range(inp[1][1]+1, inp[0][1]):
        inp.append([inp[0][0], c])

    for (x, y) in inp:
        if (x, y) not in crossed_cordinates:
            crossed_cordinates[(x, y)] = 0
        crossed_cordinates[(x, y)] += 1

count = 0
for coordinate_count in crossed_cordinates.values():
    if coordinate_count > 1:
        count += 1

print(count)
