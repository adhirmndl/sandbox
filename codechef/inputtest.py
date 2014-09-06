count = 0
n, k = raw_input().strip().split()
n = int(n)
k = int(k)

for _ in range(n):
	if input()%k == 0:
		count+=1
print count