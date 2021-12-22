import ast
import math
import copy

# Part 1: Add up all of the snailfish numbers from the homework assignment in the order they appear.
# What is the magnitude of the final sum?
# !!!!! Didnt propperly understand the reduction process in the instructions, that lead to spaghetttiiiiiii and messy solution
# Solution is based on build 01000 kind of paths to access the list
# which easily helps you to find adjacents leafs of the tree

file = open('./input.txt').read().splitlines()
file = [ast.literal_eval(x) for x in file]


def value_from_path(lst, path, isget, operation=lambda x: x):
    if len(path) == 1:
        if isget:
            return lst[path[0]]
        lst[path[0]] = operation(lst[path[0]])
    else:
        return value_from_path(lst[path[0]], path[1:], isget, operation)


def parser(elements, level, path, store):
    if level == 4:
        store.append(path)
        return store
    for i in [0, 1]:
        if isinstance(elements[i], list):
            parser(elements[i], level + 1, path + f'{i}', store)

    return store


def path_to_regular(line, path, store):
    for i in [0, 1]:
        if isinstance(line[i], list):
            path_to_regular(line[i], path + f'{i}', store)
        else:
            store.append(path + f'{i}')
    return store


def explode(path, line):
    l = [int(x) for x in list(path)]
    value0, value1 = value_from_path(line, l, True)
    line = collision(line, path, value0, '0')
    line = collision(line, path, value1, '1')
    value_from_path(line, l, False, lambda x: 0)
    return line


def collision(line, path, value, i):
    pathtoregular = path_to_regular(line, '', [])
    pathtoregular.sort()
    index = pathtoregular.index(path + i)
    replacepath = None

    if int(i) == 0:
        if index != 0:
            replacepath = pathtoregular[index - 1]
    else:
        if index != len(pathtoregular) - 1:
            replacepath = pathtoregular[index + 1]

    if replacepath:
        pathable = [int(x) for x in list(replacepath)]
        value_from_path(line, pathable, False, lambda x: x + value)

    return line


def split(line, path):
    l = [int(x) for x in list(path)]

    def operation(x):
        return [math.floor(x/2), math.ceil(x/2)]

    val = value_from_path(line, l, True)

    if val > 9:
        value_from_path(line, l, False, operation)

    return [line, val > 9, val > 9 and len(path) == 4, val > 18]


def iterate(line):
    while True:
        pathtolevel4 = parser(line, 0, '', [])

        for path in pathtolevel4:
            line = explode(path, line)

        pathtoregular = path_to_regular(line, '', [])
        was_split = False
        for path in pathtoregular:
            line, has_split, deep_split, soft_split = split(line, path)
            if has_split:
                was_split = True
            if soft_split:
                break
            if deep_split:
                break

        if not(was_split):
            break

    return line


result = file[0]
for line in file[1:]:
    result = iterate([result, line])


def calculate_magnitude(line):
    def calc(x):
        if isinstance(x, list):
            return calculate_magnitude(x)
        return x

    a = calc(line[0]) * 3
    b = calc(line[1]) * 2
    return a + b


# print(calculate_magnitude(result))


# Part 2: What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
file = open('./input.txt').read().splitlines()
file = [ast.literal_eval(x) for x in file]

maxi = 0

for i, line in enumerate(file):
    for x in range(len(file)):
        if i == x:
            continue
        r = iterate(copy.deepcopy([line, file[x]]))
        c = calculate_magnitude(r)
        maxi = maxi if maxi > c else c

print(maxi)
