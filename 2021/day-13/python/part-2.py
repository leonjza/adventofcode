with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

grid_x_y = lambda gr: (max([x for x, _ in gr]) + 1, max([y for _, y in gr]) + 1)


def get_instructions() -> list:
	""" parse input """

	d = []
	f = []

	for line in lines:
		if line == '': continue

		if line.startswith('fold'):
			axis, amt = line.split(' ')[2].split('=')
			f.append((axis, int(amt)))
			continue

		x, y = line.split(',')
		d.append((int(x), int(y)))

	return d, f


def pg(gr: set):
	""" pretty print the grid """

	max_x, max_y = grid_x_y(gr)
	c = [['.'] * (max_x) for _ in range(max_y)]

	for cord in gr:
		x, y = cord
		c[y][x] = '#'

	print('-- grid')
	[print(''.join(l)) for l in c]
	print('--')


def fold_grid(gr: set, axis: str, where: int) -> list:
	""" fold the paper on 'axis' on 'where' """

	assert axis in ['x', 'y']

	max_x, max_y = grid_x_y(gr)
	ng = set()

	for x, y in gr:
		if axis == 'x': # left
			if x < where: ng.add((x, y))
			else: ng.add((2 * where - x, y))

		if axis == 'y': # up
			if y < where: ng.add((x, y))
			else: ng.add((x, 2 * where - y))

	return ng


def main():
	""" Solve """

	dots, folds = get_instructions()
	g = set(dots)

	for fold in folds: g = fold_grid(g, *fold)

	pg(g)


if __name__ == '__main__':
	main()	
