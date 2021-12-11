from pprint import pprint
import sys

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]


grid = [[int(x) for x in l] for l in lines]
flashes = 0
g_max_x = len(grid[0])
g_max_y = len(grid)


def grid_loop():
	""" generator to loop the grid """

	for y in range(0, g_max_y):
		for x in range(0, g_max_y):
			yield x, y


def step() -> None:
	""" steps the grid by one in each position """

	for x, y in grid_loop(): grid[y][x] += 1


def should_flash() -> bool:
	""" check if theres anything to flash """

	for x, y in grid_loop():
		if grid[y][x] > 9: return True
		
	return False


def bounds(coord: tuple) -> bool:
	""" bound check an x,y tuple """

	x, y = coord
	return 0 <= x < g_max_x and 0 <= y < g_max_y


def surround(x: int, y: int):
	""" return a surrounding area of coords """

	# y
	# y  p
	# y
	#  x x x

	up    = (x, y + 1)
	down  = (x, y - 1)
	left  = (x - 1, y)
	right = (x + 1, y)

	upleft    = (x - 1, y + 1)
	upright   = (x + 1, y + 1)
	downleft  = (x - 1, y - 1)
	downright = (x + 1, y - 1)

	return [x for x in [
			up if bounds(up) else None,
			down if bounds(down) else None,
			left if bounds(left) else None,
			right if bounds(right) else None,
			upleft if bounds(upleft) else None,
			upright if bounds(upright) else None,
			downleft if bounds(downleft) else None,
			downright if bounds(downright) else None
		] if x	# filter out out of bounds
	]


def flash(coords: tuple) -> bool:
	""" 'flash' a x,y if vals > 9 """

	global flashes	# eww but whatever

	x, y = coords

	if grid[y][x] <= 9: return False

	# its a flash!
	grid[y][x] = 0
	flashes += 1

	for sx, sy in surround(*coords):
		if grid[sy][sx] != 0: grid[sy][sx] += 1

	return True


def print_g() -> None:
	""" pretty print the grid, highligting 0's """

	for x, y in grid_loop():
		v = grid[y][x]
		if v == 0: v = f'\033[91m{v}\033[0m'
		print(v, end='' if x < g_max_x - 1 else '\n')


def main():
	""" Solve """

	for i in range(1, 100+1):
		step()

		while should_flash():
			for x, y in grid_loop(): flash((x, y))

	print(f' # of flashes => {flashes}')


if __name__ == '__main__':
	main()	
