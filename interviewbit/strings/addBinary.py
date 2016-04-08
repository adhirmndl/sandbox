class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
		if len(A) < len(B):
			temp = A; A = B; B = temp
		B = B.rjust(len(A), '0')
		carry = 0
		C = [0]*len(A)
		B = B[::-1]
		A = A[::-1]
		for i in range(len(B)):
			C[i] = int(B[i]) ^ int(A[i]) ^ carry
			carry = (int(A[i]) & int(B[i])) | (int(B[i]) & carry) | (int(A[i]) & carry)
		if carry:
			C.append('1')
		return ''.join(map(str, C[::-1]))

s = Solution()
print s.addBinary("100", "11")
print s.addBinary("11", "101")
print s.addBinary("", "101")
print s.addBinary("1", "")
print s.addBinary("", "")
print s.addBinary("0", "0")
print s.addBinary("111000101", "11111111111")
