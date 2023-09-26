def printS(ind, ds, s, sum, arr, n):
    if(ind == n):
        if(s == sum):
            for i in range(len(ds)):
                print(ds[i],end=" ")
            print()
        return
    
    ds.append(arr[ind])
    s += arr[ind]
    
    printS(ind+1, ds, s, sum, arr, n)
    
    s-= arr[ind]
    ds.pop()
    
    printS(ind+1, ds, s, sum, arr, n)

def patterns():
    arr = [1, 2, 1]
    sum = 2
    n = 3
    ds = []
    printS(0, ds, 0, sum, arr, n)

patterns()