import math
# Part1 : Determine the horizontal position that the crabs can align to using the least fuel possible.
# How much fuel must they spend to align to that position?

positions = open('./input.txt').read().split(',')

positions = list(map(int, positions))
positions.sort()
is_even = len(positions) % 2 == 0
mid = len(positions) // 2
median = 0

if is_even:
    median = (positions[mid - 1] + positions[mid])//2
else:
    median = positions[mid]

count = 0
for position in positions:
    count += abs(position - median)

print(count)

# Part2 : Each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1,
# the second step costs 2, the third step costs 3, and so on. Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route!
# How much fuel must they spend to align to that position?

positions = open('./input.txt').read().split(',')

positions = list(map(int, positions))
mean = math.floor(sum(positions) / len(positions))
count = 0

for position in positions:
    for v in range(1, abs(position - mean) + 1):
        count += v

print(count)
