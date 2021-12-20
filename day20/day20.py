import sys
from functools import reduce


def extend_img(in_img, size):
    img = []
    img_w = len(in_img) + 2 * size
    empty_row = "." * img_w
    for _ in range(size):
        img.append(empty_row)
    row_ext = "." * size
    for row in in_img:
        img.append(row_ext + row + row_ext)
    for _ in range(size):
        img.append(empty_row)
    return img


def get_alg_num(x, y, img):
    alg_str = (
        img[y - 1][x - 1 : x + 2] + img[y][x - 1 : x + 2] + img[y + 1][x - 1 : x + 2]
    )
    binary_str = [0 if c == "." else 1 for c in alg_str]
    return reduce(lambda v, d: v * 2 + d, binary_str)


def step(img, enh_alg):
    img_w = len(img[0])
    empty_row = "." * img_w
    new_img = []
    new_img.append(empty_row)
    for y in range(1, len(img) - 1):
        row = "."
        for x in range(1, img_w - 1):
            num = get_alg_num(x, y, img)
            row += enh_alg[num]
        row += "."
        new_img.append(row)
    new_img.append(empty_row)
    return new_img


enh_alg = sys.stdin.readline().strip()
sys.stdin.readline()

input_img = []
for line in sys.stdin:
    input_img.append(line.strip())
input_img_h = len(input_img)
input_img_w = len(input_img[0])

steps = 50
ext = steps * 2 + 1
img = extend_img(input_img, steps + ext)
for _ in range(steps):
    img = step(img, enh_alg)

total_light_pixels = 0
for row in img[ext: -ext]:
    total_light_pixels += sum(1 if c == "#" else 0 for c in row[ext: -ext])

print(total_light_pixels)
