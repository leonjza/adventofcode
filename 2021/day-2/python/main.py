h = d = 0	# (h)orizontal pos, (d)epth

with open('../input', 'r') as f:
	for line in f.readlines():
		di, amt = line.rstrip().split(" ")
		amt = int(amt)

		if di == "forward":
			h += amt

		if di == "down":
			d += amt
		
		if di == "up":
			d -= amt

print(f'total => {h * d}')
