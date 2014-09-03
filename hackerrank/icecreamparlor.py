for _ in range(input()):
    M = input()
    N = input()
    prices = [int(i) for i in raw_input().strip().split()]
    for i in range(N-1):
        for j in range(i + 1,N):
            if prices[i] + prices[j] == M:
                print i+1, j+1

