import sys


def next(polymer, rules):
    new_polymer = polymer[0]
    for c in polymer[1:]:
        ins_char = rules[new_polymer[-1] + c]
        new_polymer += ins_char + c
    return new_polymer


template = None
rules = dict()
for line in sys.stdin:
    line = line.strip()
    if not template:
        template = line
    elif line:
        symb_pair, insert_symb = line.split(" -> ")
        rules[symb_pair] = insert_symb

p = template
for step in range(10):
    p = next(p, rules)

freq = {}
for c in p:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

min_freq = min(n for _c, n in freq.items())
max_freq = max(n for _c, n in freq.items())

print(freq)
print(len(p))
print(max_freq - min_freq)
