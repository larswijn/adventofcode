import itertools
import time

import useful_functions


puzzle_input = "3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99"


class Intcode:
    def __init__(self, program, inputs=[], memory_size='auto'):
        '''
        init the program
        :param program: str (sep=',') or list (1D) to represent instructions, see https://adventofcode.com/2019/day/2
        :param inputs: list of inputs for program to use instead of user having to manually insert them at opcode 3
        :param memory_size: int or 'auto' for auto-extension; amount of 0 padding the program should have at the end
        '''
        if type(program) not in {str, list, tuple}:
            print(f"argument program cannot be of type '{type(program)}'")
        if type(inputs) not in {int, str, list}:
            print(f"argument inputs cannot be of type '{type(inputs)}'")
        if type(memory_size) not in {int, str}:
            print(f"argument memory_size cannot be of type '{type(inputs)}'")
        if type(memory_size) == str and memory_size[:4] != 'auto':
            print(f"argument memory_size cannot be a string other than 'auto'")
        elif type(memory_size) == int and memory_size < 0:
            print(f"argument memory_size cannot be lower than 0")

        if type(program) == str:
            program = [int(x.strip()) for x in program.strip().split(',')]
        elif type(program) != list:
            program = list(program)

        self._memory_size = memory_size if type(memory_size) == int else memory_size[:4]
        if type(memory_size) == int and memory_size > 0:
            program += [0 for _ in range(memory_size)]

        self._program = [*program]  # fast shallow copy

        if type(inputs) in {int, str}:
            inputs = [inputs]
        else:
            self._inputs = [*inputs]

        # the self._start_* values are used for self.reset()
        self._start_program = [*program]
        self._start_inputs = [*inputs]

        self.opcode_arg_count = {1: 3,  # +
                                 2: 3,  # *
                                 3: 1,  # input
                                 4: 1,  # output
                                 5: 2,  # set index to arg2 if arg1 != 0
                                 6: 2,  # set index to arg2 if arg1 == 0
                                 7: 3,  # <
                                 8: 3,  # ==
                                 9: 1,  # change relative_base
                                 99: -1  # end program
                                 }

        self._outputs = []
        self._index = 0
        self._relative_base = 0
        self._steps_taken = 0
        self.is_finished = False
        self._had_error = False


    def run_until_finished(self, allow_printing=False, **kwargs):
        '''
        runs self.take_step(**kwargs) until self.is_finished is True (should be done after opcode 99)
        :returns: the full program (with the memory slots)
        '''
        while not self.is_finished:
            output = self.take_step(allow_printing=allow_printing, **kwargs)
        return self._program


    def run_until_output(self, allow_printing=False, **kwargs):
        '''
        runs self.take_step(**kwargs) until output is returned by take_step (opcode 4)
        :returns: the first output that's found
        '''
        while True:
            output = self.take_step(allow_printing=allow_printing, **kwargs)
            if output is not None:
                return output


    def add_to_input_queue(self, *args):
        self._inputs.extend(args)


    def retrieve_output(self):
        """
        generator to get all not-printed output
        """
        yield from self._outputs


    def take_step(self, allow_printing=False):
        if self.is_finished:
            return 'finished'
        self._steps_taken += 1
        POSITION_MODE, IMMEDIATE_MODE, RELATIVE_MODE = 0, 1, 2
        opcode = int(str(self._program[self._index])[-2:])
        max_parameters = self.opcode_arg_count[opcode]
        instruction = str(self._program[self._index]).zfill(max_parameters+2)
        mode_parameters = {mode: int(instruction[max_parameters-mode])
                           for mode in range(1, max_parameters+1)}
        index_parameters = {key: self._program[self._index + key] if value == POSITION_MODE else
                                 self._index + key if value == IMMEDIATE_MODE else
                                 self._relative_base + self._program[self._index + key] if value == RELATIVE_MODE else
                                 'ERROR'
                            for key, value in mode_parameters.items()}
        if self._memory_size == 'auto' and index_parameters:
            amount_index_outside_boundary = max(index_parameters.values()) - len(self._program) + 1
            if amount_index_outside_boundary > 0:
                if False:  # DEBUG
                    print("there'll be a IndexError", file=useful_functions.bypass_suppress_print, end=': ')
                    print(f"{{max index: {max(index_parameters.values())}, len program: {len(self._program)}", end='')
                    print(f", difference: {amount_index_outside_boundary}}}")
                    print("adjusting...", end='')
                    print("...   IndexError should be avoided")
                self._program += [0 for _ in range(amount_index_outside_boundary)]
        if False:  # DEBUG
            self._opcode = opcode
            self._mode_parameters = mode_parameters
            self._index_parameters = index_parameters
            self._max_parameters = max_parameters

        if opcode == 1:
            self._program[index_parameters[3]] = self._program[index_parameters[1]] + self._program[index_parameters[2]]
            self._index += 4
        elif opcode == 2:
            self._program[index_parameters[3]] = self._program[index_parameters[1]] * self._program[index_parameters[2]]
            self._index += 4
        elif opcode == 3:
            if self._inputs:
                inputs = self._inputs.pop(0)
                if allow_printing:
                    print('3>', repr(inputs))
            else:
                print("3>", end='', file=useful_functions.bypass_suppress_print)
                inputs = input()
            if type(inputs) == int or inputs.isdigit():
                self._program[index_parameters[1]] = int(inputs)
            else:
                self._program[index_parameters[1]] = ord(inputs)
            self._index += 2
        elif opcode == 4:
            if allow_printing:
                print('4>', repr(self._program[index_parameters[1]]), f" (at position {index_parameters[1]})")
            else:
                self._outputs.append(self._program[index_parameters[1]])
            self._index += 2
            return self._program[index_parameters[1]]
        elif opcode == 5:
            if self._program[index_parameters[1]] != 0:
                self._index = self._program[index_parameters[2]]
            else:
                self._index += 3
        elif opcode == 6:
            if self._program[index_parameters[1]] == 0:
                self._index = self._program[index_parameters[2]]
            else:
                self._index += 3
        elif opcode == 7:
            self._program[index_parameters[3]] = int(self._program[index_parameters[1]]
                                                    < self._program[index_parameters[2]])
            self._index += 4
        elif opcode == 8:
            self._program[index_parameters[3]] = int(self._program[index_parameters[1]]
                                                    == self._program[index_parameters[2]])
            self._index += 4
        elif opcode == 9:
            self._relative_base += self._program[index_parameters[1]]
            self._index += 2
        elif opcode == 99:
            if allow_printing:
                print('99> finished')
            self._index += 1
            self.is_finished = True
            return 'finished'
        else:
            raise TypeError(f"unknown opcode '{opcode}'")


    def reset(self, **kwargs):
        '''reset the class to the original values, or replace with them with the passed values'''
        if 'program' not in kwargs:
            kwargs['program'] = self._start_program
            kwargs['memory_size'] = 'auto' if self._memory_size == 'auto' else 0
        elif 'memory_size' not in kwargs:
            kwargs['memory_size'] = self._memory_size
        if 'inputs' not in kwargs:
            kwargs['inputs'] = self._start_inputs
        self.__dict__ = Intcode(**kwargs).__dict__


    def copy(self):
        """deepcopy of self"""
        from copy import deepcopy
        return deepcopy(self)

    deepcopy = copy


def main():
    start_time = time.time()
    program = [int(x.strip()) for x in puzzle_input.strip().split(',')]
    print("day 7 initialized")
    max_thruster_strength = 0

    for phase_settings in itertools.permutations(range(5)):
        thruster_strength = 0
        for phase in phase_settings:
            amplifier = Intcode(program=program, inputs=[phase, thruster_strength])
            thruster_strength = amplifier.run_until_output()
        if thruster_strength > max_thruster_strength:
            max_thruster_strength = thruster_strength
    
    print('pt1:', max_thruster_strength)
    print(f" (time taken: {round(time.time()-start_time, 5)}sec)")

    max_thruster_strength = 0

    for phase_settings in itertools.permutations(range(5, 10)):
        thruster_strength = 0
        with useful_functions.suppress_print():
            amplifiers = [Intcode(program=program, inputs=[phase])
                          for phase in phase_settings]
            amplifiers[0].add_to_input_queue(0)
            while True:
                for index, pc in enumerate(amplifiers):
                    index_next_pc = (index+1) % len(amplifiers)
                    output = pc.run_until_output(allow_printing=False)
                    if output == 'finished':
                        break
                    elif index + 1 == len(amplifiers):
                        thruster_strength = output
                    amplifiers[index_next_pc].add_to_input_queue(output)
                if output == 'finished':
                    break
        if thruster_strength > max_thruster_strength:
            max_thruster_strength = thruster_strength

    print('pt2:', max_thruster_strength)
    print(f" (time taken: {round(time.time()-start_time, 5)}sec)")


def _test_intcode():
    tests = {
        # day 2, pt 1
        "1,0,0,0,99": {'finally': [2,0,0,0,99], 'inputs': [], 'outputs': []},  # opcode 1
        "2,3,0,3,99": {'finally': [2,3,0,6,99], 'inputs': [], 'outputs': []},  # opcode 2
        "2,4,4,5,99,0": {'finally': [2,4,4,5,99,9801], 'inputs': [], 'outputs': []},
        "1,1,1,4,99,5,6,0,99": {'finally': [30,1,1,4,2,5,6,0,99], 'inputs': [], 'outputs': []},

        # day 5 pt 1
        "1002,4,3,4,33": {'finally': [1002,4,3,4,99], 'inputs': [], 'outputs': []},  # positional/immediate mode
        # day 5 pt 2
        "3,9,8,9,10,9,4,9,99,-1,8": {'finally': [], 'inputs': [8], 'outputs': [1]},
        "3,9,8,9,10,9,4,9,99,-1,8": {'finally': [], 'inputs': [-5], 'outputs': [0]},
        "3,9,7,9,10,9,4,9,99,-1,8": {'finally': [], 'inputs': [10], 'outputs': [0]},
        "3,9,7,9,10,9,4,9,99,-1,8": {'finally': [], 'inputs': [6], 'outputs': [1]},
        "3,9,7,9,10,9,4,9,99,-1,8": {'finally': [], 'inputs': [-5], 'outputs': [1]},
        "3,3,1108,-1,8,3,4,3,99": {'finally': [], 'inputs': [8], 'outputs': [1]},
        "3,3,1108,-1,8,3,4,3,99": {'finally': [], 'inputs': [-5], 'outputs': [0]},
        "3,3,1107,-1,8,3,4,3,99": {'finally': [], 'inputs': [10], 'outputs': [0]},
        "3,3,1107,-1,8,3,4,3,99": {'finally': [], 'inputs': [6], 'outputs': [1]},
        "3,3,1107,-1,8,3,4,3,99": {'finally': [], 'inputs': [-5], 'outputs': [1]},
        "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9": {'finally': [], 'inputs': [0], 'outputs': [0]},
        "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9": {'finally': [], 'inputs': [4], 'outputs': [1]},
        "3,3,1105,-1,9,1101,0,0,12,4,12,99,1": {'finally': [], 'inputs': [0], 'outputs': [0]},
        "3,3,1105,-1,9,1101,0,0,12,4,12,99,1": {'finally': [], 'inputs': [-4], 'outputs': [1]},
        "3,3,1105,-1,9,1101,0,0,12,4,12,99,1": {'finally': [], 'inputs': [4], 'outputs': [1]},
        "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99":
            {'finally': [], 'inputs': [4], 'outputs': [999]},
        "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
        "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99":
            {'finally': [], 'inputs': [8], 'outputs': [1000]},
        "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
        "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99":
            {'finally': [], 'inputs': [12], 'outputs': [1001]},

        # day 9 pt 1
        "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99":
            {'finally': [], 'inputs': [12], 'outputs': [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]},
        "1102,34915192,34915192,7,4,7,99,0": {'finally': [], 'inputs': [], 'outputs': [1219070632396864]},
        "104,1125899906842624,99": {'finally': [], 'inputs': [], 'outputs': [1125899906842624]},
        }
    for index, (program, result) in enumerate(tests.items()):
        pc = Intcode(program=program, inputs=result['inputs'], memory_size=1024)
        print(f"test {str(index).rjust(3)}: ", end=' ')
        if result['outputs']:
            pc.reset()
            outs, out = [], None
            with useful_functions.suppress_print():
                while out != 'finished':
                    out = pc.run_until_output()
                    outs.append(out)
            outs = outs[:-1]
            if outs == result['outputs']:
                print("outputs asserted succesfully".ljust(30), end=' | ')
            else:
                return TypeError, program, result
        else:
            print("no outputs".ljust(30), end=' | ')
        if result['finally']:
            pc.reset()
            with useful_functions.suppress_print():
                final = pc.run_until_finished()
            final = final[:max([i+1 for i, e in enumerate(final) if e != 0])]  # remove memory_size
            if final == result['finally']:
                print("final program asserted succesfully".ljust(40))
            else:
                return TypeError, program, result
        else:
            print('no final program'.ljust(40))
    return True, 'succes', 'succes'

if __name__ == '__main__':
    main()
