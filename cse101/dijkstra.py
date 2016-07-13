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
	among all edges (v, w) E with v E x, w E x
	pick the one that minimizes (Dijkstra's greedy criterion)
	A[v] + lvw  --> [v*, w*]
	add w* to X
	A[w*] = A[v*] + lv*w*
	B[w*] = B[v*]U(v*,w*)
'''

import unittest

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

class GraphTester(unittest.TestCase):
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

if __name__=='__main__':
	unittest.main()