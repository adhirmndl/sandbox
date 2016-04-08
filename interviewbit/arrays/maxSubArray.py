import random
class Solution:
    def maxSubArray(self, A):
        maxSum = currSum = A[0]
        for num in A[1:]:
            currSum = max(num, currSum + num)
            maxSum  = max(currSum, maxSum)
        return maxSum

s = Solution()
for i in range(10):
    arr = [random.randint(-10,10) for i in xrange(10)]
    print arr
    print s.maxSubArray(arr)
print s.maxSubArray([-3, -10, 3, 4, 1, -8, 6, -9, 8, -5])