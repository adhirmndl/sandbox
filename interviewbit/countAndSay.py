class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
		if A == 1:
			return 1
		return self.count(self.countAndSay(A - 1))

	def count(self, A):
		seq = [int(x) for x in str(A)]
		count = 1
		currChar = seq[0]
		res = []
		for i in seq[1:]:
			if i != currChar:
				res.append(count)
				res.append(currChar)
				currChar = i
				count = 0
			count += 1
		res.append(count)
		res.append(currChar)
		return int(''.join(map(str, res)))

s = Solution()
print s.count(1115555222)
print s.countAndSay(3)
print s.countAndSay(20)