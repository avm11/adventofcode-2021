import sys


def is_big_node(node_name):
    return all(c >= "A" and c <= "Z" for c in node_name)


cave_map = {}
for line in sys.stdin:
    n1, n2 = line.strip().split("-")
    if n2 != "start":
        cave_map.setdefault(n1, []).append(n2)
    if n1 != "start":
        cave_map.setdefault(n2, []).append(n1)

current_paths = [["start"]]
paths = []
while current_paths:
    new_current_paths = []
    for current_path in current_paths:
        last_node = current_path[-1]
        for next_node in cave_map[last_node]:
            if next_node == "end":
                paths.append(current_path + [next_node])
            elif is_big_node(next_node):
                new_current_paths.append(current_path + [next_node])
            elif next_node not in current_path:
                new_current_paths.append(current_path + [next_node])
    current_paths = new_current_paths

print(len(paths))
