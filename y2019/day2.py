import time

import useful_functions
from adventofcode.y2019.day7 import Intcode as IntcodeClass

puzzle_input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0"

def Intcode(program, full_return=False):
    if type(program) == str:
        program = [int(x.strip()) for x in program.split(',')]
    else:
        program = useful_functions.deepish_copy(program)
    index = 0
    while index+1 < len(program):
        instruction = program[index]
        
        if instruction == 1:
            program[program[index+3]] = program[program[index+1]] + program[program[index+2]]
            index += 4
        elif instruction == 2:
            program[program[index+3]] = program[program[index+1]] * program[program[index+2]]
            index += 4
        elif instruction == 99:
            index += 1
            break
        else:
            raise TypeError(f"unkown instruction {instruction}")
    return program if full_return else program[0]


def main():
    print("initialized")
    modified_puzzle_input = [int(x.strip()) for x in puzzle_input.split(',')]
    modified_puzzle_input[1], modified_puzzle_input[2] = 12, 2
    print("pt1:", Intcode(modified_puzzle_input))
    pc = IntcodeClass(modified_puzzle_input)
    print("pt1(v2):", pc.run_until_finished()[0])
    start_time = time.time()
    finished = False
    for i in range(100):
        for j in range(100):
            modified_puzzle_input[1], modified_puzzle_input[2] = i, j
            result = Intcode(modified_puzzle_input)
            if result == 19690720:
                print("pt2:", 100*i+j)
                finished = True
                break
        if finished:
            break
    

if __name__ == '__main__':
    main()
