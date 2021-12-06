# Part2 Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

file = open('./input.txt').read().splitlines()


def parse(element): return element.split(' -> ')


file = list(map(parse, file))


def spliter(val):
    x1, y1 = val[0].split(',')
    x2, y2 = val[1].split(',')
    return [[int(x1), int(y1)], [int(x2), int(y2)]]


def is_rect(val):
    return val[0][0] == val[1][0] or val[0][1] == val[1][1]


inputs = list(map(spliter, file))

crossed_cordinates = dict()

for inp in inputs:

    if is_rect(inp):
        # Horizontal or vertical winds
        for c in range(inp[0][0]+1, inp[1][0]):
            inp.append([c, inp[0][1]])
        for c in range(inp[1][0]+1, inp[0][0]):
            inp.append([c, inp[0][1]])
        for c in range(inp[0][1]+1, inp[1][1]):
            inp.append([inp[0][0], c])
        for c in range(inp[1][1]+1, inp[0][1]):
            inp.append([inp[0][0], c])
    else:
        # 45º winds
        for step in range(abs(inp[0][0] - inp[1][0]) - 1):
            coord = list('h')*2

            if inp[0][0] < inp[1][0]:
                coord[0] = inp[0][0] + step + 1
            else:
                coord[0] = inp[0][0] - step - 1

            if inp[0][1] < inp[1][1]:
                coord[1] = inp[0][1] + step + 1
            else:
                coord[1] = inp[0][1] - step - 1

            inp.append(coord)

    for (x, y) in inp:
        if (x, y) not in crossed_cordinates:
            crossed_cordinates[(x, y)] = 0
        crossed_cordinates[(x, y)] += 1

count = 0
for coordinate_count in crossed_cordinates.values():
    if coordinate_count > 1:
        count += 1

print(count)
