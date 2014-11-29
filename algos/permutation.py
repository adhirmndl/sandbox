def permute(cList):
	if len(cList) == 0 or len(cList) == 1:
		return [cList]
	if len(cList) == 2:
		return [cList, cList[::-1]] 
	masterList = []
	for e in cList:
		prefix = e 
		subList = cList[:]
		subList.remove(e)
		print subList
		for everyList in permute(subList):
			masterList += [[e] + everyList]
	return masterList
if __name__ == "__main__":
	sinput = raw_input()
	x = permute(list(sinput))
	for e in x:
		print ''.join(e)
	print len(x)