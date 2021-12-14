import sys


def update_element(state, elem, count):
    state.setdefault(elem, 0)
    state[elem] += count


def update_state(state, rules):
    new_state = dict()
    for symb_pair, count in state.items():
        if symb_pair in rules:
            first_symb, second_symb = symb_pair
            insert_symb = rules[symb_pair]
            update_element(new_state, first_symb + insert_symb, count)
            update_element(new_state, insert_symb + second_symb, count)
        else:
            add_pair(new_state, symb_pair, count)
    return new_state


def calc_freqs(state):
    freqs = dict()
    for symb_pair, count in state.items():
        first_symb, second_symb = symb_pair
        update_element(freqs, first_symb, count)
        update_element(freqs, second_symb, count)
    return {c: n // 2 for c, n in freqs.items()}
    return freqs


template = None
rules = dict()
for line in sys.stdin:
    line = line.strip()
    if not template:
        template = line
    elif line:
        symb_pair, insert_symb = line.split(" -> ")
        rules[symb_pair] = insert_symb

state = {}
for a, b in zip(template, template[1:]):
    update_element(state, a + b, 1)

for step in range(40):
    state = update_state(state, rules)
freqs = calc_freqs(state)
freqs[template[0]] += 1
freqs[template[-1]] += 1

min_freq = min(n for _c, n in freqs.items())
max_freq = max(n for _c, n in freqs.items())

print(max_freq - min_freq)
