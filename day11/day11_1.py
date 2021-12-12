import sys

AJACENT_OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def get_ajacent(x, y, w, h):
    ajacent = [(x + off_x, y + off_y) for off_x, off_y in AJACENT_OFFSETS]
    return [(xx, yy) for xx, yy in ajacent if xx >= 0 and xx < w and yy >= 0 and yy < h]


def increase_levels(octopuses):
    new_octopuses = []
    for row in octopuses:
        new_octopuses.append([l + 1 for l in row])
    return new_octopuses


def get_all_flashed(octopuses):
    flashed = []
    for x in range(len(octopuses)):
        for y in range(len(octopuses[x])):
            if octopuses[y][x] > 9:
                flashed.append((x, y))
    return flashed


def update_ajacent(octopuses, ajacent):
    for x, y in ajacent:
        octopuses[y][x] += 1


def get_new_flashed(octopuses, ajacent, flashed):
    new_flashed = []
    for x, y in set(ajacent):
        if ((x, y) not in flashed) and octopuses[y][x] > 9:
            new_flashed.append((x, y))
    return new_flashed


def reset_flashed(octopuses):
    new_octopuses = []
    for row in octopuses:
        new_octopuses.append([0 if lvl > 9 else lvl for lvl in row])
    return new_octopuses


def step(octopuses):
    width = len(octopuses[0])
    height = len(octopuses)

    new_octopuses = increase_levels(octopuses)
    new_flashed = get_all_flashed(new_octopuses)
    flashed = set()
    while new_flashed:
        ajacent = []
        for flashed_oct in new_flashed:
            x, y = flashed_oct
            ajacent.extend(get_ajacent(x, y, width, height))
            flashed.add(flashed_oct)
        update_ajacent(new_octopuses, ajacent)
        new_flashed = get_new_flashed(new_octopuses, ajacent, flashed)

    return reset_flashed(new_octopuses)


def print_map(octopuses):
    for row in octopuses:
        print("".join(str(lvl) for lvl in row))
    print()


octopuses = []
for line in sys.stdin:
    octopuses.append([int(e) for e in line.strip()])
total_flashes = 0
for _n in range(100):
    octopuses = step(octopuses)
    for row in octopuses:
        total_flashes += sum(1 if lvl == 0 else 0 for lvl in row)

print_map(octopuses)
print()
print(total_flashes)
