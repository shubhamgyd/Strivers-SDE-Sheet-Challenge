def removeDuplicates(arr):
    ptr = 0
    flag = arr[ptr]
    count1 = 0
    for i in range(1, len(arr)):
        temp = i
        count1 += 1
        if arr[temp] > arr[ptr]:
            flag = arr[temp]
        else:
            count = 0
            for j in range(i+1, len(arr)):
                if arr[j] > flag:
                    count = 1
                    flag = arr[j]
                    arr[j],arr[temp] = arr[temp], arr[j]
                    break
            if count != 1:
                break
        ptr = temp
        print(arr)
    return count1

arr = [1, 3, 3, 3, 4, 5]
print(removeDuplicates(arr))
            
            
                    