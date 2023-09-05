def longest(arr):
    n = len(arr)
    sum = 0
    maximum = -9999999
    hashmap = {} # created a dictionary
    for i in range(n):
        sum += arr[i]
        if sum == 0:
            maximum = i + 1 # if prefix sum is zero
        elif sum > 0: # if sum is greater than zero
            if sum in hashmap:
                maximum = max(maximum,i- hashmap[sum]) # updating the maximum
            else:
                hashmap[sum] = i # adding the sum with the index in the dictionary
    return maximum

arr = [1, -1, 3, 2, -2, -8, 1, 7, 10, 23]
print(longest(arr))