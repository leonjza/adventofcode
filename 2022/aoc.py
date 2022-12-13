import builtins
import sys
from builtins import print
from pathlib import Path
from pprint import pprint
from typing import List, Tuple, Callable

from rich import print as rprint


def dump(*stuff, plain: bool = False):
    """
        A wrapper to dump stuff.

        :param plain:
        :param stuff:
        :return:
    """

    for thing in stuff:
        if plain:
            pprint(thing)
        else:
            rprint(thing)


def parse(p: str, sample: bool = False, process: Callable[[str], str] = None) -> List[str]:
    """
        Returns well formatted data for input.txt
        p is typically __file__ from the caller.

        setting the sample flag searches for sample input instead
        process can be a lambda from the caller

        :param process:
        :param sample:
        :param p:
        :return:
    """

    for file_name in ['in', 'input', 'input.txt'] \
            if not sample else ['sam', 'sample', 'sample.txt']:

        target = Path(p).parent / file_name

        if not target.exists():
            continue

        with open(target, 'r') as f:
            return [process(li) if process is not None else li.strip() for li in f.readlines()]

    raise Exception(f'Could not read {"sample" if sample else "input"} data')


def digit_grid(source: list) -> Tuple[List[list[int]], int, int]:
    """
        Parses line input to produce a nested array of digits.

        Returns the grid, total rows and total columns.

        :param source:
        :return:
    """

    grid = [[int(d) for d in line] for line in source]

    return grid, len(grid), len(grid[0])


def patch_print():
    """
        Monkey patch print to stfu.

        :return:
    """

    def stfu(*args, **kwargs):
        pass

    builtins.print = stfu


def prepare_day(day: str):
    """
        Prepares a stubbed directory for a new challenge day.

        :param day:
        :return:
    """

    day_path = Path(day)
    entry = day_path / "__main__.py"
    sample = day_path / "sample.txt"

    if day_path.exists():
        print(f' e| path {day_path} already exists')
        sys.exit(1)

    print(f' i| creating {day_path}/')
    day_path.mkdir(exist_ok=False)
    print(f' i| creating entrypoint {entry}')
    entry.touch()
    print(f' i| creating empty {sample}')
    sample.touch()

    print(f' i| writing main stub code')
    with open(entry, 'w') as f:
        f.write(f"""import aoc

lines = aoc.parse(__file__, sample=True)


def part1():
    pass


def part2():
    pass


if __name__ == '__main__':
    print('running {day}')
""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python -m aoc <day>')
        sys.exit(1)

    prepare_day(sys.argv[1])
