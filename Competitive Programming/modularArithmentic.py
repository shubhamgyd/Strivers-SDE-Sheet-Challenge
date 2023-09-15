def power(a, b, m):
    # if b == 0 and c == 1:
    #     return 0
    # if b == 0:
    #     return 1
    # if b % 2 == 0:
    #     temp = power(a, b//2, c)
    #     return (temp%c * temp%c)%c
    # else:
    #     temp = power(a, b//2, c)
    #     return (a%c * temp%c * temp%c) % c
    
    result = 1
    a = a % m  # Reduce the base modulo m to prevent overflow

    while b > 0:
        # If b is odd, multiply result by a
        if b % 2 == 1:
            result = (result * a) % m
        # Square a and reduce modulo m
        a = (a * a) % m
        # Divide b by 2
        b //= 2

    return result
    

a = 4
b = 8
c = 4
print(power(a, b, c))