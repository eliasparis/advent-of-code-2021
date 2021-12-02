# Part1: How many measurements are larger than the previous measurement?
values = open("./input.txt").read().splitlines()
measurements = list(map(int, values))
count = 0
for i, measurement in enumerate(measurements[1:], start=1):
    if measurement > measurements[i - 1]:
        count = count + 1   
print(count)

# Part2: Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
three_count = 0
previous_measurement = sum(measurements[:3])
measurements_len = len(measurements)
total_measurements = measurements_len - (measurements_len % 3)
for i in range(total_measurements):
    current_measurement = sum(measurements[i:i+3])
    if(current_measurement > previous_measurement):
        three_count = three_count + 1
    previous_measurement = current_measurement
print(three_count)

