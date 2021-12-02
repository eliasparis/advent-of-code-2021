# Part 1: What do you get if you multiply your final horizontal position by your final depth?
file = open('./input.txt').read().splitlines()


def transform(row):
    move, qty = row.split(' ')
    return [move, int(qty)]


directions = list(map(transform, file))

x = 0
y = 0

for row in directions:
    if (row[0] == 'forward'):
        x += row[1]
    if (row[0] == 'down'):
        y += row[1]
    if (row[0] == 'up'):
        y -= row[1]

print(f'X {x} Y {y} : {x * y}')

# Part 2: What do you get if you multiply your final horizontal position by your final depth?

x = 0
y = 0
aim = 0

for row in directions:
    if (row[0] == 'forward'):
        x += row[1]
        y += aim * row[1]
    if (row[0] == 'down'):
        aim += row[1]
    if (row[0] == 'up'):
        aim -= row[1]

print(f'X {x} Y {y} : {x * y}')
