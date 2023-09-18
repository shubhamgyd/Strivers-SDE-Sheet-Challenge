def printS(ind, s, sum, arr, n):
    
    # condition not satisfied
    # strictly done if array contains positives only
    if(s > sum): return 0
    if(ind == n):
        if s == sum:
            return 1
        else:
            return 0
    
    s += arr[ind]
    l = printS(ind + 1, s, sum, arr, n)
    
    s -= arr[ind]
    r = printS(ind + 1, s, sum, arr, n)
    
    return l + r

if __name__=="__main__":
    arr = [1, 2, 1]
    n = 3
    sum = 2
    print(printS(0,0,sum, arr, n))