def majority(arr):
    count = 0
    Element = 0
    
    for i in range(len(arr)):
        if count == 0:
            Element = arr[i]
        if Element == arr[i]:
            count += 1
        else:
            count -= 1
    
    count1 = 0
    for i in range(len(arr)):
        if arr[i] == Element:
            count1 += 1
    
    if count1 > len(arr)//2:
        return Element
    return -1

arr = [1, 2, 1, 1, 3]
print(majority(arr))