import unittest

class Solution:
	def nextGreater(self, A):
		A = A[::-1]
		stack = []
		n = len(A)
		G = [-1] * n
		for i in xrange(n):
			# print 'stack ', stack
			e = A[i]
			if stack:
				while stack and stack[-1] <= e:
					stack.pop()
				if stack:
					G[i] = stack[-1]
				stack.append(e)
			else:
				stack.append(e)
		return G[::-1]

class SolutionTest(unittest.TestCase):
	def testPrevSmaller(self):
		s = Solution()
		self.assertEqual(s.nextGreater([4,5,2,10]), [5, 10, 10, -1])
		# self.assertEqual(s.nextGreater([3,2,1]), [-1,-1,-1])
		# self.assertEqual(s.nextGreater([]), [])
		# self.assertEqual(s.nextGreater([1]), [-1])
		# self.assertEqual(s.nextGreater([1, 2]), [-1,1])
		# self.assertEqual(s.nextGreater([4, 2]), [-1,-1])
		# self.assertEqual(s.nextGreater(range(10)), [-1,0,1,2,3,4,5,6,7,8])
		# self.assertEqual(s.nextGreater(range(10)[::-1]), [-1]*10)
		# self.assertEqual(s.nextGreater([ 39, 27, 11, 4, 24, 32, 32, 1 ]), [-1,-1,-1,-1,4,24,24,-1])

unittest.main()