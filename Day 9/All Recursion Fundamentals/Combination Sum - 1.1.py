def Combination(ind,target,temp,arr,ans):
    if ind == len(arr) :
        if target == 0:
            ans.append(temp.copy())
        return
    if arr[ind] <= target:
        temp.append(arr[ind])
        Combination(ind+1,target,temp,arr,ans)
        temp.pop()
    Combination(ind+1,target-arr[ind],temp,arr,ans)
            

def CombinationSum(target, arr):
    temp = []
    ans = []
    Combination(0,target,temp,arr,ans)
    ans.sort()
    print(ans)
    
CombinationSum(6,[2,4,6])
# CombinationSum(0,[5,-2,0,-5,2])

# Time Complexity: O(2^t*k) where t is the target, k is the average length
# Space Complexity: O(k*x), k is the average length and x is the no. of combinations
    