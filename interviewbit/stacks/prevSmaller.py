import unittest
class Solution:
	def prevSmaller(self, A):
		stack = []
		n = len(A)
		G = [-1] * n
		for i in xrange(n):
			# print 'stack ', stack
			e = A[i]
			if stack:
				while stack and stack[-1] >= e:
					stack.pop()
				if stack:
					G[i] = stack[-1]
				stack.append(e)
			else:
				stack.append(e)
		return G

class SolutionTest(unittest.TestCase):
	def testPrevSmaller(self):
		s = Solution()
		self.assertEqual(s.prevSmaller([4,5,2,10]), [-1,4,-1,2])
		self.assertEqual(s.prevSmaller([3,2,1]), [-1,-1,-1])
		self.assertEqual(s.prevSmaller([]), [])
		self.assertEqual(s.prevSmaller([1]), [-1])
		self.assertEqual(s.prevSmaller([1, 2]), [-1,1])
		self.assertEqual(s.prevSmaller([4, 2]), [-1,-1])
		self.assertEqual(s.prevSmaller(range(10)), [-1,0,1,2,3,4,5,6,7,8])
		self.assertEqual(s.prevSmaller(range(10)[::-1]), [-1]*10)
		self.assertEqual(s.prevSmaller([ 39, 27, 11, 4, 24, 32, 32, 1 ]), [-1,-1,-1,-1,4,24,24,-1])

unittest.main()