import sys
from typing import Tuple

CHUNK_CHARS = {"(": ")", "[": "]", "{": "}", "<": ">"}

ERROR_POINTS = { ")": 3, "]": 57, "}": 1197, ">": 25137 }


def is_open_symbol(c: str) -> bool:
    return c in CHUNK_CHARS


def is_corrupted(line: str) -> Tuple[bool, str]:
    open_sym_stack = []
    for chr in line:
        if is_open_symbol(chr):
            open_sym_stack.append(chr)
        else:
            if open_sym_stack:
                open_char = open_sym_stack.pop()
                if CHUNK_CHARS[open_char] != chr:
                    return True, chr
            else:
                return True, chr
    return False, ""


total_error = 0
for line in sys.stdin:
    line = line.strip()
    corrupted, invalid_char = is_corrupted(line)
    if corrupted:
        total_error += ERROR_POINTS[invalid_char]
print(total_error)
