#!/bin/python
def countingsort(a):
	ans = [0]*100
	for e in a:
		ans[e] +=1
	print ' '.join(map(str,ans))

b = input()
inputArr = [int(i) for i in raw_input().strip().split()]
countingsort(inputArr)