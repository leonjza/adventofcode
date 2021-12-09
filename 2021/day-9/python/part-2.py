from functools import reduce

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

grid = [[int(x) for x in l] for l in lines]
g_max_x = len(grid[0])
g_max_y = len(grid)


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

	return [x for x in [
			up if bounds(up) else None,
			down if bounds(down) else None,
			left if bounds(left) else None,
			right if bounds(right) else None,
		] if x	# filter out out of bounds
	]


def low_points() -> int:
	""" Find values that are the lowest in a surrounding grid """

	ret = []

	for xi in range(0, g_max_x):
		for yi in range(0, g_max_y):
			if all([grid[yi][xi] < grid[sy][sx] for sx, sy in surround(xi, yi)]):
				ret.append((xi, yi))

	return ret


def basin(coords: tuple) -> int:
	""" determine a x, y (lows < 9 in an area) """

	# start
	x, y = coords

	# for that inplace magic! https://blog.finxter.com/python-inplace-or-operator-meaning/
	c = {coords}	

	for sx, sy in surround(x, y):
		# print(f'(check) grid[y][x], grid[sy][sx] = {grid[y][x]}, {grid[sy][sx]}')
		if grid[sy][sx] > grid[y][x] and grid[sy][sx] < 9:
			# print(f'(higer) x,y = {x},{y} | sx,sy = {sx},{sy}')
			c |= basin((sx, sy))	# :O <3<3
			# print(f'(result) basin so far => {c}')

	return c


def main():
	""" Solve """

	b_sizes = sorted([len(basin(b)) for b in low_points()])
	largest = b_sizes[-3:]
	total = reduce(lambda x, y: x * y, largest)	
	print(f' total for 3 largest basins: {total}')


if __name__ == '__main__':
	main()	
