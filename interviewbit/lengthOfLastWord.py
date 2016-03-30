class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
		word = ''
		lastword = ''
		space = 0
		for i in range(len(A)):
			if A[i] == ' ':
				space = i
				word = ''
			else:
				word += A[i]
			if i == len(A) -1 and word is not '':
				lastword = word
			if i != len(A) -1 and A[i+1] == ' ' and word is not '':
				lastword = word
		return len(lastword)

s = Solution()
print s.lengthOfLastWord("this is a test string")
print s.lengthOfLastWord("")
print s.lengthOfLastWord("   abcd    ")
print s.lengthOfLastWord("  xDGBklKecz IAcOJYOH O  WY WPi")
