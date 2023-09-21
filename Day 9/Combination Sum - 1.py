def Combination(ind,target,temp,arr,ans):
    if ind == len(arr):
        if target == 0:
            ans.append(temp.copy())
        return
    
    if arr[ind] <= target:
        temp.append(arr[ind])
        Combination(ind,target-arr[ind],temp,arr,ans)
        temp.pop()
    Combination(ind+1,target,temp,arr,ans)
            

def CombinationSum(target, arr):
    ind = 0
    temp = []
    ans = []
    Combination(ind,target,temp,arr,ans)
    print(ans)
    
CombinationSum(7,[2,3,6,7])
    