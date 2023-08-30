def mergeOverlapping(arr):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        start, end = arr[i][0], arr[i][1]
        
        # Skip all the merged intervals
        if ans and end <= ans[-1][1]:
            continue
        
        # check the rest of the intervals
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
        
    return ans

if __name__=="__main__":
    arr = [[1,3],[8,10],[2,6],[15,18]]
    ans = mergeOverlapping(arr)
    print("The merged intervals are:")
    for element in ans:
        print(f"[{element[0]} {element[1]}]", end=" ")
    print()