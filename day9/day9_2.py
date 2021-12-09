import sys
from functools import reduce
from pprint import pp
from typing import List, Tuple

def adjacent_locs(x: int, y: int, m: List[List[int]]) -> List[Tuple[int, int]]:
    loc = []
    if x > 0:  # left
        loc.append((x - 1, y))
    if y > 0:  # top
        loc.append((x, y - 1))
    if x < len(m[0]) - 1:  # right
        loc.append((x + 1, y))
    if y < len(m) - 1:  # bottom
        loc.append((x, y + 1))
    return loc

def adjacent_vals(x: int, y: int, m: List[List[int]]) -> List[int]:
    locs = adjacent_locs(x, y, m)
    return [m[yy][xx] for xx, yy in locs]

def find_basin(low_x: int, low_y: int, m: List[List[int]]) -> List[Tuple[int, int]]:
    basin = []
    visited_points = set()
    points_to_visit = [(low_x, low_y)]
    while len(points_to_visit) > 0:
        x, y = points_to_visit.pop(0)
        if (x, y) in visited_points:
            continue
        visited_points.add((x, y))
        if m[y][x] != 9:
            basin.append((x, y))
            points_to_visit.extend(adjacent_locs(x, y, m))

    return basin

heightmap = []
with open(sys.argv[1]) as input:
    for line in input:
        row = list(map(int, list(line.strip())))
        heightmap.append(row)

low_points = []
for y, row in enumerate(heightmap):
    for x, height in enumerate(row):
        if height < min(adjacent_vals(x, y, heightmap)):
            low_points.append((x, y))

basins = []
for x, y in low_points:
    basins.append(find_basin(x, y, heightmap))
basins_len = [len(b) for b in basins]
basins_len.sort()
pp(reduce(lambda a, b: a * b, basins_len[-3:], 1))
