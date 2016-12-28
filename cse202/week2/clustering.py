import unittest

class Edge:
  def __init__(self, e, u, v):
    self.e = e
    self.u = u
    self.v = v

  def __cmp__(self, obj):
    return self.e - obj.e

  def __repr__(self):
    return '(' + str(self.u) + '--' + str(self.e) + '--' + str(self.v) + ')'

class Node:
  def __init__(self, val, rank, parent):
    self.val = val
    self.rank = rank
    if parent is None:
      self.parent = self
    else:
      self.parent = parent

  def __str__(self):
    if (self.parent == self):
      return str(self.val)
    return str(self.parent) + '<-' + str(self.val)

class Kruskal:

  def find(self, node):
    while node != node.parent:
      node = node.parent
    return node

  def union(self, x, y):
    rx = self.find(x)
    ry = self.find(y)
    if rx == ry:
      return #rx # any would do
    if rx.rank > ry.rank:
      ry.parent = rx
      return #rx
    else:
      rx.parent = ry
      if rx.rank == ry.rank:
        ry.rank += 1
      return #ry

  def cluster(self, nodes, edges, n):
    mapping = {}
    for i in range(1, nodes + 1):
      mapping[i] = Node(i, 0, None)

    found = False
    theedge = -1
    # edges are already sorted by weight
    for e in edges:
      if nodes == n:
        # clustering is complete
        # now look for the next edge straddling two clusters
        if self.find(mapping[e.u]) != self.find(mapping[e.v]):
          theedge = e
          break
      elif self.find(mapping[e.u]) != self.find(mapping[e.v]):
        self.union(mapping[e.u], mapping[e.v]) 
        nodes -= 1

    # for (k, v) in mapping.items():
    #   print k, v
    # print 'mincost', theedge
    return theedge.e



def file2edges(filename):
  f = open(filename)
  data = f.readlines()
  n = int(data[0])
  data = data[1:]
  edges = []
  for line in data:
    line = line.split()
    edges.append(Edge(int(line[2]), int(line[0]), int(line[1])))
  edges.sort()
  return (n, edges)


class ClusteringTester(unittest.TestCase):

  def testCluster1(self):
    nodes, edges = file2edges("cluster1.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 4)
    self.assertEquals(mincost, 7)

  def testCluster2(self):
    nodes, edges = file2edges("cluster2.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 4)
    self.assertEquals(mincost, 9)

  def testCluster3_3(self):
    nodes, edges = file2edges("cluster3.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 3)
    self.assertEquals(mincost, 35)

  def testCluster3_4(self):
    nodes, edges = file2edges("cluster3.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 4)
    self.assertEquals(mincost, 17)

  def testCluster3_5(self):
    nodes, edges = file2edges("cluster3.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 5)
    self.assertEquals(mincost, 7)

  def testCluster4(self):
    nodes, edges = file2edges("cluster4.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 4)
    self.assertEquals(mincost, 2)

  def testClusterInput(self):
    nodes, edges = file2edges("clustering_1.txt")
    k = Kruskal()
    mincost = k.cluster(nodes, edges, 4)
    self.assertEquals(mincost, 106)

class MiscTester(unittest.TestCase):
  def testFile2Edges(self):
    nodes, edges = file2edges("cluster1.txt")
    self.assertEquals(nodes, 6)
    self.assertEquals(edges[0], Edge(1, 5, 6))

  def testNodes(self):
    n = Node(10, 0, None)
    self.assertEquals(str(n), '10')
    n1 = Node(15, 1, n)
    self.assertEquals(str(n1), '10<-15')

if __name__ == '__main__':
  unittest.main()
