class Solution:
	# @param haystack : string
	# @param needle : string
	# @return an integer
	def strStr(self, haystack, needle):
		if needle == "" or haystack == "":
			return -1
		for i in range(len(haystack) - len(needle) + 1):
			for j in range(len(needle)):
				if needle[j] != haystack[i + j]:
					break
				if j == len(needle) - 1:
					return i
		return -1

s = Solution()
print s.strStr("this is a sample", "is")
print s.strStr("this is a sample", "sample")
print s.strStr("bbbbbbbbab", "baba")
