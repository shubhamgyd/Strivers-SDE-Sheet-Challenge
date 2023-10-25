def twoSum(arr,K):
    left, right = 0, len(arr)-1
    while left < right:
        if arr[left] + arr[right] == K:
            return "Yes"
        elif arr[left] + arr[right] > K:
            right -= 1
        else:
            left += 1
    return "No"

if __name__=="__main__":
    T = int(input())
    while T:
        arr = list(map(int, input().split()))
        K = int(input())
        print(twoSum(arr,K))
        T -= 1