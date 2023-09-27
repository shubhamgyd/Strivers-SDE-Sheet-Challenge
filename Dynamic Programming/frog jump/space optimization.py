def frogJump(n, heights):
    prev = 0
    prev2 = 0
    for i in range(1,n):
        fs = prev + abs(heights[i] - heights[i-1])
        ss = 99999999
        if i > 1:
            ss = prev2 + abs(heights[i] - heights[i-2])
        curi = min(fs, ss)
        prev2 = prev
        prev = curi
    return prev

arr = [30,10,60,10,60,50]
n = len(arr)
print(frogJump(n,arr))