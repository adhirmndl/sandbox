class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if A[-1] == '\n':
            A = A[:-1]
    	base = self.count(A)
    	pair = [len(A), len(A)]
    	for i in xrange(len(A)):
    		for j in xrange(len(A), i, -1):
    			curr = self.count(A[0:i]) + j - i - self.count(A[i:j]) + self.count(A[j:])
    			# print i, j, ':', curr, '[', A[0:i], self.flipped(A[i:j]), A[j:], ']'
    			if curr >= base:
    				# print base, curr, i, j, pair
    				if curr == base:
    					pair = self.smaller(pair, [i, j])
    				else:
    					pair = [i, j]
    				base = curr
    	if pair == [len(A), len(A)]:
    	    return []
    	pair[0] += 1
    	return pair

    def count(self, A):
    	return len([x for x in A if x == '1'])

    def smaller(self, p1, p2):
    	if p1[0] < p2[0]:
    		return p1
    	if p1[0] == p2[0]:
    		if p1[1] < p2[1]:
    			return p1
    	return p2

    def flipped(self, A):
    	newStr = ''
    	for i in A:
    		if i == '1':
    			newStr += '0'
    		else:
    			newStr += '1'
    	return newStr

s = Solution()
print s.flip('010')
# print s.flip('1101010001')
