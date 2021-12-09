
import math

import useful_functions
from adventofcode.y2019.day15 import solve_maze


def solve_key_door_maze(maze: list, _start=None, _keys_on_hand=None, _visited=None, _dist=None):
    """
    find the shortest path to collect all keys (lowercase letters)

    :param list maze: 2D, represent possible squares by '.', walls by '#', keys in lowercase and doors in uppercase
    :param tuple start: where to begin from (x, y)
    :param _dist: used upon recursive call; don't pass an argument
    :rtype: int
    :return: length of the shortest path
    """

    # maze = useful_functions.deepish_copy(maze)

    if _start is None:
        maze = useful_functions.deepish_copy(maze)
        for i, line in enumerate(maze):
            for j, item in enumerate(line):
                if item == '@':
                    _start = (i, j)
                    maze[i][j] = '.'
                    break
            if _start is not None:
                break
    elif type(_start) != tuple:
        raise TypeError("unexpected argument given for '_start'")

    if _keys_on_hand is None:
        _keys_on_hand = set()
    elif type(_keys_on_hand) != set:
        raise TypeError("unexpected argument given for '_keys_on_hand'")

    if False:
        if _visited is None:
            _visited = []
        elif type(_visited) != list:
            raise TypeError("unexpected argument given for '_visited'")
        _visited.append(_start)
        if _start in _visited:
            return math.inf

    if _dist is None:
        _dist = 0
    elif type(_dist) != int:
        raise TypeError("unexpected argument given for '_dist'")

    min_dist = math.inf

    try:
        if maze[_start[0]][_start[1]] == '#':  # also, raises index error if we're out of bounds
            return math.inf  # we're not a wall
        if _start[0] < 0 or _start[1] < 0:
            raise IndexError
    except IndexError:
        return math.inf # out of bounds
    if all(all(item not in {'r', 'y', 'z', 'q', 'a', 'j', 'f', 'o', 'h', 'g', 'v', 's', 'x', 'd', 'c', 'n', 'u', 'k',
                        'e', 'b', 'w', 'm', 'p', 'l', 't', 'i'} for item in line)
           for line in maze):
        # found all keys
        print("found all keys!")
        return _dist

    # maze[_start[0]][_start[1]] = '.'

    proper_maze = [[0 if item == '#'
                    else 1 if item in {'.', '@'} or item.islower() or item.lower() in _keys_on_hand
                    else 0
                    for item in row] for row in maze]
    for i, line in enumerate(maze):
        for j, item in enumerate(line):
            if item in {'r', 'y', 'z', 'q', 'a', 'j', 'f', 'o', 'h', 'g', 'v', 's', 'x', 'd', 'c', 'n', 'u', 'k',
                        'e', 'b', 'w', 'm', 'p', 'l', 't', 'i'}:
                # if it's a key
                if False:
                    print(f"finding solution for solving maze from {_start} till {(i, j)}...")
                solution = solve_maze(proper_maze, start=_start, end=(i, j))
                if solution['length'] != math.inf:
                    # and if it's obtainable
                    if False:
                        print(f"  found: distance is {solution['length']}, ending point is {solution['path'][-1]}")
                    maze[i][j] = '.'
                    with useful_functions.suppress_print():
                        min_dist = min(min_dist,
                                       solve_key_door_maze(maze, _start=(i, j),
                                                           _keys_on_hand=_keys_on_hand.union({item}),
                                                           _dist=_dist+solution['length'])
                                       )
                    maze[i][j] = item
        if False:
            print(i, 'of', len(maze))

    return min_dist


def trans2maze(maze: str) -> list:
	return [list(x) for x in maze.strip().split('\n')]


def maze_print(maze: list):
	print('\n'.join(''.join(x) for x in maze))


def block_empty_paths(maze: list):
    maze = useful_functions.deepish_copy(maze)
    found_end_point = True
    while found_end_point:
        found_end_point = False
        for x, line in enumerate(maze):
            for y, item in enumerate(line):
                if item == '.':
                    points_around = [maze[x + x_diff][y + y_diff]
                                     for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                                     if -1 < x + x_diff < len(maze) and -1 < y + y_diff < len(maze[0])]
                    if points_around.count('#') >= 3:
                        maze[x][y] = '#'
                        found_end_point = True
    return maze

