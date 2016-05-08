class Solution:
	# @param x : integer
	# @param n : integer
	# @param d : integer
	# @return an integer
	def pow(self, x, n, d):
		if x == 0:
			return 0
		k = 2
		powers = []
		while k <= n:
			powers.append(k)
			k = 2*k
		mods = [x**2%d]
		for i in powers:
			mods.append(mods[-1]**2%d)
		vals = zip(powers,mods)
		dicVals = {k:v for (k,v) in vals}
		dicVals[1] = x%d
		binStr = bin(n)[2:][::-1]
		pow2s = []
		for i in xrange(len(binStr)):
			if binStr[i] == '1':
				pow2s.append(2**i)

		# print dicVals
		# print binStr
		# print pow2s		
		prod = 1
		for i in pow2s:
			prod = (prod * dicVals[i])%d
		return prod

s = Solution()
print s.pow(-1,2,20)
print s.pow(4,4,3)
# print s.pow(-1,1,20)
# print s.pow(10,5,3)
# print s.pow(3,37,53)
# print s.power(71045970,41535484)
print s.pow(71045970,41535484,64735492)
