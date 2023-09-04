def twoSum(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] + arr[high] == target:
            return "Yes"
        elif arr[low] + arr[high] > target:
            high -= 1
        else:
            low += 1
    return "No"

if __name__=="__main__":
    arr = [2, 6, 5, 8, 11]
    n = len(arr)
    target = 14
    ans = twoSum(arr, target)
    print("This is the answer for variant 1: ", ans)