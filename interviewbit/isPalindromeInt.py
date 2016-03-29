class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A < 0:
            return 0
        return self.isPalindromeStr(str(A))
    def isPalindromeStr(self, A):
        if len(A) == 1:
            return True
        if len(A) == 2 and (A[0] == A[-1]):
            return 1
        if A[0] != A[-1]:
            return 0
        return self.isPalindromeStr(A[1:-1])

s = Solution()
print s.isPalindrome(2147447412)