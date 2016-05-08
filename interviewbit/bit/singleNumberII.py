class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
		ones = twos = 0
		mask = 0
		for i in A:
			twos = twos | (ones & i)
			ones = ones ^ i
			mask = ~(ones & twos)
			ones &= mask
			twos &= mask
		return ones
s = Solution()
print s.singleNumber([1,2,4,3,3,2,2,3,1,1])