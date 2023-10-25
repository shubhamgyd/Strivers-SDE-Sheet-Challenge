def maximumNonAdjacentSum(n,nums):
    dp = [-1]*(n+1)
    dp[0] = nums[0]
    for index in range(1,n):
        pick = nums[index]
        if index > 1:
            pick += dp[index-2]
        notpick = dp[index-1]
        dp[index] = max(pick,notpick)
    return dp[n-1]

nums = [2, 1, 4, 9]
n = len(nums)
print(maximumNonAdjacentSum(n,nums))
# 11