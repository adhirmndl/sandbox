'''
[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
'''
class Solution:
	# @param A : integer
	# @return a list of integers
	def permute(self, A):
		if len(A) == 1:
			return [A]
		res = []
		for x in A:
			curr = A[:]
			curr.remove(x)
			res.extend([[x] + i for i in self.permute(curr)])
		return res

import unittest
class SolutionTester(unittest.TestCase):
	def testCase1(self):
		s = Solution()
		self.assertEquals(s.permute([1]), [[1]])

	def testCase2(self):
		s = Solution()
		self.assertEquals(s.permute([1,2]), [[1,2], [2,1]])

	def testCase3(self):
		s = Solution()
		self.assertEquals(s.permute([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

if __name__ == '__main__':
	unittest.main()
