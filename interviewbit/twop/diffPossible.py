import unittest

'''
At j = J - 1, our difference D1 was less than diff
At j = J, our difference D2 exceeded diff.
When i = I + 1, our A[i] increases ( as the array is sorted ). 
So, for j = J - 1, the differece will be smaller than D1 
(which is even more smaller to diff.) 
Which means we do not need to explore j <= J - 1 
and we can begin exploring directly from j = J. 
So, j only keeps moving in forward direction and never needs to come back as i increases.
'''
class Solution:
	def diffPossible(self, A, num):
		n = len(A)
		j = 0
		for i in range(n):
			j = max(j, i + 1)
			while(A[j] - A[i] < num):
				j+=1
			if A[j] - A[i] == num:
				return 1
		return 0

class SolutionTester(unittest.TestCase):
	def testTwoSum(self):
		s = Solution()
		self.assertTrue(s.diffPossible([ 1, 5], 4))
		self.assertTrue(s.diffPossible([ 1, 3, 5], 4))
		self.assertTrue(s.diffPossible([ 1, 2, 2, 3, 4 ], 0))
		self.assertTrue(s.diffPossible([ 1, 2, 2, 3, 4, 8, 9, 16, 40], 4))
		self.assertTrue(s.diffPossible([ 2, 2, 27, 27, 32, 36, 43, 48, 64, 70, 79, 85, 89, 89, 90, 92, 98 ], 8))

unittest.main()