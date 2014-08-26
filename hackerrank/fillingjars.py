n, m = raw_input().split()
sumN = 0
for _ in range(int(m)):
	a, b, k = raw_input().split()
	sumN += (int(b)-int(a)+1) * int(k)
	print sumN
	# print jars
if int(n) == 0:
	print 0
	exit()
print sumN/int(n)
