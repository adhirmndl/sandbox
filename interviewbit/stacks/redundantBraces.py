class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
		mapper = {')' : '(', '}' : '{', ']' : '['}
		stack = []
		for e in A:
			if e in mapper.keys():
				#popping business
				if not stack:
					return 1
				i = 0
				while stack and stack.pop() != mapper[e]:
					i += 1
				if i < 2:
					return 1
			else:
				stack.append(e)
		if stack:
			for e in stack:
				if e in mapper.keys() + mapper.values():
					return 1
		return 0


s = Solution()
print s.braces('(a+(b+c))') == 0
# print s.braces('(a)') == 1
# print s.braces('a*(a)') == 1
# print s.braces('a+b') == 0
# print s.braces('(a+b)') == 0
# print s.braces('((a+b))') == 1
# print s.braces('a+(b+c)') == 0
# print s.braces('a + ((b + c))') == 1
