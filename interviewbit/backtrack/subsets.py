'''
[1,2,3]
[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

[]
[[]]

[1]
[[], [1]]

[1,2]
[[], [1], [1,2], [2]]
'''
class Solution:
	# @param A : integer
	# @return a list of integers
	def subsets(self, A):
		if len(A) == 0:
			return [[]]
		res = [[]]
		A.sort()
		for i in xrange(len(A)):
			curr = self.subsets(A[i+1:])
			res.extend([[A[i]] + x for x in curr])
		return res

import unittest
class SolutionTester(unittest.TestCase):
	def testCase1(self):
		s = Solution()
		self.assertEquals(s.subsets([1]), [[],[1]])

	def testCase2(self):
		s = Solution()
		self.assertEquals(s.subsets([1,2]), [[], [1], [1,2], [2]])

	def testCase3(self):
		s = Solution()
		self.assertEquals(s.subsets([1,2,3]), [
																					  [],
																					  [1],
																					  [1, 2],
																					  [1, 2, 3],
																					  [1, 3],
																					  [2],
																					  [2, 3],
																					  [3],
																					])
	def testCase4(self):
		s = Solution()
		self.assertEquals(s.subsets([15,20,12,19,4]), [[],[4],[4,12],[4,12,15],[4,12,15,19],[4,12,15,19,20],[4,12,15,20]
																							,[4,12,19],[4,12,19,20],[4,12,20],[4,15],[4,15,19]
																							,[4,15,19,20],[4,15,20],[4,19],[4,19,20],[4,20]
																							,[12],[12,15],[12,15,19],[12,15,19,20],[12,15,20]
																							,[12,19],[12,19,20],[12,20],[15],[15,19]
																							,[15,19,20],[15,20],[19],[19,20],[20]])

if __name__ == '__main__':
	unittest.main()
