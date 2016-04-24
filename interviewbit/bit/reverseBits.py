class Solution:
	def reverse(self, n):
		num = 0
		count = 0
		while n > 0:
			num = num << 1
			lastBit = n & 1
			n = n >> 1
			num += lastBit
			count += 1
		while count < 32:
			num = num << 1
			count += 1
		return num

s = Solution()
# for i in xrange(50):
# 	print i, bin(i), int(bin(i)[2:][::-1], 2) == int(bin(s.reverseBits(i))[2:], 2)

print s.reverseBits(3)