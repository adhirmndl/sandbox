class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        tracker = {}
        for i in A:
            if tracker.get(i, None):
                return i
            else:
                tracker[i] = tracker.get(i, 0) + 1
        return None

s = Solution()
print s.repeatedNumber([3,2,2,4,4])
