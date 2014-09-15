import string
def mesh(n):
	n = n+1
	print '    ', '  '.join([string.rjust(str(i), 2) for i in range(1, n)])
	for i in range(1, n):
		line = string.rjust(str(i), 2) + ' '
		perc = 50
		for j in range(0, n-1):
			if j in [k%(n-1) for k in range(i, i+4)]:
				line += '  ' + string.rjust(str(perc), 2)
				if perc != 12:
					perc = perc/2
			else:
				line += '  ' + string.rjust(str(0), 2)
		print line
mesh(5)

