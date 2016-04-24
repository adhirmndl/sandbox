class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
		num = 0
		for i in A:
			num = num ^ i
		return num

s = Solution()
print s.singleNumber([1,2,2,3,1,3])