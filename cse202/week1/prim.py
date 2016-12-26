import unittest
from sets import Set
import sys

class MST():
  def cost(self, graph):
    cost = 0
    mst_set = Set([1])
    nodes = len(graph.keys())
    # iterate till all nodes are covered
    while len(mst_set) != nodes:
      min_edge  = sys.maxint
      next_node = -1
      # find min edge amongst all nodes in set to G - set
      for source in mst_set:
        curr_min_edge = sys.maxint
        curr_next_node = -1
        # for each node find minimum
        for (node, edge) in graph[source]:
          if edge < curr_min_edge and node not in mst_set:
            curr_min_edge = edge
            curr_next_node = node
        if curr_min_edge < min_edge:
          min_edge = curr_min_edge
          next_node = curr_next_node
      cost += min_edge
      mst_set.add(next_node)
    return cost


def file2graph(filename):
  f = open(filename)
  content = f.readlines()
  (nodes, edges) = content[0].split()
  data = content[1:]
  graph = {node: [] for node in range(1, int(nodes) + 1)}
  for l in data:
    line = l.split()
    graph[int(line[0])].append((int(line[1]), int(line[2])))
    graph[int(line[1])].append((int(line[0]), int(line[2])))
  return graph

class MSTTester(unittest.TestCase):

  def testEdges1(self):
    graph = file2graph("edges1.txt")
    mst = MST()
    cost = mst.cost(graph)
    self.assertEquals(cost, 4)

  def testEdges2(self):
    graph = file2graph("edges2.txt")
    mst = MST()
    cost = mst.cost(graph)
    self.assertEquals(cost, 16)

  def testEdges3(self):
    graph = file2graph("edges3.txt")
    mst = MST()
    cost = mst.cost(graph)
    self.assertEquals(cost, -3)

  def testEdges4(self):
    graph = file2graph("edges4.txt")
    mst = MST()
    cost = mst.cost(graph)
    self.assertEquals(cost, 37)

  def testEdges(self):
    graph = file2graph("edges.txt")
    mst = MST()
    cost = mst.cost(graph)
    self.assertEquals(cost, -3612829)

  def testFile2Graph(self):
    graph = file2graph("edges1.txt")
    answer = { 1: [(2, 1), (3, 2)]
             , 2: [(1, 1), (3, 3), (4, 2)]
             , 3: [(1, 2), (2, 3), (4, 1)]
             , 4: [(2, 2), (3, 1)]
             }
    self.assertEquals(graph, answer)

if __name__ == "__main__":
  unittest.main()