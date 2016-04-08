class Solution:
	def searchInsert(self, A, b):
		i = 0
		j = len(A) - 1
		while i < j:
			mid = (i + j )/2
			if A[mid] == b:
				return mid
			if A[mid] < b:
				i = mid + 1
			else:
				j = mid - 1
		if A[i] < b :
			return i + 1
		return i

s = Solution()
# for i in xrange(39):
# 	print i, s.sortedInsert([1,3,9,11,17,21,35], i)
for i in xrange(10):
	print i, s.sortedInsert([1,3,5,6], i)