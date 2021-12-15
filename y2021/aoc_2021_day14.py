from __future__ import annotations

from collections import defaultdict, Counter

puzzle_input = 'NBOKHVHOSVKSSBSVVBCS\n\nSN -> H\nKP -> O\nCP -> V\nFN -> P\nFV -> S\nHO -> S\nNS -> N\nOP -> C\nHC -> S\nNP -> B\nCF -> V\nNN -> O\nOS -> F\nVO -> V\nHK -> N\nSV -> V\nVC -> V\nPH -> K\nNH -> O\nSB -> N\nKS -> V\nCB -> H\nSS -> P\nSP -> H\nVN -> K\nVP -> O\nSK -> V\nVF -> C\nVV -> B\nSF -> K\nHH -> K\nPV -> V\nSO -> H\nNK -> P\nNO -> C\nON -> S\nPB -> K\nVS -> H\nSC -> P\nHS -> P\nBS -> P\nCS -> P\nVB -> V\nBP -> K\nFH -> O\nOF -> F\nHF -> F\nFS -> C\nBN -> O\nNC -> F\nFC -> B\nCV -> V\nHN -> C\nKF -> K\nOO -> P\nCC -> S\nFF -> C\nBC -> P\nPP -> F\nKO -> V\nPC -> B\nHB -> H\nOB -> N\nOV -> S\nKH -> B\nBO -> B\nHV -> P\nBV -> K\nPS -> F\nCH -> C\nSH -> H\nOK -> V\nNB -> K\nBF -> S\nCO -> O\nNV -> H\nFB -> K\nFO -> C\nCK -> P\nBH -> B\nOH -> F\nKB -> N\nOC -> K\nKK -> O\nCN -> H\nFP -> K\nVH -> K\nVK -> P\nHP -> S\nFK -> F\nBK -> H\nKV -> V\nBB -> O\nKC -> F\nKN -> C\nPO -> P\nNF -> P\nPN -> S\nPF -> S\nPK -> O\n'.strip()
test_input = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.strip()

def get_pairs(puzzle):
    pairs = {}
    puzzle = puzzle.split("\n\n")[1].strip()
    for line in puzzle.split('\n'):
        key, value = line.split(' -> ')
        pairs[key] = value
    return pairs

def pair_insert(template: str, pairs: dict[str, str], steps: int) -> Counter[str]:
    polymer = defaultdict(int)
    for ch, ch2 in zip(template, template[1:]):
        polymer[ch + ch2] += 1
    for _ in range(steps):
        new_polymer = defaultdict(int)
        for key, value in polymer.items():
            ch, ch2 = key
            insertion = pairs[key]
            new_polymer[ch + insertion] += value
            new_polymer[insertion + ch2] += value
        polymer = new_polymer
    counter = defaultdict(int)
    for k, v in polymer.items():
        for ch in k:
            counter[ch] += v
    for k, v in counter.items():
        counter[k] = (v+1)//2
    return Counter(counter)

def partx(puzzle, steps: int):
    pairs = get_pairs(puzzle)
    template = puzzle.split("\n\n")[0]
    counter = pair_insert(template, pairs, steps).most_common()  # ordered by times appeared
    return counter[0][1] - counter[-1][1]

def part1(puzzle):
    return partx(puzzle, 10)

def part2(puzzle):
    return partx(puzzle, 40)

print(part1(puzzle_input))
print(part2(puzzle_input))
