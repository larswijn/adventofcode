
import useful_functions
from adventofcode.y2019.day7 import Intcode

puzzle_input = [3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,28,2,1105,12,10,1006,0,12,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,58,2,107,7,10,1006,0,38,2,1008,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,90,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,112,1006,0,65,1,1103,1,10,1006,0,91,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,144,1006,0,32,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,169,1,109,12,10,1006,0,96,1006,0,5,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,201,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,223,1,4,9,10,2,8,5,10,1,3,4,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,257,1,1,9,10,1006,0,87,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,287,2,1105,20,10,1,1006,3,10,1,3,4,10,101,1,9,9,1007,9,1002,10,1005,10,15,99,109,641,104,0,104,1,21102,1,932972962600,1,21101,0,336,0,1106,0,440,21101,838483681940,0,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3375393987,0,1,21101,394,0,0,1105,1,440,21102,46174071847,1,1,21102,1,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,988648461076,0,1,21101,428,0,0,1106,0,440,21101,0,709580452200,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,471,3,21102,461,1,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,0,1,466,109,-2,2105,1,0,0,109,4,1202,-1,1,503,1207,-3,0,10,1006,10,521,21102,1,0,-3,22102,1,-3,1,21201,-2,0,2,21101,0,1,3,21102,540,1,0,1106,0,545,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22101,0,-4,-4,1105,1,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,587,0,1105,1,545,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,606,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,21201,-1,0,1,21101,0,628,0,106,0,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

def draw(width, height, starting_color):
    BLACK_PANEL, WHITE_PANEL  = '.', '#'
    DIRECTION_LEFT, DIRECTION_RIGHT = 0, 1
    hull = [['.' for _ in range(width)] for _ in range(height)]
    robot_position, robot_orientation = (height//2, width//2), (-1, 0)  # (delta x, delta y)
    originally_at_robot = hull[robot_position[0]][robot_position[1]]
    hull[robot_position[0]][robot_position[1]] = '^'
    pc = Intcode(puzzle_input, inputs=[1 if starting_color in {1, 'white'} else 0])
    changed_items = set()
    # print('\n'.join(''.join(e) for e in hull), end='\n\n')
    # input('\n')
    import random
    while True:
        paint, direction = pc.run_until_output(), pc.run_until_output()
        if random.randint(1, 200) == 1:
            # print(paint != {BLACK_PANEL: 0, WHITE_PANEL: 1}[originally_at_robot])
            pass
        if pc.is_finished:
            print('done')
            break
        changed_items.add(robot_position)
        if paint == 0:
            hull[robot_position[0]][robot_position[1]] = BLACK_PANEL
        else:
            hull[robot_position[0]][robot_position[1]] = WHITE_PANEL
        if direction == DIRECTION_LEFT:
            if robot_orientation == (-1, 0):
                robot_orientation = (0, -1)
            elif robot_orientation == (1, 0):
                robot_orientation = (0, 1)
            elif robot_orientation == (0, -1):
                robot_orientation = (1, 0)
            elif robot_orientation == (0, 1):
                robot_orientation = (-1, 0)
        elif direction == DIRECTION_RIGHT:
            if robot_orientation == (-1, 0):
                robot_orientation = (0, 1)
            elif robot_orientation == (1, 0):
                robot_orientation = (0, -1)
            elif robot_orientation == (0, -1):
                robot_orientation = (-1, 0)
            elif robot_orientation == (0, 1):
                robot_orientation = (1, 0)

        # hull[robot_position[0]][robot_position[1]] = originally_at_robot
        robot_position = (robot_position[0]+robot_orientation[0], robot_position[1]+robot_orientation[1])
        try:
            originally_at_robot = hull[robot_position[0]][robot_position[1]]
            if robot_position[0] < 0 or robot_position[1] < 0:
                # negative indices should be avoided
                raise IndexError("list assignment index out of range")
        except IndexError:
            print("INDEXERR", end=' ')
            try:
                hull[robot_position[0]]
            except IndexError:
                print('(y)')
            else:
                if robot_position[0] < 0:
                    print('(y)')
                else:
                    print('(x)')
            return hull, changed_items
        hull[robot_position[0]][robot_position[1]] = {(-1, 0): '^' , (1, 0): 'v', (0, -1): '<', (0, 1): '>'
                                                      }[robot_orientation]
        pc.add_to_input_queue(0 if originally_at_robot == BLACK_PANEL else 1)
        # print('\n'.join(''.join(e) for e in hull))
        # input('\n')
    return hull, len(changed_items)  # lower than 10021


def main():
    with useful_functions.suppress_print():
        pt1 = draw(150, 175, 'black')[1]  # these are very delicate boundaries
    if type(pt1) != int:
        pt1 = len(pt1)
        print(f"**ERR ON PART 1**  (only gotten {pt1} positions)")
    else:
        print("pt1:", pt1)
    with useful_functions.suppress_print():
        pt2 = draw(100, 20, 'white')[0]  # these are very delicate boundaries
    if True:
        pt2 = '\n'.join([''.join(item) for item in pt2 if len(set(item)) != 1])
        while '........' in pt2:
            pt2 = pt2.replace('........', '.')
        pt2 = '\n' + pt2 + '\n'
        while '\n.' in pt2 or '.\n' in pt2:
            pt2 = pt2.replace('\n.', '\n').replace('.\n', '\n')
        pt2 = pt2.replace('#', '##').replace('.', '  ').strip()
    print("pt2:", pt2, sep='\n')


if __name__ == '__main__':
    main()
