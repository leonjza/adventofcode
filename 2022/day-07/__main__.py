import aoc

lines = aoc.parse(__file__, sample=False)

fs = {
    '/': {},
}

cwd = ['/']
totals = []


def get_fs_from_path(path: list):
    curr = fs

    for p in path:
        if p not in curr:
            raise Exception(f'invalid path {"".join(path)}')
        curr = curr[p]

    return curr


# parse what we have
for line in lines:
    match line.split(' '):
        case ['$', *cmd]:
            match cmd:
                case ['cd', dst]:
                    match dst:
                        case '..':
                            cwd.pop()
                        case '/':
                            cwd = ['/']
                        case _:
                            if dst not in (g := get_fs_from_path(cwd)):
                                g[dst] = {}
                            cwd.append(dst)
                case ['ls']:
                    pass
        case ['dir', _]:
            pass
        case [*file]:
            size, n = file
            get_fs_from_path(cwd)[n] = int(size)


def total_dirs(root: dict):
    total = 0
    for k, v in root.items():
        if isinstance(v, dict):
            total += total_dirs(v)
        else:
            total += v
    return total


def calculate_totals(root: dict):
    for k, v in root.items():
        if isinstance(v, dict):
            totals.append(total_dirs(v))
            calculate_totals(v)


calculate_totals(fs)


def part1():
    print(f'part1 => {sum([x for x in totals if x <= 100000])}')


def part2():
    need = 30000000 - (70000000 - total_dirs(fs))
    print(f'part2 => {min([x for x in totals if x >= need])}')


if __name__ == '__main__':
    part1()
    part2()
