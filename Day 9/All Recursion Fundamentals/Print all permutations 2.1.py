def func(ind, temp, ans, arr):
    if ind == len(arr):
        ans.append(arr.copy())
        return
    for i in range(ind, len(arr)):
        arr[ind],arr[i] = arr[i],arr[ind]
        func(ind+1,temp,ans,arr)
        arr[ind],arr[i] = arr[i],arr[ind]

def printPermutation(arr):
    temp = []
    ans = []
    func(0, temp, ans, arr)
    print(ans)

printPermutation([1,2,3])