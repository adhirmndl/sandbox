import heapq, unittest

class MinHeapQTester(unittest.TestCase):
	def testHeap(self):
		minheap = [9,5,6,2,3]
		heapq.heapify(minheap)
		self.assertEquals(minheap, [2,3,6,5,9])
		self.assertEquals(heapq.heappop(minheap), 2)
		self.assertEquals(minheap, [3,5,6,9])
		# self.assertEquals(minheap.delMin(), 3)
		# self.assertEquals(minheap.heapList, [0,5,9,6])
		# self.assertEquals(minheap.delMin(), 5)
		# self.assertEquals(minheap.heapList, [0,6,9])
		# self.assertEquals(minheap.delMin(), 6)
		# self.assertEquals(minheap.heapList, [0,9])
		# self.assertEquals(minheap.delMin(), 9)
		# self.assertEquals(minheap.heapList, [0])

class MaxHeapQTester(unittest.TestCase):
	def testMaxHeap(self):
		maxheap = [9,5,6,2,3]
		heapq._heapify_max(maxheap)
		self.assertEquals(maxheap, [9,5,6,2,3])
		self.assertEquals(heapq._heappop(maxheap), 9)
		self.assertEquals(minheap, [6,5,3,2])
		# self.assertEquals(maxheap.delMax(), 9)
		# self.assertEquals(maxheap.heapList, [0,6,5,3,2])
		# self.assertEquals(maxheap.delMax(), 6)
		# self.assertEquals(maxheap.heapList, [0,5,2,3])
		# self.assertEquals(maxheap.delMax(), 5)
		# self.assertEquals(maxheap.heapList, [0,3,2])
		# self.assertEquals(maxheap.delMax(), 3)
		# self.assertEquals(maxheap.heapList, [0,2])
		# self.assertEquals(maxheap.delMax(), 2)
		# self.assertEquals(maxheap.heapList, [0])


if __name__ == "__main__":
	unittest.main()