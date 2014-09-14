def numCoinsRecursive(denom, value):

	if value in denom:
		return 1

	minCoins = value
	for d in [c for c in denom if c <= value]:
		nCoins = 1 + numCoinsRecursive(denom, value - d)	
		if minCoins > nCoins:
			minCoins = nCoins
	return minCoins
def numCoinsMemoize(denom, value):

	minList = [0]
	coinsUsed = [0]
	for i in range(len(minList), value + 1):
		minVal = value
		newCoin = 1
		for d in denom:
			if i - d >= 0:
				tempVal = 1 + minList[i-d]
				if minVal > tempVal:
					minVal = tempVal
					newCoin = d
		coinsUsed.append(newCoin)
		minList.append(minVal)
	# print minList
	coinList(coinsUsed, value)
	return minList[value]

def coinList(coinsUsed, change):
	coin = change
   	while coin > 0:
		thisCoin = coinsUsed[coin]
		print(thisCoin)
		coin = coin - thisCoin

print numCoinsMemoize([1, 5, 10, 25], 63)