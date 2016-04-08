class Solution:
	# @param A : integer
	# @return a list of list of integers
	def prettyPrint(self, A):
		n = A*2-1
		arr = [[0]*n for x in range(n)]
		for i in range(A):
			for a in range(i, n -i):
				for b in range(i, n-i):
					arr[a][b] = A-i
		return arr

s = Solution()
for i in range(10):
	print '\n'.join(map(lambda x: ' '.join(map(str, x)), s.prettyPrint(i))), '\n'
