def subsets(ind,ans,temp,arr):
    # if ind == len(arr):
    #     x = []
    #     for i in range(len(temp)):
    #         x.append(temp[i])
    #     if x not in ans:
    #         ans.append(x)
    #     return

    # # pick the element
    # temp.append(arr[ind])
    # subsets(ind+1,ans,temp,arr)

    # # Do-not pick the element
    # temp.remove(arr[ind])
    # subsets(ind+1,ans,temp,arr)
    ans.append(temp.copy())
    for i in range(ind, len(arr)):
        if ( i != ind and arr[i] == arr[i - 1]):
            continue
        temp.append(arr[i])
        subsets(ind + 1, ans, temp, arr)
        temp.pop()
def uniqueSubsets(n,arr):
    arr.sort()
    ans = []
    temp = []
    subsets(0,ans,temp,arr)
    ans.sort()
    return ans

print(uniqueSubsets(3,[5,5,3,5]))
# [[], [3], [3, 5], [5], [5, 3, 5], [5, 5], [5, 5, 3, 5], [5, 5, 5]]
# [[], [3], [3, 5], [3, 5, 5], [3, 5, 5, 5], [5], [5, 5], [5, 5, 5]]
