def minimumPlatforms(arr, dep):
    arr.sort()
    dep.sort()


    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)  # updating the value with the current maximum
    return ans

arr = [775, 494, 252, 1680] 
dep = [2052, 2254, 1395, 2130]  
print(minimumPlatforms(arr, dep))