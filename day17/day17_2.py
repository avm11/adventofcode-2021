import sys
from collections import namedtuple

Pt = namedtuple("Pt", ["x", "y"])


def parse_target_area(target_str):
    _, coords_str = target_str.split(":")
    xarea, yarea = coords_str.split(",")
    x0, x1 = xarea.split("=")[1].split("..")
    y0, y1 = yarea.split("=")[1].split("..")
    return (Pt(int(x0), int(y1)), Pt(int(x1), int(y0)))


def in_target(target_area, pos):
    lt, rb = target_area
    return lt.x <= pos.x and lt.y >= pos.y and rb.x >= pos.x and rb.y <= pos.y


def miss_target(target_area, pos):
    _, rb = target_area
    return rb.x < pos.x or rb.y > pos.y


sign = lambda x: (1, -1)[x < 0]


def step(pos, vx, vy):
    new_pos = Pt(pos.x + vx, pos.y + vy)
    new_vx = 0 if vx == 0 else sign(vx) * (abs(vx) - 1)
    new_vy = vy - 1
    return (new_pos, new_vx, new_vy)


def is_hit_target(target_area, pos, vx, vy):
    while not in_target(target_area, pos) and not miss_target(target_area, pos):
        pos, vx, vy = step(pos, vx, vy)
    return in_target(target_area, pos)


target_str = sys.stdin.readline().strip()
target_area = parse_target_area(target_str)
num_hits = 0
lt, rb = target_area
for vy in range(rb.y, rb.x + 1):
    for vx in range(0, rb.x + 1):
        if is_hit_target(target_area, Pt(0, 0), vx, vy):
            num_hits += 1

print(num_hits)
