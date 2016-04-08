class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
		A = sorted(A)
		plen = len(A[0])
		if plen == 0:
			return ""
		for i in range(plen):
			temp = [x[i] for x in A]
			if len(set(temp)) > 1:
				return A[0][:i]
		return A[0]

s = Solution()
print s.longestCommonPrefix(["abcdefgh","aefghijk","abcefgh"])
print s.longestCommonPrefix(["abcdefgh","","abcefgh"])
print s.longestCommonPrefix(["abcdefgh","abcdfda","abcefgh"])
