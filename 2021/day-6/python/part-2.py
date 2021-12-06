from collections import deque

fish = deque([0] * 9)


def seed() -> None:
	"""
		Populate the initial state
	"""

	with open('../input', 'r') as f:
		l = f.read()
		s = [int(x.strip()) for x in l.split(',')]

	for n in s: fish[n] += 1


def sequence(days: int) -> None:
	"""
		Sequence the fish population growth for 'days'
		A deque() is used, thanks to: https://stackoverflow.com/a/2150125
	"""

	while days > 0:
		new_f = fish[0]
		fish.rotate(-1)

		fish[8] = new_f		# and it would create a new lanternfish with an internal timer of 8
		fish[6] += new_f	# After another day, its internal timer would reset to 6

		days -= 1


def main():
	"""
		Solve
	"""

	D = 256

	seed()
	sequence(D)

	print(f'fish # after {D} days: => {sum(fish)}')


if __name__ == '__main__':
	main()	
