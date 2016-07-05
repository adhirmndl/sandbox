'''
The file contains the edges of a directed graph.
Vertices are labeled as positive integers from 1 to 875714.
Every row indicates an edge,
the vertex label in first column is the tail
and the vertex label in second column is the head
(recall the graph is directed,
and the edges are directed from the first column vertex
to the second column vertex).
So for example, the 11th row looks like :
"2 47646".
This just means that the vertex with label 2
has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures
for computing strongly connected components (SCCs),
and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs
in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces).
So if your algorithm computes the sizes of the five largest SCCs
to be 500, 400, 300, 200 and 100,
then your answer should be "500,400,300,200,100" (without the quotes).
If your algorithm finds less than 5 SCCs,
then write 0 for the remaining terms.
Thus, if your algorithm computes only 3 SCCs
whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0" (without the quotes).
(Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course.
Because of the size of the graph you may have to manage memory carefully.
The best way to do this depends on your programming language and environment,
and we strongly suggest that you exchange tips for doing this
on the discussion forums.
'''

import unittest
import resource, sys

'''
this is to allow dfs_recursive enough stacks/memory to execute
'''
resource.setrlimit(resource.RLIMIT_STACK,(67104768, 67104768))
sys.setrecursionlimit(10**6)

'''
kosaraju-scc(graph G):
	G' = reverse(G)
	DFS-Loop G' (ordering)
	rename(G)
	DFS-Loop G  (discover SCC)
'''
def scc(graphile, n):
	# reverse
	graph = file2graph(graphile, n, False)
	leaders = dfsloop_rec(graph, n)
	# scc
	graph = file2graph(graphile, n)
	graph = renamegraph(graph, remapper)
	leaders = dfsloop_rec(graph, n)
	return leaders

class SCCTester(unittest.TestCase):
	def testCase1(self):
		answer = scc("scc_test1.txt", 9)
		self.assertEquals(answer, [3,3,3,0,0])

	def testCase2(self):
		answer = scc("scc_test2.txt", 8)
		self.assertEquals(answer, [3,3,2,0,0])

	def testCase3(self):
		answer = scc("scc_test3.txt", 8)
		self.assertEquals(answer, [3,3,1,1,0])

	def testCase4(self):
		answer = scc("scc_test4.txt", 8)
		self.assertEquals(answer, [7,1,0,0,0])

	def testCase5(self):
		answer = scc("scc_test5.txt", 12)
		self.assertEquals(answer, [6,3,2,1,0])

	def testInput(self):
		answer = scc("scc_input.txt", 875714)
		self.assertEquals(answer, [434821,968,459,313,211])

'''
global vars #TODO remove?
'''
t = 0
explored = {}
remapper = {}

'''
DFS-Loop (graph G):
	assume nodes labeled 1 to n:
	for i = n ... 1
		if i not explored
			s = i
			DFS (G, i)
'''
def dfsloop_rec(graph, n):
	global explored, t, remapper
	t = 0
	remapper = {}
	explored = {x : False for x in xrange(1, n+1)}
	sccsum = 0
	leaders  = [0,0,0,0,0]

	for i in xrange(n, 0, -1):
		if not explored[i]:
			dfs_recursive(graph, i)
			sccsize = t - sccsum
			sccsum += sccsize
			leaders.append(sccsize)
			leaders = sorted(leaders, reverse = True)[:5]

	return leaders

'''
DFS (graph G, node i):
	add i to explored
	leader(i) = s
	for each arc (i, j) in G:
		if j not in explored:
			DFS(G, j)
'''
def dfs_recursive(graph, node):
	global t
	explored[node] = True
	for vnode in graph[node]:
		if not explored[vnode]:
			dfs_recursive(graph, vnode)
	t+=1
	remapper[node] = t
	return remapper

# screws up the order :(. try on scc_input5.txt
def dfs_iterative(graph, node):
	visited, stack = [], [node], []
	while stack:
		curr = stack.pop()
		if not explored[curr.val]:
			explored[curr.val] = True
			visited.append(curr)
			stack.extend(set(graph[curr]) - set(visited))
	return [x.val for x in visited]

'''
converts file of edges (u, v) to graph (adjacency list)
n is the number of nodes expected in the graph
'''
def file2graph(filename, n, order = True):
	f = open(filename)
	graph = {}
	for i in xrange(1, n + 1):
		graph[i] = []
	for line in f.readlines():
		# maps each line to a (k,v) depending on desired order
		(k,v) = map(lambda x: int(x), order and line.split() or line.split()[::-1])
		# (k,v) = map(lambda x: int(x), order and line.split() or line.split()[::-1])
		graph[k] = graph[k]+[v]
	return graph

'''
renames the graph nodes according to provided remap
'''
def renamegraph(graph, remap):
	renamedgraph = {}
	for (node, edges) in graph.iteritems():
		renamedgraph[remap[node]] = [remap[x] for x in edges]
	return renamedgraph

class GraphTester(unittest.TestCase):

	def testf2g_input(self):
		graph = file2graph("scc_input.txt", 875714)
		self.assertEquals(len(graph.keys()), 875714)

	def testf2g_input_reverse(self):
		graph = file2graph("scc_input.txt", 875714, False)
		self.assertEquals(len(graph.keys()), 875714)

	def testrename_input(self):
		n = 875714
		graph = file2graph("scc_input.txt", n)
		self.assertEquals(graph[1], [1,2,5,6,7,3,8,4])
		remap = {}
		for i in xrange(1, n + 1):
			remap[i] = n - i + 1
		renamedgraph = renamegraph(graph, remap)
		self.assertEquals(renamedgraph[n], [875714, 875713, 875710, 875709, 875708, 875712, 875707, 875711])

	def testdfs_rec_input(self)	:
		n = 875714
		graph = file2graph("scc_input.txt", n)
		global explored, t, remapper
		t = 0
		remapper = {}
		explored = {x : False for x in xrange(1, n+1)}

		dfs_recursive(graph, 1)
		self.assertEquals(len(remapper.keys()), 600497)

	def testdfsloop_rec_input(self):
		n = 875714
		graph = file2graph("scc_input.txt", n)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [600516, 318, 288, 191, 178])

	def testdfsloop_rec_input_rev(self):
		n = 875714
		graph = file2graph("scc_input.txt", n, False)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [615205, 1157, 462, 224, 217])

	def testdfsloop_rec1(self):
		n = 9
		graph = file2graph("scc_test1.txt", n)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [6, 3, 0, 0, 0])

	def testdfsloop_rec2(self):
		n = 8
		graph = file2graph("scc_test2.txt", n)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [5, 3, 0, 0, 0])

	def testdfsloop_rec3(self):
		n = 8
		graph = file2graph("scc_test3.txt", n)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [4, 3, 1, 0, 0])

	def testdfsloop_rec4(self):
		n = 8
		graph = file2graph("scc_test4.txt", n)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [7, 1, 0, 0, 0])

	def testdfsloop_rec5(self):
		n = 12
		graph = file2graph("scc_test5.txt", n)
		leaders = dfsloop_rec(graph, n)
		self.assertEquals(leaders, [6, 3, 2, 1, 0])

	def testdfs_rec1(self)	:
		n = 9
		graph = file2graph("scc_test1.txt", n)
		global explored, t, remapper
		t = 0
		remapper = {}
		explored = {x : False for x in xrange(1, n+1)}

		dfs_recursive(graph, 1)
		self.assertEquals(remapper, {1 : 3, 4 : 2, 7 : 1})
		dfs_recursive(graph, 2)
		self.assertEquals(remapper, {1: 3, 2: 9, 3: 5, 4: 2, 5: 4, 6: 7, 7: 1, 8: 8, 9: 6})

	def testdfs_rec5(self)	:
		n = 12
		graph = file2graph("scc_test5.txt", n)
		global explored, t, remapper
		t = 0
		remapper = {}
		explored = {x : False for x in xrange(1, n+1)}

		dfs_recursive(graph, 12)
		self.assertEquals(remapper, {7: 2, 8: 1, 9: 3, 10: 5, 11: 4, 12: 6})
		dfs_recursive(graph, 6)
		self.assertEquals(remapper, {3: 7, 6: 8, 7: 2, 8: 1, 9: 3, 10: 5, 11: 4, 12: 6})
		dfs_recursive(graph, 5)
		self.assertEquals(remapper, {2: 10, 3: 7, 4: 9, 5: 11, 6: 8, 7: 2, 8: 1, 9: 3, 10: 5, 11: 4, 12: 6})
		dfs_recursive(graph, 1)
		self.assertEquals(remapper, {1: 12, 2: 10, 3: 7, 4: 9, 5: 11, 6: 8, 7: 2, 8: 1, 9: 3, 10: 5, 11: 4, 12: 6})

	def testrenamegraph(self):
		graph = file2graph("scc_test1.txt", n = 9)
		remap = {1:9, 2:2, 3:4, 4:7, 5:1, 6:5, 7:8, 8:3, 9:6}
		renamedgraph = renamegraph(graph, remap)
		expected = { 1 : [2], 2 : [3], 3 : [1, 5], 4 : [5], 5 : [6]
			, 6 : [8, 4], 7 : [8], 8 : [9], 9 : [7] }
		self.assertEquals(renamedgraph, expected)

	def testf2g(self):
		graph = file2graph("scc_test1.txt", 9)
		expected = { 1 : [4], 2 : [8], 3 : [6], 4 : [7], 5 : [2]
			, 6 : [9], 7 : [1], 8 : [5, 6], 9 : [7, 3] }
		self.assertEquals(graph, expected)

	def testf2gReverse(self):
		graph = file2graph("scc_test1.txt", 9, False)
		expected = { 1 : [7], 2 : [5], 3 : [9], 4 : [1], 5 : [8]
			, 6 : [3, 8], 7 : [4, 9], 8 : [2], 9 : [6] }
		self.assertEquals(graph, expected)

if __name__=='__main__':
	unittest.main()
