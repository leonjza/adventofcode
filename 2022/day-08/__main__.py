import aoc

grid, max_rows, max_cols = aoc.digit_grid(aoc.parse(__file__, sample=False))


def is_visible(x, y) -> bool:
    """
        Check if a tree is visible from the edge.

        :param x:
        :param y:
        :return:
    """

    # edge cases, lol
    if (x == 0 or y == 0) or (x + 1 == max_cols or y + 1 == max_cols):
        return True

    me = grid[x][y]

    def scan(row, col, horizontal: bool = False):
        """
            Scan a line to check if there is a row visible from an edge

            :param row:
            :param col:
            :param horizontal:
            :return:
        """

        if horizontal:
            return all(c < me for c in [grid[row][col] for col in range(col, max_cols) if col != y]) or \
                all(c < me for c in [grid[row][col] for col in range(0, col) if col != y])

        return all(c < me for c in [grid[row][col] for row in range(row, max_rows) if row != x]) or \
            all(c < me for c in [grid[row][col] for row in range(0, row) if row != x])

    return scan(x, y, horizontal=True) or scan(x, y)


def scenic_score(x, y) -> int:
    """
        Calculate the scenic score of a tree based on viewing distance.

        :param x:
        :param y:
        :return:
    """

    me = grid[x][y]

    def scan(row, col):
        """
            Scan a line to check if there is a row visible from an edge

            :param row:
            :param col:
            :return:
        """

        def right(r, c):
            for idx in range(c, max_cols):
                if idx == y:
                    continue

                v = grid[r][idx]

                if v == me or v > me:
                    yield v
                    break
                if v < me:
                    yield v
                else:
                    break

        def left(r, c):
            for idx in reversed(range(0, c)):
                if idx == y:
                    continue

                v = grid[r][idx]

                if v == me or v > me:
                    yield v
                    break
                if v < me:
                    yield v
                else:
                    break

        def down(r, c):
            for idx in range(r, max_rows):
                if idx == x:
                    continue

                v = grid[idx][c]

                if v == me or v > me:
                    yield v
                    break
                if v < me:
                    yield v
                else:
                    break

        def up(r, c):
            for idx in reversed(range(0, r)):
                if idx == x:
                    continue

                v = grid[idx][c]

                if v == me or v > me:
                    yield v
                    break
                if v < me:
                    yield v
                else:
                    break

        # aoc.dump(me, [g for g in up(row, col)])

        u = [a for a in up(row, col)]
        d = [a for a in down(row, col)]
        l = [a for a in left(row, col)]
        r = [a for a in right(row, col)]

        score = len(u) * len(d) * len(l) * len(r)

        # aoc.dump(locals())

        return score

    return scan(x, y)


def part1():
    v = 0
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if is_visible(x, y):
                v += 1

    print(f'part1 -> {v}')


def part2():
    v = []
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            v.append(scenic_score(x, y))

    print(f'part2 => {max(v)}')


if __name__ == '__main__':
    part1()
    part2()
