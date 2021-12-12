with open('../input', 'r') as f:
	lines = [l.rstrip() for l in f.readlines()]


nodes = [tuple(l.split('-')) for l in  lines]


def get_graph() -> dict:
	""" parse input as a dict ("graph") with all of the edges """

	# {'A': ['start', 'c', 'b', 'end'],
	# 'b': ['start', 'A', 'd', 'end'],
	# 'c': ['A'],
	# 'd': ['b'],
	# 'end': ['A', 'b'],
	# 'start': ['A', 'b']}

	g = {}

	for s, e in nodes:

		# start node
		if s in g:
			g[s].append(e)
		else:
			g[s] = [e]

		# end node
		if e in g:
			g[e].append(s)
		else:
			g[e] = [s]

	return g


def get_paths_from(graph: dict, cnode: tuple, seen: set, again: bool = False) -> int:

	# print(locals())

	if cnode == 'end': return 1
	paths = 0

	for nxt in graph[cnode]:
		# if nxt in seen: continue
		if nxt in {'start'}: continue

		if not nxt.islower():
			paths += get_paths_from(graph, nxt, seen, again)
			continue

		if nxt not in seen:
			paths += get_paths_from(graph, nxt, seen | {nxt}, again)
		elif again:
			paths += get_paths_from(graph, nxt, seen | {nxt})

	return paths


def main():
	""" Solve """

	G = get_graph()
	print(f' there are {get_paths_from(G, "start", {"start"}, True)} paths through the system')


if __name__ == '__main__':
	main()	
