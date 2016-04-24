class Solution:
	# @param A : tuple of integers
	# @return an integer
	def findMin(self, A):
		low  = 0
		high = len(A) - 1
		while (low <= high):
			if A[low] <= A[high]: return A[low]
			mid  = (low + high) / 2
			nxt  = (mid + 1) % len(A)
			prev = (mid + len(A) - 1) % len(A)
			if A[mid] <= A[nxt] and A[mid] <= A[prev]:
				return A[mid]
			elif A[mid] <= A[high]: high = mid - 1
			elif A[mid] >= A[low]:  low  = mid + 1
		return -1

s = Solution()
print s.findMin([4,5,6,7,1,2])
print s.findMin([])
print s.findMin([1,2,3,4,5,6,7])
print s.findMin([7,8,4,5,6])
print s.findMin([4,5,6,7,3])
print s.findMin([11,12,15,18,2,5,6,8])
