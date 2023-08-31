# Problem statement: 
# Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order.
# Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2
# so that it contains the last M elements.

def mergeSorted(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    ptr1 = 0
    ptr2 = 0
    while ptr1 < n:
        if arr1[ptr1] > arr2[ptr2]:
            arr1[ptr1],arr2[ptr2] = arr2[ptr2],arr1[ptr1]
            if arr2[ptr2] > arr2[ptr2+1]:
                arr2.sort()
        else:
            ptr1 += 1

# arr1 = [1,4,8,10,11]
# arr2 = [2,3,9]
arr1 = [1, 8, 8]
arr2 = [2, 3, 4, 5]
mergeSorted(arr1,arr2)
print(arr1)
print(arr2)

# Time Complexity: O(nlogn + n)
# Space Complexity: O(1)