import unittest

def sort_n_count(A):
	n = len(A)
	if n <= 1:
		return A, 0
	(B, x) = sort_n_count(A[:n/2])
	(C, y) = sort_n_count(A[n/2:])
	(D, z) = merge_n_count(B, C)
	return (D, x + y + z)

def merge_n_count(first, second):
	n = len(first) + len(second)
	merged = []
	i, j, count = 0, 0, 0
	for k in range(n):
		if i < len(first) and j < len(second):
			if first[i] <= second[j]:
				merged.append(first[i])
				i+=1
			else:
				merged.append(second[j])
				j+=1
				count += len(first) - i
		else:
			if i < len(first):
				merged.append(first[i])
				i+=1
			else:
				merged.append(second[j])
				j+=1
	return (merged, count)

class MergeTest(unittest.TestCase):
	def test_sort_n_count(self):
		self.assertEqual(sort_n_count([1,3,5,2,4,6]), ([1,2,3,4,5,6], 3))
		self.assertEqual(sort_n_count(range(10)), (range(10), 0))
		self.assertEqual(sort_n_count([6,5,4,3]), ([3,4,5,6], 6))
		self.assertEqual(sort_n_count([2,3]), ([2,3], 0))
		self.assertEqual(sort_n_count([3,2]), ([2,3], 1))
	def test_inversions(self):
		arr = [int(line) for line in open("int_array.txt")]
		self.assertEqual(sort_n_count(arr), (sorted(arr), 2407905288))

unittest.main()
