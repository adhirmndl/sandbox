class Solution:
	def numberOfBits(self, n):
		count = 0
		while n > 0:
			count += n %2
			n = n >> 1
		return count

s = Solution()
# for i in xrange(50):
# 	print i, bin(i), s.numberOfBits(i)
print -32, bin(-32), s.numberOfBits(-32)