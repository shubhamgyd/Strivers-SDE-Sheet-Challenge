def duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

if __name__=="__main__":
    arr = [1, 3, 4, 2, 1]
    print("The duplicate number is ", duplicate(arr))
    
# Link of the video
# https://youtu.be/32Ll35mhWg0