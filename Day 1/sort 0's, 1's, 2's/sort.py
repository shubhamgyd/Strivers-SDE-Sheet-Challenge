def sort(arr):
    for i in range(len(arr)):
        low = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if low > arr[j]:
                low = arr[j]
                index = j
        arr[i],arr[index] = arr[index],arr[i]
    return arr
        
arr = [0,1,2,1,1,0,2]
print(*sort(arr))