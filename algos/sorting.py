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

def bubbleTest():
	for _ in range(input()):
		print bubble([int(i) for i in raw_input().strip().split()])

def binSearch(start, end, arr, item):
	mid = (start + end)//2
	if start >= end:
		return False
	if arr[mid] == item:
		return True
	if item > arr[mid]:
		return binSearch(mid+1, end, arr, item)
	else:
		return binSearch(start, mid-1, arr, item)

if __name__== "__main__":
	print binSearch(0, 9, range(9), 10)