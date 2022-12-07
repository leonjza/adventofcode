import aoc

lines = aoc.parse(__file__, sample=False)


def part1():
    a = 0
    for line in lines:
        # parse 1-1,2-2 to tuples
        p = [x.split('-') for x in line.split(',')]
        p1, p2 = (int(p[0][0]), int(p[0][1])), \
            (int(p[1][0]), int(p[1][1]))

        # create lists of the ranges
        p1, p2 = [x for x in range(p1[0], p1[1] + 1)], \
            [x for x in range(p2[0], p2[1] + 1)]

        if all(x in p1 for x in p2) or all(x in p2 for x in p1):
            a += 1

    print(f'part 1 => {a}')


def part2():
    a = 0
    for line in lines:
        # parse 1-1,2-2 to tuples
        p = [x.split('-') for x in line.split(',')]
        p1, p2 = (int(p[0][0]), int(p[0][1])), \
            (int(p[1][0]), int(p[1][1]))

        # create lists of the ranges
        p1, p2 = [x for x in range(p1[0], p1[1] + 1)], \
            [x for x in range(p2[0], p2[1] + 1)]

        if any(x in p1 for x in p2) or any(x in p2 for x in p1):
            a += 1

    print(f'part 2 => {a}')


if __name__ == '__main__':
    part1()
    part2()
