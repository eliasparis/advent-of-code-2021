# Part 1: Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

file = open('./input.txt').read().splitlines()

count = 0

for i, line in enumerate(file):
    for ii in range(len(line)):
        value = int(line[ii])
        top = value + 1 if i == 0 else file[i - 1][ii]
        bottom = value + 1 if i == len(file) - 1 else file[i + 1][ii]
        left = value + 1 if ii == 0 else line[ii - 1]
        right = value + 1 if ii == len(line) - 1 else line[ii + 1]
        values = list(map(lambda x: int(x) > value,
                      [top, bottom, left, right]))

        # if is lowpoint calculate risk and sum
        if all(values):
            count += (value + 1)

print(count)

# Part 2: Find the three largest basins and multiply their sizes together.
# What do you get if you multiply together the sizes of the three largest basins?
# !!! not proud of this one

file = open('./input.txt').read().splitlines()


def is_low_point(value, values):
    values = list(map(lambda x: int(x) > value, values))
    return all(values)


def interate_sorroundings(i, ii):
    sorroundings = []
    sorroundingsi = []
    line = file[i]
    if i != 0:
        sorroundings.append(file[i - 1][ii])
        sorroundingsi.append((i - 1, ii))
    if i != len(file) - 1:
        sorroundings.append(file[i + 1][ii])
        sorroundingsi.append((i + 1, ii))
    if ii != 0:
        sorroundings.append(line[ii - 1])
        sorroundingsi.append((i, ii - 1))
    if ii != len(line) - 1:
        sorroundings.append(line[ii + 1])
        sorroundingsi.append((i, ii + 1))
    return [sorroundings, sorroundingsi]


def filter9(s):
    values = []
    for tup in s:
        number = int(file[tup[0]][tup[1]])
        if number != 9:
            values.append(tup)
    return values


def get_basin_size(value, i, ii):

    sorroundings, sorroundingsi = interate_sorroundings(i, ii)
    next_sorroundings = filter9(sorroundingsi)
    basin = set()

    for tupli in next_sorroundings:
        sorrounding_value = int(file[tupli[0]][tupli[1]])
        if sorrounding_value > value:
            basin.add(tupli)
            basin.update(get_basin_size(sorrounding_value, tupli[0], tupli[1]))

    return basin


basins_sizes = []

for i, line in enumerate(file):
    for ii in range(len(line)):
        value = int(line[ii])
        sorroundings, sorroundingsi = interate_sorroundings(i, ii)
        if is_low_point(value, sorroundings):
            basins_sizes.append(len(get_basin_size(value, i, ii)) + 1)

basins_sizes.sort()
maxs = basins_sizes[-3:]
result = maxs[0] * maxs[1] * maxs[2]
print(result)
