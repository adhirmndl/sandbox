class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
		intA = [int(x) for x in str(A)]
		subs = []
		ls = 0
		while ls < len(intA) -1:
			curr = intA
			ls += 1
			while len(curr) != 0 and len(curr) >= ls:
				temp = curr[:ls]
				prod = self.prod(temp)
				if prod in subs:
					return 0
				else:
					subs.append(prod)
				curr = curr[1:]
		if self.prod(intA) in subs:
			return 0
		return 1

	def prod(self, nums):
		return reduce(lambda x, y: x * y, nums, 1)

s = Solution()
print s.colorful(3245)
print s.prod([1,2,4])