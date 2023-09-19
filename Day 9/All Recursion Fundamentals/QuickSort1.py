def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high -1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[low] = arr[low], arr[j]
    return j

def quickSort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quickSort(arr, start, p_index-1)
        quickSort(arr, p_index+1, end)
        

arr = [1, 5, 3, 7, 6, 9]
quickSort(arr, 0, 5)
print(arr)