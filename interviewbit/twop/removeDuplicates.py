import unittest
'''
Notice that the array is sorted. 
This implies that all repetitions for an element
are clustered together in the array.

**Try maintaining 2 pointers in the array: **

One pointer iterates over the array and
Other pointer only moves per occurrence of a value in the array.
Now you need to make sure we choose only
one occurrence per cluster of repetition in the array,
we could probably just check if A[i] != A[i+1]. 
So, the second pointer only moves when A[i] != A[i+1]
'''
class Solution:
	# @param A : list of integers
	# @return an integer
	def removeDuplicates(self, A):
		i, j, n = 1, 1, len(A)
		while i < n and j < n:
			if A[j] == A[j-1]:
				j += 1
			else:
				A[i] = A[j]
				j += 1
				i += 1
		return i

class SolutionTester(unittest.TestCase):
	def testRemoveDuplicates(self):
		s = Solution()
		self.assertEqual(s.removeDuplicates([1,1,2]), 2)
		self.assertEqual(s.removeDuplicates([1,2,2,3,4,5,5,6]), 6)

unittest.main()