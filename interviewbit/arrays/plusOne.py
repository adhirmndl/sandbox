class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
    	A = self.trim(A)
    	A = A[::-1]
    	carry = 1
    	for i in xrange(len(A)):
    		newSum = A[i] + carry
    		A[i] = newSum % 10
    		carry = newSum / 10
    	if carry != 0:
    		A.append(carry)
    	A = A[::-1]
    	return A

    def trim(self, A):
    	pos = 0
    	for i in A:
    		if i != 0:
    			break
    		pos += 1
    	return A[pos:]

s = Solution()
print s.plusOne([1,2,9])