from collections import defaultdict, Counter, deque
from heapq import *
# get delay of each instruction
delay = {}
print("Enter the operations and cost: ")
while True:
	s = input()
	if not s:
		 break
	i, c = s.split()
	delay[i] = int(c)
	# get dependency graph as input
successors = defaultdict(list)
predecessors = defaultdict(list)
in_degree = Counter()
out_degree = Counter()
print("Enter the edges: ")
while True:
	s = input()
	if not s: 
		break
	u, v = s.split()
	successors[u].append(v)
	predecessors[v].append(u)
	in_degree[v] += 1
	out_degree[u] += 1
	# calculate priority
queue = deque([i for i in predecessors if not successors[i]])
priority = Counter()
while queue:
	node = queue.popleft()
	priority[node] = max(priority[node], delay[node])
	for predecessor in predecessors[node]:
		priority[predecessor] = max(priority[predecessor], priority[node]+delay[predecessor])
		out_degree[predecessor] -= 1
		if not out_degree[predecessor]:
			queue.append(predecessor)
	# local list scheduling
cycle = 1
ready = [(-priority[op], op) for op in delay if not in_degree[op]]
heapify(ready)
active = []
while ready or active:
	to_remove = set()
	for t,op in active:
		if t+delay[op] <= cycle:
			to_remove.add(op)
			for successor in successors[op]:
				in_degree[successor] -= 1
				if not in_degree[successor]:
					heappush(ready, (-priority[successor], successor))
	active = [(t, op) for t,op in active if op not in to_remove]
	print(f"{cycle} [{' '.join(op for p,op in ready)}] [{f' '.join(op for t,op in active)}]")

	if ready:
		_,op = heappop(ready)
		active.append((cycle, op))
	cycle += 1

cycle -= 1
print(f"Total cycles: {cycle}")
