class Solution:
	def longestPalindromeN3(self, A):
		longest = ''
		A = A.lower()
		for i in xrange(len(A)):
			j = len(A)
			while j > i:
				if self.isPalindrome(A[i:j]) and (j-i)  > len(longest):
					longest = A[i:j]
				j -= 1
		return longest

	def isPalindrome(self, A):
		for i in xrange(len(A)/2):
			if A[i] != A[len(A)-i-1]:
				return 0
		return 1		

	def longestPalindrome(self, s):
		n = len(s)
		begin = 0
		lenmax = 1
		table = [[0]*n for x in xrange(n)]
		for i in xrange(n):
			table[i][i] = 1
		for i in xrange(n-1):
			if s[i] == s[i+1]:
				table[i][i+1] = 1
				begin = i
				lenmax = 2
		# print '\n'.join(map(lambda x: ' '.join(map(str, x)), table)), '\n'
		for l in xrange(3,n+1):
			for i in xrange(n - l + 1):
				j = i + l - 1
				if s[i] == s[j] and table[i+1][j-1]:
					table[i][j] = 1
					if lenmax < l:
						begin = i
					lenmax = l
		# print '\n'.join(map(lambda x: ' '.join(map(str, x)), table)), '\n'
		return s[begin : begin + lenmax]

s = Solution()
print s.longestPalindrome("amaanaamb")	
print s.longestPalindrome("amanamplanacnalancan")	
print s.longestPalindrome('')
print s.longestPalindrome('a')
print s.longestPalindrome('ab')
print s.longestPalindrome('aba')
print s.longestPalindrome('aabb')
print s.longestPalindrome('abbcccbbbcaaccbababcbcabca')