def duplicate(arr):
    n = len(arr)
    freq = [0 for i in range(n+1)]
    for i in range(1,n+1):
        if freq[arr[i]] == 0:
            freq[arr[i]] += 1
        else:
            return arr[i]
        
    return 0

arr = [1, 3, 5, 2, 3]
print("The duplicate element is ", duplicate(arr))