#heap.py

#first trying the array method

class Heap:
	def __init__(self, arr = []):
		self.heap = arr 
		self.size = len(self.heap)
		self.length = len(self.heap)

	def left(self, i):
		return 2*i

	def right(self, i):
		return 2*i + 1

	def parent(self, i):
		return i/2

	def max_heapify(self, i):
		l = self.heap[left]
		r = self.heap[right]
		if l <= self.heapSize and self.heap[l] > self.heap[i]:
			largest = l
		else:
			largest = i
		if r <= self.heapSize and self.heap[r] > self.heap[largest]:
			largest = r
		if largest != i: 
			#exchange i and largest
			temp = self.heap[i]
			self.heap[i] = self.heap[largest]
			self.heap[largest] = self.heap[i]
			max_heapify(largest)

	def build_heap(self):
		for i in range(self.size/2, 0, -1):
			print i
			print self.heap
			self.max_heapify(i)

if __name__ == "__main__":
	hObj = Heap([16,4,10,14,7,9,3,2,8,1])
	hObj.build_heap()
	print hObj.heap