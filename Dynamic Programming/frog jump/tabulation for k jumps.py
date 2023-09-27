def k_jumps(n,arr,k):
    dp = [-1 for i in range(n)]
    if n == 0:
        return 0
    dp[0] = 0
    for index in range(1,n):
        result = 999999
        for i in range(1,k+1):
            if (index > (i - 1)):
                step = dp[index-i] + abs(arr[index] - arr[index-i])
            else:
                step = 9999999
            result = min(result,step)
        dp[index] = result
    print(dp)
    return dp[n-1]

arr = [60,30,10,60,10,60,50]
n = len(arr)
k = 3
result = 999999
print(k_jumps(n,arr,k))