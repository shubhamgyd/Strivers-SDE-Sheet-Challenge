def printRow(n):
    res = 1
    temp = []
    temp.append(1)
    for i in range(1,n):
        res = res*(n-i)
        res = res/(i)
        temp.append(int(res))
    return temp
        
def printPascalTriangle(n):
    temp = []
    for i in range(1,n+1):
        temp.append(printRow(i))
    return temp

print(printPascalTriangle(6))