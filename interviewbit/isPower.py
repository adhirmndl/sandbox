class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
    	return self.genNumbers(A)

    def genNumbers(self, A):
    	for i in self.primes(A):
    		power = 2
    		while i**power <= A:
    			if i**power == A:
    				return True
    			power += 1
    	return False

    def primes(self, n):
			sieve = [True] * n
			for i in xrange(3,int(n**0.5)+1,2):
				if sieve[i]:
					sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
			return [2] + [i for i in xrange(3,n,2) if sieve[i]]

s = Solution()
for i in range(10):
	print i, s.isPower(i)
# print s.isPower(1024000000)
print s.isPower(536870912)
print s.isPower(1024)
