with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

grid = [[x for x in l] for l in lines]
g_max_x = len(grid[0])
g_max_y = len(grid)

print(f' max x = {g_max_x}, max y = {g_max_y}')


def bounds(coord: tuple) -> bool:
	""" bound check an x,y tuple """

	x, y = coord
	return 0 <= x < g_max_x and 0 <= y < g_max_y

def surround(x: int, y: int):
	""" return a surrounding area of coords """

	up = (x, y + 1)
	down = (x, y - 1)
	left = (x - 1, y)
	right = (x + 1, y)

	s = [x for x in [
			up if bounds(up) else None,
			down if bounds(down) else None,
			left if bounds(left) else None,
			right if bounds(right) else None,
		] if x	# filter out out of bounds
	]

	# print(f'surrounds => {s}')
	return s


def low_points() -> int:
	""" Find values that are the lowest in a surrounding grid """

	ret = []

	for xi in range(0, g_max_x):
		# print(f' ** xi = {xi}')
		for yi in range(0, g_max_y):
			if all([grid[yi][xi] < grid[sy][sx] for sx, sy in surround(xi, yi)]):
				ret.append(int(grid[yi][xi]) + 1)
				# print(f'lowest val => {grid[yi][xi]}')

	return ret

def main():
	"""
		Solve
	"""

	p = low_points()
	print(f'sum of lows = {sum(p)}')


if __name__ == '__main__':
	main()	
