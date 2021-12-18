from __future__ import annotations

puzzle_input = 'target area: x=94..151, y=-156..-103'.strip()
test_input = 'target area: x=20..30, y=-10..-5'.strip()

class TargetArea:
    def __init__(self, x0: int, x1: int, y0: int, y1: int):
        self.x0, self.x1 = x0, x1
        self.x_range = range(x0, x1+1)
        self.y0, self.y1 = y0, y1
        self.y_range = range(y0, y1+1)
    def __repr__(self):
        return f"TargetArea(x={self.x0}..{self.x1}, y={self.y0}..{self.y1})"
    def __contains__(self, other: tuple[int, int]):
        return other[0] in self.x_range and other[1] in self.y_range
    def __gt__(self, other: tuple[int, int]):
        return other[0] < self.x0 and other[1] > self.y1
    def __ge__(self, other: tuple[int, int]):
        return other[0] <= self.x1 and other[1] >= self.y0

def get_target_area(string: str) -> TargetArea:
    x = [int(nr) for nr in string.split("x=")[1].split(',')[0].split("..")]
    y = [int(nr) for nr in string.split("y=")[1].split("..")]
    return TargetArea(*x, *y)

def towards_zero(nr: int):
    return -1 if nr < 0 else 0 if nr == 0 else 1

def probe_step(probe: tuple, velocity: tuple) -> (tuple, tuple):
    probe = (probe[0] + velocity[0],
             probe[1] + velocity[1])
    velocity = (velocity[0] - towards_zero(velocity[0]),
                velocity[1] - 1)
    return probe, velocity

def probe_intersects(init_velocity: tuple[int, int], target_area: TargetArea):
    probe = (0, 0)
    while probe <= target_area and probe not in target_area:
        probe, init_velocity = probe_step(probe, init_velocity)
    return probe in target_area

def part1(puzzle):
    target_area = get_target_area(puzzle)
    inf = float("inf")
    best = (-inf, -inf)
    for x in range(1, target_area.x1+1):
        for y in range(target_area.y0, 250):
            if y > best[1] and probe_intersects((x, y), target_area):
                best = (x, y)
    probe = (0, 0)
    if best[1] < 0:
        return probe[1]
    best, velocity = (-inf, -inf), best
    while probe[1] >= 0:
        probe, velocity = probe_step(probe, velocity)
        if probe[1] > best[1]:
            best = probe
    return best[1]

def part2(puzzle):
    target_area = get_target_area(puzzle)
    total = 0
    for x in range(1, target_area.x1+1):
        for y in range(target_area.y0, 250):
            if probe_intersects((x, y), target_area):
                total += 1
    return total

print(part1(puzzle_input))
print(part2(puzzle_input))
