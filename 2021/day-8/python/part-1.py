from collections import Counter

with open('../input', 'r') as f:
	lines = [(l.rstrip()) for l in f.readlines()]


uniq_to_digit = {
	6: 0,
	2: 1,
	5: 2,
	5: 3,
	4: 4,
	5: 5,
	6: 6,
	3: 7,
	7: 8,
	6: 9
}


def output_uniq_count(s: str) -> list:

	_, output = s.split('|')

	return [uniq_to_digit[len(set(x))] for x in output.lstrip().split(' ')]


def count_digits() -> None:

	d = []

	for ent in lines: d.extend(output_uniq_count(ent))

	print(sum([d.count(1), d.count(4), d.count(7), d.count(8)]))


def main():
	"""
		Solve
	"""

	count_digits()

if __name__ == '__main__':
	main()	
