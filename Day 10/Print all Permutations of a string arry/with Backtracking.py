def solution(ind, arr, ans, ds):
    if ind == len(arr):
        ans.append(ds.copy())

    for i in range(ind, len(arr)):
        ds.append(arr[i])
        arr[i],arr[ind] = arr[ind],arr[i]
        solution(ind+1,arr,ans,ds)
        arr[i],arr[ind] = arr[ind],arr[i]
        ds.pop()
        
def printAllPermuations(arr):
    ds = []
    ans = []
    ind = 0
    solution(ind, arr, ans, ds)
    return ans
    
if __name__=="__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        print(printAllPermuations(arr))