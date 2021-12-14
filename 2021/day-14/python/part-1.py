from collections import Counter

with open('../sample', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]


template = lines[0]
rules = [(m.strip(), i.strip()) for m, i in [r.split('->') for r in lines[2:]]]


def sequence(polymer: str) -> None:
	"""
		Sequence a polymer, splitting the pairs 
	"""

	# print(f' polymer => {polymer}')

	n = ''

	for i, _ in enumerate(polymer):
		pair = polymer[i-1:i+1]
		if pair == '': continue

		left, right = list(pair)
		for match, replace in rules:
			if pair == match:
				a = f'{left}{replace}{right}'

				if n[-1:] == a[0]: n += a[1:]
				else: n += f'{left}{replace}{right}'

	return n

def main():
	""" Solve """

	t = template

	for i in range(10):
		t = sequence(t)
		print(f' step {i}, len= {len(t)}')#, t= {t}')
		# print(f' step {i}, len= {len(t)}, c= {Counter(t).most_common()} | {t}')
		# print(f' step {i}, len= {len(t)}, c= {Counter([a + b for a, b in zip(t, t[1:])]).most_common()}')

	c = Counter(t).most_common()
	mcv, mcc = c[0]
	lcv, lcc = c[-1]

	print(f'mcv ({mcv}) = {mcc}, lcv ({lcv}) = {lcc} | mcc - lcc = {mcc - lcc}')


if __name__ == '__main__':
	main()	
