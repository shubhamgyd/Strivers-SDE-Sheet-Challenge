def k_jumps(n,arr,k,result):
    if n == 0:
        return 0
    for i in range(1,k+1):
        if (n > (i - 1)):
            step = k_jumps(n-i,arr,k,result) + abs(arr[n] - arr[n-i])
        else:
            step = 9999999
        result = min(result,step)
    return result

arr = [30,10,60,10,60,50]
n = len(arr)
k = 3
result = 999999
print(k_jumps(n-1,arr,k,result))