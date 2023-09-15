def Sum3(arr, k):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            sum_ = arr[i] + arr[left] + arr[right]
            if sum_ < 0:
                left += 1
            elif sum_ > 0:
                right -= 1
            else:
                target = [arr[i], arr[left], arr[right]]
                ans.append(target)
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
    return ans

arr = [-1, 0, 1, 2, -1, 4]
k = 0
print(Sum3(arr, k))