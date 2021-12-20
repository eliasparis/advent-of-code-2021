# Part 1: What is the lowest total risk of any path from the top left to the bottom right?
# https://www.analyticssteps.com/blogs/dijkstras-algorithm-shortest-path-algorithm
# https://stackabuse.com/dijkstras-algorithm-in-python/
# Only part one :(

from queue import PriorityQueue
import sys

lines = open('./input.txt').read().splitlines()
lines = [list(map(int, list(x))) for x in lines]

lnth = len(lines)
lnthrow = len(lines[0])
adjacents = [(1, 0), (0, 1)]

cost = {(i, j): sys.maxsize for i in range(lnth)
        for j in range(lnthrow)}
cost[(0, 0)] = 0
visited = {(i, j): False for i in range(lnth)
           for j in range(lnthrow)}
queue = [(0, 0)]

while(len(queue)):
    nodey, nodex = queue[0]

    if visited[(nodey, nodex)]:
        del queue[0]
        continue

    current_cost = cost[(nodey, nodex)]

    for y, x in adjacents:
        nodetup = (nodey + y, nodex + x)

        if nodetup[0] > lnth - 1 or nodetup[1] > lnthrow - 1:
            continue

        new_cost = current_cost + lines[nodetup[0]][nodetup[1]]
        adjacent_cost = cost[nodetup]
        cost[nodetup] = min(adjacent_cost, new_cost)
        queue.append(nodetup)

    visited[(nodey, nodex)] = True
    del queue[0]

print(cost[(lnth - 1, lnthrow - 1)])
