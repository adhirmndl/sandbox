class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
    	rows = []
    	if A == 0:
    		return rows
    	prev = [1]
    	rows.append(prev)
    	k = 1
    	while k < A:
    		nxt = [1]*(len(prev) + 1)
    		for i in xrange(1, len(nxt) - 1):
    			nxt[i] = prev[i] + prev [i-1]
    		rows.append(nxt)
    		prev = nxt
    		k+=1
    	return rows

    def getRow(self, n):
        return self.generate(n)[-1]

s = Solution()
print s.generate(5)
print s.getRow(5)