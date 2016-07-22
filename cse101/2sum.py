'''
The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative
(there might be some repetitions!).
This is your array of integers,
with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t
in the interval [-10000,10000]
(inclusive) such that there are distinct numbers x,y
in the input file that satisfy x+y=t.
(NOTE: ensuring distinctness requires a one-line addition
to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you,
try implementing your own hash table for it.
For example, you could compare performance under the chaining
and open addressing approaches to resolving collisions.
'''

import unittest

def twosum(arr, low, high):
	summer = {}
	for i in range(low, high + 1):
		summer[i] = []
	for i in xrange(len(arr)):
		for j in xrange(len(arr)):
			curr = arr[i] + arr[j]
			if i != j and curr >= low and curr <= high:
				pair = (arr[i], arr[j])
				if pair not in summer[curr]:
					summer[curr] += [pair]
	answer = 0
	anslist = []
	for (k, v) in summer.iteritems():
		answer += len(v)
		anslist += v
	return answer

def twosum_brute(arr, low, high):
	summap = {}
	for i in range (low, high + 1):
		summap[i] = False
	n = len(arr)
	for i in xrange(n):
		for j in xrange(n):
			curr = arr[i] + arr[j]
			if curr >= low and curr <= high:
				summap[curr] = True
	count = 0
	for (k, v) in summap.iteritems():
		if v:
			count+=1
	return count

def twosum_hash(arr, low, high):
	summap = {}
	for i in range (low, high + 1):
		summap[i] = False
	n = len(arr)
	hashmap = dict((k, False) for k in arr)
	count = 0
	for i in xrange(n):
		# print i
		for j in xrange(low, high+1):
			if (j - arr[i]) in hashmap and not summap[j]:
				count += 1
				summap[j] = True
	return count


class TwoSumTester(unittest.TestCase):
	def _testSimple(self):
		arr = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
		expected = [(-3, 6), (-3, 7), (-3, 9), (-3, 11)
								, (-1, 6), (-1, 7), (-1, 9)
								, (1, 2), (1, 6), (1, 7), (1, 9)
								, (2, 1), (2, 2), (2, 6), (2, 7)
								, (6, -3), (6, -1), (6, 1), (6, 2)
								, (7, -3), (7, -1), (7, 1), (7, 2)
								, (9, -3), (9, -1), (9, 1)
								, (11, -3), (11, -1)]
		n   = twosum(arr, 3, 10)
		self.assertEquals(n, 28)
		# self.assertEquals(pairs, sorted(expected))

	def testCase1(self):
		arr = [2,8]
		self.assertEquals(1, twosum_brute(arr, 10, 11))

	def testCase2(self):
		arr = [2,3,8]
		self.assertEquals(2, twosum_brute(arr, 10, 11))

	def testCase3(self):
		arr = [2,3,7,8]
		self.assertEquals(2, twosum_brute(arr, 10, 11))

	def testCase4(self):
		arr = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
		self.assertEquals(8, twosum_brute(arr, 3, 10))

	def _testCaseInput(self):
		file = open("2sum_input.txt")
		arr = [int(x) for x in file.readlines()]
		print twosum_brute(arr, -10000, 10000)

	def testCaseHash1(self):
		arr = [2,8]
		self.assertEquals(1, twosum_hash(arr, 10, 11))

	def testCaseHash2(self):
		arr = [2,3,8]
		self.assertEquals(2, twosum_hash(arr, 10, 11))

	def testCaseHash3(self):
		arr = [2,3,7,8]
		self.assertEquals(2, twosum_hash(arr, 10, 11))

	def testCaseHash4(self):
		arr = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
		self.assertEquals(8, twosum_hash(arr, 3, 10))

	def testCaseHashInput(self):
		file = open("2sum_input.txt")
		arr = [int(x) for x in file.readlines()]
		self.assertEquals(427, twosum_hash(arr, -10000, 10000))




if __name__=="__main__":
	unittest.main()