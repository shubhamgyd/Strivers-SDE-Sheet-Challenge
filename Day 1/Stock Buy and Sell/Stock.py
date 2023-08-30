def maxProfit(arr, n):
    purchase = arr[0]
    maximum = 0
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            purchase = arr[i]
        for j in range(i+1,n):
            if arr[j] > purchase:
                maximum = max(maximum, arr[j]-purchase)
    return maximum

arr = [7, 1, 5, 3, 6, 4]
print(maxProfit(arr, len(arr)))