import sys
from collections import namedtuple

Packet = namedtuple("Packet", ["version", "type_id", "payload"])

LITERAL_ID = 4

HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(hex_str):
    return "".join(HEX_TO_BIN[c] for c in hex_str)


def parse_int(input_data, pos, length):
    val = int(input_data[pos : pos + length], 2)
    return (val, pos + length)


def parse_header(input_data, pos):
    version, pos = parse_int(input_data, pos, 3)
    type_id, pos = parse_int(input_data, pos, 3)
    return (version, type_id, pos)


def parse_literal(input_data, pos):
    literal = 0
    last_chunk = 1
    while last_chunk == 1:
        last_chunk, pos = parse_int(input_data, pos, 1)
        chunk_data, pos = parse_int(input_data, pos, 4)
        literal = literal * 16 + chunk_data
    return (literal, pos)


def parse_packet(input_data, pos=0):
    version, type_id, pos = parse_header(input_data, pos)
    if type_id == LITERAL_ID:
        literal, pos = parse_literal(input_data, pos)
        return (Packet(version, type_id, payload=literal), pos)
    else:
        sub_packets = []
        length_type_id, pos = parse_int(input_data, pos, 1)
        if length_type_id == 0:
            total_sub_lenght, pos = parse_int(input_data, pos, 15)
            end_pos = pos + total_sub_lenght
            while pos < end_pos:
                packet, pos = parse_packet(input_data, pos)
                sub_packets.append(packet)
        else:
            num_sub_packets, pos = parse_int(input_data, pos, 11)
            for _n in range(num_sub_packets):
                packet, pos = parse_packet(input_data, pos)
                sub_packets.append(packet)

        return (Packet(version, type_id, payload=sub_packets), pos)


def version_sum(packet):
    if packet.type_id == LITERAL_ID:
        return packet.version
    else:
        return packet.version + sum(version_sum(p) for p in packet.payload)


transmission = sys.stdin.readline().strip()
root_packet, _ = parse_packet(hex_to_bin(transmission))
print(version_sum(root_packet))
