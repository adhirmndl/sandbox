graph = { 1	: set([5])
				, 2 : set([3, 5])
				, 3 : set([2])
				, 4 : set([5])
				, 5 : set([1, 2, 4])
}

def bfs(graph, source):
	visited, queue = [], [source]
	while queue:
		print queue
		curr = queue.pop(0)
		if curr not in visited:
			visited.append(curr)
			queue.extend(graph[curr] - set(visited))
	return visited

def dfs(graph, source):
	visited, stack = [], [source]
	while stack:
		print stack
		curr = stack.pop()
		if curr not in visited:
			visited.append(curr)
			stack.extend(graph[curr] - set(visited))
	return visited


# print bfs(graph, 1)
print dfs(graph, 1)