# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return 1 ( 1 corresponds to true )

# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

# class Solution {
#     public:
#         bool searchMatrix(vector<vector<int> > &matrix, int target) {
#             int n = matrix.size();
#             int m = matrix[0].size();
#             int l = 0, r = m * n - 1;
#             while (l != r){
#                 int mid = (l + r - 1) >> 1;
#                 if (matrix[mid / m][mid % m] < target)
#                     l = mid + 1;
#                 else 
#                     r = mid;
#             }
#             return matrix[r / m][r % m] == target;
#         }
# };

class Solution:
	# @param A : list of list of integers
	# @param B : integer
	# @return an integer
	def searchMatrix(self, A, B):
		print A, B
		row = -1
		i = 0
		j = len(A) - 1
		previ = -1
		while i < j:
			mid = (i+j)/2
			if previ == i:
				row = i
				break
			if A[mid][0] < B:
				previ = i
				i = mid
			else:
				j = mid 
		ind = self.binSearch(A[row], B)
		print row, ind
		if ind == -1 and row <= len(A) -2:
			ind = self.binSearch(A[row + 1], B)
			# print 'found at', row + 1, ind
		if ind == -1:
			return 0
		# print 'found at', row, ind
		return 1

	def binSearch(self, arr, b):
		i = 0
		j = len(arr) - 1
		while i <= j:
			mid = (i + j)/2
			if arr[mid] == b:
				return mid
			if arr[mid] < b:
				i = mid + 1
			else:
				j = mid - 1
		return -1

s = Solution()
# print s.binSearch([1], 1) 
# print s.searchMatrix([
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 40],
#   [43, 44, 45, 50]
# ], 51)
print s.searchMatrix([
  [1],
  [11],
  [49],
  [74],
  [77],
  [78],
  [93],
  [94]
	], 49)
# print s.searchMatrix([[1]], 1)