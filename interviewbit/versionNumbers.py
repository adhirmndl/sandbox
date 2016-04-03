class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compareVersion(self, A, B):
		if len(A) == 0:
			splitA = [0]
		else:
			splitA = [int(x) for x in A.split('.')]
		
		if len(B) == 0:
			splitB = [0]
		else:
			splitB = [int(x) for x in B.split('.')]

		i = 0
		while i < len(splitA) and i < len(splitB):
			if splitA[i] > splitB[i]:
				return 1
			if splitA[i] < splitB[i]:
				return -1
			i += 1
		j = i
		while i < len(splitA):
			if splitA[i] != 0:
				return 1
			i+=1
		while j < len(splitB):
			if splitB[j] != 0:
				return -1
			j+=1
		return 0
		

s = Solution()
print s.compareVersion('1.13.4', '1.13.4')
print s.compareVersion('', '13.0.8')
print s.compareVersion('1.0', '1')
print s.compareVersion('643443896946', '2.487969654569425698')