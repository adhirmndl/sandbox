class BinaryHeap():
	def __init__(self):
		self.heapList = [0]

	def insert(self, k):
		self.heapList.append(k)
		self.percUp(len(self.heapList) - 1)

	def percUp(self, i):
		while(i // 2 > 0):
			if self.heapList[i] < self.heapList[i // 2]:
				temp = self.heapList[i]
				self.heapList[i]      = self.heapList[i // 2]
				self.heapList[i // 2] = temp
			i = i // 2

	def percDown(self, i):
		while (i * 2 <= len(self.heapList) - 1):
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				temp = self.heapList[i]
				self.heapList[i]  = self.heapList[mc]
				self.heapList[mc] = temp
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
		return len(self.heapList <= 1)

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.heapList = [0] + alist[:]
		while i > 0:
			self.percDown(i)
			i = i - 1

bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])

print bh.heapList
print(bh.delMin())
print bh.heapList
print(bh.delMin())
print bh.heapList
print(bh.delMin())
print bh.heapList
print(bh.delMin())
print bh.heapList
print(bh.delMin())
print bh.heapList
