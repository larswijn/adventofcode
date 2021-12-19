from __future__ import annotations

import json
import operator
from itertools import permutations
from math import floor, ceil

puzzle_input = '[[6,[[9,4],[5,5]]],[[[0,7],[7,8]],[7,0]]]\n[[[[2,1],[8,6]],[2,[4,0]]],[9,[4,[0,6]]]]\n[[[[4,2],[7,7]],4],[3,5]]\n[8,[3,[[2,3],5]]]\n[[[[0,0],[4,7]],[[5,5],[8,5]]],[8,0]]\n[[[[5,2],[5,7]],[1,[5,3]]],[[4,[8,4]],2]]\n[[5,[[2,8],[9,3]]],[[7,[5,2]],[[9,0],[5,2]]]]\n[[9,[[4,3],1]],[[[9,0],[5,8]],[[2,6],1]]]\n[[0,6],[6,[[6,4],[7,0]]]]\n[[[9,[4,2]],[[6,0],[8,9]]],[[0,4],[3,[6,8]]]]\n[[[[3,2],0],[[9,6],[3,1]]],[[[3,6],[7,6]],[2,[6,4]]]]\n[5,[[[1,6],[7,8]],[[6,1],[3,0]]]]\n[2,[[6,[7,6]],[[8,6],3]]]\n[[[[0,9],1],[2,3]],[[[7,9],1],7]]\n[[[[1,8],3],[[8,8],[0,8]]],[[2,1],[8,0]]]\n[[2,9],[[5,1],[[9,3],[4,0]]]]\n[9,[8,4]]\n[[[3,3],[[6,2],8]],5]\n[[[9,[4,8]],[[1,3],[6,7]]],[9,[[4,4],2]]]\n[[[[1,3],6],[[5,6],[1,9]]],[9,[[0,2],9]]]\n[7,[[[0,6],[1,2]],4]]\n[[[[5,0],[8,7]],[[7,3],0]],[[6,7],[0,1]]]\n[[[[5,4],7],[[8,2],1]],[[[7,0],[6,9]],0]]\n[[[3,[5,6]],[[9,5],4]],[[[9,4],[8,1]],[5,[7,4]]]]\n[[[3,[7,5]],[[8,1],8]],[[[6,3],[9,2]],[[5,7],7]]]\n[8,[[2,0],[[2,6],8]]]\n[[[[5,8],9],1],[9,6]]\n[[[9,9],[8,8]],[[[3,5],[8,0]],[[4,6],[3,2]]]]\n[[5,[[5,1],6]],[[5,8],9]]\n[[7,[[1,6],6]],[[[8,6],7],[6,6]]]\n[[0,[[9,5],0]],[4,[[7,9],[4,9]]]]\n[[[[4,3],[3,5]],[[1,9],[7,6]]],[3,[[6,4],[6,0]]]]\n[[[2,6],6],[6,3]]\n[[[[1,5],[3,7]],0],[3,7]]\n[4,[[[5,5],4],[[5,5],[9,3]]]]\n[[3,[8,6]],[8,[7,7]]]\n[8,[9,5]]\n[[[6,3],[2,[3,6]]],[[[6,0],[0,2]],[[8,7],5]]]\n[[[8,[1,2]],2],7]\n[[[[8,4],[2,7]],[[3,9],7]],[[4,[8,8]],[[7,4],9]]]\n[[[8,[2,5]],[3,[1,2]]],[[4,[5,0]],3]]\n[[8,[0,3]],[[5,1],[1,1]]]\n[[[8,[3,6]],6],[[7,[1,5]],[[4,8],9]]]\n[[[5,0],[0,3]],[[2,[7,8]],[1,[4,8]]]]\n[9,[4,[9,4]]]\n[[[9,[0,4]],2],3]\n[[9,[7,[8,9]]],3]\n[[[8,6],[[3,5],[9,2]]],[[3,[9,7]],5]]\n[[6,[[7,4],2]],[2,[7,[6,0]]]]\n[1,[[[2,2],6],8]]\n[[[6,[1,8]],[[9,3],[1,8]]],[[[8,2],[9,3]],[[8,2],[9,9]]]]\n[[[[2,9],[1,7]],[[4,0],8]],[[8,9],[6,3]]]\n[[[[2,4],[6,1]],[[5,4],[2,8]]],[8,[1,[2,4]]]]\n[[[4,6],[1,6]],[3,[1,1]]]\n[[[[8,3],8],8],[1,[[4,2],3]]]\n[[[9,[8,7]],[5,9]],[8,[[5,6],[4,5]]]]\n[[[[4,1],2],[[7,8],4]],[0,6]]\n[[[9,7],[[8,6],[6,9]]],[[8,[8,4]],[[9,0],2]]]\n[[[8,5],[1,9]],[[[2,4],5],6]]\n[[[9,[9,3]],[9,[2,3]]],[7,7]]\n[[[8,[7,4]],[2,6]],[[[4,5],[9,9]],[0,[5,2]]]]\n[7,[2,2]]\n[[[[1,8],[5,2]],3],[0,[2,[4,5]]]]\n[[5,[[4,8],[5,5]]],[4,[[3,4],[6,0]]]]\n[[3,1],[4,[3,[8,2]]]]\n[[3,7],[3,[[6,1],[0,2]]]]\n[[4,[6,2]],[[3,9],8]]\n[[[[2,9],3],[[5,6],4]],[8,2]]\n[[4,[[7,9],[4,9]]],[[4,3],[7,[0,7]]]]\n[[[3,[8,9]],[[3,4],[9,5]]],3]\n[0,[[[3,0],[8,7]],[[0,9],[9,1]]]]\n[[[5,[9,9]],2],[4,8]]\n[[[[4,4],4],5],[3,4]]\n[[[3,[2,2]],7],[[3,2],0]]\n[[[[0,5],[5,2]],2],[2,[[1,2],2]]]\n[[[4,6],6],[[0,1],6]]\n[2,[[[3,9],7],[[9,8],8]]]\n[[7,9],[7,[[3,0],9]]]\n[[[1,[6,2]],[0,8]],[[[7,2],4],9]]\n[[[[4,7],[1,5]],[5,9]],[[2,[0,4]],[7,[7,0]]]]\n[[1,[[2,0],[0,4]]],[[[4,6],9],[[6,8],[0,1]]]]\n[[[[6,0],7],[7,[9,6]]],[[7,[4,9]],[9,4]]]\n[[[5,[4,6]],[[1,9],[5,8]]],[[[3,6],[2,6]],[[7,3],7]]]\n[[[6,0],[6,6]],[2,8]]\n[[[4,[7,2]],[[5,6],[2,4]]],[[[6,8],5],[4,6]]]\n[[[[9,0],9],[4,0]],[[[9,1],8],[6,4]]]\n[[6,3],[1,[[5,0],[9,9]]]]\n[[[2,7],[5,6]],[[6,[1,4]],[9,9]]]\n[[[[0,5],3],[8,7]],[[[9,9],[6,2]],[0,7]]]\n[[[5,6],[1,7]],[[[0,4],9],9]]\n[[[7,3],3],[6,[0,[8,9]]]]\n[[[0,6],[[8,5],[4,6]]],[[[2,7],[4,2]],[[8,7],[0,5]]]]\n[[[8,[7,3]],1],8]\n[[8,[8,[8,2]]],[[5,4],[1,[2,6]]]]\n[[[[1,1],[8,6]],5],9]\n[[[[2,4],[5,7]],[[5,8],[3,1]]],7]\n[[4,[[0,1],9]],[[3,8],[4,2]]]\n[3,2]\n[[3,4],[8,[[6,5],[6,6]]]]\n[[[[7,0],[3,8]],[[3,3],[2,6]]],[[8,0],9]]'.strip()
test_input = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]\n[[[5,[2,8]],4],[5,[[9,9],0]]]\n[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]\n[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]\n[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]\n[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]\n[[[[5,4],[7,7]],8],[[8,3],8]]\n[[9,3],[[9,9],[6,[4,9]]]]\n[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]\n[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.strip()

def list_rindex(lst: list, value) -> int:
    # get right-most index of value in list
    return len(lst) - operator.indexOf(reversed(lst), value) - 1


class Snailfish:
    def __init__(self, snailfishes: list):
        self.snailfishes: list[Snailfish | int] = [Snailfish(item) if isinstance(item, list) else item
                                                 for item in snailfishes]
    def __repr__(self):
        return f"Snailfish({str(self)})"
    def __str__(self):
        return '[' + ', '.join(str(item) for item in self.snailfishes).strip(', ') + ']'
    def __getitem__(self, key) -> Snailfish | int:
        if isinstance(key, (list, tuple)):
            if len(key) <= 1:
                return self.snailfishes[key[0]]
            else:
                return self.snailfishes[key[0]][key[1:]]
        else:
            return self.snailfishes[key]
    def __setitem__(self, key, value):
        if isinstance(key, (list, tuple)):
            if len(key) <= 1:
                self.snailfishes[key[0]] = value
            else:
                self.snailfishes[key[0]][key[1:]] = value
        else:
            self.snailfishes[key] = value
    def __add__(self, other) -> Snailfish:
        return Snailfish([self.snailfishes, other.snailfishes])
    def copy(self) -> Snailfish:
        return Snailfish([item.copy() if isinstance(item, Snailfish) else item
                          for item in self.snailfishes])
    def get_first_nested_pair(self, nested: int = 4) -> (list[int], Snailfish):
        for index, item in enumerate(self.snailfishes):
            if isinstance(item, Snailfish):
                if nested == 1:
                    return [index], item
                recursion = item.get_first_nested_pair(nested-1)
                if recursion[1]:
                    return [index]+recursion[0], recursion[1]
        return [], None
    def get_first_splittable(self) -> (list[int], int):
        for index, item in enumerate(self.snailfishes):
            if isinstance(item, Snailfish):
                recursion = item.get_first_splittable()
                if recursion[1]:
                    return [index]+recursion[0], recursion[1]
            elif item >= 10:
                return [index], item
        return [], None
    def _find_x_of(self, indices: list[int], zero_or_one: int) -> list[int]:
        a, b = zero_or_one, 0 if zero_or_one == 1 else 1
        if a not in indices:
            return
        new_indices = indices[:list_rindex(indices, a)] + [b]
        while isinstance(self[new_indices], Snailfish):
            new_indices.append(a)
        return new_indices
    def find_left_of(self, indices: list[int]) -> list[int]:
        return self._find_x_of(indices, 1)
    def find_right_of(self, indices: list[int]) -> list[int]:
        return self._find_x_of(indices, 0)
    def explode(self) -> bool:
        indices, values = self.get_first_nested_pair()
        if values:
            to_the_left, to_the_right = self.find_left_of(indices), self.find_right_of(indices)
            if to_the_left:
                self[to_the_left] += values[0]
            if to_the_right:
                self[to_the_right] += values[1]
            self[indices] = 0
        return bool(values)
    def split(self) -> bool:
        indices, value = self.get_first_splittable()
        if value:
            self[indices] = Snailfish([floor(value / 2), ceil(value / 2)])
        return bool(value)
    def reduce(self) -> Snailfish:
        copy, first = self.copy(), True
        while first or (splitted := copy.split()):
            while first or (exploded := copy.explode()):
                first = False
        return copy
    def _magnitude(self, index: int) -> int:
        return self[index].magnitude() if isinstance(self[index], Snailfish) else self[index]
    def magnitude(self) -> int:
        return 3 * self._magnitude(0) + 2 * self._magnitude(1)


def parse_input(puzzle: str) -> list[Snailfish]:
    return [Snailfish(json.loads(line)) for line in puzzle.split('\n')]

def part1(puzzle: str):
    snailfishes = parse_input(puzzle)
    while len(snailfishes) >= 2:
        snailfishes[0:2] = [(snailfishes[0] + snailfishes[1]).reduce()]
    return snailfishes[0].magnitude()

def part2(puzzle: str):
    snailfishes = parse_input(puzzle)
    return max((sf_a + sf_b).reduce().magnitude() for sf_a, sf_b in permutations(snailfishes, 2))

print(part1(puzzle_input))
print(part2(puzzle_input))
