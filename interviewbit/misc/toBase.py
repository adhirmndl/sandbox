def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def toDecimal(n):
	num = 0
	power = 0
	n = n.upper()
	for i in n[::-1]:
		num   += (ord(i)-64)*(26**power)
		power +=1
	return num

print toDecimal('AB')