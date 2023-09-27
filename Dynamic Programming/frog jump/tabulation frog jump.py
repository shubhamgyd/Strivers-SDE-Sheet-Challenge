import sys
def frogJump(arr,n):
    dp = [-1 for i in range(n)]
    dp[0] = 0
    for index in range(1,n):
        fs = dp[index - 1] + abs(arr[index] - arr[index - 1])
        ss = sys.maxsize
        if index > 1:
            ss = dp[index - 2] + abs(arr[index] - arr[index-2])
        dp[index] = min(fs,ss)
    print(dp)
    return dp[n-1]

arr = [30,10,60,10,60,50]
n = len(arr)
print(frogJump(arr,n))