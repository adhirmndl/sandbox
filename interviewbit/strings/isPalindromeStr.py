class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
    	A = A.lower()
    	A = [x for x in A if x.isalnum()]
    	for i in xrange(len(A)/2):
    		if A[i] != A[len(A)-i-1]:
    			return 0
    	return 1

s = Solution()
print s.isPalindrome('abc')
print s.isPalindrome('race a car')
print s.isPalindrome('A man, a plan, a canal: Panama')
