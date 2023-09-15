def trappingRainWater(arr):
    ans = 0
    left = 0
    n = len(arr)
    right = n - 1
    leftMax = 0
    rightMax = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] > leftMax:
                leftMax = arr[left]
            else:
                ans += (leftMax-arr[left])
            left += 1
        else:
            if arr[right] >= rightMax:
                rightMax = arr[right]
            else:
                ans += (rightMax-arr[right])
            right -= 1
    return ans

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingRainWater(arr))