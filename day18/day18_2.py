import sys

EXPLODE_LVL = 5
SPLIT_VALUE = 10


def num_to_expr(num):
    if type(num) is int:
        return [num]
    fst, snd = num
    return ["["] + num_to_expr(fst) + num_to_expr(snd) + ["]"]


def expr_to_num(expr):
    stack = []
    for el in expr:
        if el == "[":
            pass
        elif el == "]":
            b = stack.pop()
            a = stack.pop()
            stack.append([a, b])
        else:
            stack.append(el)
    return stack.pop()


def explode(expr):
    def find_redux(expr):
        lvl = 0
        for pos, el in enumerate(expr):
            if el == "[":
                lvl += 1
                if lvl == EXPLODE_LVL:
                    return pos
            elif el == "]":
                lvl -= 1
        return None

    def add_left(expr, v):
        new_expr = []
        updated = False
        for el in reversed(expr):
            if type(el) is int and not updated:
                new_expr.append(el + v)
                updated = True
            else:
                new_expr.append(el)
        return list(reversed(new_expr))

    def add_right(expr, v):
        new_expr = []
        updated = False
        for el in expr:
            if type(el) is int and not updated:
                new_expr.append(el + v)
                updated = True
            else:
                new_expr.append(el)
        return new_expr

    pos = find_redux(expr)
    if pos:
        a, b = expr[pos + 1], expr[pos + 2]
        left, right = expr[:pos], expr[pos + 4 :]
        return add_left(left, a) + [0] + add_right(right, b)
    else:
        return None


def split(expr):
    def find_split(expr):
        for pos, el in enumerate(expr):
            if type(el) is int and el >= SPLIT_VALUE:
                return pos
        return None

    pos = find_split(expr)
    if pos:
        val = expr[pos]
        left, right = expr[:pos], expr[pos + 1 :]
        return left + ["[", val // 2, val // 2 + val % 2, "]"] + right
    else:
        return None


def reduce(expr):
    reduced = False
    reduced_expr = expr
    while not reduced:
        explode_expr = explode(reduced_expr)
        if explode_expr:
            reduced_expr = explode_expr
            continue
        split_expr = split(reduced_expr)
        if split_expr:
            reduced_expr = split_expr
            continue
        reduced = True
    return reduced_expr


def add(expr1, expr2):
    return reduce(["["] + expr1 + expr2 + ["]"])


def magnitude(expr):
    stack = []
    for el in expr:
        if el == "[":
            pass
        elif el == "]":
            b = stack.pop()
            a = stack.pop()
            stack.append(3 * a + 2 * b)
        else:
            stack.append(el)
    return stack.pop()


expressions = []
for line in sys.stdin:
    expressions.append(num_to_expr(eval(line.strip())))

max_magnitude = 0
for i in range(len(expressions) - 1):
    for j in range(i + 1, len(expressions)):
        sum1 = add(expressions[i], expressions[j])
        sum2 = add(expressions[j], expressions[i])
        max_magnitude = max(max_magnitude, magnitude(sum1), magnitude(sum2))

print(max_magnitude)
