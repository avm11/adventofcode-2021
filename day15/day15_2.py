import sys

AJACENT_OFFSETS = [(0, -1), (-1, 0), (1, 0), (0, 1)]


def get_ajacent(x, y, w, h):
    ajacent = [(x + off_x, y + off_y) for off_x, off_y in AJACENT_OFFSETS]
    return [(xx, yy) for xx, yy in ajacent if xx >= 0 and xx < w and yy >= 0 and yy < h]

def norm(v):
    if v > 9:
        v -= 9
    return v

map_tile = []
for line in sys.stdin:
    line = line.strip()
    map_tile.append([int(lvl) for lvl in line])

TILES_NUM = 5

cavern_map = []
for r in range(TILES_NUM):
    for tile_row in map_tile:
        map_row = []
        for c in range(TILES_NUM):
            map_row.extend([norm(lvl + r + c) for lvl in tile_row])
        cavern_map.append(map_row)
cavern_size = len(cavern_map)

MAX_DIST = cavern_size * cavern_size * 9

dist_map = []
for _n in range(cavern_size):
    dist_map.append([MAX_DIST] * cavern_size)
dist_map[0][0] = 0

current_pos = (0, 0)
end_pos = (cavern_size - 1, cavern_size - 1)

unvisited = set()
for x in range(cavern_size):
    for y in range(cavern_size):
        unvisited.add((x, y))

front = set()
while current_pos != end_pos:
    cx, cy = current_pos
    current_dist = dist_map[cy][cx]
    for x, y in get_ajacent(cx, cy, cavern_size, cavern_size):
        if (x, y) not in unvisited:
            continue
        dist = current_dist + cavern_map[y][x]
        dist_map[y][x] = min(dist, dist_map[y][x])
        front.add((x, y))
    unvisited.remove(current_pos)

    current_pos = None
    min_dist = MAX_DIST
    for x, y in front:
        dist = dist_map[y][x]
        if dist < min_dist:
            current_pos = (x, y)
            min_dist = dist
    front.remove(current_pos)

print(dist_map[-1][-1])

