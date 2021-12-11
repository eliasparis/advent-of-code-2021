# Part 1: Find the first illegal character in each corrupted line of the navigation subsystem.
# What is the total syntax error score for those errors?

file = open('./input.txt').read().splitlines()

result = 0
heads = '([{<'
tails = ')]}>'
point_map = [3, 57, 1197, 25137]
legal_closing = []
ilegals = []

for line in file:
    for character in line:
        position = heads.find(character)
        if position > -1:
            legal_closing.insert(0, tails[position])
        else:
            if character == legal_closing[0]:
                del legal_closing[0]
            else:
                ilegals.append(character)
                break

mapped = map(lambda x: point_map[tails.find(x)], ilegals)

for numb in mapped:
    result += numb

print(result)

# Part 2: Find the first illegal character in each corrupted line of the navigation subsystem.
# What is the total syntax error score for those errors?

file = open('./input.txt').read().splitlines()

heads = '([{<'
tails = ')]}>'
point_map = [1, 2, 3, 4]
accum = []

for line in file:
    legal_closing = []
    for character in line:
        position = heads.find(character)
        if position > -1:
            legal_closing.insert(0, tails[position])
        else:
            if character == legal_closing[0]:
                del legal_closing[0]
            else:
                legal_closing = []
                break

    accum.append(legal_closing)


def get_result(x):
    r = 0
    for char in x:
        r = r * 5
        r += point_map[tails.find(char)]
    return r


mapacum = map(get_result, accum)
filteredacum = filter(lambda x: x != 0, mapacum)
sortedaccum = list(filteredacum)
sortedaccum.sort()

print(sortedaccum[(len(sortedaccum) - 1) // 2])
