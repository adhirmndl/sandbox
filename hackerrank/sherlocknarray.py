# Enter your code here. Read input from STDIN. Print output to STDOUT
def sherlock(a):
  #Compute and return final answer over here
  if len(a) == 1:
    return "YES"
  if len(a) == 2:
    return "NO"
  lsum = a[0] 
  rsum = 0
  rsum = sum(a) - lsum - a[1]
  for i in range (1, len(a)-1):
    if lsum == rsum:
      return "YES"
    lsum += a[i]
    rsum -= a[i+1]
  return "NO"
  # for i in range(1,len(a)-1):

if __name__ == '__main__':
  for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    print sherlock(a) 
