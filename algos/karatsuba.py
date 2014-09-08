#!/bin/python

def kmultiply(a, b):

	n = max(len(str(a)), len(str(b)))
	if n == 1:
		print a, b, a*b
		return a*b
	a1 = int(str(a)[:len(str(a))/2])
	a2 = int(str(a)[len(str(a))/2:])

	b1 = int(str(b)[:len(str(b))/2])
	b2 = int(str(b)[len(str(b))/2:])
	# a1 = int(str(a)[:(len(str(a))/2 - 1)]))
	# a2 = int(str(a)[len(str(a))/2:]))
	print a1, a2

	pl = kmultiply(a1, b1)
	pr = kmultiply(a2, b2)
	pm = kmultiply(a1 + a2, b1 + b2)
	return pl * pow(10, len(str(a)/2)) + pm * pow(10, len(str(a))) + pr
		

for _ in range(input()):
	a,b = raw_input().strip().split()
	kmultiply(a, b)