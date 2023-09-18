def reverse(start, end, arr):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def solution(arr, t):
    if len(arr) == len(t):
        i,j = 0,len(arr)-1
        while i < j:
            if arr[i] != t[j]:
                return "NO"
            i += 1
            j -= 1
        return "YES"
    return "NO"


if __name__=="__main__":
    arr = input()
    t = input()
    print(solution(arr,t))