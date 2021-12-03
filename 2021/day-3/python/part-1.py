gamma = epsilon = ''

with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]

for i in range(0, 12):
	one = zero = 0

	for l in lines:
		c = int(l[i])
		one += 1 if c == 1 else 0
		zero += 1 if c == 0 else 0

	if one > zero:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'


gamma = int(gamma, 2)	
epsilon = int(epsilon, 2)

print(f'gamma * epsilon: {gamma * epsilon}')
