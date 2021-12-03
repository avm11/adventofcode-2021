import sys

def max_bit(ones, zeroes):
    return 1 if (ones > zeroes) else 0

def bits_to_int(bits):
    val = 0
    for bit in bits:
        val = (val * 2) + bit
    return val

total_zeroes = None
total_ones = None

with open(sys.argv[1]) as input:
    for diag_data in input:
        diag_bits = [int(bit) for bit in diag_data.strip()]
        if not total_zeroes:
            total_zeroes = [0] * len(diag_bits)
            total_ones = [0] * len(diag_bits)
        total_ones = [x + y for x, y in zip(diag_bits, total_ones)]
        total_zeroes = [(1 - x) + y for x, y in zip(diag_bits, total_zeroes)]

gamma_bits = [max_bit(ones, zeroes) for ones, zeroes in zip(total_ones, total_zeroes)]
epsilon_bits = [(1 - bit) for bit in gamma_bits]

gamma_rate = bits_to_int(gamma_bits)
epsilon_rate = bits_to_int(epsilon_bits)

power_consumption = gamma_rate * epsilon_rate

print(gamma_rate, epsilon_rate, power_consumption)