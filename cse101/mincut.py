'''
The file contains the adjacency list representation of a simple undirected graph.
There are 200 vertices labeled 1 to 200.
The first column in the file represents the vertex label,
and the particular row (other entries except the first column)
tells all the vertices that the vertex is adjacent to.
So for example, the 6th row looks like : "6	155	56	52	120	......".
This just means that the vertex with label 6 is adjacent to
(i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm
for the min cut problem and use it on the above graph to compute the min cut.
(HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively,
creating a new graph from the old every time there's an edge contraction.
But you should also think about more efficient implementations.)
(WARNING: As per the video lectures,
please make sure to run the algorithm many times with different random seeds,
and remember the smallest cut that you ever find.)
'''

import unittest
import random

def file_to_graph(filename):
	f = open(filename)
	graph = dict(map(
		lambda line: (
			int(line.split()[0]),
			map(lambda x : int(x), line.split()[1:])),
		f.readlines()))
	return graph

def pickedge(graph):
	u = random.choice(graph.keys())
	v = random.choice(graph[u])
	return (u, v)

def merge(graph, u, v):
	uedges = [x for x in graph[u] if x != v]
	for vertex in uedges:
		graph[vertex] = [v if x == u else x for x in graph[vertex]]
	graph[v] = [x for x in graph[v] if x != u]
	graph[v] += uedges
	del graph[u]

def mincut(graph):
	vertices = graph.keys()
	while len(vertices) > 2:
		(u, v) = pickedge(graph)
		merge(graph, u, v)
		vertices = graph.keys()
	return len(graph.values()[0])

class MincutTester(unittest.TestCase):
	def testGraphInputmin(self):
		graph = file_to_graph("graph_input.txt")
		minseen = 200
		for i in range(200):
			test_graph = dict(graph)
			cut = mincut(test_graph)
			if minseen > cut:
				minseen = cut
		self.assertEquals(minseen, 17)

	def testGraphInput(self):
		graph = file_to_graph("graph_input.txt")
		cut   = mincut(graph)
		self.assertIsNotNone(cut)

	def testGraph4min(self):
		graph = file_to_graph("graph_4.txt")
		minseen = 4
		for i in range(45):
			test_graph = dict(graph)
			cut = mincut(test_graph)
			if minseen > cut:
				minseen = cut
		self.assertEquals(minseen, 2)

	def testGraph4(self):
		graph = file_to_graph("graph_4.txt")
		cut   = mincut(graph)
		self.assertTrue(cut <= 3)

	def testPickEdge(self):
		graph = file_to_graph("graph_4.txt")
		(u, v) = pickedge(graph)
		self.assertIsNotNone(u)
		self.assertIsNotNone(v)

	def testMerge(self):
		graph = file_to_graph("graph_4.txt")
		merge(graph, 1, 3)
		expected_graph = {2 : [3, 3, 4], 3: [2, 4, 2], 4: [2, 3]}
		self.assertIsNotNone(graph)
		self.assertEquals(graph, expected_graph)

if __name__=="__main__":
	unittest.main()