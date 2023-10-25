def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    lastprev = 0
    prev = 1
    
    for i in range(2,n+1):
        ans = prev + lastprev
        lastprev = prev
        prev = ans
    return prev


if __name__=="__main__":
    t = int(input())
    while t:
        n = int(input())
        print(fibonacci(n))
        t -= 1
        