import sys

inc_count = 0
prev_value = None
with open(sys.argv[1]) as input:
    for line in input:
        if not line.strip():
            continue
        val = int(line)
        if not prev_value:
            prev_value = val
        if val > prev_value:
            inc_count += 1
        prev_value = val
print(inc_count)
