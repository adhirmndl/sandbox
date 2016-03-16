class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return
        maxSum = currSum = A[0]
        for i in A[1:]:
            currSum = max(i, currSum + i)
            maxSum  = max(currSum, maxSum)
        return maxSum
