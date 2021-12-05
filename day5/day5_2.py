import sys
from collections import namedtuple
from typing import List, Tuple

Point = namedtuple("Point", "x, y", defaults=[0, 0])
Line = namedtuple("Line", "p1, p2")


def read_line_data(file_name: str) -> List[Line]:
    lines = []
    with open(file_name) as input:
        for line_str in input:
            from_str, to_str = line_str.split(" -> ")
            from_pt = Point._make(map(int, from_str.split(",")))
            to_pt = Point._make(map(int, to_str.split(",")))
            lines.append(Line(from_pt, to_pt))
    return lines


def box_size(lines: List[Line]) -> Tuple[int, int]:
    w = h = 0
    for line in lines:
        w = max(w, line.p1.x, line.p2.x)
        h = max(h, line.p1.y, line.p2.y)
    return w + 1, h + 1


def make_box(width, height) -> List[List[int]]:
    box = []
    for _n in range(0, height):
        box.append([0] * width)
    return box


def print_box(box: List[List[int]]) -> None:
    for row in box:
        print("".join(str(n) if n != 0 else "." for n in row))


def is_horizontal(line: Line) -> bool:
    return line.p1.y == line.p2.y


def is_vertical(line: Line) -> bool:
    return line.p1.x == line.p2.x


def mark_horizontal(box: List[List[int]], line: Line) -> None:
    start = min(line.p1.x, line.p2.x)
    stop = max(line.p1.x, line.p2.x) + 1
    for pos in range(start, stop):
        box[line.p1.y][pos] += 1


def mark_vertical(box: List[List[int]], line: Line) -> None:
    start = min(line.p1.y, line.p2.y)
    stop = max(line.p1.y, line.p2.y) + 1
    for pos in range(start, stop):
        box[pos][line.p1.x] += 1


def mark_diagonal(box: List[List[int]], line: Line) -> None:
    p1, p2 = (line.p1, line.p2) if line.p1.x < line.p2.x else (line.p2, line.p1)
    x, y = p1.x, p1.y
    while x <= p2.x:
        box[y][x] += 1
        x += 1
        y += 1 if p1.y < p2.y else -1


def mark_line(box: List[List[int]], line: Line) -> None:
    if is_horizontal(line):
        mark_horizontal(box, line)
    elif is_vertical(line):
        mark_vertical(box, line)
    else:
        mark_diagonal(box, line)


def overlaps(box: List[List[int]]) -> int:
    num_overlaps = 0
    for row in box:
        num_overlaps += sum(1 if n > 1 else 0 for n in row)
    return num_overlaps


lines = read_line_data(sys.argv[1])
box_width, box_height = box_size(lines)
box = make_box(box_width, box_height)
for line in lines:
    mark_line(box, line)
# print_box(box)
print(overlaps(box))
