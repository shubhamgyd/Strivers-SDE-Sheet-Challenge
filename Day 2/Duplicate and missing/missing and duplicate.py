def missing_Duplicate(arr):
    temp = [0,0]
    n = len(arr)
    temp1 = [0]*(n+1)
    for i in range(n):
        if (temp1[arr[i]] == 0):
            temp1[arr[i]] += 1
        else:
            temp[0] = arr[i]
            break
    for i in range(1,n+1):
        if temp1[i] == 0:
            temp[1] = i
    return temp

# arr = [3,1,2,5,3]
arr = [3,1,2,5,4,6,7,5]
print("The duplicate element is ",missing_Duplicate(arr))