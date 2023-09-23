def getPermutation(n,k):
    fact = 1
    numbers = []
    for i in range(1,n):
        fact = fact*i
        numbers.append(i)
    numbers.append(n)
    ans = ""
    k = k - 1
    while True:
        ans = ans + str(numbers[k//fact])
        numbers.remove(numbers[k//fact])
        if(len(numbers) == 0):
            break
        k = k % fact
        fact = fact // len(numbers)
    return ans

n = 4
k = 17
print(getPermutation(n,k))       