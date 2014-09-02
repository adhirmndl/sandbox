#!/bin/python
def insertionSort(ar):    
	for i in range(len(ar)-1, -1, -1):
		temp = ar[i]
		for j in range(i-1, -1, -1):
			if(ar[j] > ar[i]):
				ar[j+1] = ar[j]
				print ' '.join(map(str,ar))
			else:
				ar[j+1] = temp
				# print ar
				break
	print ' '.join(map(str,ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)