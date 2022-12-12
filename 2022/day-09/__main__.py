import aoc

lines = aoc.parse(__file__, sample=False)

# [('D', 1), ('U', 1)]
instructions = [(x, int(y)) for (x, y) in [line.split(' ') for line in lines]]


def sign(s: int) -> int:
    """
        Figure out if s is + or -

        :param s:
        :return:
    """

    return -1 if s < 0 else 1


def direction(v: tuple) -> tuple:
    """
        Parse a file instruction to a move. We expect a parsed
        instructions in a tuple ('D', 4)

        :param v:
        :return:
    """

    i, d = v
    r, c = 0, 0

    match i:
        case 'U':
            r = +d
        case 'D':
            r = -d
        case 'L':
            c = -d
        case 'R':
            c = +d

    print(f'=' * 100)
    print(f' i| instruction direction={i}, distance={d}')

    return r, c


def part1():
    """
        Solver for part 1

        :return:
    """

    H = [(0, 0)]
    T = [(0, 0)]

    def tail():
        """
            Process the tail if necessary. This is typically when the distance is > 1
            from the head.

            :return:
        """

        def move_tail():
            """
                Move a tail along. We're assuming the head will always, at most
                be 1 distance away.

                :return:
            """

            print(f' ! searching for new tail location starting from H{H[-1][0], H[-1][1]}, T{T[-1][0], T[-1][1]}')

            # current distance
            d = max(abs(H[-1][0] - T[-1][0]), abs(H[-1][1] - T[-1][1]))
            # x,y diff value
            rd, cd = H[-1][0] - T[-1][0], H[-1][1] - T[-1][1]
            # x,y (+/-) to be used when moving
            rds, cds = sign(rd), sign(cd)

            print(f' ! -> distance={d}, row-diff={rd}, col-diff={cd}, row-sign={rds}, col-sign={cds}')

            if rd == 0:
                print(f' ! -> row-diff is zero so moving col')
                t = (T[-1][0], T[-1][1] + (cds * 1))
            elif cd == 0:
                print(f' ! -> col-diff is zero so moving row')
                t = (T[-1][0] + (rds * 1), T[-1][1])
            else:
                print(f' ! -> neither row nor col is zero, assuming diag move')
                t = (T[-1][0] + (rds * 1), T[-1][1] + (cds * 1))

            td = max(abs(t[0] - T[-1][0]), abs(t[1] - T[-1][1]))
            nd = max(abs(H[-1][0] - t[0]), abs(H[-1][1] - t[1]))
            print(f' ! -> moving from T{T[-1]} to T{t} (which has distance {td} from old, new distance from head {nd})')
            assert td == 1 and nd == 1
            T.append(t)

        # manhattan distance
        distance = max(abs(H[-1][0] - T[-1][0]), abs(H[-1][1] - T[-1][1]))
        print(f' i| (a) distance from tail T{T[-1]} to head H{H[-1]} is now {distance}')

        if distance > 1:
            move_tail()

        distance = max(abs(H[-1][0] - T[-1][0]), abs(H[-1][1] - T[-1][1]))
        print(f' i| (b) distance from tail T{T[-1]} to head H{H[-1]} is now {distance}')

    def head(where: tuple):
        t_row, t_col = where

        print(f' i| moving H from={H[-1]}, to={where} | T{T[-1]}')

        # moves slide a single axis only

        if t_col == 0:
            print(f' i| moving *rows* by iterating {abs(t_row)}, sign={sign(t_row)}')
            for k in range(abs(t_row)):
                t = H[-1][0] + (1 * sign(t_row)), H[-1][1]
                print(f' i| moving H to {t}')
                H.append(t)
                # H.append((k, h_col))
                tail()

        else:
            print(f' i| moving *columns* by iterating {abs(t_col)}, sign={sign(t_col)}')
            for k in range(abs(t_col)):
                t = H[-1][0], H[-1][1] + (1 * sign(t_col))
                print(f' i| moving H to {t}')
                H.append(t)
                # H.append((h_row, k))
                tail()

    # work
    [head(direction(i)) for i in instructions]
    print(f'part1 => {len(set(T))}')

    # import matplotlib.pyplot as plt
    # hx, hy = zip(*H)
    # tx, ty = zip(*T)
    # plt.plot(hx, hy, color='red')
    # plt.plot(tx, ty, color='blue')
    # plt.show()


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
