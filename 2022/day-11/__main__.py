import math
from copy import deepcopy

import aoc

lines = aoc.parse(__file__, sample=False)

# children
M = {}


def parse():
    """
        Parse the input instructions and save to M

        :return:
    """

    cm = 0

    for line in lines:
        match line.split(' '):
            case ['Monkey', n]:
                cm = int(n.replace(":", ""))
                M[cm] = {'inspected': 0}

            case ['Starting', 'items:', *items]:
                M[cm]['items'] = [int(x.replace(',', '')) for x in items]

            case ['Operation:', *formula]:
                M[cm]['operation'] = formula[-2:]

            case ['Test:', *test]:
                M[cm]['test'] = int(test[-1])

            case ['If', 'true:', *where]:
                M[cm]['true'] = int(where[-1])

            case ['If', 'false:', *where]:
                M[cm]['false'] = int(where[-1])

            case ['']:
                pass

            case _:
                raise Exception(f'unmatched line: {line}')


def eval_math(ops: list[str]) -> int:
    """
        Evaluate a mathematical expression passed as a list
        if strings using eval() :>

        :param ops:
        :return:
    """

    # aoc.dump(locals())

    s, o, e = ops
    if e == 'old':
        e = s

    return eval(' '.join([s, o, e]))


def part1():
    """
        Solve part 1

        :return:
    """

    monkeys = deepcopy(M)

    for _ in range(20):
        for idx, monkey in monkeys.items():
            for item in list(monkey['items']):  # use list() to create a copy
                monkey['inspected'] += 1
                worry = eval_math([str(item)] + monkey["operation"])
                worry = worry // 3

                monkey['items'].remove(item)
                w = monkey['true'] if (worry % monkey['test'] == 0) else monkey['false']
                monkeys[w]['items'].append(worry)

    most_inspected = list(dict(sorted(monkeys.items(), key=lambda i: i[1]["inspected"])).items())[-2:]
    inspected = [x['inspected'] for _, x in most_inspected]

    a, b = inspected
    print(f'part1 => {a * b}')


def part2():
    """
        Solve part 2

        :return:
    """

    monkeys = deepcopy(M)

    # this mod thing totally came from reddit. mostly thanks to this explanation
    # answer: https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/izv7hpx/
    mod = math.prod([m['test'] for _, m in monkeys.items()])

    for _ in range(10000):
        for idx, monkey in monkeys.items():
            for item in list(monkey['items']):  # use list() to create a copy
                monkey['inspected'] += 1
                worry = eval_math([str(item)] + monkey["operation"])
                worry = worry % mod

                monkey['items'].remove(item)
                w = monkey['true'] if (worry % monkey['test'] == 0) else monkey['false']
                monkeys[w]['items'].append(worry)

    most_inspected = list(dict(sorted(monkeys.items(), key=lambda i: i[1]["inspected"])).items())[-2:]
    inspected = [x['inspected'] for _, x in most_inspected]

    # aoc.dump(locals())

    a, b = inspected
    print(f'part2 => {a * b}')


if __name__ == '__main__':
    parse()

    part1()
    part2()
