'''
The file contains an adjacency list representation
of an undirected weighted graph with 200 vertices
labeled 1 to 200.
Each row consists of the node tuples that are adjacent
to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry
indicating that this row corresponds to the vertex labeled 6.
The next entry of this row "141,8200" indicates that there is
an edge between vertex 6 and vertex 141 that has length 8200.
The rest of the pairs of this row indicate the other vertices
adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph,
using 1 (the first vertex) as the source vertex,
and to compute the shortest-path distances between 1
and every other vertex of the graph.
If there is no path between a vertex v and vertex 1,
we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances
to the following ten vertices,
in order: 7,37,59,82,99,115,133,165,188,197.
You should encode the distances as a
comma-separated string of integers.
So if you find that all ten of these vertices except 115
are at distance 1000 away from vertex 1 and 115 is 2000 distance away,
then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000.
Remember the order of reporting DOES MATTER,
and the string should be in the same order in which
the above ten vertices are given.
The string should not contain any spaces.
Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward
O(mn) time implementation of Dijkstra's algorithm should work fine.
OPTIONAL: For those of you seeking an additional challenge,
try implementing the heap-based version.
Note this requires a heap that supports deletions,
and you'll probably need to maintain some kind of mapping
between vertices and their positions in the heap.
'''

'''
algo
initialize:
x = {s}            [vertices processed so far]
A[s] = 0           [computed shortest path distances]
B[s] = empty path  [computed shortest path]

main loop:
while X != V:
	among all edges (v, w) E with v E x, w !E x
	pick the one that minimizes (Dijkstra's greedy criterion)
	A[v] + lvw  --> [v*, w*]
	add w* to X
	A[w*] = A[v*] + lv*w*
	B[w*] = B[v*]U(v*,w*)
'''

import unittest
import sys
import bisect

def dijkstra(graph, s):
	n = len(graph.keys())
	X = [s]
	A = [0]*(n + 1)
	B = [[] for x in (range(n + 1))]
	vertices = sorted(graph.keys())

	while X != vertices:
		mingreed = sys.maxint
		wsel     = 0
		vsel     = 0
		for vertex in X:
			for (w, e) in graph[vertex].iteritems():
				if w not in X:
					greed = A[vertex] + e
					if mingreed > greed:
						mingreed = greed
						wsel = w
						vsel = vertex
		bisect.insort(X, wsel)
		A[wsel] = A[vsel] + graph[vsel][wsel]
		B[wsel] = B[vsel] + [wsel]
	return A[1:]


def file2graph(filename):
	f = open(filename)
	graph = {}
	for l in f.readlines():
		line = l.split()
		key = int(line[0])
		g = {}
		for kv in line[1:]:
			(k,v) = kv.split(',')
			g[int(k)] = int(v)
		graph[key] = g
	return graph

class DijkstraTester(unittest.TestCase):
	def testFile2Graph(self):
		graph = file2graph('dijkstra_input1.txt')
		self.assertIsNotNone(graph)
		expected = { 1: {8: 2, 2: 1}
							 , 2: {1: 1, 3: 1}
							 , 3: {2: 1, 4: 1}
							 , 4: {3: 1, 5: 1}
							 , 5: {4: 1, 6: 1}
							 , 6: {5: 1, 7: 1}
							 , 7: {8: 1, 6: 1}
							 , 8: {1: 2, 7: 1}}
		self.assertEquals(graph, expected)

	def testDijkstra1(self):
		graph = file2graph('dijkstra_input1.txt')
		result = dijkstra(graph, 1)
		expected = [0, 1, 2, 3, 4, 4, 3, 2]
		self.assertEquals(result, expected)

	def testDijkstra2(self):
		graph = file2graph('dijkstra_input2.txt')
		result = dijkstra(graph, 1)
		expected = [0, 1, 3, 6]
		self.assertEquals(result, expected)

	def testDijkstraInput(self):
		required = [7,37,59,82,99,115,133,165,188,197]
		graph = file2graph('dijkstra_input.txt')
		result = dijkstra(graph, 1)
		answer = [result[i-1] for i in required]
		expected = [2599,2610,2947,2052,2367,2399,2029,2442,2505,3068]
		self.assertEquals(answer, expected)


if __name__=='__main__':
	unittest.main()