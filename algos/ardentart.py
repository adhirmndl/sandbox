#arraypairsum.py
def pairsum_on2(arr, numsum):
	for i in range(len(arr)):
		# print "i " + str(i)
		for j in range(i+1, len(arr)):
			# print j
			if arr[j] == (numsum - arr[i]):
				print arr[i], arr[j]

def pairsum_onlogn(arr, numsum):
	arr.sort()
	left, right = (0, len(arr) - 1)

	while (left < right):
		cursum = arr[left] + arr[right]
		if cursum == numsum:
			print arr[left], arr[right]
			left +=1 # or right -=1
		if cursum < numsum:
			left +=1
		else:
			right -=1


if __name__ == "__main__":
	# pairsum_on2([4,3,7,8,2,1,5], 6)
	pairsum_onlogn([4,3,7,8,2,1,5,3], 6)