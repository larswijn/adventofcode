from __future__ import annotations
import math

puzzle_input = '4438624262\n6263251864\n2618812434\n2134264565\n1815131247\n2612457325\n8585767584\n7217134556\n2825456563\n8248473584'.strip()
test_input = '5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526'.strip()


class Map:
    def __init__(self, width: int, height: int, graph: list[int]):
        self.width, self.height = width, height
        self.graph = list(graph)
        self.flashes = 0
        self.flashed: set[(int, int)] = set()
    
    def __repr__(self):
        return f"Map({self.width}, {self.height}, {self.graph})"

    def _assert_valid_index(index: (int, int)):
        assert isinstance(key, tuple) and len(key) == 2 and key[0] >= 0 <= key[1], key
    
    def __getitem__(self, key):
        self._assert_valid_index(key)
        return self.graph[key[0]*self.width+key[1]]

    def __setitem__(self, key, value):
        self._assert_valid_index(key)
        self.graph[key[0]*self.width+key[1]] = value
    
    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (y, x), self[y, x]
    
    def flash(self, pos: (int, int)):
        if pos in self.flashed:
            return
        self.flashes += 1
        self.flashed.add(pos)
        for neighbour in self.get_neighbours(pos):
            self[neighbour] += 1
            if self[neighbour] > 9:
                self.flash(neighbour)
    
    def get_neighbours(self, pos: (int, int)) -> list[(int, int)]:
        y, x = pos
        neighbours = []
        for delta_y in range(-1, 2):
            for delta_x in range(-1, 2):
                if 0 <= (y+delta_y) < self.height and 0 <= (x+delta_x) < self.width and not delta_y == delta_x == 0:
                    neighbours.append((y + delta_y, x + delta_x))
        return neighbours
    
    def tick(self, amount: int = 1) -> (int, bool):
        """
        step `amount` of times for every octopus
        return total amount of flashes this produced and whether all octopuses flashed on the final step
        """
        self.flashes = 0
        for _ in range(amount):
            for pos, value in self:
                value = self[pos] = value+1
                if value > 9:
                    self.flash(pos)
            for flashed in self.flashed:
                self[flashed] = 0
            self.flashed = set()
        return self.flashes, len(self.flashed) == self.width * self.height
    
    @staticmethod
    def from_string(string: str) -> Map:
        width, height = len(string.split('\n')[0]), len(string.split('\n'))
        values = [int(x) for x in string.replace('\n', '')]
        return Map(width, height, values)


def part1(puzzle):
    octopuses_map = Map.from_string(puzzle)
    return octopuses_map.tick(100)[0]

def part2(puzzle):
    octopuses_map = Map.from_string(puzzle)
    i, all_flashed = 0, False
    while not all_flashed:
        _, all_flashed = octopuses_map.tick()
        i += 1
    return i

print(part1(puzzle_input))
print(part2(puzzle_input))
