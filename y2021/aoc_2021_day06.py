from collections import defaultdict

puzzle_input = '''2,3,1,3,4,4,1,5,2,3,1,1,4,5,5,3,5,5,4,1,2,1,1,1,1,1,1,4,1,1,1,4,1,3,1,4,1,1,4,1,3,4,5,1,1,5,3,4,3,4,1,5,1,3,1,1,1,3,5,3,2,3,1,5,2,2,1,1,4,1,1,2,2,2,2,3,2,1,2,5,4,1,1,1,5,5,3,1,3,2,2,2,5,1,5,2,4,1,1,3,3,5,2,3,1,2,1,5,1,4,3,5,2,1,5,3,4,4,5,3,1,2,4,3,4,1,3,1,1,2,5,4,3,5,3,2,1,4,1,4,4,2,3,1,1,2,1,1,3,3,3,1,1,2,2,1,1,1,5,1,5,1,4,5,1,5,2,4,3,1,1,3,2,2,1,4,3,1,1,1,3,3,3,4,5,2,3,3,1,3,1,4,1,1,1,2,5,1,4,1,2,4,5,4,1,5,1,5,5,1,5,5,2,5,5,1,4,5,1,1,3,2,5,5,5,4,3,2,5,4,1,1,2,4,4,1,1,1,3,2,1,1,2,1,2,2,3,4,5,4,1,4,5,1,1,5,5,1,4,1,4,4,1,5,3,1,4,3,5,3,1,3,1,4,2,4,5,1,4,1,2,4,1,2,5,1,1,5,1,1,3,1,1,2,3,4,2,4,3,1'''.strip()
test_input = '''3,4,3,1,2'''.strip()

class Fish:
    _fishes = defaultdict(int)
    @staticmethod
    def new_fish(timer: int):
        Fish._fishes[timer] += 1
    @staticmethod
    def tick_all(debug=False):
        new_fishes = defaultdict(int)
        for timer, fish_amount in Fish._fishes.items():
            if timer == 0:
                new_fishes[8] += fish_amount
                new_fishes[6] += fish_amount
            else:
                new_fishes[timer-1] += fish_amount
        Fish._fishes = new_fishes
        if debug:
            print(dict(Fish._fishes))
    @staticmethod
    def fish_count():
        return sum(Fish._fishes.values())
    @staticmethod
    def reset_fishes():
        Fish._fishes = defaultdict(int)

def partx(puzzle, i):
    Fish.reset_fishes()
    for x in puzzle.split(','):
        Fish.new_fish(int(x))
    for i in range(i):
        Fish.tick_all()
    return Fish.fish_count()

def part1(puzzle):
    return partx(puzzle, 80)

def part2(puzzle):
    return partx(puzzle, 256)

print(part1(puzzle_input))
print(part2(puzzle_input))
