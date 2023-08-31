def swapIfGreater(arr1, arr2, index1, index2):
    if arr1[index1] > arr2[index2]:
        arr1[index1], arr2[index2] = arr2[index2], arr1[index1]

def gapMethod(arr1, arr2, n, m):
    # len of the imaginary single array:
    len = n + m

    # Initial gap:
    gap = (len // 2) + (len % 2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < len:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)
            
if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    gapMethod(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print()