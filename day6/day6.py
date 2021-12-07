# Part 1 Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?

fishes = open('./input.txt').read().split(',')
fishes = list(map(int, fishes))
day = 1

while day <= 80:
    new_fishes = []
    old_fishes = []

    for fish in fishes:
        if fish == 0:
            new_fishes.append(8)

    for fish in fishes:
        old_fishes.append(fish - 1 if fish > 0 else 6)

    fishes = [*old_fishes, *new_fishes]
    day += 1

print(len(fishes))

# Part 2 How many lanternfish would there be after 256 days?
# !!! Same as above but improving performance

fishes = open('./input.txt').read().split(',')
fishes = list(map(int, fishes))
fish_per_day = [fishes.count(x) for x in range(9)]

day = 1

while day <= 18:
    new_fishes_count = fish_per_day[0]
    fish_per_day = fish_per_day[1:] + [new_fishes_count]
    fish_per_day[6] += new_fishes_count

    day += 1

print(sum(fish_per_day))
