#!/bin/python
# MaxXor.py
# Complete the function below.


def  maxXor( l,  r):
	maxXorVal = 0
	for i in range(l, r + 1):
		for j in range(l, r + 1):
			temp = i^j
			if maxXorVal < temp:
				maxXorVal = temp
	return maxXorVal

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
