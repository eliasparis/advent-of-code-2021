import math
# Part 1: Decode the structure of your hexadecimal-encoded BITS transmission;
# what do you get if you add up the version numbers in all packets?

file = open('./input.txt').read()
binary = ''.join([bin(int(x, 16))[2:].zfill(4) for x in file])

packetsvs = []


def parsepackets(i):
    packetsvs.append(int(binary[i:i+3], 2))
    i += 3
    paktype = int(binary[i: i+3], 2)
    i += 3

    if paktype == 4:
        while True:
            i += 5
            if binary[i - 5] == '0':
                break
    else:
        lengthtypeid = binary[i]
        i += 1
        if lengthtypeid == '0':
            # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            packetend = i + 15 + int(binary[i:i + 15], 2)
            i += 15
            while i < packetend:
                i = parsepackets(i)

        else:
            # If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            subpacketsnumb = int(binary[i:i+11], 2)
            i += 11
            for subpacket in range(subpacketsnumb):
                i = parsepackets(i)

    return i


parsepackets(0)
print(sum(packetsvs))

# Part 2: What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?

file = open('./input.txt').read()
binary = ''.join([bin(int(x, 16))[2:].zfill(4) for x in file])

operations = [
    sum,
    math.prod,
    min,
    max,
    lambda x: x[0],
    lambda x: 1 if x[0] > x[1] else 0,
    lambda x: 1 if x[0] < x[1] else 0,
    lambda x: 1 if x[0] == x[1] else 0,
]


def parsepackets(i):
    i += 3
    paktype = int(binary[i: i+3], 2)
    i += 3

    if paktype == 4:
        value = [0]
        while True:
            i += 5
            value[0] = 16*value[0] + int(binary[i-4:i], 2)
            if binary[i - 5] == '0':
                break
    else:
        lengthtypeid = binary[i]
        i += 1
        value = []

        if lengthtypeid == '0':
            # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            packetend = i + 15 + int(binary[i:i + 15], 2)
            i += 15
            while i < packetend:
                i, val = parsepackets(i)
                value.append(val)

        else:
            # If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            subpacketsnumb = int(binary[i:i+11], 2)
            i += 11
            for subpacket in range(subpacketsnumb):
                i, val = parsepackets(i)
                value.append(val)

    return (i, operations[paktype](value))


print(parsepackets(0)[1])
