# Enter your code here. Read input from STDIN. Print output to STDOUT
import copy
def cavities(matrix):
  #Compute and return final answer over here
  n = len(matrix)
  answer = copy.deepcopy(matrix)  
  for i in range(1, n-1):
    for j in range(1, n-1):
      l=[]
      l.append(matrix[i-1][j])
      l.append(matrix[i][j-1])
      l.append(matrix[i][j+1])
      l.append(matrix[i+1][j])
      l.sort()
      if l[-1] < matrix[i][j]:
        answer[i][j] = 'X'
  for i in xrange(n):
    print ''.join(map(str,answer[i])) 
if __name__ == '__main__':
  n = input()
  matrix = [[x for x in list(str(input()))] for x in xrange(n)] 
  cavities(matrix) 
