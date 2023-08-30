def rotate90degree(matrix,n,m):
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()
        
arr = [[1,2,3],[4,5,6],[7,8,9]]
rotate90degree(arr,len(arr),len(arr[0]))
print(arr)