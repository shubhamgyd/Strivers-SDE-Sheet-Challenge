def mergeOverlapping(arr):
    n = len(arr)
    arr.sort()
    ans = []
    
    for i in range(n):
        # if the current intervals does not
        # lie in the last interval
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        
        # if the current interval
        # lies in the last interval
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans

if __name__=="__main__":
    arr = [[1,3],[8,10],[2,6],[15,18]]
    ans = mergeOverlapping(arr)
    print("The merged intervals are:")
    for element in ans:
        print(f"[{element[0]},{element[1]}]", end=" ")