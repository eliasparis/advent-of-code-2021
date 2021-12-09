# Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?

file = [x.split(' | ')[1] for x in open('./input.txt').read().splitlines()]
lengths = [7, 4, 3, 2]
count = 0

for line in file:
    count += len(list(filter(lambda x: len(x) in lengths, line.split(' '))))

print(count)

# Part 2: For each entry, determine all of the wire/segment connections and decode the four-digit output values.
# What do you get if you add up all of the output values?

file = [x.split(' | ') for x in open('./input.txt').read().splitlines()]


def check_chars(sample, test) -> bool:
    return all(map(lambda char: char in sample, list(test)))


def convert_output_to_int(numbers, output) -> int:
    output = map(lambda v: ''.join(sorted(v)), output.split(' '))
    number = map(lambda v: str(numbers.index(v)), output)
    number = ''.join(number)
    return int(number)


addoutput = 0

for line in file:
    sequence, output = line
    sequence = sequence.split(' ')

    # find numbers by segments
    one = next(v for v in sequence if len(v) == 2)
    four = next(v for v in sequence if len(v) == 4)
    seven = next(v for v in sequence if len(v) == 3)
    eight = next(v for v in sequence if len(v) == 7)
    three = next(v for v in sequence if len(v) == 5 and check_chars(v, one))
    nine = next(v for v in sequence if len(v) ==
                6 and check_chars(v, ''.join(set([three, four]))))
    zero = next(v for v in sequence if len(v) ==
                6 and v != nine and check_chars(v, one))
    six = next(v for v in sequence if len(v) == 6 and v != nine and v != zero)
    two = next(v for v in sequence if len(v) ==
               5 and check_chars(v, set(eight) - set(nine)))
    five = next(v for v in sequence if len(v) == 5 and v != two and v != three)

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    numbers = [''.join(sorted(v)) for v in numbers]
    addoutput += convert_output_to_int(numbers, output)

print(addoutput)
