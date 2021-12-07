import sys
from typing import List

def calc_fuel(positions: List[int], pos: int) -> int:
    def move_fuel_cost(p1: int, p2: int) -> int:
        n = abs(p1 - p2)
        return int((n + 1) * n / 2)
    return sum(move_fuel_cost(p, pos) for p in positions)

positions = None
with open(sys.argv[1]) as input:
    positions = list(map(int, input.readline().split(",")))
max_pos = max(positions)
min_fuel_pos = 0
min_fuel = calc_fuel(positions, 0)
for pos in range(1, max_pos + 1):
    pos_fuel = calc_fuel(positions, pos)
    if pos_fuel < min_fuel:
        min_fuel_pos = pos
        min_fuel = pos_fuel
print(min_fuel_pos, min_fuel)
