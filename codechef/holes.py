for _ in range(input()):
	word = raw_input().upper()
	holes = 0
	for e in word:
		if (e in ['A', 'D', 'O', 'P', 'Q', 'R']):
			holes +=1
		if (e in ['B'] ):
			holes +=2
	print holes
