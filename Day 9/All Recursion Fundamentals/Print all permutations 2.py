def func(ind, temp, ans, arr):
    if ind == len(arr):
        ans.append(temp.copy())
        return
    for i in range(ind, len(arr)):
        temp.append(arr[i])
        arr[ind],arr[i] = arr[i],arr[ind]
        func(ind+1,temp,ans,arr)
        arr[ind],arr[i] = arr[i],arr[ind]
        temp.pop()

def printPermutation(arr):
    temp = []
    ans = []
    func(0, temp, ans, arr)
    print(ans)

printPermutation([1,2,3])