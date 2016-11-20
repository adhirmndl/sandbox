import unittest

class SequenceTester(unittest.TestCase):
	def testTrivial(self):
		arr = [5,3,4,8,4,6,7]
		self.assertEquals(sequence(arr), 5)

def sequence(arr):
	n = len(arr)
	memoized = [1] * n
	for i in xrange(n):
		longest = memoized[i]
		for j in xrange(i):
			if arr[i] >= arr[j] and memoized[j] + 1 > longest:
				longest = memoized[j] + 1
		memoized[i] = longest
	return memoized[-1]

if __name__ == "__main__":
	unittest.main()