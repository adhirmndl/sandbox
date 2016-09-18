class Solution:
	# @param A : integer
	# @return a list of integers
	def grayCode(self, A):
		return [int(x, 2) for x in self.grayCodeHelper(A)]
	def grayCodeHelper(self, A):
		if A == 1:
			return list("01")
		subresult = self.grayCodeHelper(A-1)
		res = []
		res.extend(['0'+x for x in subresult])
		res.extend(['1'+x for x in subresult[::-1]])
		return res

import unittest
class SolutionTester(unittest.TestCase):
	def testCase1(self):
		s = Solution()
		self.assertEquals(s.grayCode(1), [0, 1])
	def testCase2(self):
		s = Solution()
		self.assertEquals(s.grayCode(2), [0, 1, 3, 2])
	def testCase3(self):
		s = Solution()
		self.assertEquals(s.grayCode(3), [0, 1, 3, 2, 6, 7, 5, 4])

if __name__ == '__main__':
	unittest.main()


'''
0
1

00
01
11
10

000
001
011
010
110
111
101
100
'''