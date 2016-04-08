class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
    	n = len(A)
    	for i in xrange(n):
    		A[i] = A[i] + (A[A[i]] % n) * n;
    	print A
    	for i in xrange(n):
    		A[i] = A[i] / n;
    	return A

s = Solution()
print s.arrange([ 4, 0, 2, 1, 3 ])