'''
Problem Statement
    	
The old song declares "Go ahead and hate your neighbor",
and the residents of Onetinville have taken those words to heart.
Every resident hates his next-door neighbors on both sides.
Nobody is willing to live farther away from the town's well than his neighbors,
so the town has been arranged in a big circle around the well.
Unfortunately, the town's well is in disrepair and needs to be restored.
You have been hired to collect donations for the Save Our Well fund.

Each of the town's residents is willing to donate a certain amount,
as specified in the int[] donations, which is listed in clockwise order
around the well. However, nobody is willing to contribute to a fund 
to which his neighbor has also contributed. 
Next-door neighbors are always listed consecutively in donations, 
except that the first and last entries in donations are also 
for next-door neighbors. 
You must calculate and return the maximum amount of donations that can be collected.
'''

import unittest

class BadNeighborsTester(unittest.TestCase):
	def testCase1(self):
		donations = [10, 3, 2, 5, 7, 8]
		neighbors = BadNeighbors()
		self.assertEquals(neighbors.maxDonations(donations), 19)
	def testCase2(self):
		donations = [11, 15]
		neighbors = BadNeighbors()
		self.assertEquals(neighbors.maxDonations(donations), 15)
	def testCase3(self):
		donations = [7, 7, 7, 7, 7, 7, 7]
		neighbors = BadNeighbors()
		self.assertEquals(neighbors.maxDonations(donations), 21)
	def testCase4(self):
		donations = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
		neighbors = BadNeighbors()
		self.assertEquals(neighbors.maxDonations(donations), 16)
	def testCase5(self):
		donations = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
								6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
								52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
		neighbors = BadNeighbors()
		self.assertEquals(neighbors.maxDonations(donations), 2926)

class BadNeighbors:
	def maxDonations(self, donations):
		n = len(donations)
		memoized = [(donations[i], set([i])) for i in xrange(n)]
		for i in xrange(n):
			for j in xrange(i):
				if memoized[j][0] + donations[i] > memoized[i][0] and (i+1)%n not in memoized[j][1] and (i-1)%n not in memoized[j][1]:
					memoized[i] = (memoized[j][0] + donations[i], memoized[i][1] | memoized[j][1])
		for (k, v) in memoized:
			print k, v
		result = [k for (k,v) in memoized]
		return max(result)


if __name__ == "__main__":
	unittest.main()