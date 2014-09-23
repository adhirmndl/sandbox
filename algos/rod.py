def rodcut(price, n):
	maxP = price

	for i in range(1, n):
		for j in range(i):
			if maxP[i] < maxP[j] + price[i-j-1]:
				maxP[i] = maxP[j] + price[i-j-1]
	print maxP
	return maxP[n-1]

if __name__ == "__main__":
	price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	print rodcut(price, 10)
