import sys


def stock(arr,n):
    min_ = sys.maxsize
    max_ = 0
    for i in range(n):
        min_ = min(min_, arr[i])
        max_ = max(max_,arr[i] - min_)
        
    return max_

arr = [7, 1, 5, 3, 6, 4]
n = len(arr)
print(stock(arr, n))