class Solution:
	# @param A : string
	# @return an integer
	def atoi(self, A):
		A = self.extract(A)
		i = 0
		num = 0
		for n in A:
			num += n * 10**i
			i += 1
		if num > 2147483647:
			num = 2147483647
		if num < -2147483648:
			num = -2147483648
		return num

	def extract(self, A):
		i = 0
		newA = []
		numStart = False
		mul = 1
		while i < len(A):
			if (ord(A[i]) >=48 and ord(A[i]) <= 59) or A[i] == '+' or A[i] == '-':
				numStart = True
				if A[i] == '-':
					mul = -1
					i += 1
					continue
				if A[i] == '+':
					i += 1
					continue
				newA.append(int(A[i]))
			elif numStart:
				break
			if not numStart and not (ord(A[i]) >= 48 and ord(A[i]) <= 59) and A[i] != ' ':
				return [0]
			i += 1
		return [mul * x for x in newA][::-1]

s = Solution()
print s.atoi('9 2405')
print s.atoi('12019 2405')
print s.atoi('    31219 2405')
print s.atoi('')
print s.atoi('  233d ')
print s.atoi('  -897 ')
print s.atoi('- 5 88C ')
print s.atoi('  +897 ')
print s.atoi('  +7 ')
print s.atoi('  V7 ')
 