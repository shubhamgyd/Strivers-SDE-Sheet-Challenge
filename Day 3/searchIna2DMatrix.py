def search(mat, target):
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = n*m
    while(low <= high):
        mid = (low + high)//2
        row,col = mid//m, mid%m
        if mat[row][col] == target:
            return True
        elif mat[row][col] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

mat = [[3, 4, 7, 9],[12, 13, 16, 18],[20, 21, 23, 29]]
target = 13

print(search(mat, target))