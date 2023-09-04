def twoSum(arr, target):
    n = len(arr)
    temp = {}
    ans = []
    for i in range(n):
        num = arr[i]
        moreNeeded = target - num
        if (moreNeeded in temp):
            ans.append("YES")
            ans.append([temp[moreNeeded],i])
            return ans
        temp[arr[i]] = i
    return ["No",[-1,-1]]

if __name__=="__main__":
    arr = [2, 6, 5, 8, 11]
    n = len(arr)
    target = 14
    ans = twoSum(arr, target)
    print("This is the answer for variant 1: ", ans[0])
    print("The indices are:", ans[1])