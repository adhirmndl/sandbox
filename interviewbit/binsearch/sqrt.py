class Solution:
	# @param A : integer
	# @return an integer
	def sqrt(self, A):
		if A == 0:
			return 0
		start = 1
		end   = A - 1
		prev  = 0
		while start <= end:
			mid = (start + end) / 2
			sqr = mid*mid
			# print prev, sqr
			if sqr == A or prev == sqr:
				return mid
			if sqr > A:
				end = mid
			else:
				start = mid	
			prev = sqr
		return start

s = Solution()
for i in xrange(101):
	print i, s.sqrt(i)