#!/bin/python
def insertionSort(ar):    
	shifts = 0
	for i in range(1, len(ar)):
		for j in range(0,i):
			if(ar[i] < ar[j]):
				temp = ar[i]
				ar.pop(i)
				ar.insert(j, temp)
				shifts += i - j
				break
		# print ' '.join(map(str,ar))
	print shifts

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)