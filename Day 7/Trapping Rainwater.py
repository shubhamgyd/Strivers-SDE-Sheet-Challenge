def trappingWater(arr):
    n = len(arr)
    left = 0
    right = n
    water = 0
    while left < right - 1:
        trap = (right-left)*min(left, right)
        water = max(water, trap)
        if left < right:
            left += 1
        else:
            right -= 1
    return water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingWater(arr))