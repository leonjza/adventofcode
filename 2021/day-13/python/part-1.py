from pprint import pprint
import sys

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]


def get_instructions() -> tuple:
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


dots, folds = get_instructions()
max_x, max_y = max([x for x, _ in dots]) + 1, max([y for _, y in dots]) + 1
pg = lambda gr: [print(''.join(l)) for l in gr]

def pl(l: list) -> str:
	""" print a condensed line """

	v = ""
	cnt = 0
	for c in l:
		if c == ".": cnt+=1
		else:
			v += str(cnt) if cnt > 0 else ''
			v += c
			cnt = 0

	return v + (str(cnt) if cnt > 0 else '') + (' len => ' + str(len(l)))


def plot_dots() -> None:
	""" parse the original state """

	g = [['.'] * (max_x) for _ in range(max_y)]

	# populate
	for cord in dots:
		x, y = cord
		g[y][x] = '#'

	return g


def fold_grid(gr: list, axis: str, where: int) -> list:
	""" fold the paper on 'axis' on 'where' """

	direction = None
	if axis == 'y': direction = 'up'
	if axis == 'x': direction = 'left'
	assert direction is not None

	print(f' * folding on {axis} {direction} at {where}')

	g = None

	if direction == 'up':
		g = [l for l in gr[:where]]
		rem = [l for l in gr[where:][::-1]]

		for i, (a, b) in enumerate(zip(g, rem)):
			g[i] = [('#' if (ca == '#' or cb == '#') else '.') for ca, cb in zip(a, b)]

	if direction == 'left':
		g = [l[:where] for l in gr]
		rem = [l[where+1:][::-1] for l in gr]

		for i, (a, b) in enumerate(zip(g, rem)):
			if (set(a) == set('.')) and (set(b) == set('.')): continue

			cp = [('#' if (ca == '#' or cb == '#') else '.') for ca, cb in zip(a, b)]

			print('----- VALUE DUMP -----')
			print(f'gr[{i}]  > {"".join(gr[i])}')
			print(f'gr[{i}]  | {pl(gr[i])}')
			print(f'a      > {"".join(a)}')
			print(f'a      | {pl(a)}')
			print(f'b      > {"".join(b)}')
			print(f'b      | {pl(b)}')
			print(f'a & b  > {"".join(cp)}')
			print(f'a & b  | {pl(cp)}')
			print('----- END   DUMP -----')

			g[i] = cp


	assert g is not None
	return g


def main():
	""" Solve """

	cow = lambda gx: sum(x.count('#') for x in gx)
	g = plot_dots()
	print(f' max x= {max_x}, max_y = {max_y}')

	for fold in folds:
		g = fold_grid(g, *fold)
		print(f' ! {cow(g)} "dots". x={len(g[0])},y={len(g)}')
		break
		# pg(g)

	# pg(g)
	print(f' there are {cow(g)} visible dots')


if __name__ == '__main__':
	main()	
