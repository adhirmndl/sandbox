import unittest

class SolutionTester(unittest.TestCase):
	def test_trivial(self):
		s = Solution()
		a = [1, 3, 4, 7]
		b = [2, 3, 7, 9]
		result = s.intersect(a, b)
		expected = [3, 7]
		self.assertEquals(result, expected)

	def test_none(self):
		s = Solution()
		a = [1, 3, 4, 7]
		b = [8, 9, 10, 11]
		result = s.intersect(a, b)
		self.assertEquals(result, [])
		result = s.intersect(b, a)
		self.assertEquals(result, [])

	def test_empty(self):
		s = Solution()
		a = []
		b = []
		result = s.intersect(a, b)
		self.assertEquals(result, [])
		result = s.intersect(b, a)
		self.assertEquals(result, [])
		result = s.intersect([1,2,3], [])
		self.assertEquals(result, [])
		result = s.intersect([], [1,2,3])
		self.assertEquals(result, [])

	def test_rep(self):
		s = Solution()
		a = [1,2,2,2,4]
		b = [2,2,4,4,5]
		result = s.intersect(a, b)
		self.assertEquals(result, [2,2,4])

class Solution:
	def intersect(self, a, b):
		i, j = 0, 0
		res  = []
		while (i < len(a) and j < len(b)):
			if a[i] < b[j]:
				i += 1
			elif a[i] > b[j]:
				j += 1
			else:
				res.append(a[i])
				i += 1
				j += 1
		return res

if __name__ == "__main__":
	unittest.main()