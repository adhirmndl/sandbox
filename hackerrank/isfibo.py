k = input()
fibSeries = [0,1]
for i in range(0, k):
	n = input()
	while fibSeries[-1] < n:
		fibSeries.append(fibSeries[-1] + fibSeries[-2]);
	if n in fibSeries:
		print "IsFibo"
	else:
		print "IsNotFibo"