n = input(); k = input()
candies = [input() for _ in range (0,n)]
candies.sort()
i = 0; minFair = candies[-1] - candies[0]
while i+k-1 < len(candies):
	if candies[i+k-1] - candies[i] < minFair:
		minFair = candies[i+k-1] - candies[i]
	i+=1
print minFair