import math

def longest(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    n = len(arr)
    lastSmaller = -9999
    cnt = 0
    longest = 1
    for i in range(n):
        if (arr[i] - 1 == lastSmaller):
            cnt += 1
            lastSmaller = arr[i]
        elif (lastSmaller != arr[i]):
            cnt = 1
            lastSmaller = arr[i]
        longest = max(longest, cnt)
        
    return longest

arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
print(longest(arr))