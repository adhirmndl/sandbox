class Solution:
    # @param A : list of integers
    # @return an integer
    # Given an unsorted integer array, find the first missing positive integer
    # Given [1,2,0] return 3,
    # [3,4,-1,1] return 2,
    # [-8, -7, -6] returns 1
    # Your algorithm should run in O(n) time and use constant space.
    def firstMissingPositive(self, A):
        A.sort()
        i = 0
        while A[i] < 1 and i < len(A) - 1:
            i+=1
        curr = 1
        while i < len(A) - 1:
            if A[i] != curr:
                return curr
            curr+=1
            i+=1
        if A[-1] < 1:
            return 1
        return A[-1] + 1




s = Solution()
print s.firstMissingPositive([1,2,0])
print s.firstMissingPositive([3,4,-1,1])
print s.firstMissingPositive([-8,-7,-6])
print s.firstMissingPositive([1])
print s.firstMissingPositive([1,2,3,4,5,6])
