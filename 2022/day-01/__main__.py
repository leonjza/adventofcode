import aoc

lines = aoc.parse(__file__)

elves = [0]
i = 0

for line in lines:
    if line == '':
        i += 1
        elves.append(0)
        continue

    elves[i] = elves[i] + int(line)

# part 1
print(max(elves))

# part 2
elves.sort(reverse=True)
print(sum(elves[:3]))
