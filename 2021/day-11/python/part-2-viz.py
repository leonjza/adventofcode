import curses
import time

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]


grid = [[int(x) for x in l] for l in lines]
flashes = 0
g_max_x = len(grid[0])
g_max_y = len(grid)

# curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)

# clear the canvas
stdscr.clear()
stdscr.refresh()

# get a color palette
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_GREEN, -1)
curses.init_pair(2, curses.COLOR_YELLOW, -1)


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


def everyone_flashing() -> bool:
	""" check if everyone flashed """

	return all([(True if grid[x][y] == 0 else False) for x, y in grid_loop()])


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

	x, y = coords

	if grid[y][x] <= 9: return False

	# its a flash!
	grid[y][x] = 0

	for sx, sy in surround(*coords):
		if grid[sy][sx] != 0:
			print_g()
			grid[sy][sx] += 1

	return True


def print_g() -> None:
	""" pretty print the grid, highligting 0's """

	stdscr.clear()

	for i, b in enumerate(grid):
		stdscr.addstr(i+1, 1, '')
		for c in b:
			if c == 0:
				stdscr.addstr('*'.ljust(2), curses.color_pair(1))
			elif c == 10:
				stdscr.addstr('*'.ljust(2), curses.color_pair(2))
			else:
				stdscr.addstr('.'.ljust(2))
		stdscr.addstr(i+2, 1, '')

	time.sleep(0.005)
	stdscr.refresh()


def main():
	""" Solve """

	print_g()
	time.sleep(0.1)

	for i in range(1, 1000+1):
		if everyone_flashing(): 
			print_g()
			return

		step()

		while should_flash():
			for x, y in grid_loop(): flash((x, y))


if __name__ == '__main__':
	main()	
