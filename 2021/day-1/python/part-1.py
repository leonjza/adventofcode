c = p = t = 0	# (c)urrent val, (p)revious val, (t)otal vals

with open('../input', 'r') as f:
	for line in f.readlines():
		c = int(line.rstrip())

		if p == 0:	# first reading
			p = c
			continue

		t += 1 if c > p else 0
		p = c

print(f'total => {t}')
