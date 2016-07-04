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

class Node:
	def __init__(self, val, final = False):
		self.val    = val
		self.final  = final
	def __eq__(self, other):
		print self, other
		print self.val, self.final, other.val, other.final
		return (self.val, self.final) == (other.val, other.final)
	def __hash__(self):
		return self.val
	# def __str__(self):
	# 	return '[' + str(self.val) + ',' + str(self.final) + ']'

t = 0
remapper = {}
explored = {}

'''
kosaraju-scc(graph G):
	G' = reverse(G)
	DFS-Loop G' (ordering)
	rename(G)
	DFS-Loop G  (discover SCC)
'''
def scc(graphile, n):
	global t
	t = 0
	# reverse
	(nodemap, graph) = file2graph(graphile, n, False)
	leaders = dfsloop(graph, nodemap, n)
	print leaders
	print remapper
	graph   = None
	nodemap = None
	t       = 0
	# scc
	(nodemap, graph) = file2graph(graphile, n)
	renamegraph(graph, remapper)
	nodemap = {}
	for node in graph.keys():
		nodemap[node.val] = node
	print node2graph(graph)
	print 'graph keys'
	for key in graph.keys():
		print key.val, key.final, key
	print
	for (k,v) in nodemap.iteritems():
		print k, v.final, v
	print
	leaders = dfsloop(graph, nodemap, n)
	print leaders
	return []

'''
DFS-Loop (graph G):
	assume nodes labeled 1 to n:
	for i = n ... 1
		if i not explored
			s = i
			DFS (G, i)
'''
def dfsloop(graph, nodemap, n):
	global explored
	explored = {i : False for i in xrange(1, n + 1)}
	leaders = []
	for i in xrange(n, 0, -1):
		if not explored[i]:
			leaders.append(i)			
			dfs(graph, nodemap[i])
	return sorted(leaders, reverse = True)
'''
DFS (graph G, node i):
	add i to explored
	leader(i) = s
	for each arc (i, j) in G:
		if j not in explored:
			DFS(G, j)
'''
def dfs(graph, node):
	global t
	explored[node.val] = True
	print node.val, node.final, node
	for vnode in graph[node]:
		if not explored[vnode.val]:
			dfs(graph, vnode)
	t+=1
	remapper[node.val]	= t

'''
converts file of edges (u, v) to graph (adjacency list)
n is the number of nodes expected in the graph
'''
def file2graph(filename, n, order = True):
	f = open(filename)
	graph = {}
	nodemap = {}
	for i in xrange(1, n + 1):
		nodei = Node(i)
		nodemap[i] = nodei
		graph[nodei] = []
	for line in f.readlines():
		# maps each line to a (k,v) depending on desired order
		(k,v) = map(lambda x: nodemap[int(x)], order and line.split() or line.split()[::-1])
		# (k,v) = map(lambda x: int(x), order and line.split() or line.split()[::-1])
		graph[k] = graph[k]+[v]
	return (nodemap, graph)

'''
renames the graph nodes according to provided remap
'''
def renamegraph(graph, remap):
	for node in graph.keys():
		# this works because of same shared Node instance
		node.val = remap[node.val]
		node.final = True

'''
util function to convert graph from Node representation to int
'''
def node2graph(nodegraph):
	graph = {}
	for (k, v) in nodegraph.iteritems():
		graph[k.val] = map(lambda x: int(x.val), v)
	return graph

class GraphTester(unittest.TestCase):

	def testf2g_input(self):
		(nodemap, nodegraph) = file2graph("scc_input.txt", 875714)
		self.assertEquals(len(nodegraph.keys()), 875714)

	def testf2g_input_reverse(self):
		(nodemap, nodegraph) = file2graph("scc_input.txt", 875714, False)
		self.assertEquals(len(nodegraph.keys()), 875714)

	def testrename_input(self):
		n = 875714
		(nodemap, nodegraph) = file2graph("scc_input.txt", n)
		remap = {}
		for i in xrange(1, n + 1):
			remap[i] = n - i + 1
		renamegraph(nodegraph, remap)
		self.assertEquals(len(nodegraph.keys()), n)

	def testdfsloop(self):
		n = 9
		(nodemap, nodegraph) = file2graph("scc_test1.txt", n)
		leaders = dfsloop(nodegraph, nodemap, n)
		self.assertEquals(leaders, [9, 8])

	def testdfs(self)	:
		n = 9
		(nodemap, nodegraph) = file2graph("scc_test1.txt", n)
		global explored
		explored = {x : False for x in xrange(1, 9+1)}
		dfs(nodegraph, nodemap[1])
		self.assertEquals(remapper, {1 : 3, 4 : 2, 7 : 1})
		dfs(nodegraph, nodemap[2])
		self.assertEquals(remapper, {1: 3, 2: 9, 3: 5, 4: 2, 5: 4, 6: 7, 7: 1, 8: 8, 9: 6})

	def testrenamegraph(self):
		(nodemap, nodegraph) = file2graph("scc_test1.txt", n = 9)
		remap = {1:9, 2:2, 3:4, 4:7, 5:1, 6:5, 7:8, 8:3, 9:6}
		renamegraph(nodegraph, remap)
		graph = node2graph(nodegraph)
		expected = { 1 : [2], 2 : [3], 3 : [1, 5], 4 : [5], 5 : [6]
			, 6 : [8, 4], 7 : [8], 8 : [9], 9 : [7] }
		self.assertEquals(graph, expected)

	def testrenameref(self):
		(nodemap, nodegraph) = file2graph("scc_test1.txt", n = 9)
		remap = {1:9, 2:2, 3:4, 4:7, 5:1, 6:5, 7:8, 8:3, 9:6}
		renamegraph(nodegraph, remap)
		nodemap = {}
		for node in nodegraph.keys():
			nodemap[node.val] = node
		for node in nodegraph.keys():
			print id(node), node.val, node.final, node
		print
		for nodeu in nodemap.values():
			self.assertTrue(nodeu in nodegraph.keys())
			print id(nodeu), nodeu.val, nodeu.final, nodeu
			print nodeu in nodegraph.keys()
			print nodegraph[nodeu]
			for nodev in nodegraph[nodeu]:
				self.assertTrue(nodev in nodegraph.keys())

	def testrename1(self):
		# n = 875714
		n = 9
		(nodemap, nodegraph) = file2graph("scc_test1.txt", n)
		remap = {}
		for i in xrange(1, n + 1):
			remap[i] = n - i + 1
		renamegraph(nodegraph, remap)
		graph = node2graph(nodegraph)
		expected = { 1 : [3,7], 2 : [5,4], 3 : [9], 4 : [1], 5 : [8]
			, 6 : [3], 7 : [4], 8 : [2], 9 : [6] }
		self.assertEquals(graph, expected)

	def testf2g(self):
		(nodemap, nodegraph) = file2graph("scc_test1.txt", 9)
		graph = node2graph(nodegraph)
		expected = { 1 : [4], 2 : [8], 3 : [6], 4 : [7], 5 : [2]
			, 6 : [9], 7 : [1], 8 : [5, 6], 9 : [7, 3] }
		self.assertEquals(graph, expected)

	def testf2gReverse(self):
		(nodemap, nodegraph) = file2graph("scc_test1.txt", 9, False)
		graph = node2graph(nodegraph)
		expected = { 1 : [7], 2 : [5], 3 : [9], 4 : [1], 5 : [8]
			, 6 : [3, 8], 7 : [4, 9], 8 : [2], 9 : [6] }
		self.assertEquals(graph, expected)

class SCCTester(unittest.TestCase):
	def testCase1(self):
		answer = scc("scc_test1.txt", 9)
		self.assertEquals(answer, [3,3,3,0,0])

	def testCase2(self):
		answer = scc("scc_test2.txt", 9)
		self.assertEquals(answer, [3,3,2,0,0])

	def testCase3(self):
		answer = scc("scc_test3.txt", 9)
		self.assertEquals(answer, [3,3,1,1,0])

	def testCase4(self):
		answer = scc("scc_test4.txt", 9)
		self.assertEquals(answer, [7,1,0,0,0])

	def testCase5(self):
		answer = scc("scc_test5.txt", 9)
		self.assertEquals(answer, [6,3,2,1,0])

	def _testInput(self):
		answer = scc("scc_input.txt", 875714)
		print answer
		# self.assertEquals(answer, [])

if __name__=='__main__':
	unittest.main()
