class Solution:
	# @param A : string
	# @param B : integer
	# @return a strings
	def convert(self, A, B):
		if B == 1:
			return A
		arr = [[] for x in range(B)]
		n = len(A)
		flag = False
		pos = 0
		for i in range(n):
			if pos == 0 or pos == B-1:
				flag = not flag
			arr[pos].append(A[i])
			pos = flag and pos+1 or pos-1
		return ''.join(map(lambda x : ''.join(x), arr))

s = Solution()
print s.convert("paypalishiring", 1)
print s.convert("paypalishiring", 3)
print s.convert("", 3)
