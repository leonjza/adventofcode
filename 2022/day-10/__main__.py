import queue
from queue import Queue
from typing import Generator, Any

import aoc

lines = aoc.parse(__file__, sample=False, process=lambda x: x.split(' '))


class CPU(object):
    """
        The CPU
    """

    q: Queue[tuple[str, int, int]]

    cycles: int
    X: int
    current_instruction: tuple[str, int, int]

    # part 1
    breakpoints: list[int]
    breakpoint_values: list[Any]

    # part 2
    pixels: list[list[str]]

    def __init__(self):
        self.q = queue.Queue()

        self.X = 1
        self.cycles = 0
        self.current_instruction = ('start', 0, 0)
        self.breakpoints = []
        self.breakpoint_values = []

        # fill the screen with .'s in a 40 x 6 grid
        self.pixels = [[' '] * 40 for _ in range(6)]

    def idle(self):
        """
            Check if the CPU is idle (no instructions left)

            :return:
        """

        return self.q.empty()

    def _get_ins(self, pop: bool = False):
        """
            Gets the instruction to work on.

            :return:
        """

        if pop:  # force fetching a new instruction
            self.current_instruction = self.q.get()

        # if the CPU hasn't started yet, get the first inst
        elif self.current_instruction[0] == 'start':
            self.current_instruction = self.q.get()

        return self.current_instruction

    def _set_ins(self, i: tuple[str, int, int]):
        """
            Sets the current instruction.

            :param i:
            :return:
        """

        self.current_instruction = i

    def set_breakpoint(self, cycle: int | list[int]):
        """
            Set a CPU cycle based breakpoint.

            :param cycle:
            :return:
        """

        if isinstance(cycle, list):
            for c in cycle:
                self.breakpoints.append(c)
            return

        self.breakpoints.append(cycle)

    def process_breakpoint(self):
        """
            Process the "breakpoints" for part 1

            :return:
        """

        if self.cycles in self.breakpoints:
            self.breakpoint_values.append(self.X)

    def process_crt(self):
        """
            Process the CRT screen drawing for part2

            :return:
        """

        # based on the CPU cycle, get the row/col value
        row, col = self.cycles // 40, (self.cycles % 40) - 1  # 40 pixels per row

        # if the X register (which is 3 pixels wide) intersects with
        # the cycle (relative to the row/col), write to it
        if col in [self.X - 1, self.X, self.X + 1]:
            self.pixels[row][col] = '▓'

    def tick(self):
        """
            Process instructions, keeping an instruction cost in mind.

            :return:
        """

        i, v, c = self._get_ins()

        c -= 1
        self.cycles += 1

        self.process_breakpoint()
        self.process_crt()

        # only action instructions when the cost is zero
        if c != 0:
            self._set_ins((i, v, c))
            return

        # if c is 0, the tick cost has passed, and we can execute the instruction

        if i == 'addx':
            self.X += v

        if i == 'noop':
            pass
        if i == 'stop':
            return

        # set the next instruction
        if not self.idle():
            self._get_ins(pop=True)

    def push(self, i: tuple[str, int, int]):
        self.q.put(i)


def parse_instructions() -> Generator:
    """
        Parse CPU instructions.

        Returns instruction, count, cost

        :return:
    """

    for line in lines:
        match line:
            case ['noop\n']:
                yield 'noop', 0, 1
            case ['addx', v]:
                yield 'addx', int(v), 2

    # add a stop instruction to lazily fix the CPU's off by one :P
    yield 'stop', 0, 0


def part1():
    """
        Solve part 1

        :return:
    """

    bps = [20, 60, 100, 140, 180, 220]

    cpu = CPU()
    cpu.set_breakpoint(bps)

    for ins in parse_instructions():
        cpu.push(ins)

    while not cpu.idle():
        cpu.tick()

    print(f'part1 => {sum([x * y for x, y in zip(bps, cpu.breakpoint_values)])}')


def part2():
    """
        Solve part 2

        :return:
    """

    cpu = CPU()

    for ins in parse_instructions():
        cpu.push(ins)

    while not cpu.idle():
        cpu.tick()

    print('part2 =>')
    for row in cpu.pixels:
        print(''.join(row))


if __name__ == '__main__':
    part1()
    part2()
