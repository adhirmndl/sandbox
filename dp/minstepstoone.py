'''
compute min steps to one
'''

import unittest
class MinStepsOneTester(unittest.TestCase):
	def testCase1(self):
		self.assertEquals(minStepsOne(1), 0)
		self.assertEquals(minStepsOne(4), 2)
		self.assertEquals(minStepsOne(7), 3)
		self.assertEquals(minStepsOne(10), 3)
		# self.assertEquals(minStepsOne(1), 0)
		# self.assertEquals(minStepsOne(1), 0)

def minStepsOne(n):
	mem = [0] * (n + 1)
	for i in xrange(2, n + 1):
		mem[i] = 1 + mem[i - 1]
		if i % 2 == 0:
			mem[i] = min(mem[i], 1 + mem[i/2])
		if i % 3 == 0:
			mem[i] = min(mem[i], 1 + mem[i/3])
	return mem[-1]

if __name__ == "__main__":
	unittest.main()