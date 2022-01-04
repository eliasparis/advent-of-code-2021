# Part 1: What is the first step on which no sea cucumbers move?

file = open('./input.txt').read().splitlines()
step, moved, leny, lenx = 0, True, len(file), len(file[0])
grid = {(x, y): file[y][x] for x in range(lenx) for y in range(leny)}

while moved:
    moved = False
    # move east
    for x, y in [(x, y) for x, y in grid if grid[x, y] == '>' and grid[(x + 1) % lenx, y] == '.']:
        grid[(x + 1) % lenx, y] = '>'
        grid[x, y] = '.'
        moved = True

    # move south
    for x, y in [(x, y) for x, y in grid if grid[x, y] == 'v' and grid[x, (y + 1) % leny] == '.']:
        grid[x, (y + 1) % leny] = 'v'
        grid[x, y] = '.'
        moved = True

    step += 1

print(step)
