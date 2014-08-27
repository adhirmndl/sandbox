for _ in range(input()):
	n = input()
	reXor = 0
	arrNum = raw_input().split()
	for i in range(len(arrNum)):
	 	if(i%2 == 0):
	 		reXor^=int(arrNum[i])

	if (n%2 == 0):
		print 0
	else:
		print reXor
