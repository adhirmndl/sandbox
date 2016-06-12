def cut_rod(prices, n):
	if n == 0:
		return 0
	q = -1
	for i in range(1, n + 1):
		q = max(q, prices[i] + cut_rod(prices, n - i))
	return q

def memoized_cut_rod(prices, n):
	q = [-1] * (n + 1)
	return memoized_cut_rod_helper(prices, n, q)

def memoized_cut_rod_helper(prices, n, q):
	if q[n] >= 0:
		return q[n]
	if n == 0:
		return 0
	val = -1
	for i in range(1, n + 1):
		val = max(val, prices[i] + memoized_cut_rod_helper(prices, n - i, q))
	q[n] = val
	return q[n]

def bottom_up_cut_rod(prices, n):
	r = [-1] * (n + 1)
	s = [0] * (n + 1)
	r[0] = 0
	for j in range(1, n + 1):
		q = -1
		for i in range(1, j + 1):
			if q < prices[i] + r[j - i]:
				q = prices[i] + r[j - i]
				s[j] = i
		r[j] = q
	cuts = print_cuts(s, n)
	chunks = [prices[x] for x in cuts]
	chunks.append(r[n])
	return chunks

def print_cuts(s, n):
	r = []	
	while n > 0:
		r.append(s[n])
		n = n - s[n]
	return r

if __name__ == '__main__':
	prices = [0,1,5,8,9,10,17,17,20,24,30]
	for i in range(11):
		print
		print 'length    : ', i
		print ' cut_rod  : ', cut_rod(prices, i)
		print ' memoized : ', memoized_cut_rod(prices, i)
		print ' bottoms  : ', bottom_up_cut_rod(prices, i)
