with open('../input', 'r') as f:
	l = f.read()
	crabs = [int(x.strip()) for x in l.split(',')]

max_h = max(crabs)
min_h = min(crabs)


def least_fuel() -> tuple:
	"""
		Loop max_h and count the fuel cost for everyone moving that much
	"""

	m = float('inf')

	for r in range(min_h + 1, max_h):
		f = sum([abs(v - r) for v in crabs])
		if f < m: m = f

	return m


def main():
	"""
		Solve
	"""

	shortest = least_fuel()
	print(f'Shortest path will cost {shortest}')


if __name__ == '__main__':
	main()	
