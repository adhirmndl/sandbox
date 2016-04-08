class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
	def coverPoints(self, X, Y):
		prev = (X[0], Y[0])
		dist = 0
		for i in range(1, len(X)):
			curr = (X[i], Y[i])
			dist += self.distance(prev, curr)
			prev = curr
		return dist

	def distance(self, prev, curr):
		diff = (abs(curr[0] - prev[0]), abs(curr[1] - prev[1]))
		return max(diff[0], diff[1])
		
s = Solution()
print s.coverPoints([-7, -13], [1, -5])
a = [ 4,   8,  -7, -5, -13,  9, -7,  8 ]
b = [ 4, -15, -10, -3, -13, 12,  8, -8 ]
print s.coverPoints(a, b)