#manasa.py
from sets import Set

def manasa(n, a, b):
	prev = [a, b]
	for i in range(2, n):
		next = [] 
		for an in prev:
			next.append(an + a)
			next.append(an + b)
		prev = next
		print next
	ans = list(Set(next))
	ans.sort()
	print ' '.join(map(str,ans))

def manasaPattern(n, a, b):
	ans = set()
	for i in range(0, n):
		ans.add((n-1-i)*a + i*b) 
	ans = list(Set(ans))
	ans.sort()
	print ' '.join(map(str,ans))

if __name__ == '__main__':
	_t = int(raw_input());
	for i in range(0, _t):
		n = int(raw_input());
		a = int(raw_input());
		b = int(raw_input());
		manasaPattern(n, a, b)	