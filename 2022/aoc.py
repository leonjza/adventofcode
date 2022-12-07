import sys
from pathlib import Path
from typing import List


def parse(p: str, sample: bool = False) -> List[str]:
    """
        Returns well formatted data for input.txt
        p is typically __file__ from the caller.

        setting the sample flag searches for sample input instead

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
            return [li.strip() for li in f.readlines()]

    raise Exception(f'Could not read {"sample" if sample else "input"} data')


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
