import unittest

class SolutionTester(unittest.TestCase):
	def test_trivial(self):
		arr = [1,1,0,1,1,0,0,1,1,1]
		s = Solution()
		ans = s.maxone(arr, 1)
		self.assertEquals(ans, [0, 1, 2, 3, 4])

	def test_case1(self):
		arr = [1,1,0,1,1,1,0,1,1,1]
		s = Solution()
		ans = s.maxone(arr, 1)
		self.assertEquals(ans, range(3,10))

	def test_case2(self):
		arr = [1,0,0,0,0,0,1,0,1,1]
		s = Solution()
		ans = s.maxone(arr, 2)
		self.assertEquals(ans, [5,6,7,8,9])

	def test_case3(self):
		arr = [0, 1, 1]
		s = Solution()
		ans = s.maxone(arr, 3)
		self.assertEquals(ans, [0,1,2])

	def test_case4(self):
		arr = [0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0]
		s = Solution()
		ans = s.maxone(arr, 46)
		self.assertEquals(ans, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98])

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
		n = len(A)
		left = 0
		right = 0
		noZerosInWindow = 0
		if A[right] == 0:
			noZerosInWindow += 1
		bestLeft = 0
		bestRight = 0

		while right < n:
			if noZerosInWindow <= B:
				right += 1
				if right < n and A[right] == 0:
					noZerosInWindow += 1
			if noZerosInWindow > B:
				if A[left] == 0:
					noZerosInWindow -= 1
				left += 1

			if right >= n:
				if n - 1 - left > bestRight - bestLeft:
					bestLeft = left
					bestRight = n - 1
				elif right - left > bestRight - bestLeft:
					bestLeft = left
					bestRight = right
		#print bestLeft, bestRight
		if bestRight > n - 1:
			bestRight = n - 1
		return range(bestLeft, bestRight+1)
if __name__ == "__main__":
	unittest.main()