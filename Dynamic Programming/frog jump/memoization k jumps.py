def k_jumps(n,dp,arr,k,result):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    for i in range(1,k+1):
        if (n > (i - 1)):
            step = k_jumps(n-i,dp,arr,k,result) + abs(arr[n] - arr[n-i])
        else:
            step = 9999999
        result = min(result,step)
        dp[n] = result
    return dp[n]

arr = [30,10,60,10,60,50]
n = len(arr)
k = 3
result = 999999
dp = [-1 for i in range(n)]
print(k_jumps(n-1,dp,arr,k,result))