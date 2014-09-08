n, k = raw_input().strip().split()
n = int(n); k = int(k); i = 0; count = 0
while 1:
	if input()%k == 0:
		count+=1
	i+=1
	if i >= n:
		break
print count