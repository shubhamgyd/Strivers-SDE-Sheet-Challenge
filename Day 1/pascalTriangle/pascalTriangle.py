def triangle(n,r):
    res = 1
    for i in range(r):
        res = res*(n-i)
        res = res/(r - i)
    return int(res)
                
            
    
print(triangle(5,2))