class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
    	memoize = [[1]*B]*A
    	for i in xrange(1, A):
    		for j in xrange(1,B):
    			memoize[i][j] = memoize[i-1][j] + memoize[i][j-1]
    	return memoize[A-1][B-1]

s = Solution()
print s.uniquePaths(2,2)
print s.uniquePaths(3,2)
print s.uniquePaths(4,4)
print s.uniquePaths(14,15)
