import string

import aoc

lines = aoc.parse(__file__, sample=False)
# use as the scoring mechanism
prio = '_' + string.ascii_lowercase + string.ascii_uppercase


def part1():
    p = []
    for line in lines:
        half = int(len(line) / 2)
        p1, p2 = line[:half], line[half:]
        c = set(p1).intersection(set(p2))
        # get the score by finding the index if the intersection
        # of the previous two sets
        p.append(prio.index(c.pop()))

    print(f'part 1 => {sum(p)}')


def part2():
    p = []
    for i in range(0, len(lines), 3):
        g1, g2, g3 = lines[i:i + 3]
        c = set(g1).intersection(g2, g3)
        p.append(prio.index(c.pop()))

    print(f'part 2=> {sum(p)}')


if __name__ == '__main__':
    part1()
    part2()
