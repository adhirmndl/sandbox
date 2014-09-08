#!/bin/python
def bubble(array):
	n = len(array)
	for i in range(n - 1):
		for j in range(i + 1,n):
			if array[i] > array[j]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
		print array
	print array
for _ in range(input()):
	print bubble([int(i) for i in raw_input().strip().split()])
