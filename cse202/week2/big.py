import unittest

class Cluster:

  def invert(self, bit):
    return '1' if bit == '0' else '0'

  def similar(self, v):
    output = []
    for i in range(len(v)):
      output.append(v[:i] + self.invert(v[i]) + v[i + 1:])
      for j in range(i + 1, len(v)):
        output.append(v[:i] + self.invert(v[i]) + v[i+1 : j] + self.invert(v[j]) + v[j+1:])
    return output

  def cluster(self, filename):
    heads = {}
    _, vs = file2graph(filename)
    for v in vs:
      heads[v] = v
    clusters = len(heads)
    for v in vs:
      vhead = heads[v]
      while vhead != heads[vhead]:
        vhead = heads[vhead]

      for neighbor in self.similar(v):
        if heads.get(neighbor):
          head = heads[neighbor]
          while heads[head] != head:
            head = heads[head]
          if vhead != head:
            heads[head] = vhead
            clusters -=1
    return clusters

def file2graph(filename):
  data = open(filename).readlines()
  vertices = int(data[0].split()[0])
  data = data[1:]
  edges = [''.join(x.split()) for x in data]
  return vertices, edges

class ClusterTester(unittest.TestCase):

  def test_11_8_6(self):
    c = Cluster()
    self.assertEquals(c.cluster('11-8-6.txt'), 6)
  def test_2_2_1(self):
    c = Cluster()
    self.assertEquals(c.cluster('2-2-1.txt'), 1)
  def test_22_16_4(self):
    c = Cluster()
    self.assertEquals(c.cluster('22-16-4.txt'), 4)
  def test_24_24_7(self):
    c = Cluster()
    self.assertEquals(c.cluster('24-24-7.txt'), 7)
  def test_3_24_1(self):
    c = Cluster()
    self.assertEquals(c.cluster('11-8-6.txt'), 6)
  def testBig(self):
    c = Cluster()
    self.assertEquals(c.cluster('clustering_big.txt'), 6118)

  def test_file2graph(self):
    v, e = file2graph("2-2-1.txt")
    self.assertEquals(v, 2)
    self.assertEquals(e, ['00', '00'])

  def test_invert(self):
    c = Cluster()
    self.assertEquals(c.invert('1'), '0')
    self.assertEquals(c.invert('0'), '1')

  def test_similar(self):
    c = Cluster()
    self.assertEquals(c.similar('00'), ['10', '11', '01'])
    self.assertEquals(c.similar('111'), ['011', '001', '010',
                                         '101', '100', '110'])
    self.assertEquals(c.similar('1111'), ['0111', '0011', '0101',
                                          '0110', '1011', '1001',
                                          '1010', '1101', '1100',
                                          '1110'])

if __name__ == '__main__':
  unittest.main()