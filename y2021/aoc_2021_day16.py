from __future__ import annotations

import math

puzzle_input = 'A20D74AFC6C80CEA7002D4009202C7C00A6830029400F500218080C3002D006CC2018658056E7002DC00C600E75002ED6008EDC00D4003E24A13995080513FA309482649458A054C6E00E6008CEF204BA00B080311B21F4101006E1F414846401A55002F53E9525B845AA7A789F089402997AE3AFB1E6264D772D7345C6008D8026200E41D83B19C001088CB04A294ADD64C0129D818F802727FFF3500793FFF9A801A801539F42200DC3801A39C659ACD3FC6E97B4B1E7E94FC1F440219DAFB5BB1648E8821A4FF051801079C379F119AC58ECC011A005567A6572324D9AE6CCD003639ED7F8D33B8840A666B3C67B51388440193E003413A3733B85F2712DEBB59002B930F32A7D0688010096019375300565146801A194844826BB7132008024C8E4C1A69E66108000D39BAD950802B19839F005A56D9A554E74C08028992E95D802D2764D93B27900501340528A7301F2E0D326F274BCAB00F5009A737540916D9A9D1EA7BD849100425D9E3A9802B800D24F669E7691E19CFFE3AF280803440086C318230DCC01E8BF19E33980331D631C593005E80330919D718EFA0E3233AE31DF41C67F5CB5CAC002758D7355DD57277F6BF1864E9BED0F18031A95DDF99EB7CD64626EF54987AE007CCC3C4AE0174CDAD88E65F9094BC4025FB2B82C6295F04100109263E800FA41792BCED1CC3A233C86600B48FFF5E522D780120C9C3D89D8466EFEA019009C9600A880310BE0C47A100761345E85F2D7E4769240287E80272D3CEFF1C693A5A79DFE38D27CCCA75E5D00803039BFF11F401095F714657DC56300574010936491FBEC1D8A4402234E1E68026200CC5B8FF094401C89D12E14B803325DED2B6EA34CA248F2748834D0E18021339D4F962AB005E78AE75D08050E10066114368EE0008542684F0B40010B8AB10630180272E83C01998803104E14415100623E469821160'.strip()
test_input = 'D2FE28'.strip()

def hex2bin(string: str) -> str:
    bin_str = ''
    for ch in string:
        bin_str += bin(int(ch, 16))[2:].rjust(4, '0')
    return bin_str

def parse_groups(string: str, index: int):
    groups = []
    while True:
        group, index = string[index:index+5], index+5
        groups.append(group[1:])
        if group[0] == '0':
            return groups, index

def parse_bits(string: str, index: int = 0, part: int = 1) -> tuple:
    version, type_id, index = int(string[index:index+3], 2), int(string[index+3:index+6], 2), index+6
    if type_id == 4:
        groups, index = parse_groups(string, index)
        return version, type_id, int(''.join(groups), 2), index
    else:
        length_type_id, index = int(string[index], 2), index+1
        subpackets = []
        if length_type_id == 0:
            subpacket_length, index = int(string[index:index+15], 2), index+15
            subpacket_index = index + subpacket_length
            while index < subpacket_index:
                subpackets.append(parse_bits(string, index, part=part))
                index = subpackets[-1][-1]
        else:
            nrs_subpacket, index = int(string[index:index+11], 2), index+11
            while len(subpackets) < nrs_subpacket:
                subpackets.append(parse_bits(string, index, part=part))
                index = subpackets[-1][-1]
        if part == 1:
            return version, type_id, subpackets, index
        values = [packet[2] for packet in subpackets]
        funcs = {0: sum, 1: math.prod, 2: min, 3: max, 5: lambda v: int(v[0] > v[1]),
                 6: lambda v: int(v[0] < v[1]), 7: lambda v: int(v[0] == v[1])}
        return version, type_id, funcs[type_id](values), index

def get_version_numbers(packet: tuple) -> list[int]:
    total = [packet[0]]
    if isinstance(packet[2], list):
        for p in packet[2]:
            total.extend(get_version_numbers(p))
    return total
    
def part1(puzzle):
    packet = parse_bits(hex2bin(puzzle.strip()), part=1)
    return sum(get_version_numbers(packet))

def part2(puzzle):
    packet = parse_bits(hex2bin(puzzle.strip()), part=2)
    return packet[2]

print(part1(puzzle_input))
print(part2(puzzle_input))
