factorial = [1]
for _ in range(input()):
	n = input()
	if len(factorial) <= n:
		for i in range(len(factorial), n + 1):
			factorial.append(factorial[-1] * i)
	print factorial[n]