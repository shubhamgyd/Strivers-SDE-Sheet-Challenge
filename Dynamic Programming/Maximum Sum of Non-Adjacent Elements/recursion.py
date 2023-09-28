def compute(ind, nums, dp):
    if ind == 0:
        return nums[ind]
    if ind < 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    
    pick = nums[ind] + compute(ind-2,nums,dp)
    notPick = 0 + compute(ind-1,nums,dp)
    dp[ind] = max(pick,notPick)
    return dp[ind]

def maximumNonAdjacentSum(nums):    
    ind = len(nums)
    dp = [-1 for i in range(len(nums))]
    return compute(ind-1, nums, dp)

nums = [2, 1, 4, 9]
print(maximumNonAdjacentSum(nums))
# 11