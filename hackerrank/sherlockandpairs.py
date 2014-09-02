#!/bin/python

for i in range(input()):
	n = input()
	arr = [int(i) for i in raw_input().strip().split()]
	arrMap = {} 
	for e in arr:
	 	arrMap[e] = 0
	for e in arr:
	 	arrMap[e] = arrMap[e] + 1
	pairs = 0
	for v in arrMap.values():
		if v > 1:
			pairs += (v*(v-1))
	print pairs 
