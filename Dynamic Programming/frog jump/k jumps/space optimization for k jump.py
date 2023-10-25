def k_jumps(n,arr,k):
    dp = [0 for i in range(k)]
    if n == 0:
        return 0
    for index in range(1,n):
        result = 999999
        for i in range(1,k+1):
            if (index > (i - 1)):
                step = dp[k-i] + abs(arr[index] - arr[index-i])
            else:
                step = 9999999
            result = min(result,step)
        dp.remove(dp[0])
        dp.append(result)
    print(dp)
    return dp[k-1]

arr = [30,10,60,10,60,50]
n = len(arr)
k = 3
result = 999999
print(k_jumps(n,arr,k))