def longest_increasing_sub(arr):
	n = len(arr)
	mem = [0]*n
	mem[0] = 1
	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j]:
				mem[i] = max(mem[i], mem[j] + 1)
		if mem[i] == 0:
			mem[i] = mem[i - 1]
	print mem

longest_increasing_sub([5,2,8,6,3,6,9,7])
longest_increasing_sub([1,100,82,30,4,40,5,50,6,60,50])
