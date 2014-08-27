#!/bin/python
def insertionSort(ar):    
	for i in range(1, len(ar)):
		for j in range(0,i):
			if(ar[i] < ar[j]):
				temp = ar[i]
				ar.remove(temp)
				ar.insert(j, temp)
				break
		print ' '.join(map(str,ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)