def trappingWater(arr):
    n = len(arr) 
    waterTrapped = 0
    for i in range(n):
        j = i
        leftMax = 0
        rightMax = 0
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        j = i
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        temp = min(leftMax, rightMax) - arr[i]
        waterTrapped += temp
    return waterTrapped

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingWater(arr))