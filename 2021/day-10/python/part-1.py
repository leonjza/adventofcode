with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

LEFT = ['(', '[', '{', '<']
RIGHT = [')', ']', '}', '>']

SCORE = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
 }


def find_illegal_char(l :str) -> str:
	""" find the first syntax issue """

	stack = []
	for c in l:
		if c in LEFT: stack.append(c)
		if c in RIGHT:
			if stack[-1:][0] == LEFT[RIGHT.index(c)]: stack.pop()
			else: return c


def main():
	""" Solve """

	c = [find_illegal_char(l) for l in lines]
	print(f' sum => {sum([c.count(r) * SCORE[r] for r in RIGHT if r])}')


if __name__ == '__main__':
	main()	
