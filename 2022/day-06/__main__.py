import aoc

lines = aoc.parse(__file__, sample=False)


def start_of_marker(target: str, c: int):
    # broken_brain.exe
    # return [target[x] for x in range(len(target)) if len(set(target[-x:])) <= c]
    m = []
    for idx in range(len(target)):
        m.append(target[idx])
        if len(set(m[-c:])) == c:
            return len(m)


def part1():
    for line in lines:
        print(f'part1 => {start_of_marker(line, 4)}')


def part2():
    for line in lines:
        print(f'part2 => {start_of_marker(line, 14)}')


if __name__ == '__main__':
    part1()
    part2()
