def count(arr):
    ans = 0
    maxi = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            ans += 1
        else:
            ans = 0
        maxi = max(maxi, ans)
    return maxi

arr = [1,1,0,0,1,1,1]
print(count(arr))