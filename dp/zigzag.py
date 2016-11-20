'''
Problem Statement
    	
A sequence of numbers is called a zig-zag sequence if the differences
between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a zig-zag sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence 
because the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, 
the first because its first two differences are positive 
and the second because its last difference is zero.

Given a sequence of integers, sequence, 
return the length of the longest subsequence of sequence 
that is a zig-zag sequence. 
A subsequence is obtained by deleting some number of elements 
(possibly zero) from the original sequence, 
leaving the remaining elements in their original order.
'''

import unittest

class ZigZagTester(unittest.TestCase):
	def testCase1(self):
		zigzag = ZigZag()
		sequence = [1, 7, 4, 9, 2, 5]
		self.assertEquals(zigzag.longestZigZag(sequence), 6)

	def testCase2(self):
		zigzag = ZigZag()
		sequence = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8 ]
		self.assertEquals(zigzag.longestZigZag(sequence), 7)

	def testCase3(self):
		zigzag = ZigZag()
		sequence = [44]
		self.assertEquals(zigzag.longestZigZag(sequence), 1)

	def testCase4(self):
		zigzag = ZigZag()
		sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEquals(zigzag.longestZigZag(sequence), 2)

	def testCase5(self):
		zigzag = ZigZag()
		sequence = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
		self.assertEquals(zigzag.longestZigZag(sequence), 8)

	def testCase6(self):
		zigzag = ZigZag()
		sequence = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
								600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
								67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
								477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
								249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
		self.assertEquals(zigzag.longestZigZag(sequence), 36)

class ZigZag:
	def longestZigZagTrue(self, sequence):
		n = len(sequence)
		memoized = [(1, True)] * n
		for i in xrange(n):
			longest, zig = memoized[i]
			for j in xrange(i):
				if sequence[i] - sequence[j] > 0 and not memoized[j][1] and memoized[j][0] + 1 > longest:
					longest = memoized[j][0] + 1
					zig = True
				if sequence[i] - sequence[j] < 0 and memoized[j][1] and memoized[j][0] + 1 > longest:
					longest = memoized[j][0] + 1
					zig = False
			memoized[i] = longest, zig
		return memoized[-1][0]

	def longestZigZagFalse(self, sequence):
		n = len(sequence)
		memoized = [(1, False)] * n
		for i in xrange(n):
			longest, zig = memoized[i]
			for j in xrange(i):
				if sequence[i] - sequence[j] > 0 and not memoized[j][1] and memoized[j][0] + 1 > longest:
					longest = memoized[j][0] + 1
					zig = True
				if sequence[i] - sequence[j] < 0 and memoized[j][1] and memoized[j][0] + 1 > longest:
					longest = memoized[j][0] + 1
					zig = False
			memoized[i] = longest, zig
		return memoized[-1][0]

	def longestZigZag(self, sequence):
		return max(self.longestZigZagTrue(sequence),self.longestZigZagFalse(sequence))


if __name__ == "__main__":
	unittest.main()