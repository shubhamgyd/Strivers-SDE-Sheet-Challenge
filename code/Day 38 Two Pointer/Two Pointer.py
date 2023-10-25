def segreate_0_1(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1
        if arr[left] ==1 and arr[right] == 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1


if __name__=="__main__":
    T = int(input())
    while T:
        arr = list(map(int, input().split()))
        segreate_0_1(arr)
        print(arr)
        T -= 1