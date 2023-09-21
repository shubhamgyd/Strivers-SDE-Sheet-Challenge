def Combination(ind,target,temp,arr,ans):
    if ind > 0 and target == 0:
        x = temp.copy()
        ans.append(x)
        return
    
    for i in range(ind,len(arr)):
        if i != ind and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            break
        temp.append(arr[i])
        Combination(i+1,target-arr[i],temp,arr,ans)
        temp.pop()
            

def CombinationSum(target, arr):
    ind = 0
    temp = []
    ans = []
    arr.sort()
    Combination(ind,target,temp,arr,ans)
    ans.sort()
    print(ans)
    
# CombinationSum(0,[5,-2,0,-5,2])
CombinationSum(7,[5,-1,8,2,7,0])
    