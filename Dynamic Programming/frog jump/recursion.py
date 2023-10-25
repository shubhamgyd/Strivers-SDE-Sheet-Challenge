import sys


def jumps(n,arr):
    if n == 0:
        return 0
    
    fs = jumps(n-1, arr) + abs(arr[n] - arr[n-1])
    
    ss = sys.maxsize
    if n > 1:
        ss = jumps(n-2,arr) + abs(arr[n] - arr[n-2])
    
    return min(fs, ss)

if __name__=="__main__":
    arr = [30,10,60,10,60,50]
    n = len(arr)
    print(jumps(n-1,arr))