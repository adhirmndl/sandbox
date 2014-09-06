x, balance = raw_input().strip().split()
x = float(x)
balance = float(balance)

if x!=0 and x%5 == 0:
	if x <= balance - 0.5:
		balance -= (x+0.5)
print "{0:.2f}".format(balance)
	