class Solution:
	def search(self, A, B):
		if len(A) == 0:
			return -1
		ind = self.findMinIndex(A)
		arr = A[ind:] + A[:ind]
		bindex = self.binSearch(arr, B)
		if bindex == -1:
			return -1
		return (ind + bindex) % len(A)

	def findMinIndex(self, A):
		low  = 0
		high = len(A) - 1
		while (low <= high):
			if A[low] <= A[high]: return low
			mid  = (low + high) / 2
			nxt  = (mid + 1) % len(A)
			prev = (mid + len(A) - 1) % len(A)
			if A[mid] <= A[nxt] and A[mid] <= A[prev]:
				return mid
			elif A[mid] <= A[high]: high = mid - 1
			elif A[mid] >= A[low]:  low  = mid + 1
		return -1

	def binSearch(self, A, B):
		n = len(A)
		low = 0
		high = n - 1
		while low <= high:
			mid = (low + high ) / 2
			if A[mid] == B:
				return mid
			if A[mid] < B:
				low = mid + 1
			else:
				high = mid - 1
		return -1

s = Solution()
# print range(10)
# print s.binSearch(range(10), 3)
# print s.binSearch(range(10), 9)
# print s.binSearch(range(10), 10)
# print s.binSearch(range(10), 4)
# print s.binSearch(range(10), 7)

print s.findMinIndex([4, 5, 6, 7, 0, 1, 2])
# for x in range(8):
# 	print x, s.search([4, 5, 6, 7, 0, 1, 2], x)
print 10, s.search([4, 5, 6, 7, 0, 1, 2], 10)
print 1, s.search([], 1)
print 1, s.search([3], 1)
print 1, s.search([3,2], 1)
print 1, s.search([3,2], 1)

