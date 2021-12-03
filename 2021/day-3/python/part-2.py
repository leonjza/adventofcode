MOST_COMMON = 1
LEAST_COMMON = 0

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

def filter_bits(lines: list, common: int) -> list:
	while True:

		for i in range(0, 12):
			one = zero = 0

			for l in lines:
				c = int(l[i])
				one += 1 if c == 1 else 0
				zero += 1 if c == 0 else 0

			if one > zero:
				lines = [x for x in lines if x[i] == ('1' if common == MOST_COMMON else '0')]
			elif zero > one:
				lines = [x for x in lines if x[i] == ('0' if common == MOST_COMMON else '1')]
			elif zero == one:
				lines = [x for x in lines if x[i] == ('1' if common == MOST_COMMON else '0')]
			else:
				raise Exception('wtf')

			if len(lines) == 1:
				return lines[0]

oxygen = int(filter_bits(lines, MOST_COMMON), 2)
co2 = int(filter_bits(lines, LEAST_COMMON), 2)

print(f' oxy * c02 => {oxygen * co2}')
