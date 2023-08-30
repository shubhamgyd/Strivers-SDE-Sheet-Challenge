# def rotate90degree(matrix):
#     n = len(matrix)
#     temp = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(3):
#         temp[i][2] = matrix[0][i]
#     for i in range(3):
#         temp[i][1] = matrix[1][i]
#     for i in range(3):
#         temp[i][0] = matrix[2][i]
#     return temp
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