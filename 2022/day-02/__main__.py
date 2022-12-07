import aoc

lines = aoc.parse(__file__, sample=False)

# play, key, key, play score
ROCK = A = X = 1
PAPER = B = Y = 2
SCISSORS = C = Z = 3

LOSS, DRAW, WIN = 0, 3, 6

WIN_STATES = [
    (SCISSORS, ROCK),
    (PAPER, SCISSORS),
    (ROCK, PAPER)
]


def is_a_win(p1: int, p2: int) -> bool:
    for con in WIN_STATES:
        if con == (p1, p2):
            return True

    return False


def score(p1: int, p2: int) -> int:
    if p1 == p2:
        # print(f'draw so {p2} + {DRAW} = {p2 + DRAW}')
        return p2 + DRAW

    if is_a_win(p1, p2):
        # print(f'win  so {p2} + {WIN} = {p2 + WIN}')
        return p2 + WIN

    # print(f'loss so {p2} + {WIN} = {p2 + LOSS}')
    return p2 + LOSS


s = []
for line in lines:
    a, b = line.split(' ')
    a, b = eval(a), eval(b)
    s.append(score(a, b))

print(f'part1 => {sum(s)}')


def should_play(p1: int, want: str) -> int:
    # x = loss, y = draw, z = win
    if want == 'Y':  # draw
        return p1

    for x in [ROCK, PAPER, SCISSORS]:
        if not is_a_win(p1, x) and want == 'X':
            return x
        if is_a_win(p1, x) and want == 'Z':
            return x

    return ROCK


s = []
for line in lines:
    a, b = line.split(' ')
    a = eval(a)
    c = should_play(a, b)
    s.append(score(a, c))

print(f'part2 => {sum(s)}')
