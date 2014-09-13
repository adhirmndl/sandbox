#!/bin/python
#hanoi

def moveDisk(fromPole, toPole, n):
	print 'moving disk', n, 'from', fromPole, 'to', toPole
	toPole.insert(0, fromPole.pop(0))
	print 'FROM', fromPole, 'TO', toPole

def moveTower(fromPole, toPole, withPole, n):
	if n >= 1:
		moveTower(fromPole, withPole, toPole, n - 1)
		moveDisk(fromPole, toPole, n)
		moveTower(withPole, toPole, fromPole, n - 1)

if __name__ == "__main__":
	n = input("disks = ")
	moveTower(range(n), [], [], n)
