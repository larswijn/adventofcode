
import math
import random
import time

import useful_functions
from adventofcode.y2019.day7 import Intcode

puzzle_input = '''3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,102,1,1034,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,102,1,1034,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,1001,1038,0,1043,101,0,1037,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,101,0,1035,1040,101,0,1038,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,5,1032,1006,1032,165,1008,1040,9,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,73,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,101,0,1039,1034,1002,1040,1,1035,1002,1041,1,1036,1002,1043,1,1038,101,0,1042,1037,4,1044,1105,1,0,43,57,94,36,95,30,10,40,88,72,99,97,53,21,87,48,77,40,75,69,46,98,78,22,21,38,17,12,96,34,94,81,18,49,92,1,26,67,48,15,80,51,60,92,9,77,89,64,15,85,53,94,84,99,70,7,8,69,79,79,41,62,98,22,94,92,69,97,65,96,47,99,71,4,75,10,89,85,13,89,93,93,33,46,80,61,80,75,47,99,54,63,54,57,99,80,97,77,48,33,97,95,92,20,75,3,90,84,1,50,15,94,80,95,93,70,22,3,74,69,27,99,91,66,99,1,67,12,94,31,78,83,51,97,25,4,92,85,3,96,60,5,98,69,23,95,70,92,99,1,5,84,51,87,60,67,56,98,44,80,71,81,59,58,97,82,48,87,4,76,87,45,23,75,62,89,29,37,83,22,89,81,48,64,92,30,13,90,89,83,50,49,14,89,2,34,39,84,88,21,1,81,41,74,95,89,37,82,30,87,11,93,78,67,99,8,95,84,26,93,9,95,7,18,93,94,55,96,50,92,97,43,88,53,22,91,91,35,5,79,34,66,56,24,95,49,86,72,98,52,19,81,10,90,78,12,76,8,37,87,62,80,98,52,19,40,97,83,70,18,94,77,62,87,13,35,90,35,78,68,84,89,77,13,71,19,81,54,96,88,22,40,99,24,62,85,37,95,97,89,64,30,18,98,95,9,27,76,85,49,99,31,55,71,89,95,86,94,69,24,98,32,84,99,72,82,89,61,75,30,90,74,10,71,14,80,55,68,61,99,54,84,49,17,74,83,79,38,25,90,38,99,36,89,14,38,80,71,92,10,4,65,35,78,95,40,36,78,13,39,83,76,82,64,16,96,95,31,75,95,79,2,89,38,36,87,36,76,81,38,42,92,38,7,83,87,83,87,54,96,99,78,50,43,94,96,41,87,77,8,90,78,72,79,49,82,82,56,13,94,34,90,44,82,22,60,96,48,97,2,88,87,47,92,40,91,4,58,93,29,61,83,98,99,7,8,91,30,15,88,20,90,79,10,93,31,41,95,94,56,94,95,70,93,50,94,40,37,42,84,45,35,59,27,75,80,52,90,93,15,21,92,18,52,96,83,1,90,86,12,79,21,38,98,13,74,99,40,85,41,60,94,54,44,98,83,35,57,76,66,94,94,59,82,62,77,76,22,87,39,95,98,5,90,60,88,46,91,23,58,16,83,79,7,99,11,53,76,12,88,96,88,35,58,63,81,12,26,79,89,79,26,28,23,5,90,1,76,85,55,74,44,42,88,78,36,83,61,86,92,37,62,82,80,60,46,78,32,76,20,56,77,81,9,40,45,81,85,46,7,65,96,90,19,83,16,78,66,25,24,87,80,55,93,71,84,21,86,38,79,80,94,11,42,81,89,56,18,81,33,86,72,48,86,90,59,10,92,35,77,39,94,58,97,36,5,90,96,87,40,21,22,74,80,42,32,59,60,96,25,26,95,54,90,54,15,18,98,61,91,58,84,2,19,83,36,87,60,99,63,34,79,84,92,25,74,62,6,76,84,33,80,54,91,84,3,83,95,34,22,92,88,6,88,93,17,87,59,95,17,98,65,24,20,90,95,31,74,93,30,66,80,79,72,98,7,74,34,87,77,3,24,4,82,93,42,53,90,47,82,65,65,16,75,91,79,20,93,77,54,71,81,47,82,18,78,94,92,63,75,36,87,34,87,31,92,29,98,22,80,95,91,17,97,35,79,87,87,61,93,93,99,63,95,36,90,78,77,61,83,0,0,21,21,1,10,1,0,0,0,0,0,0'''.strip()


def print_area(area):
    try:
        print('\n'.join(''.join(x) for x in area))
    except TypeError:
	    print('\n'.join(''.join(map(str, x)) for x in area))


def generate_maze(program) -> (list, tuple, tuple):
    """
    generate a maze based on an intcode program

    :param program: str or list, the intcode program
    :return: a maze, the starting position, and the end position
    """
    pc = Intcode(program)
    area = [[' ' for _ in range(81)] for _ in range(61)]
    droid_pos = [30, 40]
    original_droid_pos = droid_pos.copy()
    area[droid_pos[0]][droid_pos[1]] = 'D'
    output = None
    prev_direction = direction = None
    system_pos = None
    splitted_path = []
    step = -1
    while True:
        if system_pos is not None and step % 10 == 0:
            # 1/2 requirements fulfilled (system pos was found)
            if not splitted_path:
                # all requirements fulfilled (no more split paths)
                break
        step += 1
        if True:  # useless if statement, should always be true; there to collapse if-blocks
            if area[droid_pos[0]][droid_pos[1]+1] == ' ':
                direction = 4
            elif area[droid_pos[0]][droid_pos[1]-1] == ' ':
                direction = 3
            elif area[droid_pos[0]-1][droid_pos[1]] == ' ':
                direction = 1
            elif area[droid_pos[0]+1][droid_pos[1]] == ' ':
                direction = 2
            else:
                if prev_direction == 1 and area[droid_pos[0]][droid_pos[1]+1] not in {'#', '.'}:
                    direction = 4
                elif prev_direction == 2 and area[droid_pos[0]][droid_pos[1]-1] not in {'#', '.'}:
                    direction = 3
                elif prev_direction == 3 and area[droid_pos[0]-1][droid_pos[1]] not in {'#', '.'}:
                    direction = 1
                elif prev_direction == 4 and area[droid_pos[0]+1][droid_pos[1]] not in {'#', '.'}:
                    direction = 2
                else:
                    if splitted_path:
                        area[droid_pos[0]][droid_pos[1]] = '.'
                        pc, droid_pos, prev_direction = splitted_path.pop()
                        area[droid_pos[0]][droid_pos[1]] = 'D'
                        # print(f"tracked back to a previous splitting point")
                        continue
                    possible_directions = [1, 2, 3, 4]
                    if area[droid_pos[0]][droid_pos[1]+1] == '#':
                        possible_directions.remove(4)
                    if area[droid_pos[0]][droid_pos[1]-1] == '#':
                        possible_directions.remove(3)
                    if area[droid_pos[0]-1][droid_pos[1]] == '#':
                        possible_directions.remove(1)
                    if area[droid_pos[0]+1][droid_pos[1]] == '#':
                        possible_directions.remove(2)
                    print(f"possible dirs: {possible_directions}")
                    direction = random.choice(possible_directions)
        if sum([area[droid_pos[0]][droid_pos[1]+1] == ' ', area[droid_pos[0]][droid_pos[1]-1] == ' ',
                area[droid_pos[0] - 1][droid_pos[1]] == ' ', area[droid_pos[0]+1][droid_pos[1]] == ' ']) > 1:
            # empty spots multiple ways
            splitted_path.append([pc.deepcopy(),
                                  useful_functions.deepish_copy(droid_pos),
                                  prev_direction,
                                  ])
        pc.add_to_input_queue(direction)
        output = pc.run_until_output()
        if output == 0:
            if direction == 1:
                area[droid_pos[0]-1][droid_pos[1]] = '#'
            elif direction == 2:
                area[droid_pos[0]+1][droid_pos[1]] = '#'
            elif direction == 3:
                area[droid_pos[0]][droid_pos[1]-1] = '#'
            elif direction == 4:
                area[droid_pos[0]][droid_pos[1]+1] = '#'
        elif output == 1:
            area[droid_pos[0]][droid_pos[1]] = '.'
            if direction == 1:
                droid_pos[0] -= 1
            elif direction == 2:
                droid_pos[0] += 1
            elif direction == 3:
                droid_pos[1] -= 1
            elif direction == 4:
                droid_pos[1] += 1
            area[droid_pos[0]][droid_pos[1]] = 'D'
        elif output == 2:
            # we found the end point; move the droid and save it
            area[droid_pos[0]][droid_pos[1]] = '.'
            if direction == 1:
                droid_pos[0] -= 1
            elif direction == 2:
                droid_pos[0] += 1
            elif direction == 3:
                droid_pos[1] -= 1
            elif direction == 4:
                droid_pos[1] += 1
            area[droid_pos[0]][droid_pos[1]] = 'D'
            system_pos = droid_pos.copy()
        if step % 50 == 0:
            # print progress periodically
            print('\n' * 3, flush=False)
            print_area(area)
            print(f"step:  {step},  |  prev_dir: {prev_direction},  dir: {direction}")
            time.sleep(0.1)
        prev_direction = direction

    # locate start and end point, clean up the 'seeker'
    area[original_droid_pos[0]][original_droid_pos[1]] = 'X'
    area[system_pos[0]][system_pos[1]] = 'O'
    area[droid_pos[0]][droid_pos[1]] = '.'

    # bring back to only the relevant area
    minimum_x_real_area = minimum_y_real_area = math.inf
    maximum_x_real_area = maximum_y_real_area = 0
    for offset in range(len(area) // 2):
        if len(set(area[len(area) // 4 + offset])) == 1:
            continue
        help_x_real_area = [i for i, e in enumerate(area[len(area) // 4 + offset]) if e != ' ']
        minimum_x_real_area = min(minimum_x_real_area, min(help_x_real_area))
        maximum_x_real_area = max(maximum_x_real_area, max(help_x_real_area))
    help_y_real_area = [i for i, e in enumerate(area) if len(set(e)) != 1]
    minimum_y_real_area = min(help_y_real_area)
    maximum_y_real_area = max(help_y_real_area)
    real_area = [row[minimum_x_real_area:maximum_x_real_area + 1]
                 for row in area[minimum_y_real_area:maximum_y_real_area + 1]]
    original_droid_pos = original_droid_pos[0] - minimum_y_real_area, original_droid_pos[1] - minimum_x_real_area
    system_pos = system_pos[0] - minimum_y_real_area, system_pos[1] - minimum_x_real_area
    return real_area, original_droid_pos, system_pos


def old_solve_maze(maze: list, start: tuple, end: tuple, _visited=None, _dist=None):
    """
    find the shortest path from start to end in maze, recursively

    :param list maze: 2D, represent possible squares by 1, walls by 0
    :param tuple start: where to begin from (x, y)
    :param tuple end: where to end at (x, y)
    :param _visited: used upon recursive call; don't pass an argument
    :param _dist: used upon recursive call; don't pass an argument
    :rtype: dict
    :return: the length of the shortest path ('length'), and the shortest path ('path')
    """

    # maze = useful_functions.deepish_copy(maze)  # VERY INEFFICIENT

    if _dist is None:
        _dist = 0
    elif type(_dist) != int:
        raise TypeError("unexpected argument given for '_dist'")

    if _visited is None:
        _visited = []
    elif type(_visited) != list:
        raise TypeError("unexpected argument given for '_visited'")

    if start in _visited:
        return {'length': math.inf, 'path': _visited}  # start position is a previously visited position
    try:
        if maze[start[0]][start[1]] == 0:
            return {'length': math.inf, 'path': _visited}  # start position is a wall
        if start[0] < 0 or start[1] < 0:
            raise IndexError
    except IndexError:
        return {'length': math.inf, 'path': _visited}  # out of bounds

    min_dist = math.inf
    _visited.append(start)
    # maze[start[0]][start[1]] = 0

    if start == end:
        return {'length': _dist, 'path': _visited}  # found the end

    for dif_x, dif_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        _visited_copy = _visited.copy()
        result = solve_maze(maze, (start[0] + dif_x, start[1] + dif_y), end, _visited_copy, _dist + 1)
        if result['length'] < min_dist:
            min_dist = result['length']
            _visited = result['path']

    return {'length': min_dist, 'path': _visited}


def solve_maze(maze: list, start: tuple, end: tuple, _visited=None, _dist=None):
    """
    find the shortest path from start to end in maze, recursively

    :param list maze: 2D, represent possible squares by 1, walls by 0
    :param tuple start: where to begin from (x, y)
    :param tuple end: where to end at (x, y)
    :param _visited: used upon recursive call; don't pass an argument
    :param _dist: used upon recursive call; don't pass an argument
    :rtype: dict
    :return: the length of the shortest path ('length'), and the shortest path ('path')
    """

    # maze = useful_functions.deepish_copy(maze)  # VERY INEFFICIENT

    if _dist is None:
        _dist = 0
    elif type(_dist) != int:
        raise TypeError("unexpected argument given for '_dist'")

    if _visited is None:
        _visited = set()
    elif type(_visited) != set:
        raise TypeError("unexpected argument given for '_visited'")

    if start in _visited:
        return math.inf  # start position is a previously visited position
    try:
        if maze[start[0]][start[1]] == 0:
            return math.inf  # start position is a wall
        if start[0] < 0 or start[1] < 0:
            raise IndexError
    except IndexError:
        return math.inf # out of bounds

    min_dist = math.inf
    _visited.add(start)
    # maze[start[0]][start[1]] = 0

    if start == end:
        return _dist  # found the end

    for dif_x, dif_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        result = solve_maze(maze, (start[0] + dif_x, start[1] + dif_y), end, _visited, _dist + 1)
        if result < min_dist:
            min_dist = result
            # _visited = result['path']

    return 'path'


def main():
    print("initialized day15")
    start_time = time.time()
    with useful_functions.suppress_print():
        maze, start, end = generate_maze(puzzle_input)
    print("generated maze")
    print(f" (time taken: {round(time.time()-start_time, 5)}sec)")
    maze = [[1 if item in {'.', 'O', 'X'} else 0 for item in row] for row in maze]
    print("pt1:", solve_maze(maze, start, end)['length'])
    print(f" (time taken: {round(time.time()-start_time, 5)}sec)")
    distances_to_end = [solve_maze(maze, (x, y), end)['length']
                        for x in range(len(maze))
                        for y in range(len(maze[0]))
                        if maze[x][y] != 0]
    max_distance_maze = max([item for item in distances_to_end if not math.isinf(item)])
    print("pt2:", max_distance_maze)
    print(f" (time taken: {round(time.time()-start_time, 5)}sec)")

if __name__ == '__main__':
    main()

# from adventofcode.y2019.day15 import *; from adventofcode.y2019 import day15; main()
