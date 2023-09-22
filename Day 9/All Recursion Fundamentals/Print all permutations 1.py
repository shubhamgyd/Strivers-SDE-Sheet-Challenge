def func(arr, temp, hashmap, ans):
    if len(temp) == len(arr):
        ans.append(temp.copy())
        return
    
    for i in range(len(arr)):
        if hashmap[arr[i]] != 1:
            temp.append(arr[i])
            hashmap[arr[i]] = 1
            func(arr, temp, hashmap, ans)
            temp.pop()
            hashmap[arr[i]] = 0

def printPermutations(arr):
    hashmap = dict()
    for i in range(len(arr)):
        hashmap[arr[i]] = 0
    temp = []
    ans  = []
    func(arr, temp, hashmap, ans)
    print(ans)
    
printPermutations([1,2,3])

# Time Complexity: O(n! * n), where n is the length of the arr.
# Space Complexity: O(n) + O(n), where n is the length of the arr.