import sys
from typing import List

def adjacent_vals(x: int, y: int, m: List[List[int]]) -> List[int]:
    loc = []
    if x > 0:  # left
        loc.append(m[y][x - 1])
    if y > 0:  # top
        loc.append(m[y - 1][x])
    if x < len(m[0]) - 1:  # right
        loc.append(m[y][x + 1])
    if y < len(m) - 1:  # bottom
        loc.append(m[y + 1][x])
    return loc

heightmap = []
with open(sys.argv[1]) as input:
    for line in input:
        row = list(map(int, list(line.strip())))
        heightmap.append(row)

risk_level = 0
for y, row in enumerate(heightmap):
    for x, height in enumerate(row):
        if height < min(adjacent_vals(x, y, heightmap)):
            risk_level += height + 1
print(risk_level)
