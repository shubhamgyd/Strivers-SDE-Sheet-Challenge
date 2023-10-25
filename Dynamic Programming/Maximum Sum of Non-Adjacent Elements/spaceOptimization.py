def compute(ind, nums):
    prev = nums[0]
    prev2 = 0
    for i in range(1,ind):
        take = nums[i]
        if i > 1:
            take += prev2
        nottake = 0 + prev
        curi = max(take, nottake)
        prev2 = prev
        prev = curi
    return prev


def maximumNonAdjacentSum(nums):    
    ind = len(nums)
    return compute(ind, nums)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(maximumNonAdjacentSum(nums))
    