def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__=="__main__":
    t = int(input())
    while t:
        n = int(input())
        print(fibonacci(n))
        t -= 1
    