import heapq
import math
from collections import defaultdict

import numpy as np


def part1():
    with open("Input/input16.txt") as fp:
        input = fp.readline()
        input = "8A004A801A8002F478"

    binary_input = ""
    binary_hex_dict = {
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
        "F": "1111"
    }

    for s in input:
        binary_input += binary_hex_dict[s]

    packet = Packet(binary_input)
    read_packet(packet)
    print(packet.get_total_version_id() + packet.version)

def read_packet(packet):
    if all(ss == "0" for ss in packet.s):
        return

    sub_packet_length_processed = 0

    sub_packet_length_processed += 3
    type_id = packet.type_id
    sub_packet_length_processed += 3

    if type_id == 4:
        literal_value_code = packet.s[6:]
        i = 0
        five_bits = literal_value_code[5 * i:5 * (i + 1)]
        binary_literal_value = ""
        literal_values = []
        while True:
            sub_packet_length_processed += 5
            binary_literal_value += five_bits[1:]
            i += 1
            if five_bits[0] == "0":
                literal_values.append(int(binary_literal_value, 2))
                if sub_packet_length_processed != len(packet.s):
                    packet.sub_packets.append(read_packet(Packet(packet.s[sub_packet_length_processed:])))
                    break
                else:
                    break
            five_bits = literal_value_code[5 * i:5 * (i + 1)]
    else:
        length_type_id = int(packet.s[6])
        if length_type_id == 0:
            binary_sub_packet_bit_length = packet.s[7:7+15]
            sub_packet_bit_length = int(binary_sub_packet_bit_length, 2)
            packet.sub_packets.append(read_packet(Packet(packet.s[7+15:7+15+sub_packet_bit_length])))
        else:
            remaining_number_of_sub_packets = int(packet.s[7:7+11], 2)
            while packet.sub_package_count() < remaining_number_of_sub_packets:
                packet.sub_packets.append(read_packet(Packet(packet.s[7+11:])))

    return packet


class Packet:
    def __init__(self, s):
        self.s = s
        self.sub_packets = []

    def add_sub_packet(self, p):
        self.sub_packets.append(p)

    @property
    def version(self):
        return int(self.s[0:0+3], 2)

    @property
    def type_id(self):
        return int(self.s[3:6], 2)

    def sub_package_count(self):
        if len(self.sub_packets) == 0:
            return 1

        return sum(s.sub_package_count() for s in self.sub_packets)

    def get_total_version_id(self):
        if len(self.sub_packets) == 0:
            return self.version

        return sum(p.get_total_version_id() for p in self.sub_packets)
