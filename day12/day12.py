# Part 1: How many paths through this cave system are there that visit small caves at most once?

file = open('./input.txt').read().splitlines()
file = [x.split('-') for x in file]
reversered = list(map(lambda x: x[::-1], file))
file = file + reversered


def iterate(nodes, accumulator):

    if not(len(nodes)):
        return accumulator

    new_nodes = []
    for node in nodes:
        if node[-1] == 'end':
            continue

        next_nodes = [x for x in file if x[0] == node[-1]]
        for next_node in next_nodes:
            if next_node[1].islower() and next_node[1] in node:
                continue

            appendable = node + [next_node[1]]
            new_nodes.append(appendable)

    accumulator.extend(new_nodes)
    return iterate(new_nodes, accumulator)


initials = [x for x in file if x[0] == 'start']
results = list(filter(lambda x: x[-1] == 'end', iterate(initials, initials)))

print(len(results))

# Part 2: Single cave can only be visited once.
# Given these new rules, how many paths through this cave system are there?

file = open('./input.txt').read().splitlines()
file = [x.split('-') for x in file]
reversered = list(map(lambda x: x[::-1], file))
file = file + reversered
file = [x for x in file if x[1] != 'start']


def lowercase_is_repeated(node):
    lowers = [x for x in node if x != 'start' or x != 'end']
    lowers = [x for x in lowers if x.islower()]
    return len(lowers) != len(set(lowers))


def iterate(nodes, accumulator):

    if not(len(nodes)):
        return accumulator

    new_nodes = []
    for node in nodes:
        if node[-1] == 'end':
            continue

        next_nodes = [x for x in file if x[0] == node[-1]]
        for next_node in next_nodes:

            # chec if a lower case node is already twice
            if next_node[1].islower():
                if next_node[1] in node:
                    if lowercase_is_repeated(node):
                        continue

            appendable = node + [next_node[1]]
            new_nodes.append(appendable)

    accumulator.extend(new_nodes)
    return iterate(new_nodes, accumulator)


initials = [x for x in file if x[0] == 'start']
results = list(filter(lambda x: x[-1] == 'end', iterate(initials, initials)))

print(len(results))
