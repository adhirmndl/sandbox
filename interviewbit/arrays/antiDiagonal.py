class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
		if a == []:
			return a
		res = []
		for i in xrange(len(a[0])):
			curr = []
			j = 0
			k = i
			while j<=len(a)-1 and k>=0:
				curr.append(a[j][k])
				j+=1
				k-=1
			res.append(curr)
		for i in xrange(1, len(a)):
			curr = []
			k = len(a[0]) - 1
			j = i
			while j<=len(a)-1 and k>=0:
				curr.append(a[j][k])
				j+=1
				k-=1
			res.append(curr)

		return res

s = Solution()
# print s.diagonal([[1,2,3],[4,5,6],[7,8,9]])
print s.diagonal([[1,2],[3,4]])