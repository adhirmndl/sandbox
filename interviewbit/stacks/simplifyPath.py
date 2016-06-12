class Solution:
	def simplifyPath(self, A):
		path = A.split('/')
		path = [e for e in path if e != '']
		stack = []
		for e in path:
			if e == '..':
				if stack:
					stack.pop()
			elif e == '.':
				continue
			else:
				stack.append(e)
		return '/' + '/'.join(stack)

s = Solution()
print s.simplifyPath("/a/./b/../../c/")
print s.simplifyPath("/home//foo/")