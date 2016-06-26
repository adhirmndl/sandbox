import unittest
# 10 25 29 21
# 100 615 587 518
# 1000 10297 10184 8921
def swap(A, a, b):
	tmp  = A[a]
	A[a] = A[b]
	A[b] = tmp

def partition(A, left, right):
	p = A[left]
	i = left + 1
	for j in range(left+1, right):
		if A[j] < p:
			swap(A, i, j)
			i += 1
	swap(A, left, i-1)
	return i - 1

def quicksort(A, start, end):
	if end == start:
		return 0
	pLocation = partition(A, start, end)
	left_sum  = quicksort(A, start, pLocation)
	right_sum = quicksort(A, pLocation + 1, end)
	return end - start + left_sum + right_sum - 1

def partition_last(A, left, right):
	p = A[right - 1]
	A[right - 1] = A[left]
	A[left] = p

	i = left + 1
	for j in range(left+1, right):
		if A[j] < p:
			swap(A, i, j)
			i += 1
	swap(A, left, i-1)
	return i - 1

def quicksort_last(A, start, end):
	if end == start:
		return 0
	pLocation = partition_last(A, start, end)
	left_sum  = quicksort_last(A, start, pLocation)
	right_sum = quicksort_last(A, pLocation + 1, end)
	return end - start + left_sum + right_sum - 1

def calculate_median(a, b, c):
	if (a[0] - b[0]) * (c[0] - a[0]) >= 0:
		return a
	elif (b[0] - a[0]) * (c[0] - b[0]) >= 0:
		return b
	else:
		return c

def partition_median(A, left, right):
	length    = right - left
	if length % 2 == 0:
		middle = left + length / 2 - 1
	else:
		middle = left + length / 2
	(pivot, pindex) = calculate_median((A[left], left), (A[middle], middle), (A[right - 1], right - 1))

	p = A[pindex]
	A[pindex] = A[left]
	A[left] = p

	i = left + 1
	for j in range(left+1, right):
		if A[j] < p:
			swap(A, i, j)
			i += 1
	swap(A, left, i-1)
	return i - 1

def quicksort_median(A, start, end):
	if end == start:
		return 0
	pLocation = partition_median(A, start, end)
	left_sum  = quicksort_median(A, start, pLocation)
	right_sum = quicksort_median(A, pLocation + 1, end)
	return end - start + left_sum + right_sum - 1

class QuickSortTester(unittest.TestCase):
	def testPartitionLast(self):
		arr = [3, 8, 2, 5, 1, 4, 7, 6]
		self.assertEquals(partition_last(arr, 0, len(arr)), 5)

	def testSmall(self):
		arr = [3, 8, 2, 5, 1, 4, 7, 6]
		self.assertEquals(quicksort(arr, 0, len(arr)), 15)
		self.assertEquals(arr, sorted(arr))

	def test10(self):
		f = open("10.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort(arr, 0, len(arr)), 25)
		self.assertEquals(arr, sorted(arr))

	def test10_last(self):
		f = open("10.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_last(arr, 0, len(arr)), 29)
		self.assertEquals(arr, sorted(arr))

	def test10_median(self):
		f = open("10.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_median(arr, 0, len(arr)), 21)
		self.assertEquals(arr, sorted(arr))

	def test100(self):
		f = open("100.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort(arr, 0, len(arr)), 615)
		self.assertEquals(arr, sorted(arr))

	def test100_last(self):
		f = open("100.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_last(arr, 0, len(arr)), 587)
		self.assertEquals(arr, sorted(arr))

	def test100_median(self):
		f = open("100.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_median(arr, 0, len(arr)), 518)
		self.assertEquals(arr, sorted(arr))

	def test1000(self):
		f = open("1000.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort(arr, 0, len(arr)), 10297)
		self.assertEquals(arr, sorted(arr))

	def test1000_last(self):
		f = open("1000.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_last(arr, 0, len(arr)), 10184)
		self.assertEquals(arr, sorted(arr))

	def test1000_median(self):
		f = open("1000.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_median(arr, 0, len(arr)), 8921)
		self.assertEquals(arr, sorted(arr))

	def testLargeInput(self):
		f = open("quicksort_input.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort(arr, 0, len(arr)), 162085)
		self.assertEquals(arr, sorted(arr))

	def testLargeInput_last(self):
		f = open("quicksort_input.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_last(arr, 0, len(arr)), 164123)
		self.assertEquals(arr, sorted(arr))

	def testLargeInput_median(self):
		f = open("quicksort_input.txt")
		arr = [int(line) for line in f.readlines()]
		self.assertEquals(quicksort_median(arr, 0, len(arr)), 138382)
		self.assertEquals(arr, sorted(arr))

unittest.main()