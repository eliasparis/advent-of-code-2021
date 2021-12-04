# Part1 Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
# What is the power consumption of the submarine?
file = open('./input.txt').read().splitlines()

gama_rate = ''
epsilon_rate = ''
input_length = len(file[0])
file_length = len(file)
wheel = [0 for i in range(input_length)]

for line in file:
    for i, value in enumerate(line):
        wheel[i] += int(value)

for value in wheel:
    if value > file_length/2:
        gama_rate += '1'
        epsilon_rate += '0'
    else:
        gama_rate += '0'
        epsilon_rate += '1'


decimal_gama_rate = int(gama_rate, 2)
decimal_epsilon_rate = int(epsilon_rate, 2)

power_consumtion = decimal_gama_rate * decimal_epsilon_rate
print(power_consumtion)

# Part2 Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating,
# then multiply them together. What is the life support rating of the submarine?


def bit_criteria(is_most_common=True):

    oxygen_generator_rating = file

    for i in range(input_length):

        ogr_len = len(oxygen_generator_rating)

        if ogr_len == 1:
            break

        summ = 0
        for line in oxygen_generator_rating:
            summ += int(line[i])

        comparison = '1' if summ >= ogr_len/2 else '0'
        if is_most_common == False:
            comparison = '1' if comparison == '0' else '0'

        def filtering(value): return value[i] == (comparison)
        oxygen_generator_rating = list(
            filter(filtering, oxygen_generator_rating))

    return int(oxygen_generator_rating[0], 2)


oxygen_generator_rating = bit_criteria()
co2_scrubber_rating = bit_criteria(False)
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(f'life_support_rating: {life_support_rating}')
