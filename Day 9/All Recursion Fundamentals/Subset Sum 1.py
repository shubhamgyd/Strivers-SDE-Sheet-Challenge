def subsetSum(ind, arr, sum, ans):
    if ind == len(arr):
        ans.append(sum)
        return
    
    # ans = []
    # pick the element
    sum += arr[ind]
    (subsetSum(ind+1, arr, sum, ans))
     
    # Do-not pick the element
    sum -= arr[ind]
    (subsetSum(ind+1, arr, sum, ans))

sum = 0
ans = []
subsetSum(0,[3,1,2],0, ans)
ans.sort()
print(ans)

# Time Complexity: O(2^N) + O(2^N * log(2^N))
# Space Complexity: O(2^N)