h = d = a= 0	# (h)orizontal pos, (d)epth, (a)im

with open('../input', 'r') as f:
	for line in f.readlines():
		di, amt = line.rstrip().split(" ")
		amt = int(amt)

		if di == "forward":
			h += amt
			d += (a * amt)

		if di == "down":
			a += amt
		
		if di == "up":
			a -= amt

print(f'total => {h * d}')
