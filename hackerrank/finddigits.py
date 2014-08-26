for _ in range(input()):
  n=input()
  nDigits = list(str(n))

  count = 0
  for i in nDigits:
  	if int(i) != 0:
  		if(n%int(i) == 0):
  			count += 1

  print count 