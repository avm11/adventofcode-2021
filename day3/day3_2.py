import sys
from typing import List

def oxygen_criteria(ones, zeroes):
    return 1 if (ones >= zeroes) else 0

def co2_criteria(ones, zeroes):
    return 0 if (zeroes <= ones) else 1

def bits_to_int(bits):
    val = 0
    for bit in bits:
        val = (val * 2) + bit
    return val

def calc_ones(diags: List[List[int]], bit_pos: int) -> int:
    return sum(d[bit_pos] for d in diags)

def calc_rating(diags: List[List[int]], criteria):
    raited_diags = diags.copy()
    diag_len = len(diags[0])
    bit_pos = 0
    while bit_pos < diag_len and len(raited_diags) > 1:
        ones = calc_ones(raited_diags, bit_pos)
        zeroes = len(raited_diags) - ones
        filter_bit = criteria(ones, zeroes)
        raited_diags = list(filter(lambda diag: diag[bit_pos] == filter_bit, raited_diags))
        bit_pos += 1
    return bits_to_int(raited_diags[0])

diags = []
with open(sys.argv[1]) as input:
    for diag_data in input:
        diag_bits = [int(bit) for bit in diag_data.strip()]
        diags.append(diag_bits)

oxygen_rating = calc_rating(diags, oxygen_criteria)
co2_rating = calc_rating(diags, co2_criteria)

life_rating = oxygen_rating * co2_rating
print(oxygen_rating, co2_rating, life_rating)
