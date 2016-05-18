class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def findCount(self, A, B):
		index = self.binSearch(A, B)
		print index
		if index == -1:
			return 0
		#count forward
		i = index+1
		count = 1
		while(i < len(A) and A[i] == B):
			i+=1
			count+=1
		#count backward
		i = index -1
		while(i >= 0 and A[i] == B):
			i-=1
			count+=1
		return count

	def binSearch(self, A, B):
		start = 0
		end   = len(A) -1
		while (start <= end):
			mid = (start + end)/2
			if A[mid] == B:
				return mid
			elif A[mid] < B:
				start = mid+1
			else:
				end   = mid - 1
		return -1

s = Solution()
# print s.findCount([5,7,7,8,8,10], 11)
arr = [ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ]
print s.findCount(arr, 1)
