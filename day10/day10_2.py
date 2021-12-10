import sys
from typing import Tuple

CHUNK_CHARS = {"(": ")", "[": "]", "{": "}", "<": ">"}

ERROR_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def is_open_symbol(c: str) -> bool:
    return c in CHUNK_CHARS


def is_corrupted(line: str) -> bool:
    open_sym_stack = []
    for chr in line:
        if is_open_symbol(chr):
            open_sym_stack.append(chr)
        else:
            if open_sym_stack:
                open_char = open_sym_stack.pop()
                if CHUNK_CHARS[open_char] != chr:
                    return True
            else:
                return True
    return False


def line_completeon(line: str) -> str:
    open_sym_stack = []
    for chr in line:
        if is_open_symbol(chr):
            open_sym_stack.append(chr)
        else:
            open_sym_stack.pop()
    compl = [CHUNK_CHARS[c] for c in open_sym_stack]
    compl.reverse()
    return "".join(compl)

def score(compl: str) -> int:
    total_score = 0
    for c in compl:
        total_score *= 5
        total_score += ERROR_POINTS[c]
    return total_score


lines = (line.strip() for line in sys.stdin)
incomplete_lines = filter(lambda l: not is_corrupted(l), lines)
scores = [score(line_completeon(line)) for line in incomplete_lines]
scores.sort()
print(scores[len(scores) // 2])
