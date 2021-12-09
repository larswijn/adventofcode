import math

import useful_functions

universes = [
'''
.#..#
.....
#####
....#
...##
''',  # mini example
'''
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
''',  # small example #1
'''
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##
''',  # small example #2
'''
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
''',  # big example
'''  
.##.#.#....#.#.#..##..#.#.
#.##.#..#.####.##....##.#.
###.##.##.#.#...#..###....
####.##..###.#.#...####..#
..#####..#.#.#..#######..#
.###..##..###.####.#######
.##..##.###..##.##.....###
#..#..###..##.#...#..####.
....#.#...##.##....#.#..##
..#.#.###.####..##.###.#.#
.#..##.#####.##.####..#.#.
#..##.#.#.###.#..##.##....
#.#.##.#.##.##......###.#.
#####...###.####..#.##....
.#####.#.#..#.##.#.#...###
.#..#.##.#.#.##.#....###.#
.......###.#....##.....###
#..#####.#..#..##..##.#.##
##.#.###..######.###..#..#
#.#....####.##.###....####
..#.#.#.########.....#.#.#
.##.#.#..#...###.####..##.
##...###....#.##.##..#....
..##.##.##.#######..#...#.
.###..#.#..#...###..###.#.
#..#..#######..#.#..#..#.#
'''  # puzzle input
]

universe = universes[-1]
universe = [list(item) for item in universe.strip().split('\n')]

def best_monitor_location(universe=universe) -> (tuple, int):
    max_astroids_seen = 0
    best_position = ()
    for x, line in enumerate(universe):
        for y, item in enumerate(line):
            if item == '#':
                amount = len(get_seen_astroids(universe, (x, y)))
                if amount > max_astroids_seen:
                    max_astroids_seen = amount
                    best_position = (x, y)
    return best_position, max_astroids_seen


def get_seen_astroids(universe, astroid_pos: tuple) -> list:
    astroid_x, astroid_y = astroid_pos
    seeable_astroids = dict()
    for x, line in enumerate(universe):
        for y, item in enumerate(line):
            if item == '#' and (x, y) != astroid_pos:
                delta_x, delta_y = x - astroid_x, y - astroid_y
                angle_delta_x, angle_delta_y = delta_x, delta_y
                gcd = math.gcd(angle_delta_x, angle_delta_y)
                if gcd != 1:
                    angle_delta_x, angle_delta_y = angle_delta_x//gcd, angle_delta_y//gcd
                if (angle_delta_x, angle_delta_y) in seeable_astroids:
                    other = seeable_astroids[(angle_delta_x, angle_delta_y)]
                    this = delta_x, delta_y
                    if abs(other[0]) > abs(this[0]) or abs(other[1]) > abs(this[1]):
                        seeable_astroids[(angle_delta_x, angle_delta_y)] = delta_x, delta_y
                else:
                    seeable_astroids[(angle_delta_x, angle_delta_y)] = delta_x, delta_y
    return seeable_astroids


def sort_astroid_destruction(astroids):
	if type(astroids) == dict:
		astroids = list(astroids.values())
	sorted_astroids = []
	# right_astroids = [(x, y) for x, y in astroids if y >= 0]
	top_right_astroids = [(x, y) for x, y in astroids if x < 0 and y >= 0]
	top_right_astroids.sort(key=lambda x: math.degrees(math.atan2(x[1],x[0])), reverse=True)
	bottom_right_astroids = [(x, y) for x, y in astroids if x >= 0 and y >= 0]
	bottom_right_astroids.sort(key=lambda x: math.degrees(math.atan2(x[1],x[0])), reverse=True)
	# left_astroids = [(x, y) for x, y in astroids if y < 0]
	top_left_astroids = [(x, y) for x, y in astroids if x >= 0 and y < 0]
	top_left_astroids.sort(key=lambda x: math.degrees(math.atan2(x[1],x[0])), reverse=True)
	bottom_left_astroids = [(x, y) for x, y in astroids if x < 0 and y < 0]
	bottom_left_astroids.sort(key=lambda x: math.degrees(math.atan2(x[1],x[0])), reverse=True)

	return top_right_astroids + bottom_right_astroids + top_left_astroids + bottom_left_astroids


def find_xth_astroid_to_be_destroyed(universe, xth_astroid_to_be_destroyed, allow_printing=False):
    universe = useful_functions.deepish_copy(universe)
    if allow_printing:
        print(universe)
        print('\n'.join(''.join(e) for e in universe))
    best_position, max_astroids_seen = best_monitor_location(universe)
    astroids_seen = get_seen_astroids(universe, best_position)
    universe[best_position[0]][best_position[1]] = 'X'
    if allow_printing:
        print(best_position, max_astroids_seen)
        print('\n'.join(''.join(e) for e in universe), end='\n\n')
    xth_astroid = 0
    while '#' in useful_functions.flatten(universe):
        astroids_seen = get_seen_astroids(universe, best_position)
        astroid_destruction_order = useful_functions.chunks(sort_astroid_destruction(astroids_seen), 9)
        for chunk in astroid_destruction_order:
            for (ast_x, ast_y) in chunk:
                universe[best_position[0] + ast_x][best_position[1] + ast_y] = str(xth_astroid%9+1)
                xth_astroid += 1
                if xth_astroid == xth_astroid_to_be_destroyed:
                    if allow_printing:
                        print('\n'.join(''.join(e) for e in universe))
                        input('(press enter to continue) ')
                    return best_position[0] + ast_x, best_position[1] + ast_y
            if allow_printing:
                print('\n'.join(''.join(e) for e in universe))
                input('(press enter to continue) ')
            for index, (ast_x, ast_y) in enumerate(chunk):
                universe[best_position[0] + ast_x][best_position[1] + ast_y] = '.'
    print(f"finished  (destroyed astroids: {xth_astroid})")


def main(universe=universe):
    if universe != [list(item) for item in universes[-1].strip().split('\n')]:
        print("WARNING: current selected universe isn't equal to the puzzle input")
    best_position, max_astroids_seen = best_monitor_location(universe)
    print('pt1: position ', best_position, f" sees {max_astroids_seen} astroids ", ' (swapped x and y)',
          sep='')
    position_of_200th_asteroid_to_be_vaporized = find_xth_astroid_to_be_destroyed(universe, 200)
    print("pt2:", position_of_200th_asteroid_to_be_vaporized[1]*100+position_of_200th_asteroid_to_be_vaporized[0])


if __name__ == '__main__':
    main()