with open('../input', 'r') as f:
	l = f.read()
	fish = [int(x.strip()) for x in l.split(',')]


def sequence(days: int):
	"""
		Sequence the fish population growth for 'days'
	"""

	while days > 0:
		# print(f' fish on day {days} => {len(fish)}')

		f_idx = 0
		while f_idx < len(fish):
			v = fish[f_idx]

			if v == 0:				# new fish!
				fish[f_idx] = 7		# reset to 6
				fish.append(9)		# add new fish
				continue

			fish[f_idx] -= 1
			f_idx += 1

		days -= 1


def main():
	"""
		Solve
	"""

	D = 80

	sequence(days=D)
	print(f' fish # after {D} days: => {len(fish)}')


if __name__ == '__main__':
	main()	
