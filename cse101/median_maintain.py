import unittest

class MinHeap():
	def __init__(self):
		self.heapList = [0]

	def insert(self, k):
		self.heapList.append(k)
		self.percUp(len(self.heapList) - 1)

	def percUp(self, i):
		while(i // 2 > 0):
			if self.heapList[i] < self.heapList[i // 2]:
				self.heapList[i], self.heapList[i //2] = self.heapList[i // 2], self.heapList[i]
			i = i // 2

	def percDown(self, i):
		while (i * 2 <= len(self.heapList) - 1):
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
			i = mc

	def minChild(self, i):
		# only one left child left at the leaf level
		if i * 2 + 1 > len(self.heapList) - 1:
			return 2 * i
		else:
			if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def findMin(self):
		return self.heapList[1]

	def delMin(self):
		minVal = self.heapList[1]
		self.heapList[1] = self.heapList[-1]
		self.heapList.pop()
		self.percDown(1)
		return minVal

	def isEmpty(self):
		return len(self.heapList) <= 1

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.heapList = [0] + alist[:]
		while i > 0:
			self.percDown(i)
			i = i - 1

class MaxHeap():
	def __init__(self):
		self.heapList = [0]

	def insert(self, k):
		self.heapList.append(k)
		self.percUp(len(self.heapList) - 1)

	def percUp(self, i):
		while(i // 2 > 0):
			if self.heapList[i] > self.heapList[i // 2]:
				self.heapList[i], self.heapList[i //2] = self.heapList[i // 2], self.heapList[i]
			i = i // 2

	def percDown(self, i):
		while (i * 2 <= len(self.heapList) - 1):
			mc = self.maxChild(i)
			if self.heapList[i] < self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
			i = mc

	def maxChild(self, i):
		# only one left child left at the leaf level
		if i * 2 + 1 > len(self.heapList) - 1:
			return 2 * i
		else:
			if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def findMax(self):
		return self.heapList[1]

	def delMax(self):
		maxVal = self.heapList[1]
		self.heapList[1] = self.heapList[-1]
		self.heapList.pop()
		self.percDown(1)
		return maxVal

	def isEmpty(self):
		return len(self.heapList) <= 1

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.heapList = [0] + alist[:]
		while i > 0:
			self.percDown(i)
			i = i - 1

class MinHeapTester(unittest.TestCase):
	def testMinHeap(self):
		minheap = MinHeap()
		minheap.buildHeap([9,5,6,2,3])
		self.assertEquals(minheap.heapList, [0,2,3,6,5,9])
		self.assertEquals(minheap.delMin(), 2)
		self.assertEquals(minheap.heapList, [0,3,5,6,9])
		self.assertEquals(minheap.delMin(), 3)
		self.assertEquals(minheap.heapList, [0,5,9,6])
		self.assertEquals(minheap.delMin(), 5)
		self.assertEquals(minheap.heapList, [0,6,9])
		self.assertEquals(minheap.delMin(), 6)
		self.assertEquals(minheap.heapList, [0,9])
		self.assertEquals(minheap.delMin(), 9)
		self.assertEquals(minheap.heapList, [0])

class MaxHeapTester(unittest.TestCase):
	def testMaxHeap(self):
		maxheap = MaxHeap()
		maxheap.buildHeap([9,5,6,2,3])
		self.assertEquals(maxheap.heapList, [0,9,5,6,2,3])
		self.assertEquals(maxheap.delMax(), 9)
		self.assertEquals(maxheap.heapList, [0,6,5,3,2])
		self.assertEquals(maxheap.delMax(), 6)
		self.assertEquals(maxheap.heapList, [0,5,2,3])
		self.assertEquals(maxheap.delMax(), 5)
		self.assertEquals(maxheap.heapList, [0,3,2])
		self.assertEquals(maxheap.delMax(), 3)
		self.assertEquals(maxheap.heapList, [0,2])
		self.assertEquals(maxheap.delMax(), 2)
		self.assertEquals(maxheap.heapList, [0])

'''
The goal of this problem is to implement the "Median Maintenance" algorithm
(covered in the Week 5 lecture on heap applications).
The text file contains a list of the integers from 1 to 10000 in unsorted order;
you should treat this as a stream of numbers, arriving one by one.
Letting xi denote the ith number of the file,
the kth median mk is defined as the median of the numbers x1,...,xk.
(So, if k is odd,
		then mk is the ((k+1)/2)th smallest number among x1,...,xk;
if k is even,
		then mk is the (k/2)th smallest number among x1,...,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits).
That is, you should compute (m1+m2+m3+...+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based
and search-tree-based implementations of the algorithm.
'''
def maintain_median(arr):
	high = MinHeap()
	low  = MaxHeap()
	medians = []

	for i in arr:
		if low.isEmpty():
			low.insert(i)
			medians.append(i)
			continue

		if i <= low.findMax():
			low.insert(i)
		else:
			high.insert(i)

		nlow = len(low.heapList)
		nhigh = len(high.heapList)
		if nlow > nhigh + 1:
			high.insert(low.delMax())
		elif nlow < nhigh:
			low.insert(high.delMin())
		medians.append(low.findMax())

		# print '*'*7
		# print 'low', low.heapList
		# print 'high', high.heapList
		# print 'medians', medians
		# print
	return medians


class MedianTester(unittest.TestCase):
	def testCase1(self):
		data   = [9, 9, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		answer = [9, 9, 9, 7, 7, 3, 4, 4, 5, 5, 6, 6]
		self.assertEquals(maintain_median(data), answer)

	def testCase2(self):
		data = [2, 8, 9, 7, 3, 1, 4]
		answer = [2, 2, 8, 7, 7, 3, 4]
		self.assertEquals(maintain_median(data), answer)

	def testCaseInput(self):
		f = open('median_input.txt')
		data = [int(x) for x in f.readlines()]
		self.assertEquals(sum(maintain_median(data)), 46831213)


if __name__=="__main__":
	unittest.main()