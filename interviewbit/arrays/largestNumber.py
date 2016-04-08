class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
    	A = sorted(A, cmp=self.customSort)
    	return ''.join(map(str, A))

    def customSort(self, x, y):
    	if int(str(x) + str(y)) > int(str(y) + str(x)):
    		return -1
    	if int(str(x) + str(y)) == int(str(y) + str(x)):
    		return 0
    	return 1

s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])
print s.largestNumber([12,121])
print s.largestNumber([27,271])
print s.largestNumber([8,89])