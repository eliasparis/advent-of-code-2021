# Part 1: What is the highest y position it reaches on this trajectory?

file = open('./input.txt').read().splitlines()
x, y = [list(map(int, x.split(','))) for x in file]
xmin, xmax = x
ymin, ymax = y


# Because initial yspeed is the same on positive when reached y0
# print(sum(range(abs(int(ymin)))))

# Part 2: How many distinct initial velocity values cause the probe to be within the target area after any step?
in_target_shoots = set()

xvmin = 0
for i in range(xmin + 1):
    sumatory = sum(range(i + 1))
    if not(sumatory > xmin):
        xvmin = i
xvmax = xmax

yvmin = ymin
yvmax = -ymin - 1


for xvelocity in range(xvmin, xvmax + 1):
    for yvelocity in range(yvmin, yvmax + 1):

        newx = xvelocity
        newy = yvelocity
        newxvelocity = xvelocity
        newyvelocity = yvelocity

        while newx <= xmax and newy >= ymin:

            in_target_x = newx >= xmin and newx <= xmax
            in_target_y = newy >= ymin and newy <= ymax
            in_target = in_target_x and in_target_y

            if in_target:
                in_target_shoots.add((xvelocity, yvelocity))

            newxvelocity = 0 if newxvelocity == 0 else newxvelocity - 1
            newx += newxvelocity

            newyvelocity = newyvelocity - 1
            newy += newyvelocity


print(in_target_shoots)
print(len(in_target_shoots))
