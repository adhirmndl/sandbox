#!/bin/python
word1 = raw_input().strip(); word2 = raw_input().strip()
ref = [0]*26
for c in list(word1):	
	ref[ord(c) - 97] +=1
for c in list(word2):	
	ref[ord(c) - 97] -= 1
ans = 0
for i in ref:
	ans += abs(i)
print ans 