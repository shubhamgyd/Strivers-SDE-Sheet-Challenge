def minimumCoins(arr, n):
    ans = []
    for i in range(len(arr)-1, -1, -1):
        while n >= arr[i]:
            n -= arr[i]
            ans.append(arr[i])
    return ans

if __name__=="__main__":
    n = 49
    arr = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    ans = minimumCoins(arr, n)
    print("The minimum number of coins is", len(ans))
    print("The coins are")
    for i in range(len(ans)):
        print(ans[i], end=' ')
    