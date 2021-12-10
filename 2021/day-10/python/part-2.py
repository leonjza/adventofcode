with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

LEFT = ['(', '[', '{', '<']
RIGHT = [')', ']', '}', '>']

SCORE = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
 }


def has_syntax_error(l :str) -> bool:
	""" find the first syntax issue """

	stack = []
	for c in l:
		if c in LEFT: stack.append(c)
		if c in RIGHT:
			if stack[-1:][0] == LEFT[RIGHT.index(c)]: stack.pop()
			else: return True

	return False


def completion_score(l: str) -> int:
	""" determine the completion score """

	stack = []
	for c in l:
		if c in LEFT: stack.append(c)
		if c in RIGHT: stack.pop()

	completion = [RIGHT[LEFT.index(c)] for c in stack]
	completion.reverse()

	s = 0
	for c in completion: s = s * 5 + SCORE[c]

	return s


def main():
	""" Solve """

	incomplete = [l for l in lines if not has_syntax_error(l)]
	score = sorted([completion_score(l) for l in incomplete])
	mid = int((len(score) - 1) / 2)

	print(f' completion score => {score[mid]}')


if __name__ == '__main__':
	main()	
