import sys


def algorithm(arr,n):
    max = -sys.maxsize - 1
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max

arr = [-1, 2, -2, -3, 5, -1, 7, 6, -2]
n = len(arr)
maximum = algorithm(arr, n)
print("The maximum subarray sum is:", maximum)