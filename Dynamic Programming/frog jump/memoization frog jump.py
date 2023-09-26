import sys
def f(ind,arr,dp):
    if ind == 0:
        return 0
    if(dp[ind] != -1):
        return dp[ind]
    left = f(ind-1,arr,dp) + abs(arr[ind] - arr[ind-1])
    right = sys.maxsize
    if(ind > 1):
        right = f(ind-2,arr,dp) + abs(arr[ind] - arr[ind-2])
    dp[ind] = min(left,right)
    return dp[ind]

def frogJump(arr,n):
    dp = [-1 for i in range(n)]
    return f(n-1,arr,dp)

arr = [30,10,60,10,60,50]
n = len(arr)
print(frogJump(arr,n))