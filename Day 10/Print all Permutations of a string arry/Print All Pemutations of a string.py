def solution(ds, arr,ans,d):
    if len(ds) == len(arr):
        ans.append(ds.copy())
        return
    
    for i in range(len(arr)):
        if d[i] == 0:
            ds.append(arr[i])
            d[i] = 1
            solution(ds, arr, ans, d)
            ds.remove(arr[i])
            d[i] = 0
        
        
def printAllPermutations(arr):
    ds = []
    ans = []
    d = [0]*len(arr)
    solution(ds,arr,ans,d)
    return ans

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        print(printAllPermutations(arr))
    