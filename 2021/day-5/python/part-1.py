with open('../input', 'r') as f:
	lines = [l.rstrip().split('->') for l in f.readlines()]


def str_coord_2_tuple(coord: list) -> tuple:
	"""
		Just parse the input data into something better
	"""

	if len(coord) != 2:
		raise Exception(f'coord list was not len 2: {len(coord)}')

	xy1, xy2 = coord
	x1, y1 = xy1.strip().split(',')
	x2, y2 = xy2.strip().split(',')

	return (int(x1), int(y1)), (int(x2), int(y2))

# store events as parsed x,y tuples
hydro_vents = []
for xy in lines: hydro_vents.append(str_coord_2_tuple(xy))

# prepare grid with max x,y
max_cord = int(max(max(map(max, hydro_vents))))
grid = [[0 for i in range(max_cord + 1)] for j in range(max_cord + 1)]


def is_hori_or_vert(coord: list) -> bool:
	"""
		Check if a coordinate pair is a horizontal or vertical line
	"""

	(x1, y1), (x2, y2) = coord

	return (x1 == x2) or (y1 == y2)

def mark_line(coord: list) -> None:
	"""
		Mark coordinates on our grid
	"""

	def r(a, b):
		""" tiny range helper to change direction if needed """
		return range(a, b + 1 if a < b else b - 1, -1 if a > b else 1)

	(x1, y1), (x2, y2) = coord

	if x1 == x2:
		for y in r(y1, y2): grid[x1][y] += 1

	if y1 == y2:
		for x in r(x1, x2): grid[x][y1] += 1


def count_coord(gte: int) -> int:
	"""
		Count how many coords are greater than or equal to 'gt'
	"""

	r = 0

	for row in grid:
		for v in row: r += 1 if v >= gte else 0

	return r

def main():
	"""
		Solve
	"""

	for ev in hydro_vents:
		if not is_hori_or_vert(ev): continue
		mark_line(ev)

	print(f'overlap > 2 = {count_coord(2)}')


if __name__ == '__main__':
	main()	
