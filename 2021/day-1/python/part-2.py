c = p = t = 0	# (c)urrent val, (p)revious val, (t)otal vals
windows = []
window_size = 3

with open('../input', 'r') as f:
	lines = [int(l.rstrip()) for l in f.readlines()]

# <3 https://stackoverflow.com/a/6822773
for l in range(len(lines) - window_size + 1):
	windows.append(sum(lines[l: l + window_size]))

for c in windows:
	if p == 0:	# first reading
		p = c
		continue

	t += 1 if c > p else 0
	p = c

print(f'total => {t}')
