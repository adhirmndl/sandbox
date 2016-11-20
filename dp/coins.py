# n coins (v1, v2, ..., vn)
# s
# min number of coins

import sys
import unittest

def coins(values, s):
	computed = [0]*(s + 1)
	for i in range(1, s + 1):
		if i in values:
			computed[i] = 1
		else:
			mincoins = sys.maxint
			for v in values:
				if i - v >= 0 and computed[i - v] + 1 < mincoins:
					mincoins = computed[i - v] + 1
			computed[i] = mincoins
	return computed

class CoinTester(unittest.TestCase):
	def testCase1(self):
		arr = [1,3,5]
		s = 11
		self.assertEquals(coins(arr, s), [0, 1, 2, 1, 2, 1, 2, 3, 2, 3, 2, 3])

if __name__=="__main__":
	unittest.main()