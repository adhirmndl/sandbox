# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return 2.
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def findCount(self, A, B):
		start = end = -1
		i = 0
		j = len(A) - 1
		while i < j:
			mid = (i + j)/2
			if A[mid] < B:
				i = mid + 1
			else:
				j = mid
		if A[i] != B: return 0
		start = i
		j = len(A) - 1
		while i < j:
			mid = (i + j) /2 + 1
			if A[mid] > B:
				j = mid - 1
			else:
				i = mid
		end = j
		return end - start + 1

s = Solution()
print s.findCount([5,7,7,8,8,8,10], 8)