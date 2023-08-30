def rotate90degree(matrix):
    n = len(matrix)
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(3):
        temp[i][2] = matrix[0][i]
    for i in range(3):
        temp[i][1] = matrix[1][i]
    for i in range(3):
        temp[i][0] = matrix[2][i]
    return temp

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate90degree(arr))
