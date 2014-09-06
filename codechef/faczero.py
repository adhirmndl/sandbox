for _ in range(input()):
	number = input()
	nZero = 0; div = 5; n10 = 0
	i = 1
	while pow(div,i) <= number:
		n10 += int(number/pow(div,i))
		i+=1
	print n10	