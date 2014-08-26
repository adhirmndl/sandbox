for _ in range(input()):
	n = input()
	i = 0
	while (n - i*5) >= 0:
		if ((n - i*5) % 3 == 0):
			print (n - i*5)*'5' + i*5*'3'
			break
		i+=1
	if (n - i*5) < 0:
		print -1
