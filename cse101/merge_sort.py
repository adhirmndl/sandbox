import unittest

def merge_sort(A):
	n = len(A)
	if n <= 1:
		return A
	first = merge_sort(A[:n/2])
	second = merge_sort(A[n/2:])
	return merge(first, second)

def merge(first, second):
	n = len(first) + len(second)
	merged = []
	i, j = 0, 0
	for k in range(n):
		if i < len(first) and j < len(second):
			if first[i] <= second[j]:
				merged.append(first[i])
				i+=1
			else:
				merged.append(second[j])
				j+=1
		else:
			if i < len(first):
				merged.append(first[i])
				i+=1
			else:
				merged.append(second[j])
				j+=1
	return merged

class MergeTest(unittest.TestCase):
	def test_merge_sort(self):
		self.assertEqual(merge_sort([1,3,5,2,4,6]), [1,2,3,4,5,6])
		self.assertEqual(merge_sort([6,5,4,3]), [3,4,5,6])
		self.assertEqual(merge_sort([2,3]), [2,3])

unittest.main()
