def fibonacci(n):
    if n < 1: return 0
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

if __name__=="__main__":
    t = int(input())
    while t:
        n = int(input())
        print(fibonacci(n))
        t -= 1