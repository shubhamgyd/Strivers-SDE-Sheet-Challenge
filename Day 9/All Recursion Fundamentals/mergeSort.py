def merge(arr, l, m, r): 
    temp = []
    left = l
    right = m+1
    while left <= m and right <= r:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= m:
        temp.append(arr[left])
        left += 1
    while right <= r:
        temp.append(arr[right])
        right += 1
    
    for i in range(len(temp)):
        arr[l+i] = temp[i]
def mergeSort(arr, l, r):
    if l == r :
        return
    mid = (l + (r-l)//2)
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)
    
arr = [4, 1, 3, 9, 7]
mergeSort(arr,0,len(arr)-1)
print(arr)

# Time Complexity: O(N * LogN)
# Space Complexity: O(N)