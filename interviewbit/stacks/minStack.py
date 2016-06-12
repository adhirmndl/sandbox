import unittest

class MinStack:
	def __init__(self):
		self.minstack = []
		self.stack = []
	# @param x, an integer
	def push(self, x):
		self.stack.append(x)
		if not self.minstack or x <= self.minstack[-1]:
			self.minstack.append(x)

	# @return nothing
	def pop(self):
		if self.stack:
			e = self.stack.pop()
			if self.minstack[-1] == e:
				self.minstack.pop()

	# @return an integer
	def top(self):
		if self.stack:
			return self.stack[-1]
		else:
			return -1

	# @return an integer
	def getMin(self):
		if not self.minstack:
			return -1
		return self.minstack[-1]

class MinStackTest(unittest.TestCase):
	def testStack(self):
		mint = MinStack()
		mint.push(3)
		mint.push(9)
		mint.push(2)
		mint.push(0)
		mint.push(23)
		self.assertEqual(mint.getMin(), 0)
		mint.pop()
		self.assertEqual(mint.getMin(), 0)
		mint.pop()
		self.assertEqual(mint.getMin(), 2)
		mint.pop()
		self.assertEqual(mint.getMin(), 3)
		mint.pop()
		self.assertEqual(mint.getMin(), 3)
		mint.pop()
		self.assertEqual(mint.getMin(), -1)

unittest.main()
