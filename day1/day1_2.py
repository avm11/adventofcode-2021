import sys

inc_count = 0
window = []
with open(sys.argv[1]) as input:
    for line in input:
        val = int(line)

        if len(window) < 3:
            window.append(val)
            continue

        first = window.pop(0)
        window.append(val)
        if val > first:
            inc_count += 1
print(inc_count)
