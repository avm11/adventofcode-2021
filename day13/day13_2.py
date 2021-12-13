import sys

def print_points(points, width, height):
    for y in range(height):
        row = ['#' if (x, y) in points else "." for x in range(width)]
        print("".join(row))

def fold_up(points, fold_row):
    fold_offset = fold_row * 2
    folded_points = set()
    for x, y in points:
        if y <= fold_row:
            folded_points.add((x, y))
        else:
            folded_points.add((x, fold_offset - y))
    return folded_points


def fold_left(points, fold_col):
    fold_offset = fold_col * 2
    folded_points = set()
    for x, y in points:
        if x <= fold_col:
            folded_points.add((x, y))
        else:
            folded_points.add((fold_offset - x, y))
    return folded_points

points = set()
folds = []

read_points = True
for line in sys.stdin:
    if not line.strip():
        read_points = False
    elif read_points:
        sx, sy = line.strip().split(",")
        points.add((int(sx), int(sy)))
    else:
        fold_params = line.strip().split(" ")[-1]
        fold_dir, fold_pos = fold_params.split("=")
        folds.append((fold_dir, int(fold_pos)))

folded_points = points
w = h = 0
for d, p in folds:
    if d == "x":
        folded_points = fold_left(folded_points, p)
        w = p
    elif d == "y":
        folded_points = fold_up(folded_points, p)
        h = p
    else:
        print("Invalid direction:", d)
        sys.exit(1)

print_points(folded_points, w, h)

