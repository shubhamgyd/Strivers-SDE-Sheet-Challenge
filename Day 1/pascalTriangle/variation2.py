def triangle(n):
    print(1, end=" ")
    res = 1
    for i in range(1,n):
        res = res*(n-i)
        res = res/(i)
        print(int(res), end=" ")

triangle(5)