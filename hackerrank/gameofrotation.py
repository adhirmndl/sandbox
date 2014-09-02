#!/bin/python

def pmean(ar):
	sumArr = 0
	maxsum = 0
	i = 1
	for e in ar:
		sumArr += e*i
		i+=1
	maxsum = sumArr
	arraysum = sum(ar)
	for e in ar:
		sumArr = sumArr - arraysum + e*len(ar) 
		if(maxsum < sumArr):
			maxsum = sumArr
		# print sumArr
	return maxsum

n = input()
ar = [int(i) for i in raw_input().strip().split()]
print pmean(ar)