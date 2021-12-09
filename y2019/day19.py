import useful_functions
from adventofcode.y2019.day7 import Intcode

puzzle_input = "109,424,203,1,21102,1,11,0,1105,1,282,21101,18,0,0,1106,0,259,2101,0,1,221,203,1,21102,1,31,0,1106,0,282,21101,0,38,0,1106,0,259,21002,23,1,2,22102,1,1,3,21101,0,1,1,21102,57,1,0,1106,0,303,2102,1,1,222,21002,221,1,3,21002,221,1,2,21101,0,259,1,21101,0,80,0,1105,1,225,21101,123,0,2,21101,91,0,0,1105,1,303,1201,1,0,223,20101,0,222,4,21101,259,0,3,21102,225,1,2,21101,0,225,1,21102,118,1,0,1105,1,225,21001,222,0,3,21102,58,1,2,21101,133,0,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,1201,1,0,223,20101,0,221,4,21002,222,1,3,21101,20,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22102,1,-3,1,22102,1,-2,2,22101,0,-1,3,21101,250,0,0,1105,1,225,21202,1,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21201,-2,0,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,1,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,1,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0"


def generate_tractor_beam_naive(program, size=50):
    presentation = [['.' for x in range(size)] for y in range(size)]
    for x in range(0, size):
        for y in range(0, size):
            pc = Intcode(program, inputs=[x, y])
            output = pc.run_until_output()
            if output:
                presentation[x][y] = '#'
    return presentation


def generate_tractor_beam(program, size=50):
    presentation = [['.' for x in range(size)] for y in range(size)]
    original_pc = Intcode(program)
    lowest_x, highest_x = 999_999, 0
    for x in range(size):
        for y in range(size):
            if x < 10 and y < 10:
                # let's assume we NEED to do the top-left 10x10 square for inconsistencies
                pc = original_pc.copy()
                pc._inputs = [x, y]
                output = pc.run_until_output()
                if y == 9:
                    if output:
                        if x < lowest_x:
                            lowest_x = x
                        if x > highest_x:
                            highest_x = x
                if output:
                    presentation[x][y] = '#'
            elif x > highest_x + 2 or x < lowest_x - 2 or (y < 10 and x > 12):
                # some shortcuts, with 'padding' of 2
                continue
            else:
                pc = Intcode(puzzle_input, inputs=[x, y])
                output = pc.run_until_output()
                if output:
                    presentation[x][y] = '#'
                    if x < lowest_x:
                        lowest_x = x
                    if x > highest_x:
                        highest_x = x
    return presentation


def find_space(tractor_beam: list, space=10):
    space -= 1
    for x, line in enumerate(tractor_beam):
        for y, item in enumerate(line):
            if item == '.':
                continue
            if y + space + 1 > len(tractor_beam[0]):
                break
            if x + space + 1 > len(tractor_beam):
                continue
            if tractor_beam[x][y + space] == '.':
                # y is too low
                continue
            if tractor_beam[x + space][y] == '.':
                # x is too low
                continue
            return x, y
    return 'tractor beam too small'


def main():
    tractor_beam = generate_tractor_beam(puzzle_input, size=50)
    pt1 = sum(line.count('#') for line in tractor_beam)
    print("pt1:", pt1)
    tractor_beam = generate_tractor_beam(puzzle_input, size=1000)
    print(" generated tractor beam for pt2...")
    pt2 = find_space(tractor_beam, space=100)
    print("pt2:", pt2)


if __name__ == '__main__':
    main()
