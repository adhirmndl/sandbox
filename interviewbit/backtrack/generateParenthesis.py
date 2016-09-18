class Solution:
	def __init__(self):
		self.result = []
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
		self.result = []
		self.genParen("", A, A)
		return self.result

	def genParen(self, s, left, right):
		if left > right:
			return;
		if left == 0 and right == 0:
			self.result.append(s)
			return
		if left > 0:
			self.genParen(s + "(", left - 1, right)
		if right > 0:
			self.genParen(s + ")", left, right - 1)

import unittest
class SolutionTester(unittest.TestCase):
	def testGenParen1(self):
		s = Solution()
		res = s.generateParenthesis(1)
		self.assertEquals(res, ['()'])

	def testGenParen2(self):
		s = Solution()
		res = s.generateParenthesis(2)
		self.assertEquals(res, ['(())','()()'])

	def testGenParen3(self):
		s = Solution()
		res = s.generateParenthesis(3)
		self.assertEquals(res, ["((()))", "(()())", "(())()", "()(())", "()()()"])

	def testGenParen4(self):
		s = Solution()
		res = s.generateParenthesis(4)
		self.assertEquals(res, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])

if __name__ == "__main__":
	unittest.main()

