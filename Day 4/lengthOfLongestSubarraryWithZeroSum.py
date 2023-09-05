def longestSub(arr):
    n = len(arr)
    sum = 0
    for i in range(n-1):
        sum1 = arr[i]
        if arr[i] == 0:
            sum = max(sum, 1)
        for j in range(i+1,n):
            sum1 += arr[j]
            if sum1 == 0:
                res = j - i + 1
                sum = max(sum, res)
    return sum

arr = list(map(int, input().strip().split()))
print(longestSub(arr))
# 1 45 22 0 10 -37 37 29 23 2 9 0 2 15 49 6 27 25 35 50 39 1 42 49 20 33 28 40 26 14 38 26 25 16 49