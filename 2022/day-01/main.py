with open('input.txt') as f:
    lines = f.readlines()

elves = [0]
i = 0

for line in lines:
    line = line.strip()
    if line == '':
        i += 1
        elves.append(0)
        continue

    elves[i] = elves[i] + int(line)

# part 1
print(max(elves))
elves.sort(reverse=True)

# part 2
print(sum(elves[:3]))
