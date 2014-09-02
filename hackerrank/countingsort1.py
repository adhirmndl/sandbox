#!/bin/python
def countingsort(a):
	ans = [0]*100
	for e in a:
		ans[e] +=1
	i = 0
	output = '' 
	for n in ans:
		output += (str(i)+ ' ')*n	
		i+=1
	sumarr = 0
	for i in range(len(ans)):
		sumarr += ans[i]
		ans[i] = sumarr
	print ' '.join(map(str,ans))

n = input()
inputArr = []
for i in range(n):
	inputArr.append(int(raw_input().strip().split()[0]))
countingsort(inputArr)