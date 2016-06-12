import unittest

class Solution:
	def evalRPN(self, exp):
		stack  = []
		ops    = ['+', '-', '*', '/']
		for e in exp:
			if e in ops:
				if stack:
					e = self.op(e, stack.pop(), stack.pop())
			stack.append(e)
		return stack[0]

	def op(self, op, b, a):
		a, b = int(a), int(b)
		if op == '+':
			return a + b
		if op == '-':
			return a - b
		if op == '*':
			return a*b
		if op == '/':
			return a/b

class SolutionTest(unittest.TestCase):
	def testPrevSmaller(self):
		s = Solution()
		self.assertEqual(s.evalRPN(['4', '5', '+']), 9)
		self.assertEqual(s.evalRPN(['4', '5', '*']), 20)
		self.assertEqual(s.evalRPN(['4', '5', '3', '*', '+']), 19)
		self.assertEqual(s.evalRPN(["2", "1", "+", "3", "*"]), 9)
		self.assertEqual(s.evalRPN(["4", "13", "5", "/", "+"]), 6)

unittest.main()