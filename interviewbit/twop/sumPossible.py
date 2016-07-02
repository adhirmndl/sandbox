import unittest

class Solution:
	def twoSum(self, A, num):
		n = len(A)
		j = n - 1
		for i in range(n):
			while (j > i):
				if (i != j and A[i] + A[j] == num): return True
				if (A[i] + A[j] < num)            : break
				j -= 1
		return False

class SolutionTester(unittest.TestCase):
	def testTwoSum(self):
		s = Solution()
		self.assertTrue(s.twoSum([1,2,3,5,8,9], 12))

unittest.main()