from copy import deepcopy
# Part 1: How many pixels are lit in the resulting image?
# & Part 2: Start again with the original input image and apply the image enhancement algorithm 50 times.
# How many pixels are lit in the resulting image?

algo, _, *image = open('./input.txt').read().splitlines()

image = [list(x) for x in image]
steps = 50


def get_new_value(*l):
    string = ''.join(l[0]+l[1]+l[2])
    string = string.replace('.', '0')
    string = string.replace('#', '1')
    number = int(string, 2)
    value = algo[number]
    return value


def pad_image(img, val):
    pad = val*(len(img[0])+2)
    return [list(pad)] + [[val] + list(x) + [val] for x in img] + [list(pad)]


last_image = pad_image(image, '.')
last_count = 0

for step in range(steps):
    new_image = deepcopy(last_image)
    infiniti = pad_image(last_image, '.' if step % 2 == 0 else '#')
    count = 0

    for y in range(len(last_image)):
        for x in range(len(last_image[0])):

            value = get_new_value(
                infiniti[y][x:x+3], infiniti[y+1][x:x+3], infiniti[y+2][x:x+3])
            new_image[y][x] = value

            count += 1 if value == '#' else 0

    last_image = pad_image(new_image, '.' if step % 2 != 0 else '#')
    last_count = count

    # for line in new_image:
    #     print(''.join(line))

print(last_count)
