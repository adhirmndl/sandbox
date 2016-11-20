import unittest
from collections import defaultdict

class Solution:
  def lszero_brute(self, A):
    memoize = {}
    for i in xrange(len(A)):
      if i == 0:
        memoize[0] = [[A[i]]]
      else:
        prev = memoize[i - 1]
        curlist = [[A[i]]]
        for ilist in prev:
          temp = ilist[:]
          temp.append(A[i])
          curlist.append(temp)
          memoize[i] = curlist
    maxrange = []
    for (k, v) in memoize.items():
      for rangeList in v:
        if sum(rangeList) == 0 and len(rangeList) > len(maxrange):
          maxrange = rangeList
    return maxrange

  def lszero(self, A):
    N = len(A)
    pre = [None]*N
    curr = 0
    for i in xrange(N):
        curr += A[i]
        pre[i] = curr 
    #print pre

    seen_table = defaultdict(list)
    seen_table[0]=[-1]
    longest = -1
    indices = None
    for i in xrange(N):
        s = pre[i]
        seen_table[s].append(i)
        gap = seen_table[s][-1] - seen_table[s][0]
        if gap > longest:
            longest = gap
            indices = (seen_table[s][0]+1,seen_table[s][-1]+1)
    if indices:
        return A[indices[0]:indices[1]]
    else:
        return []

class SolutionTester(unittest.TestCase):
	def testInput(self):
		s = Solution()
		self.assertEquals(s.lszero([1,2,-2,4,-4]), [2, -2, 4, -4])

	def testFailingInput(self):
		s = Solution()
		self.assertEquals(s.lszero([1, 2, -3, 3]), [1, 2, -3])

if __name__ == "__main__":
	unittest.main()