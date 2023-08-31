def count_Inversions(arr):
    n = len(arr)
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                res += 1
    return res

# arr = [5, 4, 3, 2, 1]
# arr = [5, 3, 2, 1, 4]
arr = [1, 20, 6, 4, 5]
result = count_Inversions(arr)
print("The count inversion for the given array is ", result)