class Solution:
    # @param A : integer
    # @return an integer
    def rotateMatrix(self, A):
    	return zip(*A[::-1])

s = Solution()
print s.rotateMatrix([[1,2,3],[4,5,6]])
