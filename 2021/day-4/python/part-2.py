HORIZONTAL = 1
VERTICAL = 2

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

# extract input numbers
numbers = [int(x) for x in lines[0].split(',')]
boards_string = lines[1:]
boards = {}


def line_to_marked(input: str, row: int) -> dict:
	"""
		Parse a board row into marked values
	"""

	return {
		'row': row,
		'lines': [{
			'value': int(v),
			'column': i,
			'hit': False 
		} for i, v in enumerate(input.split())]
	}

def mark_numbers(c: int) -> None:
	"""
		Mark a number anywhere on a board as 'hit' = True
	"""

	for i, board in boards.items():
		for row in board:
			for v in row['lines']:
				if v['value'] == c:
					v['hit'] = True

def get_board_hit_values(board: dict, direction: int, idx: int) -> list:
	"""
		Depending on the direction, scan the board and return only values
		that are marked as 'hit' = True
	"""

	if direction == HORIZONTAL:
		for row in board:
			if row['row'] != idx: continue
			return [x['value'] for x in row['lines'] if x['hit'] == True]

	r = []
	if direction == VERTICAL:
		for row in board:
			for val in row['lines']:
				if val['hit'] == True and val['column'] == idx:
					r.append(val['value'])

	return r

def check_win() -> (int, dict):
	"""
		Check for a winning board that has 5 values marked as
		'hit' = True in either a horizontal or vertical row
	"""

	for i, board in boards.items():

		for cidx in range(0,5):	# check every column
			values = get_board_hit_values(board, VERTICAL, cidx)
			if len(values) == 5:
				return i, board

		for row in board: # check every row.
			values = get_board_hit_values(board, HORIZONTAL, row['row'])
			if len(values) == 5: 
				return i, board

	return None, None

def sum_numbers_by_mark(board: dict, hit: bool) -> int:
	"""
		Sum the numbers on a board based on a hit type
	"""

	total = 0

	for row in board:
		for val in row['lines']:
			if val['hit'] == hit: total += val['value']

	return total

def main():
	"""
		Solve
	"""

	# parse the string boards into a dictionary
	i = r = 0

	for l in boards_string:
		if l == '':
			i += 1
			r = 0
			continue

		if i in boards:
			boards[i].append(line_to_marked(l, r))
		else:
			boards[i] = [line_to_marked(l, r)]

		r += 1

	# process the input numbers
	processed_numbers = []
	lwin = None
	for n in numbers:
		processed_numbers.append(n)
		mark_numbers(n)

		# there can be multiple wins when a number is called
		# filter them all out and mark the last
		while True:
			boardid, win = check_win()

			if not win: break

			lwin = win
			boards.pop(boardid, None)

		if len(boards) != 0: continue

		unmarked_sum = sum_numbers_by_mark(lwin, False)
		print(f'sum * last # => {unmarked_sum * n}')

		break

if __name__ == '__main__':
	main()	
