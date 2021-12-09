
import useful_functions

puzzle_input = '''
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
'''.strip()

puzzle_input = '''
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
'''.strip()

puzzle_input = '''
<x=-19, y=-4, z=2>
<x=-9, y=8, z=-16>
<x=-4, y=5, z=-11>
<x=1, y=9, z=-13>
'''.strip()

puzzle_input = [[int(x.split('=')[1].strip('>')) for x in line.split(',')]
                 for line in puzzle_input.split('\n')]


def rotate(moons, velocities=None, steps=1, allow_printing=True):
    if velocities is None:
        velocities = [[0 for _ in range(len(moons[0]))] for _ in range(len(moons))]
    else:
        velocities = useful_functions.deepish_copy(velocities)
    moons = useful_functions.deepish_copy(moons)
    if allow_printing:
        print(moons, velocities, sep='\n', end='')

    for step in range(steps):
        if allow_printing:
            print(f"\nafter {step} steps:")
        for index, (moon, velocity) in enumerate(zip(moons, velocities)):
            if allow_printing:
                print(index, moon, velocity)
            for other_index, other_moon in enumerate(moons):
                if other_index == index:
                    continue
                velocity = [x+1 if other_moon[i] > moon[i] else x-1 if other_moon[i] < moon[i] else x
                            for i, x in enumerate(velocity)]
            velocities[index] = velocity
        moons = [[x + velocity[i] for i, x in enumerate(moon)]
                 for velocity, moon in zip(velocities, moons)]

    return moons, velocities


def calc_energy(moons, velocities):
    moons = [sum(abs(x) for x in a)
             for a in moons]
    velocities = [sum(abs(x) for x in a)
             for a in velocities]
    return sum(x*y
               for x, y in zip(moons, velocities))


def find_repeating_state(moons, allow_printing=False):
    moons = useful_functions.deepish_copy(moons)
    velocities = [[0 for _ in range(len(moons[0]))] for _ in range(len(moons))]
    amount_of_rotations = 0
    if len(moons[0]) == 1:
        m, v = useful_functions.deepish_copy(moons), useful_functions.deepish_copy(velocities)
        while True:
            m, v = rotate(m, v, steps=1, allow_printing=allow_printing)
            amount_of_rotations += 1
            if v == velocities and m == moons:
                return amount_of_rotations
    else:
        # moons with x, y, z coords
        moon_coords = [[[coord[i], ] for coord in moons] for i in range(len(moons[0]))]
        repetition_rates = []
        for coord in moon_coords:
            repetition_rates.append(find_repeating_state(coord, allow_printing=allow_printing-1>0))
        return useful_functions.lcm(*repetition_rates)


def main():
    steps = 1000
    orig_moons = useful_functions.deepish_copy(puzzle_input)
    moons, velocities = rotate(orig_moons, steps=steps, allow_printing=False)
    print("using",
          '!!!TEST!!!' if puzzle_input != [[-19, -4, 2], [-9, 8, -16], [-4, 5, -11], [1, 9, -13]] else 'original',
          "puzzle input", end=' | ')
    print(f"performed {steps} steps", f" (not the required steps!)" if steps != 1000 else '')
    total_energy = calc_energy(moons, velocities)
    print("Sum of total energy (pt1):", total_energy)
    print("... Calculating pt2 ...")
    moon_coords = [[[coord[i], ] for coord in orig_moons] for i in range(len(orig_moons[0]))]
    repetition_rates = []
    print(" [█   ]")
    for i, coord in enumerate(moon_coords, 2):
        repetition_rates.append(find_repeating_state(coord, allow_printing=False))
        print(" [", ('█'*i).ljust(4), ']', sep='')
    repeating_state = useful_functions.lcm(*repetition_rates)
    print("pt2:", repeating_state)


if __name__ == '__main__':
    main()