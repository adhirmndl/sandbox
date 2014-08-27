# Enter your code here. Read input from STDIN. Print output to STDOUT
import copy
def twoarrays(a,b,k):
  #Compute and return final answer over here
  a.sort()
  b.sort(reverse=True)
  for i in range(len(a)):
    if a[i] + b[i] < k:
      return 'NO'
  return 'YES' 
if __name__ == '__main__':
  for _ in range(input()):
    n, k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    print twoarrays(a,b,k) 
