class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if A[-1] == '\n':
            A = A[:-1]
        A = [-1 if x == '1' else 1 for x in A]
        maxSum = currSum = l = 0
        pair = [len(A), len(A)]
        for i in xrange(len(A)):
            if (currSum + A[i]<0):
                l = i+1
                currSum = 0
            else:
                currSum += A[i]
            if currSum > maxSum:
                maxSum = currSum
                pair = [l, i]
        if pair == [len(A), len(A)]:
            return []
        pair = [x+1 for x in pair]
        return pair

s = Solution()
print s.flip('010')
print s.flip('1101010001')


