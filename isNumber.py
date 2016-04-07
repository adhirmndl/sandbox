class Solution:
	# @param A : string
	# @return an integer
	def isNumber(self, A):
		allowed = '.+-e'
		A = A.strip()
		if len(A) == 0 or A[-1] in allowed:
			return 0
		seen = {k: v for (k,v) in zip(allowed, [0]*len(allowed))}
		for i in range(len(A)):
			if not (A[i].isdigit() or A[i] in allowed):
				return 0
			if A[i] in allowed:
				if seen[A[i]] != 0 or (A[i] == 'e' and not (i>0 and A[i-1].isdigit())):
					return 0
				seen[A[i]] = 1
				if A[i] == 'e':
					seen['-'] = 0
					seen['+'] = 0				
					seen['.'] = 1
		return 1

s = Solution()
print s.isNumber(''), 0, ''
print s.isNumber('0'), 1, '0'
print s.isNumber(" 0.1"), 1, " 0.1"
print s.isNumber("abc" ), 0, "abc" 
print s.isNumber("1 a" ), 0, "1 a" 
print s.isNumber("2e10"), 1, "2e10"
print s.isNumber("0.1e10"), 1, "0.1e10"
print s.isNumber("-0.1e-10"), 1, "-0.1e-10"
print s.isNumber("0xFF"), 0, "0xFF"
print s.isNumber("3."), 0, "3."
print s.isNumber("3e0.1"), 0, "3e0.1"
print s.isNumber("1f"), 0, "1f"
print s.isNumber("1u"), 0, "1u"
print s.isNumber("1000LL"), 0, "1000LL"
print s.isNumber("1000L"), 0, "1000L"
print s.isNumber("0008"), 1, "0008"
print s.isNumber("+    "), 0, "+   "
print s.isNumber("1.e1"), 0, "1.e1"
print s.isNumber("-01.1e-10"), 1, "-01.1e-10"
