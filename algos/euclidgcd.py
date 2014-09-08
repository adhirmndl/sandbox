def euclid(a, b):
	if b==0:
		return a
	return euclid(b, a % b)

for _ in range(input()):
	a, b = [int(i) for i in raw_input().strip().split()]
	print euclid(a, b)