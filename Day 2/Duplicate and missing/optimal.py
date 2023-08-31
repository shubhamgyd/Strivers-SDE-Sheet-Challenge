def missing(arr):
    n = len(arr)
    Sn = (n*(n+1))//2
    Sn2 = (n*(n+1)*(2*n + 1))//6
    S, S2 = 0,0
    for i in range(n):
        S += arr[i]
        S2 += arr[i]*arr[i]
        
    val1 = S - Sn # x - y
    val2 = S2 - Sn2 
    val2 = val2/val1 # x + y
    
    x = (val1 + val2)//2
    y = x - val1
    
    return [int(x), int(y)]


arr = [3,1,2,5,4,6,7,5]
print("The duplicate element is ",missing(arr))
    