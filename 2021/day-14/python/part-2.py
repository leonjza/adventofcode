from collections import Counter

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]


template = lines[0]
rules = dict([(m.strip(), i.strip()) for m, i in [r.split('->') for r in lines[2:]]])
# rules = dict([r.split('->') for r in lines[2:]])


def sequence(pairs: Counter, count: Counter) -> None:
	"""
		Add pair counts for the simulation.

		pairs: Counter({'NN': 1, 'NC': 1, 'CB': 1})
	"""

	op = pairs.copy()

	for (left, right), ins in rules.items():
		oc = op[left + right]		# original pairs' count
		
		pairs[left + right] -= oc	# remove pair
		pairs[left + ins] += oc		# add new left pair
		pairs[ins + right] += oc	# add new right pair
		count[ins] += oc			# increment the letter count

# def sum_pair_chars(pairs: Counter) -> Counter:
#	""" create a character sum from pairs """
# 	nc = Counter()
# 	for (a, b), c in pairs.items():
# 		nc[a] += c
# 		nc[b] += c
# 	return nc

def main():
	""" Solve """

	p, c = Counter([(a + b) for a, b in zip(template, template[1:])]), Counter(template)

	for i in range(40): sequence(p, c)

	# s = sum_pair_chars(p).most_common()
	s = c.most_common()
	mcv, mcc = s[0]
	lcv, lcc = s[-1]

	print(f'mcv ({mcv}) = {mcc}, lcv ({lcv}) = {lcc} | mcc - lcc =  {mcc - lcc}')


if __name__ == '__main__':
	main()	
