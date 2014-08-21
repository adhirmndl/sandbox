# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = A/B
    wraps = A/B
    chocs = 0
    
    while (wraps >= C1):
    	chocs = wraps/C1
    	answer += chocs
    	wraps = wraps%C1 + chocs
                
    # write code to compute answer
    print answer
