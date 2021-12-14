# Part 1: Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

lines = open('./input.txt').read().splitlines()
template = lines[:1][0]
instructions = [x.split(' -> ') for x in lines[2:]]
instructionslist = [x[0] for x in instructions]

for _ in range(10):
    polymer_template = ''

    for i in range(len(template) - 1):
        pair = template[i:i+2]
        if pair in instructionslist:
            polymer = instructions[instructionslist.index(pair)][1]
            polymer_template += f'{template[i]}{polymer}'
        else:
            polymer_template += template[i]
    polymer_template += template[-1:]
    template = polymer_template

polymers = list(set(template))
values = list(map(lambda x: len([y for y in template if y == x]), polymers))
result = max(values) - min(values)
print(result)


# Part 2: Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
# !!! brute force doesnt work, optimize

lines = open('./input.txt').read().splitlines()
template = lines[:1][0]
instructions = [x.split(' -> ') for x in lines[2:]]
instructionslist = [x[0] for x in instructions]
accum = dict.fromkeys(instructionslist, 0)

for i in range(len(template) - 1):
    pair = template[i:i+2]
    accum[pair] += 1

for _ in range(40):
    new_accum = dict.fromkeys(instructionslist, 0)
    for key, value in accum.items():
        newpolymer = instructions[instructionslist.index(key)][1]
        new_accum[f'{key[0]}{newpolymer}'] += value
        new_accum[f'{newpolymer}{key[1]}'] += value

    accum = new_accum

polymers = list(set(''.join(new_accum.keys())))


def n(polymer):
    count = 0
    countn = 0
    for key, value in new_accum.items():
        if polymer == key[0]:
            count += value
        if polymer == key[1]:
            countn += value
    return max([count, countn])


counts = list(map(n, polymers))
result = max(counts) - min(counts)
print(result)
