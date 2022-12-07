import copy

import aoc

lines = aoc.parse(__file__, sample=False)

# sample
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
sample_containers = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
}

# input
#             [C]         [N] [R]
# [J] [T]     [H]         [P] [L]
# [F] [S] [T] [B]         [M] [D]
# [C] [L] [J] [Z] [S]     [L] [B]
# [N] [Q] [G] [J] [J]     [F] [F] [R]
# [D] [V] [B] [L] [B] [Q] [D] [M] [T]
# [B] [Z] [Z] [T] [V] [S] [V] [S] [D]
# [W] [P] [P] [D] [G] [P] [B] [P] [V]
#  1   2   3   4   5   6   7   8   9

input_containers = {
    1: ['W', 'B', 'D', 'N', 'C', 'F', 'J'],
    2: ['P', 'Z', 'V', 'Q', 'L', 'S', 'T'],
    3: ['P', 'Z', 'B', 'G', 'J', 'T'],
    4: ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C'],
    5: ['G', 'V', 'B', 'J', 'S'],
    6: ['P', 'S', 'Q'],
    7: ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N'],
    8: ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R'],
    9: ['V', 'D', 'T', 'R'],
}


def part1():
    cn = copy.deepcopy(input_containers)

    def move(count: int, frm: int, to: int) -> None:
        for x in range(count):
            cn[to].append(cn[frm].pop())

    for line in lines:
        # move 1 from 2 to 1
        _, c, _, f, _, t = line.split(' ')
        move(int(c), int(f), int(t))

    print(f"part 1 => {''.join([s[-1:][0] for _, s in cn.items()])}")


def part2():
    cn = copy.deepcopy(input_containers)

    def move(count: int, frm: int, to: int) -> None:
        # get the value and replace it with the
        # "stack" removed
        v = cn[frm][-count:]
        cn[frm] = cn[frm][:-count]

        cn[to] = cn[to] + v

    for line in lines:
        # move 1 from 2 to 1
        _, c, _, f, _, t = line.split(' ')
        move(int(c), int(f), int(t))

    print(f"part 2 => {''.join([s[-1:][0] for _, s in cn.items()])}")


if __name__ == '__main__':
    part1()
    part2()
