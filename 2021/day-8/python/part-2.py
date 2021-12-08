import sys
from collections import Counter
from pprint import pprint

with open('../input', 'r') as f:
	lines = [(l.rstrip()) for l in f.readlines()]

uniq_to_digit = { 
	2: 1, 
	4: 4, 
	3: 7, 
	7: 8 
}


def determine_pattern(i: list) -> dict:
	"""
		This was the first attempt. It did not really work.
		I got close, but the accuracy was poo.
	"""

	print(f'(input) => {i}')

	#   0:      1:      2:      3:      4:
	#  aaaa    ....    aaaa    aaaa    ....
	# b    c  .    c  .    c  .    c  b    c
	# b    c  .    c  .    c  .    c  b    c
	#  ....    ....    dddd    dddd    dddd
	# e    f  .    f  e    .  .    f  .    f
	# e    f  .    f  e    .  .    f  .    f
	#  gggg    ....    gggg    gggg    ....

	#   5:      6:      7:      8:      9:
	#  aaaa    aaaa    aaaa    aaaa    aaaa
	# b    .  b    .  .    c  b    c  b    c
	# b    .  b    .  .    c  b    c  b    c
	#  dddd    dddd    ....    dddd    dddd
	# .    f  e    f  .    f  e    f  .    f
	# .    f  e    f  .    f  e    f  .    f
	#  gggg    gggg    ....    gggg    gggg

	#  00
	# 1  2
	#  33
	# 4  5
	#  66
	f = {	# seperators
		0: '.',
		1: '.',
		2: '.',
		3: '.',
		4: '.',
		5: '.',
		6: '.',
	}

	def print_f():
		print(f'''
      R     P
      -------
      {f[0]}{f[0]}    00
     {f[1]}  {f[2]}  1  2
      {f[3]}{f[3]}    33
     {f[4]}  {f[5]}  4  5
      {f[6]}{f[6]}    66
	''')

	k = {}

	# get the known uniques
	for x in i:
		u = len(set(x))
		if u not in uniq_to_digit: continue
		k[uniq_to_digit[u]] = x

	print(f'k => {k}')

	print(' -- char acount')
	print(f'all => {Counter("".join(i))}')
	print(f'rem => {Counter("".join([x for x in i if x not in k.values()]))}')
	print(' --')

	# occurance counts leak some positions \o/
	l = Counter(''.join([x for x in i if x not in k.values()]))
	a = Counter(''.join(i))
	print(' processing bottom left char (f[4])')
	f[4] = min(l, key=l.get)
	print(f' f[4] got set to {f[4]}\n')

	print_f()

	print(' processing top left char (f[1])')
	f[1] = list(a.keys())[list(a.values()).index(6)]
	print(f' f[1] got set to {f[1]}\n')

	print_f()

	# print(' processing top right char (f[2])')
	# f[2] = list(a.keys())[list(a.values()).index(9)]
	# print(f' f[2] got set to {f[2]}\n')

	# print_f()

	# sample k
	# {8: 'acedgfb', 7: 'dab', 4: 'eafb', 1: 'ab'}

	# populate field characters for the known ones

	# process 1, populating f[2] & f[5]
	# 1: ''.join([f[2], f[5]]),
	print(f' processing *1*')
	print(f' k[1] => {k[1]}, (set f[2], f[5])')
	t = list(k[1])
	# t.remove(f[2])
	f[2] = t[0]
	f[5] = t[1]
	print(f' nf => {f}')

	print_f()

	# process 7, populating f[0], f[2] and f[5]
	# 7: ''.join([f[0], f[2], f[5]]),
	# 2 & 5 is already populated here
	print(f' processing *7*')
	print(f' k[7] => {k[7]}, (set f[0])')
	t = list(k[7])
	t.remove(f[2]) # already set
	t.remove(f[5]) # already set
	print(f' t => {t}')
	f[0] = t[0]
	print(f' nf => {f}')

	print_f()

	# process 4, populating f[1], f[2], f[3], f[5]
	# 4: ''.join([f[1], f[2], f[3], f[5]]),
	# 1, 2 & 5 is already populated here
	print(f' processing *4*')
	print(f' k[4] => {k[4]}, (set f[1], f[3])')
	t = list(k[4])
	t.remove(f[2]) # already set
	t.remove(f[5]) # already set
	t.remove(f[1]) # already set
	print(f' t => {t}')
	f[3] = t[0]
	print(f' nf => {f}')

	print_f()

	# process 8, populating f[0] to f[7]
	# 8: ''.join([f[0], f[1], f[2], f[3], f[4], f[5], f[6]]),
	# only needs to be set here
	print(f' processing *8*')
	print(f' k[8] => {k[8]}, (set f[4], f[6])')
	t = list(k[8])
	t.remove(f[0]) # already set
	t.remove(f[1]) # already set
	t.remove(f[2]) # already set
	t.remove(f[3]) # already set
	t.remove(f[4]) # already set
	t.remove(f[5])
	print(f' t => {t}')
	f[6] = t[0]
	print(f' nf => {f}')

	#  00
	# 1  2
	#  33
	# 4  5
	#  66

	p = {	# full
		0: ''.join([f[0], f[1], f[2], f[4], f[5], f[6]]),
		1: ''.join([f[2], f[5]]),
		2: ''.join([f[0], f[2], f[3], f[4], f[6]]),
		3: ''.join([f[0], f[2], f[3], f[5], f[6]]),
		4: ''.join([f[1], f[2], f[3], f[5]]),
		5: ''.join([f[0], f[1], f[3], f[5], f[6]]),
		6: ''.join([f[0], f[1], f[3], f[4], f[5], f[6]]),
		7: ''.join([f[0], f[2], f[5]]),
		8: ''.join([f[0], f[1], f[2], f[3], f[4], f[5], f[6]]),
		9: ''.join([f[0], f[1], f[2], f[3], f[5], f[6]]),
	}

	print_f()

	print('(all) ', end='')
	for _i, _v in enumerate(f):
		print(f'f[{_i}] ({f[_i]}) = {a[f[_i]]} ' , end='')
	print('!')

	print('(rem) ', end='')
	for _i, _v in enumerate(f):
		print(f'f[{_i}] ({f[_i]}) = {l[f[_i]]} ' , end='')
	print('!')
		
	print(f' pos => {f}')
	print(f' map p => {p}')
	# pprint(p)

	return p


def determine_pattern2(i: list) -> dict:
	"""
		This one finally worked... :(
	"""

	print(f'(input) => {i}')
	print(f'(input len) => {[len(x) for x in i]}')
	k = {}

	# get the known uniques
	for x in i:
		u = len(set(x))
		if u not in uniq_to_digit: continue
		k[uniq_to_digit[u]] = ''.join(sorted(x))

	pprint(k)

	# {8: 'acedgfb', 7: 'dab', 4: 'eafb', 1: 'ab'}

	# lengths (known) (value, len)
	# (1, 2), (4, 4), (7, 3), (8, 7)
	# lengths (unknown) (value, len)
	# (2, 5), (3, 5), (5, 5), (6, 6), (9, 6), (0, 6)
	# left: (5, 5), (6, 6), (9, 6), (0, 6)

	def print_f():
		print('''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
		''')

	# get numbers by imagining the bars, removing known
	# ones to determine a number

	# # 5 len ints = 2, 3, 5
	# for x in [s for s in i if len(set(s)) == 5]:
	# 	print('---')
	# 	print(f'(-1) {x}-{k[1]} = {diff(x, k[1])}')
	# 	print(f'(-4) {x}-{k[4]} = {diff(x, k[4])}')
	# 	print(f'(-7) {x}-{k[7]} = {diff(x, k[7])}')
	# 	print(f'(-8) {x}-{k[8]} = {diff(x, k[8])}')

	# 	# # 2
	# 	# v = diff(x, k[7])
	# 	# v = diff(v, k[4])
	# 	# if len(v) == 2:
	# 	# 	print(f' setting 2 to {x}')
	# 	# 	k[2] = x

	# 	# 3
	# 	v = diff(x, k[1])
	# 	if len(v) == 3:
	# 		print(f' setting 3 to {x}')
	# 		k[3] = x

	# 	# 5
	# 	v = diff(x, k[4])	# 2
	# 	print(f'v (x-4) => {v}')
	# 	v = diff(v, k[1])
	# 	# v = diff(v, k[7])
	# 	print(f'v => {v}')

	# 5 len ints = 2, 3, 5
	for x in [s for s in i if len(set(s)) == 5]:

		if len(set(x) - set(k[1])) == 3:
			k[3] = x

		if len(set(x) - (set(k[4]) - set(k[1]))) == 3:
			k[5] = x 

		if len(set(x) - (set(k[8]) - (set(k[4]) | set(k[7])))) == 3:
			k[2] = x


	# 6 len ints = 9, 6, 0
	for x in [s for s in i if len(set(s)) == 6]:

		if len(set(x) - set(k[1])) == 5:
			k[6] = x

		if len(set(x) - set(k[4])) == 2:
			k[9] = x 

		if len(set(x) - (set(k[4]) - set(k[1]))) == 5:
			k[0] = x


	return k

	# leaving this so that you can laugh at me debugging this pos

	# determine 2 (len = 5)
	for x in [s for s in i if len(set(s)) == 5]:
		print(f'\n ?? 2 = {x}')
		print(f'2->1 = {x}->{k[1]} = {diff(x, k[1])}')
		print(f'2->3 = {x}->{k[3]} = {diff(x, k[3])}')
		print(f'2->4 = {x}->{k[4]} = {diff(x, k[4])}')
		print(f'2->7 = {x}->{k[7]} = {diff(x, k[7])}')
		print(f'2->8 = {x}->{k[8]} = {diff(x, k[8])}')
		if len(diff(x, k[1])) != 5: continue
		if len(diff(x, k[3])) != 2: continue
		if len(diff(x, k[4])) != 3: continue
		if len(diff(x, k[7])) != 4: continue
		if len(diff(x, k[8])) != 2: continue

		print(f'\n * * setting 2 to {x}')
		k[2] = x
		break

	# determine 5 (len = 5)
	for x in [s for s in i if len(set(s)) == 5]:
		print(f'\n ?? 5 = {x}')
		print(f'5->1 = {x}->{k[1]} = {diff(x, k[1])}')
		print(f'5->2 = {x}->{k[2]} = {diff(x, k[2])}')
		print(f'5->3 = {x}->{k[3]} = {diff(x, k[3])}')
		print(f'5->4 = {x}->{k[4]} = {diff(x, k[4])}')
		print(f'5->7 = {x}->{k[7]} = {diff(x, k[7])}')
		print(f'5->8 = {x}->{k[8]} = {diff(x, k[8])}')
		if len(diff(x, k[1])) != 5: continue
		if len(diff(x, k[2])) != 4: continue
		if len(diff(x, k[3])) != 2: continue
		if len(diff(x, k[4])) != 5: continue
		if len(diff(x, k[7])) != 4: continue
		if len(diff(x, k[8])) != 2: continue

		print(f'\n * * setting 5 to {x}')
		k[5] = x
		break

	print_f()

	# # determine 6 (len = 6)
	# for x in [s for s in i if len(set(s)) == 6]:
	# 	print(f'\n ?? 6 = {x}')
	# 	print(f'6->1 = {x}->{k[1]} = {diff(x, k[1])}')
	# 	print(f'6->2 = {x}->{k[2]} = {diff(x, k[2])}')
	# 	print(f'6->3 = {x}->{k[3]} = {diff(x, k[3])}')
	# 	print(f'6->4 = {x}->{k[4]} = {diff(x, k[4])}')
	# 	print(f'6->7 = {x}->{k[7]} = {diff(x, k[7])}')
	# 	print(f'6->8 = {x}->{k[8]} = {diff(x, k[8])}')
	# 	# if len(diff(x, k[1])) != 5: continue
	# 	# if len(diff(x, k[2])) != 4: continue
	# 	# if len(diff(x, k[3])) != 2: continue
	# 	# # if len(diff(x, k[4])) != 3: continue
	# 	# if len(diff(x, k[7])) != 4: continue
	# 	# if len(diff(x, k[8])) != 2: continue

	# 	# print(f' * setting 5 to {x}')
	# 	# k[5] = x
	# 	# break

	# determine 9 (len = 6)
	for x in [s for s in i if len(set(s)) == 6]:
		print(f'\n ?? 9 = {x}')
		print(f'9->1 = {x}->{k[1]} = {diff(x, k[1])}')
		print(f'9->2 = {x}->{k[2]} = {diff(x, k[2])}')
		print(f'9->3 = {x}->{k[3]} = {diff(x, k[3])}')
		print(f'9->4 = {x}->{k[4]} = {diff(x, k[4])}')
		print(f'9->5 = {x}->{k[4]} = {diff(x, k[5])}')
		print(f'9->7 = {x}->{k[7]} = {diff(x, k[7])}')
		print(f'9->8 = {x}->{k[8]} = {diff(x, k[8])}')
		if len(diff(x, k[1])) != 4: continue
		if len(diff(x, k[2])) != 3: continue
		# if len(diff(x, k[3])) != 2: continue
		# if len(diff(x, k[4])) != 5: continue
		if len(diff(x, k[7])) != 3: continue
		if len(diff(x, k[8])) != 1: continue

		print(f'\n * * setting 9 to {x}')
		k[9] = x
		break

	print_f()

	# determine 0 (len = 6)
	for x in [s for s in i if len(set(s)) == 6]:
		print(f'\n ?? 0 = {x}')
		print(f'0->1 = {x}->{k[1]} = {diff(x, k[1])}')
		print(f'0->2 = {x}->{k[2]} = {diff(x, k[2])}')
		print(f'0->3 = {x}->{k[3]} = {diff(x, k[3])}')
		print(f'0->4 = {x}->{k[4]} = {diff(x, k[4])}')
		print(f'0->5 = {x}->{k[4]} = {diff(x, k[5])}')
		print(f'0->7 = {x}->{k[7]} = {diff(x, k[7])}')
		print(f'0->8 = {x}->{k[8]} = {diff(x, k[8])}')
		print(f'0->9 = {x}->{k[8]} = {diff(x, k[9])}')
		if len(diff(x, k[1])) != 4: continue
		# if len(diff(x, k[2])) != 3: continue
		# if len(diff(x, k[3])) != 2: continue
		if len(diff(x, k[4])) != 4: continue
		if len(diff(x, k[7])) != 3: continue
		if len(diff(x, k[8])) != 1: continue

		print(f'\n * * setting 0 to {x}')
		k[0] = x
		break

	pprint(dict(sorted(k.items())))


def output_pattern_to_digit(s: str) -> int:
	"""
		Decodes the output pattern to an int
	"""

	inp, output = s.split('|')
	pattern_to_digit = determine_pattern2([x for x in inp.rstrip().split(' ')])

	output = output.lstrip().split(' ')
	ret = []

	print(f'(output)     => {output}')

	for v in output:
		for d, p in pattern_to_digit.items():
			if len(v) != len(p): continue
			if all(i in v for i in p): ret.append(d)

	print(f'(output int) => {ret}\n')

	return int(''.join(str(x) for x in ret))


def count_digits() -> None:

	d = []

	for ent in lines:
		print('-' * 30)
		d.append(output_pattern_to_digit(ent))

	return d


def main():
	"""
		Solve
	"""

	print(f'sum => {sum(count_digits())}')

if __name__ == '__main__':
	main()	
