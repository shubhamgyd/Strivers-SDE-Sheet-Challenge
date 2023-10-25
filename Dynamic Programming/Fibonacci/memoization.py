def fibonacci(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n] != -1:
        return dp[n]
    left = fibonacci(n-1, dp)
    right = fibonacci(n-2, dp)
    return left + right

if __name__=="__main__":
    t = int(input())
    while t:
        n = int(input())
        dp = [-1]*(n+1)
        print(fibonacci(n,dp))
        t -= 1